"""Packaging regressions for an unchanged S1 PDF rebuilt with another TeX version."""

from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


PACKAGE = Path(__file__).resolve().parents[1] / "paper_assets/paper_ii_journal"


def load_module(name):
    spec = importlib.util.spec_from_file_location(name, PACKAGE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load_module("build")
verifier = load_module("verify_package")


def digest(data):
    return sha256(data).hexdigest()


class PreservedLowerPdfTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="ringmin-package-test-")
        self.addCleanup(temporary.cleanup)
        self.here = Path(temporary.name)
        self.lower = self.here / "lower_supplement"
        self.lower.mkdir()
        for name in verifier.REQUIRED:
            path = self.here / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"fixture\n")
        records = {}
        for name in ("main", "upper_supplement", "lower"):
            source = self.lower / "supplement.tex" if name == "lower" else self.here / (name + ".tex")
            source.write_bytes((name + " source\n").encode())
            source.with_suffix(".pdf").write_bytes((name + " delivered PDF\n").encode())
            records[name] = {
                "source_sha256": digest(source.read_bytes()),
                "pdf_sha256": digest(source.with_suffix(".pdf").read_bytes()),
                "pages": 1,
                "passes": 3,
                "unresolved_or_box_warnings": [],
            }
        self.report = {"documents": records}
        self.delivered = records["lower"]["pdf_sha256"]
        self.rebuilt = digest(b"S1 built with a different TeX distribution\n")
        (self.lower / "MANIFEST.json").write_text(json.dumps({"outputs": {
            path.name: digest(path.read_bytes()) for path in self.lower.iterdir()
        }}), encoding="utf-8")

    def preserve(self):
        self.report["documents"]["lower"].update(
            pdf_sha256=self.rebuilt,
            delivered_pdf_sha256=self.delivered,
            delivery_policy="preserved-baseline",
            matches_preserved_pdf=False,
        )

    def validate(self):
        (self.here / "BUILD_REPORT.json").write_text(json.dumps(self.report), encoding="utf-8")
        verifier.validate_build_report(self.here, self.lower)

    def test_different_rebuild_keeps_delivery_bound_to_original_manifest(self):
        self.preserve()
        self.validate()
        self.assertEqual(digest((self.lower / "supplement.pdf").read_bytes()), self.delivered)

    def test_false_match_flag_is_rejected_in_both_directions(self):
        self.preserve()
        record = self.report["documents"]["lower"]
        for rebuilt, claimed_match in ((self.rebuilt, True), (self.delivered, False)):
            with self.subTest(rebuilt=rebuilt, claimed_match=claimed_match):
                record.update(pdf_sha256=rebuilt, matches_preserved_pdf=claimed_match)
                with self.assertRaisesRegex(ValueError, "inconsistent preserved PDF comparison"):
                    self.validate()

    def test_false_delivered_digest_is_rejected(self):
        self.preserve()
        self.report["documents"]["lower"]["delivered_pdf_sha256"] = self.rebuilt
        with self.assertRaisesRegex(ValueError, "stale preserved PDF"):
            self.validate()

    def test_changed_delivery_rehashed_in_report_still_fails_manifest(self):
        self.preserve()
        pdf = self.lower / "supplement.pdf"
        pdf.write_bytes(pdf.read_bytes() + b"tampering\n")
        self.report["documents"]["lower"]["delivered_pdf_sha256"] = digest(pdf.read_bytes())
        with self.assertRaisesRegex(ValueError, "lower payload hash: supplement.pdf"):
            self.validate()

    def test_preservation_cannot_hide_changed_source(self):
        self.preserve()
        source = self.lower / "supplement.tex"
        source.write_bytes(source.read_bytes() + b"changed mathematical source\n")
        self.report["documents"]["lower"]["source_sha256"] = digest(source.read_bytes())
        with self.assertRaisesRegex(ValueError, "lower payload hash: supplement.tex"):
            self.validate()

    def test_legacy_report_still_requires_delivered_rebuild_equality(self):
        self.validate()
        self.report["documents"]["lower"]["pdf_sha256"] = self.rebuilt
        with self.assertRaisesRegex(ValueError, "stale build PDF: lower"):
            self.validate()

    def test_preservation_policy_is_explicit_and_complete(self):
        self.preserve()
        record = self.report["documents"]["lower"]
        record["delivery_policy"] = "ignore-delivery"
        with self.assertRaisesRegex(ValueError, "unknown lower delivery policy"):
            self.validate()
        record["delivery_policy"] = "preserved-baseline"
        del record["matches_preserved_pdf"]
        with self.assertRaisesRegex(ValueError, "missing preserved PDF comparison"):
            self.validate()

    def test_main_and_upper_remain_strict_even_with_preservation_metadata(self):
        for name in ("main", "upper_supplement"):
            with self.subTest(name=name):
                record = self.report["documents"][name]
                delivered = record["pdf_sha256"]
                record.update(pdf_sha256=self.rebuilt, delivered_pdf_sha256=delivered,
                              delivery_policy="preserved-baseline", matches_preserved_pdf=False)
                with self.assertRaisesRegex(ValueError, "stale build PDF: " + name):
                    self.validate()
                record["pdf_sha256"] = delivered

    def test_builder_records_actual_rebuild_and_leaves_s1_bytes_untouched(self):
        before = {p.name: p.read_bytes() for p in self.lower.iterdir()}
        rebuilt_pdf = b"fresh S1 PDF bytes\n"
        rebuilt_record = dict(self.report["documents"]["lower"], pdf_sha256=digest(rebuilt_pdf))
        with patch.object(builder, "HERE", self.here), \
             patch.object(builder, "compile_document", return_value=(rebuilt_pdf, rebuilt_record)), \
             patch.object(builder.subprocess, "check_output", return_value=b"test compiler\n"):
            builder.build(["lower"])
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.lower.iterdir()})
        saved = json.loads((self.here / "BUILD_REPORT.json").read_text())["documents"]["lower"]
        self.assertEqual(saved["pdf_sha256"], digest(rebuilt_pdf))
        self.assertEqual(saved["delivered_pdf_sha256"], self.delivered)
        self.assertFalse(saved["matches_preserved_pdf"])
        self.assertEqual(saved["delivery_policy"], "preserved-baseline")


if __name__ == "__main__":
    unittest.main()
