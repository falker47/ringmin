# Task log

## 2026-11-21 · Startup and publisher instructions

Read the repository contract, compact project index, current status, finite-certification entry and relevant publication roadmap. Matched the clean local checkout, remote branch and live PR #12 to `040d301e600acc12430f76333ec3243268dd3d3e`. Created the requested branch from that revision. The expected changes were confined to the new publication directory, its test and this dossier.

Read the live JOGO guidelines and followed Springer's journal-template download link. The official HTTP endpoint returned the ZIP. A first curl invocation could not write to a temporary path created in a separate Windows sandbox. A fresh download to the task's staging directory succeeded. Verified the archive CRC and hashed the archive and selected members. Read the original class, reference style, template example and user manual. Windows console encoding interrupted the first source-header inspection. Repeated the read as UTF-8 output while preserving the original publisher bytes.

## 2026-11-21 · Typesetting

Installed the four missing standard LaTeX dependencies in the existing user-level TeX Live 2025 installation. The Windows tlmgr launcher required registry access, and its command wrapper split a compound file-search expression. A single-filename query identified sttools, which supplies cuted. The install completed without changing the configured default package repository.

Ported the title block, abstract, keywords, MSCs, theorems, tables, figure floats, appendices and declarations. Incorporated the original table and appendix sources in place. Put the six original vector files beside the manuscript with the publisher's figure names. The build expands the maintained numbers file into one uploadable TeX source. Transcribed all 16 bibliography entries to BibTeX. In the first compiled bibliography the publisher style printed question marks for three missing publication locations and dropped two name particles. Supplied the verified locations and grouped the two family names. Checked the resulting bibliography and all DOI links.

## 2026-11-21 · Verification and handoff

The first full suite gave 98 passes and one failure. The regression isolated an extra wording change in the availability sentence. Restored the surrounding reviewed wording and kept the requested revision macro. The first auxiliary-file comparison recognized only 46 plain-number fields. A brace-aware reader then compared all 67 keys, including the 21 explicit appendix tags, and found zero numbering differences.

Rebuilt the final PDF, compared both scientific texts and all figures, compiled the flat export independently, inspected the rendered layout and verified all 48 endpoint strings and 16 DOI targets in the PDF. The final local suite passed all 99 tests. The [evidence](EVIDENCE.md) records the environment and reproduction commands. The handoff is independent review of the formatted draft.

## 2026-11-21 · Noninteractive test launch on Windows

On a second full run at commit `85954f2`, Windows rejected duplication of the pytest process's inherited standard-input handle before the new build subprocess could start. The suite reported 98 passes and one failure. The standalone three-pass build on that commit succeeded. Set the new test's child stdin to the null device, as in the existing journal test.

Reproduced the original handle error deliberately in a disposable process, then ran the corrected upload test with the same invalid parent handle. It passed. The full repository suite passed all 99 tests with the fix. Reviewed the three affected paths for the follow-up commit.
