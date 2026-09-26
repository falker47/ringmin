> DERIVED public copy of the historical audit; see ../EVIDENCE_MANIFEST.json and ../EVIDENCE.md.

# Log operativo dei comandi

I dettagli con stdout/stderr, exit code, URL e timestamp sono in commands.jsonl, nei file *.http.json e nei file di risposta nominati sotto. Le chiamate a connettori e web sono letture, non comandi shell. Non sono stati eseguiti comandi Git di scrittura.

## Avvio e fonti

- Get-Content AGENTS.md e Get-Content RINGMIN_REVIEW_PROTOCOL.md: lettura completata, exit 0; il protocollo è stato riletto da solo per evitare troncamento dell'output aggregato.
- git --no-optional-locks status --porcelain=v1 --untracked-files=all; git rev-parse --show-toplevel HEAD; git branch --show-current; git remote -v: tentativi iniziali respinti per dubious ownership. Il processo PowerShell aggregato terminava 0 a causa delle letture successive: questo non rappresenta successo dei singoli comandi Git.
- Ripetuti con git -c safe.directory=REPOSITORY_ROOT: successo. HEAD=80919666c3c54f8ce20cf66c456d413f6a2c075f; branch=main; origin=https://github.com/falker47/ringmin.git; solo lo ZIP esentato untracked. Nessuna configurazione persistente scritta.
- Get-Content PROJECT_KNOWLEDGE.md; Get-Content CURRENT_STATUS.md; Get-Content research/NEXT_RESEARCH_STEPS.md: exit 0, output conservato in startup0.json.
- Get-Content ops/TASK-20260919__archival_metadata/TASK_STATUS.md; Get-Content ops/TASK-20260919__archival_metadata/EVIDENCE.md; Get-Content reproducibility/global_brackets/README.md; Get-Content paper_assets/journal_dcg/README.md; Get-Content paper_assets/journal_dcg/BUILD_MANIFEST.json: exit 0, output in sources.json.
- rg -n '^#{1,4} |Zenodo|zenodo|PersonalContext|[A-Z]:[/\\]|/tmp/' sulle due knowledge richieste, SOURCE_MAP e dossier: indice mirato, exit 0.
- Get-Content reproducibility/global_brackets/manifest.json; Get-Content knowledge/CERTIFICATION.md | Select-Object -Skip 47 -First 59; Get-Content knowledge/FIXED_ORDER_THEORY.md | Select-Object -Skip 1937 -First 45; Get-Content paper_assets/journal_dcg/SOURCE_MAP.md | Select-Object -First 49: exit 0, output in reads_remote_attempt.json.
- Get-Command gh,python -ErrorAction SilentlyContinue | Select-Object Name,Source: Python disponibile; gh non trovato. Il programma Python reale è registrato da python_environment.json.
- Get-ChildItem -LiteralPath reproducibility/.work/archival_metadata -Force | Select-Object Name,Mode,Length: exit 0; unica voce cff-tools.
- Letture delle skill Google Drive, Google Sheets e reference-live-read-search-safety.md effettuate tramite Get-Content, exit 0.

## Remoto e isolamento

- Nuova directory esterna creata con New-Item e suffisso UTC/GUID: questa directory. Nessun checkout/worktree/branch creato.
- git -c safe.directory=REPOSITORY_ROOT ls-remote origin refs/heads/main refs/tags/v1.1.0-dcg-presubmission 'refs/tags/v1.1.0-dcg-presubmission^{}': primo tentativo sandbox fallito per rete; retry elevato autorizzato exit 0, output in remote_refs.json.
- python -B "AUDIT_ORIGINALS/audit_helper.py" local: exit 0; 702 hash iniziali (701 tracked + ZIP), status/staged/HEAD, albero baseline e CFF, ambiente Python. git cat-file -t sul main remoto non presente localmente ha exit 128, registrato come disponibilità locale, non identity mismatch. Nessun fetch nel repository.
- python -B "AUDIT_ORIGINALS/audit_helper.py" fetch https://api.github.com/repos/falker47/ringmin/releases/tags/v1.1.0-dcg-presubmission github_release.json: exit 0, HTTP 200.
- python -B "AUDIT_ORIGINALS/remote_read.py": exit 0; quattro GET parallele GitHub compare, tag, README main e Zenodo search, tutte HTTP 200. Gli URL esatti sono nel helper e nei log HTTP.
- python -B "AUDIT_ORIGINALS/archive_acquisition.py": exit 0; quattro GET parallele per record Zenodo, DOI, archivio e documentazione CFF, tutte HTTP 200. Timestamp e hash salvati.
- Le richieste di rete elevate sono state autorizzate dal sistema di permessi. Non è stato installato software o modificato alcun servizio.

## Verifiche eseguite

- python -B "AUDIT_ORIGINALS/compare_archive.py": exit 0; checksum/sicurezza membri/albero completo 701 file PASS; originali 13 PASS; ancestry e sei commit lineari README-only PASS. Usa git ls-tree e git cat-file --batch; comando e digest dell'output binario nei log.
- python -B "AUDIT_ORIGINALS/run_verifier_once.py": exit 0; avvia esattamente una volta il comando seguente dalla directory extracted.
- python -I -S verify_global_brackets.py: exit 0, stderr vuoto, PASS_GLOBAL_BRACKETS e pinned_input_verification=PASS. Ambiente e output completo in verifier_execution.json, verifier.stdout.txt, verifier.stderr.txt. Nessun --mathematical-only o generatore.
- python -B "AUDIT_ORIGINALS/audit_helper.py" final: exit 0; snapshot repository_after.json e status_after.json.
- python -B "AUDIT_ORIGINALS/finalize_audit.py": exit 0; confronto metadati, preservazione, 13 hash BUILD_MANIFEST e preservazione dell'estratto dopo il verifier PASS; produce AUDIT.md, EVIDENCE.json e CHECKPOINT.md.

## Connettori e tentativi non shell

- Google Drive/Sheets: metadata Registry; State A1:AA10; History A1:AA50 e A51:G100; ricerca mirata PersonalContext, lettura del router e projects/ringmin.md. Soltanto letture; risposte conservate selettivamente.
- Web open release GitHub e ricerca Zenodo: cache miss/inaccessibilità; web search sito Zenodo per ringmin e versione senza risultati. Nessuna inferenza di assenza. L'API Zenodo successiva ha dato un record pubblicato.
- Tentativo di salvare un JSON troppo lungo in un argomento shell: Windows errore 206 prima dell'avvio, nessun file prodotto da quel tentativo; salvataggio poi riuscito con apply_patch esterno.
- Un invio del generatore di report via functions.exec ha avuto SyntaxError nel wrapper JavaScript prima di ogni tool call; nessuno script o verifier avviato. Wrapper corretto e finalizzazione riuscita.
- Helper e report scritti esclusivamente qui con apply_patch o operazioni Python. I cookie di trasporto non sono conservati nei log finali; i byte dei payload acquisiti e i relativi hash non sono stati alterati.

## Limite delle attestazioni

Le letture documentali riportano risultati storici, non li rieseguono. Non sono stati eseguiti test di solver, ricerche, build, CI, generatori, retained pilots o verifier storico. Il controllo indipendente in questa task riguarda identità e byte; la singola esecuzione è dello stesso verifier archiviato.

