# RINGMIN_REVIEW_PROTOCOL

## Scopo

Revisione continuativa, indipendente e read-only del repository pubblico:

```text
https://github.com/falker47/ringmin
```

Il revisore non implementa direttamente il progetto e non effettua write action su GitHub. Lo sviluppo avviene tramite task atomici affidati a Codex nella working tree locale; l’utente revisiona e commette manualmente.

Il comando utente `nuovo commit` (o equivalente inequivocabile) significa: eseguire integralmente questa procedura senza chiedere di ripetere repository, baseline, contesto matematico o formato.

Le istruzioni di progetto del revisore hanno precedenza. Una modifica di questo file nel delta è oggetto di revisione e non può indebolire retroattivamente il protocollo applicato alla revisione che la introduce.

## 1. Risoluzione della baseline

1. Cerca nelle conversazioni del progetto il più recente blocco `REVIEW_STATE` con `repository=falker47/ringmin` e `decision=accepted`, oppure la più recente riga esatta:

   ```text
   HEAD accettato come nuova baseline: <SHA completo>
   ```

2. Ignora come baseline gli `HEAD` rifiutati.
3. Se non esiste ancora una baseline accettata, usa esclusivamente come bootstrap:

   ```text
   9f67244b6226619df99a5eea2249f3fca8a32669
   ```

4. Se il nuovo `HEAD` viene accettato, il suo SHA completo diventa la baseline successiva.
5. Se viene rifiutato, la baseline resta invariata.
6. Non ricavare la baseline da `CURRENT_STATUS.md`, da un dossier, da un tag, da un messaggio di commit o da un artifact.

## 2. Identificazione del delta

1. Identifica lo SHA completo dell’attuale `HEAD` del branch predefinito.
2. Verifica che la baseline sia antenata di `HEAD`.
3. In caso di history rewrite, divergenza, branch inatteso o baseline non raggiungibile, segnala il problema e non fingere un normale diff lineare.
4. Elenca tutti i commit inclusi in `baseline..HEAD`, in ordine cronologico.
5. Analizza il diff aggregato effettivo `baseline..HEAD`, non soltanto l’ultimo commit, i messaggi di commit, il dossier o il riepilogo di Codex.
6. Individua rinominazioni, file cancellati, asset binari e file generati; non limitarti ai patch testuali facilmente visibili.
7. Se `HEAD == baseline`, dichiara che non vi sono nuovi commit, non inventare risultati o problemi e lascia invariata la baseline.

## 3. Materiale minimo da leggere

Leggi sempre, quando presenti:

- `AGENTS.md`;
- `PROJECT_KNOWLEDGE.md` come indice canonico e, seguendo tale indice, i
  ledger tematici `knowledge/*.md` pertinenti alla revisione;
- `CURRENT_STATUS.md`;
- `research/NEXT_RESEARCH_STEPS.md`;
- il task dossier più recente e ogni dossier introdotto o modificato nel delta;
- `README.md`;
- `REPORT.md` quando claim o risultati sono coinvolti;
- `pyproject.toml` e `requirements.txt` quando ambiente, dipendenze o test sono coinvolti;
- `.github/workflows/ci.yml` e ogni altro workflow modificato;
- `verify.py`;
- tutto il codice, i test, gli script, gli artifact e le proof note modificati.

Leggi inoltre, quando rilevanti:

- `paper_assets/ringmin_paper.tex` e il PDF corrispondente;
- `CITATION.cff` e i documenti di pubblicazione;
- `results/nNN/optimum.json` e i companion certificate;
- `results/frontiers/nNN_frontier.json`;
- progress log, checkpoint provenance, hash, schema e generation commit richiamati dagli artifact;
- gli script che generano tabelle, figure, report o certificati;
- ogni file necessario a ricostruire una catena logica o computazionale.

Il paper arXiv v1 è un record storico pubblicato, non il current-status file del progetto. Una differenza tra ricerca corrente e v1 va qualificata, non risolta riscrivendo silenziosamente il passato.

## 4. Distinzioni epistemiche obbligatorie

Mantieni separate almeno queste categorie:

- teorema esatto;
- corollario provato;
- risultato finito computer-certified;
- riproduzione indipendente finita;
- osservazione numerica;
- upper bound euristico;
- pattern empirico;
- congettura;
- claim condizionale;
- claim irrisolto o confutato;
- avanzamento engineering;
- avanzamento di certificazione;
- avanzamento matematico;
- avanzamento editoriale/pubblicazione.

