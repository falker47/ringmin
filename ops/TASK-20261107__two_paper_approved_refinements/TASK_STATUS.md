# Task Status

```text
task=TASK-20261107__two_paper_approved_refinements
mode=STRICT
state=READY_FOR_REVIEW
started_at=2026-11-07
updated_at=2026-11-07
base_head=4303fe4d937c5f2c7915070a0aaffa67f9b448ca
branch=codex/ringmin-editorial-review
integration=local_commit_only_no_push
```

## Objective

Apply the author's seven exact approved prose replacements in the two journal
manuscripts, preserve the removed historical paragraph, and deliver synchronized
PDFs and a verified Paper II package with accurate per-document provenance.

## Scientific or engineering question

Engineering/editorial preservation: do the approved sources compile cleanly and
preserve all formulas, formal statements, proofs, citations, disclosures and
protected bytes? No mathematical claim, certified scope or accepted baseline is
advanced. Public arXiv versions are outside this task.

## In scope and expected delta

- Two main TeX sources and PDFs; Paper I build manifest.
- Paper II report, inner/outer manifests and source bundle.
- Three accompanying documentation files with stale build pointers/page count.
- CURRENT_STATUS.md and this task's audit/provenance dossier.

## Out of scope and protected paths

All other 857 baseline tracked files, including S1/S2 sources, PDFs, checkers,
public deposits, scientific code/results/certificates, proof notes, ledgers,
roadmap and all earlier dossiers. The preceding source ZIP is preserved in
ignored work storage and at the baseline Git blob. No push, merge, PR,
submission, Registry promotion or regeneration of S1/S2.

## Completion gates

- [x] Exact approved source hashes and baseline blob pins confirmed.
- [x] Full historical paragraph preserved with historical-only qualification.
- [x] Repeated three-pass main builds; zero final-log warnings; identical repeats.
- [x] Formula, statement/proof, citation, date/preamble and AI invariants checked.
- [x] 20 supplement files and complete inherited build records preserved.
- [x] Unchanged validate_build_report and verify_package.py pass.
- [x] Eight relevant PDF pages inspected; extracted-text spot checks pass.
- [x] Three current-document pointers synchronized; no stable claim duplicated.
- [x] Final diff, all 17 untracked files and whitespace inspected.
- [x] Local-only integration scope prepared; staged checks precede commit.

The exact resulting commit and post-commit working-tree state are reported in
the final CHATGPT_CODEX_HANDOFF_V1; no push is authorized for this task.

## Blockers

None. Cross-toolchain PDF identity and page counts are not asserted. Hosted CI,
mathematical certification and external independent acceptance are not claimed.

## Handoff

See EVIDENCE.md and FINAL_ARTIFACT_CHECKS.json. Integration is expressly local
only. Exactly one next atomic task: independent editorial/provenance review of
the resulting local commit, without scientific baseline promotion.
