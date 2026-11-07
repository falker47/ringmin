# Controllo indipendente del perimetro editoriale

Data: 7 novembre 2026. Modalita STRICT. Baseline:
7d257221d9034ca5f895f062e45e782d8e77b6c2.

## Esito e portata

Non sono state individuate modifiche del significato matematico nei due diff
editoriali congelati. Questa e una valutazione del confronto testuale svolta
da un agente distinto dagli editor dei due manoscritti, non una nuova revisione
delle prove, accettazione scientifica o approvazione esterna.

Sono stati letti integralmente i diff dei due sorgenti e i due rapporti
editoriali. Il controllo ha confrontato ciascuna aggiunta con il contesto
della baseline e con il ruolo del risultato gia enunciato; gli enunciati e le
prove non sono stati riesaminati per stabilirne la validita matematica.

## Paper I: significato delle modifiche

- La descrizione dei vincoli consecutivi spiega il rilassamento gia definito;
  la frase immediatamente successiva richiede tutti i vincoli di coppia per
  la geometria completa. Non introduce un'equivalenza catena/geometria.
- "Global infimum" coincide con la definizione nell'introduzione e non
  aggiunge un'affermazione di raggiungimento dell'infimo.
- "The certificate" risolve l'antecedente di "It". L'indipendenza dal pruning
  storico era gia esplicita per entrambi i lati nella sezione 6.
- "The argument has four parts" cambia la funzione della frase introduttiva,
  ma lascia intatti i quattro contenuti e il successivo paragrafo che distingue
  il risultato classico di Supnick dai contributi geometrici. Non cambia
  attribuzioni o affermazioni di novita.
- "Two independent arguments" conserva l'indipendenza dei due obblighi
  matematici. L'esclusione leggermente sopra il limite inferiore, il testimone
  superiore e il rapporto con il verificatore restano distinti.
- L'espansione di DP non altera la ricorrenza o la complessita. Il nuovo
  incipit sui floating conserva tutti i quantificatori e ribadisce il raggio
  al quale i testimoni hanno slack.
- La riproduzione distingue istruzioni dal resoconto storico senza aggiornare
  surrettiziamente l'ambiente, i conteggi o le dichiarazioni scientifiche.

## Paper II: significato delle modifiche

- L'apertura ripete il dominio dell'abstract: raggi interi consecutivi e
  tangenza esterna al cerchio centrale. Non introduce un altro problema.
- Il risultato anticipato resta quello di esistenza e caratterizzazione
  effettiva. La distinzione dalla valutazione efficiente rimane esplicita.
- I nuovi raccordi annunciano gli oggetti e i ruoli gia presenti. In
  particolare, "The closing estimate makes concatenation useful" richiama
  lo stesso costo unitario di separazione usato nella prova esistente:
  il testo non sostituisce la prova di concatenazione con il lemma di chiusura,
  ne afferma un costo totale indipendente dal numero di copie.
- Le due approssimazioni sono quelle della quantizzazione dei tipi e della
  lunghezza delle parole. Il bilanciamento e attribuito alla distribuzione,
  come nei vincoli del programma lineare, non a ogni parola individuale.
- Il raccordo alle costruzioni superiori annuncia il recupero di permutazioni
  effettive con fattibilita per tutte le coppie nel dominio dei blocchi che
  viene subito definito. Non promuove la sola correttezza delle marginali
  a fattibilita e non attribuisce ottimalita ai quattro blocchi.
- La descrizione della mappa delle dipendenze e piu ordinaria ma non elimina
  una fonte richiesta. La sezione inferiore, S1 e S2 rimangono protetti.
- L'ambiguita preesistente sul referente di "The lower and upper bounds"
  e segnalata, con una candidata separata, nel rapporto Paper II. Il diff
  non la corregge implicitamente e non rafforza la conclusione.

## Controlli eseguiti

Comando locale, dalla radice del worktree:

    python ops/TASK-20261107__two_paper_editorial_review/check_scope.py

Esito: exit 0. Il checker usa i blob Git della baseline per i due manoscritti
e la fotografia iniziale dei byte per gli altri file tracciati.

| Controllo | Risultato |
|---|---|
| Paper I | 19 ambienti protetti, 249 formule delimitate e 16 ambienti matematici invariati |
| Paper II | 14 ambienti protetti, 268 formule delimitate e 11 ambienti matematici invariati |
| Preamboli, label, occorrenze dei riferimenti e citazioni, disclosure | Invariati in entrambi |
| Paper I dopo l'inizio delle appendici | Invariato integralmente |
| Paper II sezione dell'endpoint inferiore | Invariata integralmente |
| Inventario protetto fuori dall'allowlist editoriale | 835 file tracciati identici byte per byte |
| Controlli negativi in memoria | Sei alterazioni di formula/prova/disclosure correttamente respinte |
| File modificati o aggiunti | Tutti nell'allowlist esplicita o nel dossier del task |

