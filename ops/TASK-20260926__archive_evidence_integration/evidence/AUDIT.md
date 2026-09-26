> DERIVED public copy of the historical audit; see ../EVIDENCE_MANIFEST.json and ../EVIDENCE.md.

# POST-RING-6 — Archive Evidence Audit

**PASS — modalità STRICT, audit read-only.** Verificata la catena release, tag,
snapshot accettato, record Zenodo pubblicato, DOI di versione, archivio e verifier.
Nessuna nuova accettazione scientifica, promozione di baseline o autorizzazione
alla submission deriva da questo esito.

## Identità e letture live

- Repository locale: REPOSITORY_ROOT; branch main, HEAD 80919666c3c54f8ce20cf66c456d413f6a2c075f.
- Main remoto: 7201f788b586ae059078dde6221d58b0ce8f79a1.
- Registry (private source; see registry_state.json):
  riga ringmin, baseline 80919666c3c54f8ce20cf66c456d413f6a2c075f, stato accepted,
  updated_at_utc=2026-09-19T18:33:13Z. Riletti State e History.
  Le accettazioni pregresse ricevute restano decisioni di review precedenti.
- Compare API: baseline antenata di main, sei commit lineari, zero behind,
  delta aggregato esclusivamente README.md; controllato ogni parent.
  Nessuna novità rispetto all'handoff, nessuna accettazione di main.