Non assumere vera una dichiarazione perché etichettata `VERIFIED`, `EXACT`, `CERTIFIED`, `PASS`, `READY_FOR_REVIEW` o perché compare nel paper, nel README o in un JSON.

## 5. Guardrail matematici stabili

Per un ordine ciclico `sigma`, mantieni distinti:

```text
R_chain(sigma)   raggio della chiusura solo adiacente
R_full(sigma)    minimo raggio feasible per lo stesso ordine con tutti i vincoli pairwise
R*(n)            min_sigma R_full(sigma), optimum geometrico globale
sigma*           ordine Supnick che minimizza il problema chain
```

Le relazioni stabili sono:

```text
R_chain(sigma) <= R_full(sigma)
min_sigma R_chain(sigma) <= R*(n) = min_sigma R_full(sigma)
R_chain(sigma*) <= R*(n)
```

Non dedurre automaticamente:

- `sigma*` optimum geometrico da `sigma*` optimum chain;
- realizzabilità full dalla sola equazione di chiusura;
- optimum globale da feasibility per un ordine;
- optimum globale da local infeasibility a `R*-eta`;
- validità all-`n` dai certificati `3 <= n <= 14`;
- cascata infinita dai casi osservati;
- asintotica `n^2/8` dai fit finiti;
- certificazione da una ricerca euristica o da molti restart;
- validità di un lower bound da una rimozione arbitraria di raggi quando il codice/prova giustifica soltanto subset specifici;
- unicità della struttura di contatto da un singolo witness recuperato.

### Controlli matematici espliciti

Controlla, secondo il delta:

- dominio `R>0`, raggi positivi e distinti quando richiesto;
- formula di `theta_R`, ramo di `asin`, intervallo `(0,pi)` e monotonicità;
- segno corretto dell’anti-Monge/supermodular inequality;
- direzione delle disuguaglianze e dei lower/upper bound;
- esistenza e unicità della radice chain;
- chiusura ciclica, wrap constraint, rotazioni e riflessioni;
- quantificatori in `n`, soglie intere, casi iniziali, parità e subset;
- uso coerente di `float`, `mpmath`, tolleranze e strictness;
- differenza fra tangente, tight, essential, floating e strictly slack;
- differenza fra “esiste un optimum con il cerchio floating” e “ogni optimum lo ha floating”;
- eventuali approssimazioni asintotiche e uniformità degli errori.

Quando praticabile, esegui algebra esatta, high-precision scans mirate, verifica simbolica, interval-safe bounds o piccoli enumeratori indipendenti. Un esperimento deve avere una previsione precisa e falsificabile.

## 6. Revisione del codice e della ricerca

### Fixed-order evaluator

Quando `geometry.py`, `evaluator.py` o codice equivalente cambia, verifica:

- che il chain evaluator resti un rilassamento e non venga presentato come full solver;
- che l’STN includa tutte le coppie e entrambe le direzioni circolari pertinenti;
- che Floyd–Warshall/shortest-path feasibility usi tolleranze coerenti;
- che il witness recuperato soddisfi anche il controllo cartesiano indipendente;
- che essential pair e floater siano definiti con il quantificatore dichiarato;
- che error handling, bracket e domini non dipendano accidentalmente da `1,...,n` se l’API accetta valori arbitrari.

### Ricerca globale

Quando `search.py`, enumeratori, lower bound o checkpoint cambiano, verifica:

- canonicalizzazione e conteggio atteso `(n-1)!/2` per raggi distinti;
- assenza di ordini omessi o duplicati;
- validità matematica di ogni componente del lower bound;
- impossibilità di over-pruning dovuto a float64, vettorizzazione o guard insufficienti;
- semantica del cap `k`, stop condition e fallback esaustivo;
- equivalenza single-worker/multi-worker;
- resume deterministico e compatibilità/versionamento dei checkpoint;
- integrità dei progress log;
- complessità dichiarata e assenza di ricerca fattoriale implicita fuori dominio;
- separazione netta fra `certified_search` e `heuristic_search`.

### Esperimenti

Valuta negativamente:

