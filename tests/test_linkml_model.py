"""Offline acceptance tests through the LinkML command interface."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml


PROJECT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT / "scripts/linkml_model.py"
FIXTURE = PROJECT / "tests/fixtures/linkml"


class LinkMLCommandTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Build once to obtain a valid dataset for mutation-based validation tests.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "project"
            shutil.copytree(FIXTURE, root)
            result = subprocess.run([sys.executable, str(SCRIPT), "build", "--root", str(root)],
                                    text=True, capture_output=True)
            if result.returncode:
                raise AssertionError(result.stderr)
            cls.valid = yaml.safe_load((root / "generated/linkml/architecture.yaml").read_text())

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "project"
        shutil.copytree(FIXTURE, self.root)

    def run_command(self, command="build", *args, success=True):
        result = subprocess.run([sys.executable, str(SCRIPT), command, "--root", str(self.root), *args],
                                text=True, capture_output=True)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout)
        return result

    def read_yaml(self, path):
        return yaml.safe_load((self.root / path).read_text())

    def write_yaml(self, path, value):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump(value))

    def test_reproducible_build_and_traceability(self):
        before = {str(p.relative_to(self.root)): p.read_bytes()
                  for p in self.root.rglob("*") if p.is_file()}
        self.run_command()
        paths = ["generated/linkml/architecture.yaml", "generated/linkml/architecture.schema.json",
                 "indexes/linkml-report.json", "indexes/linkml-report.md"]
        first = {p: (self.root / p).read_bytes() for p in paths}
        self.run_command()
        self.assertEqual(first, {p: (self.root / p).read_bytes() for p in paths})
        for path, content in before.items():
            self.assertEqual((self.root / path).read_bytes(), content)
        self.run_command("validate")
        report = json.loads((self.root / "indexes/linkml-report.json").read_text())
        codes = {row["code"] for row in report["diagnostics"]}
        self.assertTrue({"missing_evidence", "revision_mismatch", "unresolved_link"} <= codes)
        dataset = self.read_yaml(paths[0])
        old = [e for e in dataset["evidence"] if e.get("declared_commit") == "old-commit"]
        self.assertEqual(len(old), 2)
        self.assertTrue(all(e["reviewed"] is False and e["status"] == "needs-review" for e in old))
        uses = [r for r in dataset["relationships"] if r["predicate"] == "uses"]
        self.assertEqual(len(uses), 1)
        self.assertEqual(uses[0]["source"], "concept:listener")

    def test_dry_run_has_no_writes(self):
        before = sorted(str(p.relative_to(self.root)) for p in self.root.rglob("*"))
        self.run_command("build", "--dry-run")
        self.assertEqual(before, sorted(str(p.relative_to(self.root)) for p in self.root.rglob("*")))

    def test_hand_authored_example(self):
        self.run_command("validate", "--data", "example.yaml")

    def test_strict_accepts_fully_recorded_provenance(self):
        data = copy.deepcopy(self.valid)
        for repo in data["repositories"]:
            repo.update(snapshot_commit="known", record_commit="known")
        for evidence in data["evidence"]:
            evidence.update(availability="present", revision_state="matches",
                            declared_commit="known", snapshot_commit="known")
        self.write_yaml("generated/linkml/architecture.yaml", data)
        self.run_command("validate", "--strict")

    def test_invalid_build_preserves_all_outputs(self):
        self.run_command()
        paths = ["generated/linkml/architecture.yaml", "generated/linkml/architecture.schema.json",
                 "indexes/linkml-report.json", "indexes/linkml-report.md"]
        previous = {p: (self.root / p).read_bytes() for p in paths}
        mappings = self.read_yaml("model/linkml/mappings.yaml")
        mappings["assertions"][0]["target"] = "concept:missing"
        self.write_yaml("model/linkml/mappings.yaml", mappings)
        self.assertIn("dangling entity reference", self.run_command(success=False).stderr)
        self.assertEqual(previous, {p: (self.root / p).read_bytes() for p in paths})

    def test_schema_and_reference_failures(self):
        mutations = {
            "required": lambda d: d["concepts"][0].pop("name"),
            "type": lambda d: d["evidence"][0].update(reviewed="false"),
            "predicate": lambda d: d["relationships"][0].update(predicate="imagines"),
            "duplicate": lambda d: d["concepts"].append(copy.deepcopy(d["concepts"][0])),
            "dangling": lambda d: d["relationships"][0].update(target="concept:missing"),
            "evidence": lambda d: d["relationships"][0].update(evidence=["evidence:missing"]),
            "empty_evidence": lambda d: d["relationships"][0].update(evidence=[]),
            "false_revision": lambda d: d["evidence"][0].update(revision_state="matches", declared_commit="unknown"),
        }
        for label, mutate in mutations.items():
            with self.subTest(label=label):
                data = copy.deepcopy(self.valid)
                mutate(data)
                self.write_yaml("generated/linkml/architecture.yaml", data)
                self.run_command("validate", success=False)

    def test_strict_rejects_unresolved_provenance(self):
        self.write_yaml("generated/linkml/architecture.yaml", self.valid)
        result = self.run_command("validate", "--strict", success=False)
        self.assertIn("unresolved provenance", result.stderr)

    def test_malformed_frontmatter_preserves_previous_output(self):
        self.run_command()
        target = self.root / "generated/linkml/architecture.yaml"
        previous = target.read_bytes()
        (self.root / "human/one/listener.md").write_text("---\nid: [broken\n---\n")
        self.run_command(success=False)
        self.assertEqual(target.read_bytes(), previous)

    def test_duplicate_input_identity(self):
        path = self.root / "human/two/routing-key.md"
        path.write_text(path.read_text().replace("id: routing-key", "id: listener"))
        self.assertIn("duplicate identity", self.run_command(success=False).stderr)

    def test_path_escape_and_symlink_escape(self):
        path = self.root / "generated/concepts/listener.md"
        path.write_text("---\nsource_paths: [../outside.md]\n---\n")
        self.assertIn("path escape", self.run_command(success=False).stderr)
        outside = Path(self.temporary.name) / "outside.md"
        outside.write_text("outside")
        path.unlink()
        path.symlink_to(outside)
        self.assertIn("path escape", self.run_command(success=False).stderr)

    def test_changed_assertion_evidence_fails(self):
        path = self.root / "human/one/listener.md"
        path.write_text(path.read_text().replace("A listener uses a routing key.", "Changed."))
        self.assertIn("evidence no longer matches", self.run_command(success=False).stderr)

    def test_optional_and_required_roots(self):
        path = "model/linkml/sources.yaml"
        config = self.read_yaml(path)
        config["repositories"].append({"id": "repo:optional", "root": "human/absent", "include": []})
        self.write_yaml(path, config)
        self.run_command()
        config["repositories"][-1]["required"] = True
        self.write_yaml(path, config)
        self.assertIn("missing required root", self.run_command(success=False).stderr)

    def test_snapshot_record_mismatch(self):
        (self.root / "sources/one.md").write_text("---\ncommit: other\n---\n")
        self.run_command()
        report = json.loads((self.root / "indexes/linkml-report.json").read_text())
        self.assertIn("snapshot_mismatch", {row["code"] for row in report["diagnostics"]})


if __name__ == "__main__":
    unittest.main()
