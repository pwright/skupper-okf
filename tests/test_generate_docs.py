"""Check Markdown regeneration, round trips, and output preflight."""

import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name, filename):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


REPORT = load_script("document_report", "report-generated-docs.py")
GENERATE = load_script("document_generate", "generate-docs.py")
COMMIT = "a" * 40


class GenerateDocsTests(unittest.TestCase):
    def model(self, source):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            path = repo / "docs/example.md"
            path.parent.mkdir()
            with path.open("w", encoding="utf-8", newline="") as destination:
                destination.write(source)
            return REPORT.document_model(path, repo, COMMIT)

    def assert_round_trip(self, source):
        original = self.model(source)
        recreated = GENERATE.render_document(original)
        self.assertEqual(self.model(recreated), original)
        return original, recreated

    def test_round_trip_complete_blocks_and_nested_sections(self):
        self.assert_round_trip('''---
# retain comments
title: Example
reviewed: false
custom: [one, two]
---
Introduction with **bold** and <span>HTML</span>.

# Main

- parent
  - nested

> quoted
>
> # heading inside quote

| a | b |
| --- | --- |
| 1 | 2 |

```sh
echo example
```

---

<div>HTML</div>

### Deep

paragraph

## Sibling

text
''')

    def test_setext_multiline_empty_and_literal_hash_headings(self):
        self.assert_round_trip('''First line
second *line* #
=============

## ### ##

# ###

Final #
-------
''')

    def test_adjacent_html_badges_round_trip_as_one_block(self):
        source = ('# Heading\n\n'
                  '<a href="https://example.com"><img src="badge.svg" /></a>\n'
                  '<a href="https://example.org"><img src="other.svg" /></a>\n\n'
                  '**note**\n')
        model, _ = self.assert_round_trip(source)
        self.assertEqual(model['children'][0]['children'][0]['kind'], 'html')
        self.assertEqual(model['children'][0]['children'][0]['markdown'],
                         source.split('\n\n')[1])

    def test_preserves_frontmatter_raw_crlf_and_toml(self):
        for raw in ('---\r\n# comment\r\ntitle: Example\r\n---\r\n',
                    '+++\ntitle = "Example"\n+++\n'):
            with self.subTest(raw=raw):
                original, recreated = self.assert_round_trip(raw + '# Heading\n\ntext\n')
                self.assertTrue(recreated.startswith(original['frontmatter']['raw']))
        self.assert_round_trip('---\ntitle: Example\n---')
        self.assert_round_trip('')

    def test_frontmatter_edits_must_update_raw_and_data(self):
        model = self.model('---\ntitle: Example\n---\n# Heading\n')
        model['frontmatter']['data']['title'] = 'Edited'
        with self.assertRaisesRegex(ValueError, 'disagree'):
            GENERATE.render_document(model)
        model['frontmatter']['raw'] = '---\ntitle: Edited\n---\n'
        self.assertIn('title: Edited', GENERATE.render_document(model))

    def test_unrepresentable_section_hierarchy_is_rejected(self):
        model = self.model('# Parent\n\n## Child\n')
        model['children'][0]['children'][0]['level'] = 1
        with self.assertRaisesRegex(ValueError, 'higher heading level'):
            GENERATE.render_document(model)
        model = self.model('# Parent\n\n## Child\n')
        model['children'][0]['children'].append({
            'type': 'block', 'id': 'extra', 'kind': 'paragraph', 'markdown': 'parent text',
        })
        with self.assertRaisesRegex(ValueError, 'cannot retain its parent'):
            GENERATE.render_document(model)

    def test_cli_generation_and_explicit_overwrite(self):
        model = self.model('# Example\n\ntext\n')
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = root / 'input.jsonl'
            report.write_text(json.dumps(model) + '\n')
            output = root / 'output'
            self.assertEqual(GENERATE.generate(report, output), 1)
            recreated = output / 'docs/example.md'
            self.assertEqual(REPORT.document_model(recreated, output, COMMIT), model)
            recreated.write_text('existing content')
            with self.assertRaisesRegex(ValueError, 'output exists'):
                GENERATE.generate(report, output)
            self.assertEqual(recreated.read_text(), 'existing content')
            self.assertEqual(GENERATE.generate(report, output, overwrite=True), 1)
            self.assertEqual(REPORT.document_model(recreated, output, COMMIT), model)

    def test_invalid_later_record_and_duplicate_paths_write_nothing(self):
        model = self.model('# Example\n')
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = root / 'input.jsonl'
            output = root / 'output'
            for second, message in ((dict(model, git_commit='bad'), 'schema validation'),
                                    (model, 'duplicate document path')):
                with self.subTest(message=message):
                    report.write_text(json.dumps(model) + '\n' + json.dumps(second) + '\n')
                    with self.assertRaisesRegex(ValueError, message):
                        GENERATE.generate(report, output)
                    self.assertFalse(output.exists())

    def test_escaping_paths_symlinks_and_filename_mismatch_are_rejected(self):
        model = self.model('# Example\n')
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = root / 'output'
            output.mkdir()
            for path, filename in (('../escape.md', 'escape.md'),
                                   ('/absolute.md', 'absolute.md'),
                                   ('docs/example.md', 'different.md')):
                with self.subTest(path=path):
                    with self.assertRaisesRegex(ValueError, 'invalid Markdown'):
                        GENERATE.output_path(output, dict(model, path=path, filename=filename))
            outside = root / 'outside'
            outside.mkdir()
            (output / 'docs').symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(ValueError, 'escapes'):
                GENERATE.output_path(output, model)
            self.assertEqual(list(outside.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