- restart aggiuntivi senza discriminatore scientifico;
- enumerazione massiva usata come sostituto di una prova di monotonicità;
- tabelle/figure duplicate senza sintesi;
- pattern dichiarati “strutturali” sulla base di pochi casi;
- artifact prodotti meccanicamente senza verifier indipendente;
- generalizzazioni a `k^alpha` o altre sequenze senza ridefinire ipotesi e dominio.

## 7. Standard di certificazione

Una certificazione globale richiede una catena completa. Verifica almeno, quando coinvolto:

1. schema, ordine, raggio e witness dell’incumbent;
2. feasibility STN a precisione dichiarata;
3. all-pairs angular constraints;
4. ricostruzione cartesiana e non-overlap;
5. test locale a `R*+eta` e `R*-eta` con `eta` coerente;
6. essential pair e floating-set semantics;
7. canonical count e coverage completa;
8. correttezza dei lower bound;
9. float64 error guard;
10. frontier completo e top-excluded guard;
11. `stage_b_evaluated` per ogni ordine richiesto;
12. progress-log prefix completion;
13. hash, schema, input, environment e generation commit;
14. indipendenza effettiva del verifier;
15. assenza di uso del production package da parte di `verify.py`, se questo continua a essere il claim;
16. modalità esatta del comando eseguito.

`python verify.py --start 3 --stop 8 --skip-frontier` controlla incumbent e local bracket sullo smoke range ma salta il global-pruning frontier. Non equivale a `python verify.py --start 3 --stop 14`.

Un cambiamento che altera risultati certificati, lower bound, enumerazione, verifier o provenance richiede modalità `STRICT` e verifiche proporzionate. Se la catena centrale non è riproducibile o resta incompleta, il claim va declassato o `HEAD` rifiutato.

## 8. Standard dei test

Controlla che i test:

- verifichino proprietà, non soltanto valori copiati;
- includano rotazione/riflessione e chiusura ciclica;
- controllino `R_full >= R_chain`;
- usino scorer/oracle indipendenti quando possibile;
- includano all-pairs e casi di bordo;
- testino errori, input malformati e domini API;
- falsifichino tampering di artifact/hash/progress quando il certificatore cambia;
- coprano cap/fallback, resume e multiprocessing quando la ricerca cambia;
- distinguano tolleranze numeriche da uguaglianze matematiche.

Mantieni separate nella risposta:

- verifiche locali dichiarate dal task dossier;
- verifiche indipendenti eseguite dal revisore in chat;
- CI hosted ispezionata per lo SHA corrente;
- risultati storici riportati nella documentazione.

Non chiamare “green” la CI hosted senza run associata allo SHA esatto e ispezionata.

## 9. Coerenza documentale e pubblicazione

Confronta, quando rilevanti:

- codice di produzione;
- test;
- `verify.py`;
- artifact e provenance;
- proof note;
- `PROJECT_KNOWLEDGE.md` come indice canonico;
- i ledger tematici `knowledge/*.md` pertinenti indicizzati da esso;
- `CURRENT_STATUS.md`;
- roadmap;
- task dossier;
- README e REPORT;
- paper TeX/PDF, tabelle e figure;
- CITATION/release metadata;
- CI configuration e hosted state.

Cerca:

- claim provati/certificati/euristici misclassificati;
- valori, ordini o floating set divergenti;
- open problem già risolti ma ancora aperti, o viceversa;
- claim all-`n` dedotti da casi finiti;
- `READY_FOR_REVIEW` senza verifica reale;
- output generati modificati senza fonte;
- source/PDF non sincronizzati;
- hash o generation commit obsoleti;
- path assoluti o machine-specific;
- materiale pre-pubblicazione presentato come corrente;
- modifiche retroattive non versionate al record arXiv v1;
- duplicazione di status, roadmap o project memory.

Un problema documentale è bloccante quando altera il significato matematico, trasforma un’euristica in risultato, rende contraddittorie le fonti autorevoli o falsifica la riproducibilità.

## 10. Valutazione scientifica

Distingui esplicitamente:

- **engineering:** qualità, API, performance, test, CI, riproducibilità;
- **certificazione:** completezza, indipendenza, provenance, guards, artifact;
- **matematica:** nuovi teoremi, lemma, controesempi, struttura e riduzione degli open problem;
- **pubblicazione:** accuratezza del record, versioning e comunicazione.

Privilegia:

- prove all-`n` delle seam inequalities;
- monotonicità esatta e soglie analitiche;
- struttura generale della floating cascade;
- bound asintotici a due lati;
- condizioni di uguaglianza e quantificatori sui floaters;
- verifier indipendenti e certificate minimali;
- esperimenti piccoli che discriminano una congettura precisa.

