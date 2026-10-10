"""Integration checks for mq parsing and jsonschema.mq validation."""

import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("document_report", ROOT / "tools/report-generated-docs.py")
REPORT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REPORT)
COMMIT = "a" * 40


class DocumentModelTests(unittest.TestCase):
    def model(self, source):
        with TemporaryDirectory() as temporary:
            repo = Path(temporary)
            path = repo / "docs/example.md"
            path.parent.mkdir()
            with path.open("w", encoding="utf-8", newline="") as source_file:
                source_file.write(source)
            return REPORT.document_model(path, repo, COMMIT)

    def validate(self, document):
        return REPORT.command_json([
            "mq", "-I", "json", "-F", "json", "-L", str(REPORT.MODULES),
            'import "jsonschema" | jsonschema::validate(self, schema)',
            "--argjson", "schema", REPORT.SCHEMA.read_text(),
        ], json.dumps(document))

    def test_section_hierarchy_and_metadata(self):
        model = self.model("intro\n\n# First\n\n### Deep\n\ntext\n\n## Sibling\n\n# Next\n")
        self.assertEqual((model["path"], model["filename"], model["git_commit"]),
                         ("docs/example.md", "example.md", COMMIT))
        intro, first, next_section = model["children"]
        self.assertEqual(intro["markdown"], "intro")
        self.assertEqual(first["heading"], "First")
        self.assertEqual([section["heading"] for section in first["children"]], ["Deep", "Sibling"])
        self.assertEqual(first["children"][0]["children"][0]["markdown"], "text")
        self.assertEqual(next_section["heading"], "Next")
        self.assertNotIn("frontmatter", model)
        self.assertEqual(self.validate(model), [])
        self.assertEqual(self.model("intro\n\n# First\n\n### Deep\n\ntext\n\n## Sibling\n\n# Next\n"), model)

    def test_inline_heading_markup_setext_and_empty_heading(self):
        model = self.model("# Héllo **🌍** [link](url) #\n\nSetext *heading*\n===============\n\n# ###\n")
        self.assertEqual([node["heading"] for node in model["children"]],
                         ["Héllo **🌍** [link](url)", "Setext *heading*", ""])

    def test_complete_blocks_and_frontmatter(self):
        source = '''---
name: example
---
# Heading

- first
  continuation

  another paragraph
  - nested

- second

> quote
>
> # quoted heading

| a | b |
| --- | --- |
| one | two |

---

<div>html</div>

    indented code

```py
print(1)
```
'''
        model = self.model(source)
        self.assertEqual(model["frontmatter"], {
            "format": "yaml", "raw": "---\nname: example\n---\n",
            "data": {"name": "example"},
        })
        blocks = model["children"][0]["children"]
        self.assertEqual([block["kind"] for block in blocks],
                         ["list", "blockquote", "table", "thematicBreak", "html", "code", "code"])
        self.assertEqual(blocks[0]["markdown"],
                         "- first\n  continuation\n\n  another paragraph\n  - nested\n\n- second")
        self.assertEqual(blocks[2]["markdown"], "| a | b |\n| --- | --- |\n| one | two |")
        self.assertEqual(blocks[-1]["markdown"], "```py\nprint(1)\n```")
        self.assertEqual(self.validate(model), [])

    def test_yaml_frontmatter_preserves_comments_line_endings_and_custom_values(self):
        raw = (
            "---\r\n# retained comment\r\ntitle: Example\r\nreviewed: false\r\n"
            "tags: [one, two]\r\ncustom:\r\n  score: 3\r\n  missing: null\r\n"
            "timestamp: 2026-08-26T16:01:08Z\r\n---\r\n"
        )
        model = self.model(raw + "# Heading\r\n")
        self.assertEqual(model["frontmatter"]["raw"], raw)
        self.assertEqual(model["frontmatter"]["data"], {
            "title": "Example", "reviewed": False, "tags": ["one", "two"],
            "custom": {"score": 3, "missing": None}, "timestamp": "2026-08-26T16:01:08Z",
        })
        self.assertEqual(self.validate(model), [])

    def test_toml_and_empty_yaml_frontmatter(self):
        raw = '+++\ntitle = "Example"\nreviewed = false\n[custom]\nscore = 3\n+++\n'
        model = self.model(raw + "# Heading\n")
        self.assertEqual(model["frontmatter"], {
            "format": "toml", "raw": raw,
            "data": {"title": "Example", "reviewed": False, "custom": {"score": 3}},
        })
        self.assertEqual(self.validate(model), [])
        empty = self.model("---\n---\n# Heading\n")
        self.assertEqual(empty["frontmatter"]["data"], None)
        self.assertEqual(self.validate(empty), [])

    def test_validation_rejects_invalid_frontmatter_wrapper(self):
        model = self.model("---\ntitle: Example\n---\n# Heading\n")
        for frontmatter in (
            dict(model["frontmatter"], format="unsupported"),
            {"format": "yaml", "data": {}},
            dict(model["frontmatter"], unexpected=True),
        ):
            with self.subTest(frontmatter=frontmatter):
                self.assertTrue(self.validate(dict(model, frontmatter=frontmatter)))

    def test_nested_list_content_is_not_promoted_to_sections(self):
        source = '- list\n\n  ```sh\n  echo nested\n  ```\n\n  ## nested heading\n\n  paragraph\n\n- another\n'
        model = self.model(source)
        self.assertEqual(len(model["children"]), 1)
        self.assertEqual(model["children"][0]["kind"], "list")
        self.assertEqual(model["children"][0]["markdown"], source.rstrip("\n"))

    def test_upstream_html_anchors_and_comments_keep_their_block_kind(self):
        model = self.model('<a id="overview"></a>\n# Overview\n<!--ASSEMBLY-->\n\ntext\n')
        anchor, section = model["children"]
        self.assertEqual(anchor["kind"], "html")
        self.assertEqual(anchor["markdown"], '<a id="overview"></a>')
        self.assertEqual(section["heading"], "Overview")
        self.assertEqual(section["children"][0]["kind"], "html")
        self.assertEqual(section["children"][0]["markdown"], '<!--ASSEMBLY-->')
        self.assertEqual(self.validate(model), [])

    def test_separate_lists_tables_and_reference_links(self):
        source = '''1. ordered

- unordered

| a |
| --- |
| b |

| c |
| --- |
| d |

[ref]: https://example.com

Reference [link][ref] and <span>inline</span>.
'''
        blocks = self.model(source)["children"]
        self.assertEqual([block["kind"] for block in blocks],
                         ["list", "list", "table", "table", "paragraph", "paragraph"])
        self.assertEqual(blocks[-2]["markdown"], "[ref]: https://example.com")
        self.assertEqual(blocks[-1]["markdown"], "Reference [link][ref] and <span>inline</span>.")

    def test_validation_rejects_invalid_metadata_and_nested_blocks(self):
        model = self.model("# Heading\n\ntext\n")
        for field, invalid in (("path", "/absolute.md"), ("path", "../outside.md"),
                               ("filename", "docs/example.md"), ("git_commit", "invalid")):
            with self.subTest(field=field, invalid=invalid):
                corrupted = dict(model, **{field: invalid})
                self.assertTrue(self.validate(corrupted))
        missing_commit = dict(model)
        del missing_commit["git_commit"]
        self.assertTrue(self.validate(missing_commit))
        model["children"][0]["children"][0]["kind"] = "unsupported"
        self.assertTrue(self.validate(model))


if __name__ == "__main__":
    unittest.main()