Il primo tentativo del checker aveva interpretato la spaziatura autore
doppio-backslash seguito da [3pt] come apertura di formula e aveva segnalato
un falso cambiamento. E stata corretta la distinzione fra il comando di
a-capo e il delimitatore matematico. Nessun manoscritto e stato modificato
per superare il controllo.

I conteggi non sono conteggi di teoremi: includono ambienti di prova,
definizione, tabella, bibliografia e verbatim. Le formule delimitate e gli
ambienti matematici sono categorie controllate separatamente.

## Identita dei sorgenti ispezionati

SHA-256 dei byte effettivi dopo la revisione:

- Paper I: cccbf47849706ed2abfc5184c02792884adbf4886acd665da6b49d62a9696ab4
- Paper II: 652ba43d477ab47485ebb65709af4674048e83f9bb886198afaf88a38d8f3d9b

## Riesame finale della correzione di impaginazione e della provenienza

Dopo il primo congelamento e stata riletta la sola ulteriore modifica a
Paper I: "The local reproduction for this manuscript used Python 3.14.3 and
returned" diventa "The manuscript's local Python 3.14.3 run returned".
Versione Python, natura locale e appartenenza al manoscritto rimangono identiche.
La modifica serve a risolvere l'overfull rilevato dal coordinatore; non
presenta il risultato storico come una nuova esecuzione del verifier.

Sono stati letti i diff dei due README, di READINESS.md e di
EDITORIAL_CHECKLIST.md, nonche i delta di BUILD_MANIFEST.json e
BUILD_REPORT.json. Sono stati ispezionati integralmente i helper task-local
editorial_build.py e compare_builds.py.

Controlli aggiuntivi eseguiti in sola lettura, exit 0:

- I record JSON lower e upper_supplement sono esattamente uguali ai record
  della baseline; non sono sostituiti con risultati della toolchain corrente.
- Gli hash di tutti gli input e dell'output dichiarati dal manifest di
  Paper I corrispondono ai byte attuali.
- Il checker di scope passa nuovamente dopo la correzione di impaginazione.
- Il comando python -I -S paper_assets/paper_ii_journal/verify_package.py
  restituisce PASS per 38 payload nell'archivio e 26 nel manifest candidato.

Il builder compila solo i due main con input dichiarati, tre passaggi isolati
senza shell escape, chiusura dei recorder e registrazione degli hash.
La consegna rifiuta sorgenti/PDF non corrispondenti ai record e warning residui.
L'esportazione aggiorna il bundle di Paper II ricopiando i byte dei supplementi.
Il confronto dei build controlla i record di warning, la ripetibilita dei PDF
e i numeri effettivi di label/citazioni negli aux: 58/6 per Paper I e 20/8 per
Paper II. I record esaminati riportano 19 e 9 pagine prima/dopo, senza nuovi
warning. Questa lettura e verifica di coerenza non e una mia riesecuzione dei
build o una nuova ispezione visiva delle pagine.

Era stata segnalata al coordinatore una residua frase non datata nel README
di Paper II, relativa al replay S1 in TeX Live 2023 e al gate require-delivered.
La correzione finale e stata riletta: ora attribuisce esplicitamente quegli
esiti al 3 novembre e dichiara che il gate sui tre documenti non e stato
rieseguito in questo task. Il problema documentario e risolto.
Dopo la riesportazione sono stati nuovamente eseguiti il verifier del pacchetto
(PASS: 38 payload archivio, 26 manifest) e il checker di scope (PASS: 835 file
protetti invariati), entrambi con exit 0. Nessun nuovo esito matematico o build
dei supplementi viene inferito.

## Limiti

Il checker e intenzionalmente locale e riconosce gli ambienti e i delimitatori
usati da questi sorgenti; non e un parser TeX generale. La conservazione
testuale non dimostra correttezza matematica. Il confronto semantico della
prosa e una valutazione editoriale separata, e non sostituisce la decisione
dell'autore sui punti lasciati aperti nei due rapporti.

Build, avvisi, immagini PDF, sincronizzazione degli archivi e stato finale
Git sono verifiche del coordinatore, registrate separatamente in EVIDENCE.md.
Non sono stati eseguiti qui verifier matematici, test del solver o hosted CI.
Le revisioni indipendenti dei supplementi non sono riaperte ne promosse da
questo controllo.

Il prossimo passo resta unico: revisione dell'autore dei due diff e delle
formulazioni candidate intenzionalmente non applicate.