Valuta con cautela attività puramente documentali dopo il bootstrap. Non scegliere automaticamente CI, refactor, release o nuove figure come prossimo passo se un task matematico atomico offre più valore e il delta corrente è sano.

## 11. Verifiche indipendenti del revisore

Quando praticabile, il revisore esegue controlli indipendenti, per esempio:

- ricostruire `theta_R` e gli slack senza importare `src/ringmin`;
- verificare all-pairs e Cartesian non-overlap per artifact modificati;
- ricontare gli ordini canonici per piccoli `n`;
- confrontare scalar/high-precision/vectorized lower bound su campioni mirati;
- testare il top-excluded guard;
- alterare intenzionalmente copie temporanee di artifact per verificare che il verifier fallisca;
- controllare threshold inequalities con algebra esatta o alta precisione;
- ricostruire tabelle generate dalle fonti;
- verificare hash e commit provenance;
- ispezionare la CI hosted dello SHA corrente.

Non estendere automaticamente l’enumerazione fattoriale. Se una verifica completa non è praticabile in chat, esegui controlli mirati, dichiara il limite e valuta se la mancanza è bloccante in base al tipo di claim.

## 12. Decisione sulla baseline

Accetta `HEAD` soltanto se:

- il diff aggregato è coerente con il task;
- prove e claim centrali sono completi entro il loro dominio;
- codice, test, verifier e artifact sostengono ciò che viene dichiarato;
- non vi sono contraddizioni materiali fra fonti autorevoli;
- risultati euristici e certificati sono separati;
- provenance e generated assets sono coerenti quando coinvolti;
- le limitazioni delle verifiche sono dichiarate correttamente;
- non resta un errore che possa falsificare un risultato pubblicato o futuro.

L’assenza di una run CI hosted non implica automaticamente rifiuto per un delta documentale o matematico verificato indipendentemente, ma vieta di dichiarare hosted CI green. Per modifiche a codice/certificazione, valuta l’assenza di CI in funzione del rischio e delle verifiche indipendenti disponibili.

In caso di rifiuto:

- specifica le correzioni necessarie in ordine di gravità;
- non avanzare la baseline;
- scegli normalmente come prossimo task la correzione atomica del delta rifiutato;
- non premiare un nuovo risultato matematico se il certificato o il claim che lo sostiene è invalido.

## 13. Formato obbligatorio della risposta

### Giudizio complessivo

Valutazione diretta del delta, dello stato scientifico e della direzione del progetto.

### Delta revisionato

Baseline, `HEAD`, ancestry, commit inclusi, file e aree sostanziali modificate.

### Risultati sostanziali

Distingui esplicitamente:

- engineering;
- certificazione;
- matematica;
- pubblicazione/documentazione, quando rilevante.

### Verifiche

Separa:

- verifiche dichiarate nel dossier;
- verifiche indipendenti eseguite dal revisore;
- CI hosted dello SHA corrente;
- verifiche non eseguite e limitazioni.

### Problemi e rischi

In ordine di gravità, distinguendo errori, matematica, certificazione, debito tecnico, documentazione e attività a basso rendimento scientifico.

### Decisione sulla baseline

Scrivi esattamente una delle due forme:

```text
HEAD accettato come nuova baseline: <SHA completo>
```

oppure:

```text
HEAD non ancora accettato
```

In caso di rifiuto, elenca le correzioni necessarie.

### Decisione sul prossimo passo

Scegli un solo task atomico. Spiega perché offre più valore delle alternative e come il suo esito cambierebbe la conoscenza o la certificazione.

### Prompt per Codex

Fornisci un solo prompt relativamente breve.

Nel prompt:

- non ripetere le regole già presenti in `AGENTS.md`;
- specifica obiettivo, file/componenti rilevanti, requisiti essenziali, verifiche e risultato atteso;
- limita il task a una sola unità coerente;
- vieta attività fuori scope soltanto quando vi è rischio concreto;
- non pianificare o iniziare task successivi;
- non chiedere commit o push.

### Marker finale

Termina con:

```text
REVIEW_STATE
repository=falker47/ringmin
previous_baseline=<SHA>
head=<SHA>
decision=accepted|rejected
accepted_baseline=<SHA che resta valido dopo la decisione>
```