- [Release GitHub](https://github.com/falker47/ringmin/releases/tag/v1.1.0-dcg-presubmission): ID 392208463;
  titolo: Ringmin 1.1.0-dcg-presubmission - finite DCG pre-submission companion; pubblicata 2026-09-19T20:41:26Z;
  draft=false, prerelease=false; nessun asset caricato separatamente.
  Lo stato editoriale rimane pre-submission.
- Tag v1.1.0-dcg-presubmission: oggetto commit 80919666c3c54f8ce20cf66c456d413f6a2c075f,
  verificato da ls-remote e API refs. Il target_commitish=main non identifica
  lo snapshot ed è stato tenuto distinto.
- [Record Zenodo](https://zenodo.org/records/22849826): 22849826,
  status=published, state=done, submitted=true; creato 2026-09-19T20:41:42.893111+00:00.
- [DOI di versione](https://doi.org/10.5281/zenodo.22849826):
  HTTP 200 alla pagina https://zenodo.org/records/22849826.
  Concept DOI osservato nel record: 10.5281/zenodo.22849825;
  non risolto separatamente e non usato come DOI della versione.

Risposte, timestamp, URL e hash: file *.http.json e risposte JSON originali.
I cookie di trasporto sono esclusi dai log conservati. Registry: registry_*.json.

## Metadati effettivi e differenze letterali

Confrontati con CITATION.cff letto tramite git show dal commit del tag e con
Expected Zenodo metadata nel dossier richiesto. Dettagli: metadata_comparison.json.

| Campo | Osservato |
|---|---|
| Tipo | Software |
| Titolo software | Ringmin: minimum central circle software and exact finite certificates |
| Creatore | Falconi, Maurizio; nessun ORCID; affiliation null |
| Licenza | mit-license; pagina risolta collega la licenza MIT |
| Keyword | Esattamente le sette keyword CFF |
| Descrizione | CFF identico dopo sola decodifica delle entità HTML |
| Repository | https://github.com/falker47/ringmin |
| Versione CFF | 1.1.0-dcg-presubmission |
| Versione Zenodo | v1.1.0-dcg-presubmission |
| Relazione | isSupplementTo al tree GitHub del tag |

La versione Zenodo include il prefisso v e coincide esattamente con il tag;
il CFF lo omette. Il link depositato usa /tree/tag, non /releases/tag/.
Sono differenze letterali esplicitamente registrate, non discrepanze materiali
d'identità: repository, tag e payload verificati identificano la stessa versione.
Non si attribuisce a Zenodo un algoritmo di conversione non verificato.
Titolo software CFF e titolo release sono distinti.

La descrizione include arXiv:2607.28654v2, il limite n=14 e il carattere
pre-submission senza journal acceptance. Nessuna relazione bibliografica
strutturata ad arXiv è presente, né richiesta dal mapping documentato.
La [documentazione ufficiale CFF](https://help.zenodo.org/docs/github/describe-software/citation-file/)
è stata riletta, ma la sua conversione non è prova di deposito.
Non è stato necessario accedere a bozze o usare autenticazione Zenodo.

## Archivio: confronto indipendente dei byte

Acquisito dal link effettivo del record:
https://zenodo.org/api/records/22849826/files/falker47/ringmin-v1.1.0-dcg-presubmission.zip/content

- Acquisizione: 2026-09-26T16:17:23.975530+00:00.
- Dimensione locale e dichiarata: **7.121.271 byte**.
- MD5 locale e dichiarato: c9521218ecd506a591d9de508d065370.
- SHA-256 locale: fa23122ab8907af001b0ecdde0900530573a61b5d4749971f141115d7017d087.
- Solo prefisso rimosso: falker47-ringmin-8091966/.
- **701/701 file byte-identici ai blob Git** del commit 80919666c3c54f8ce20cf66c456d413f6a2c075f.
- **0 mancanti, 0 extra, 0 contenuti diversi**.
- **152 membri directory**, tutti giustificati dall'albero.
- Ispezione pre-estrazione: nessun traversal, nome assoluto/ambiguo Windows,
  duplicato/collisione case-insensitive, link simbolico o membro cifrato.
- **13/13 originali** corrispondenti a dimensioni e SHA-256 del manifest.
- Report Windows: 350201 byte; SHA-256
  96bdf9b53977724f1b8c0640425365bf32897fd4415104f17bfd1afbfa52c693.
- 6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0
  resta il digest del campo certificate canonico, non dei byte del report.

ARCHIVE_INVENTORY.csv riporta percorso, modalità/ID blob Git, dimensioni,
SHA-256 ed esito per file. zip_members_before_extraction.json conserva i membri.
Il confronto usa git ls-tree e git cat-file --batch, non il checkout Windows.
Nessuna normalizzazione CRLF/LF del payload.

Inclusi tutti i verifier, codice/test, certificati/originali, proof note, dossier,
manoscritto e manifest journal, fonti storiche e sequel, nei distinti ruoli.
Assenti .git, cache/file extra e ZIP untracked esentato. Le fixture
DELIBERATELY_INVALID restano input negativi intenzionali, non certificati.
Anche i 13 hash del BUILD_MANIFEST journal corrispondono, secondo
la sua convenzione esplicita sui testi protetti; nessun build è stato eseguito.
La copia estratta conserva tutti i byte dopo l'esecuzione.

## Verifier: una sola esecuzione completa

Comando dalla copia estratta:

~~~text
python -I -S verify_global_brackets.py
~~~

Python 3.14.3, Windows 11 build 26200, sola standard library senza site.
Interprete in python_environment.json; cwd in verifier_execution.json.
Inizio 2026-09-26T16:24:21.969465+00:00, fine 2026-09-26T16:24:26.016113+00:00;
tempo processo 4.047 s. **Exit code 0**, stderr vuoto.

Output: **PASS_GLOBAL_BRACKETS**, input binding **PASS**, 13 originali, 908
intervalli, 47 witness, 3.004 coppie esterne, 6.008 disuguaglianze angolari,
copertura dichiarata dal verifier 3.374.988.556 classi.
Output integrale: verifier.stdout.txt e verifier_execution.json.

È esecuzione osservata dello **stesso verifier archiviato**, non nuova proof
review o nuovo cross-check matematico. Il confronto dei byte è un controllo
di integrità indipendente dal solver. Autenticità dell'esecuzione generatrice
e metadati storici restano non controllati, come dichiara l'output.

## Fonti, preservazione e limiti

Letti AGENTS.md e RINGMIN_REVIEW_PROTOCOL.md, indice, stato e priorità archivistica;
dossier archivistico richiesto; README e manifest global_brackets e journal_dcg;
sezioni pertinenti di CERTIFICATION, FIXED_ORDER_THEORY e SOURCE_MAP.
PersonalContext 00_README.md e projects/ringmin.md sono stati letti tramite Drive:
il checkpoint Windows del 17 settembre è storico e superato dalle accettazioni
successive e dagli input versionati. Nessun report è stato richiesto o rigenerato.

Controllato il percorso locale documentato reproducibility/.work/archival_metadata:
contiene cff-tools. Nessuna scansione indiscriminata del disco, dossier o checkpoint.
La ricerca web senza risultati non è stata usata per negare l'esistenza del deposito;
l'API ufficiale Zenodo ha restituito il record.
Primi tentativi web: cache miss/inaccessibilità. Ownership Git risolta con
safe.directory limitato al comando, senza scrivere configurazioni. Rete sandbox
risolta con letture elevate autorizzate. Un log troppo lungo come argomento shell
ha fallito prima dell'avvio ed è stato salvato con patch nella directory esterna.

Preservazione finale: **701 tracked e ZIP untracked invariati**; tracked/staged
senza modifiche. Resta soltanto:
paper_assets/v1_correction/source_bundle/ringmin_finite_v2_arxiv.zip.
Il suo SHA-256 è e6abaf4cffadf8a72c520b71adf66bc13b1870ab8fe7bd25ad79aad5a04689db.
HEAD, index, config, packed-refs e riferimenti Git nominati invariati.
Cache ignorate non scansionate. Nessuna modifica a repository, servizi,
Registry o PersonalContext; nessun commit/push.

La CI run 35830854156 success è solo handoff ricevuto, non riletta e non prova
archivistica. Non eseguiti test, build, generatori, piloti, ricerche, verifier
storico o recupero checkpoint. Nessuna revisione matematica riaperta.

Il claim finito pregresso resta: per ogni n=3,...,14,
L_n < R*(n) <= U_n, larghezza esattamente 10^-11.
Non implica uguaglianze decimali, unicità, classificazione di ordini ottimi,
proprietà universali floating/contatto, n>14 o certificazione retroattiva float64.
Il pacchetto seam del manoscritto resta criterio fixed-order generale,
persistenza per k fissato e k=1,2,3 con onset 8,13,17.
Prova matematica, review indipendente del workflow, risultati storici,
esecuzione osservata e peer review editoriale sono livelli distinti.

**Missing evidence: NONE per i criteri dell'audit.**
external_writes=NONE indica nessuna scrittura sui servizi; i soli output
locali autorizzati sono in AUDIT_ORIGINALS.

## Prossima task proposta, non eseguita

Riconciliare la documentazione archivistica con release e DOI verificati, in una task distinta senza modificare i claim scientifici.

Checkpoint completo: CHECKPOINT.md. Evidenze strutturate: EVIDENCE.json.
