# Ringmin — revisione STRICT del candidato globale

Data: 17 settembre 2026. Oggetto: esclusivamente il pacchetto scientifico non committato allegato da Mauri. Nessuna accettazione di HEAD, promozione di baseline o chiusura nel Registry.

## 1. Verdetto

**Il payload originale supporta il claim `L_n < R*(n) <= U_n` per tutti gli interi `n=3,...,14`, con ampiezza esatta `10^-11`.** Ho ricostruito una catena di verifica distinta dai PASS presenti nel pacchetto: intervalli mediante il coseno, DP forward, visita completa della partizione e geometria cartesiana razionale. Non ho trovato un controesempio al claim originale né un errore nella sua riduzione matematica.

**L'attuale coppia di checker del pacchetto non è però accettabile come verificatore autonomo completo del claim: ho riprodotto un falso positivo sostanziale.** Entrambi accettano un certificato alterato per n=4 con `L=0.5`, `U=0.50000000001`, intervalli corretti, lower proof corretta e nessun testimone superiore. Il bound superiore è falso, dimostrabilmente anche senza calcolo trascendentale. Questo è un blocker P1 dell'integrazione del verificatore, non una confutazione del payload originale.

Il giudizio è una revisione computer-assisted del pacchetto identificato, non una prova verificata da proof assistant, una peer review umana o un'attestazione della CI hosted.

## 2. Identificazione e confini

| Oggetto | SHA-256 |
|---|---|
| ZIP caricato, `ringmin_global_interval_review_packet(1).zip` | `5b12b4580d6712b5d682defd569a5b32ef669d766c2c468d8b6aa4785d7ddefe` |
| Payload canonico `certificate` | `6f6c15e1db037a3faadadc52893a9a90ae7b59d6d5b42e934c81c1a0abd21cc0` |
| Report Windows, byte completi | `96bdf9b53977724f1b8c0640425365bf32897fd4415104f17bfd1afbfa52c693` |
| Report Linux originario, byte completi | `cfb95a8354c9ea0529f5ece85118712a3e94c36aed1e14a43b6f32c6e98549db` |
| Generatore `ringmin_global_interval_replay.py` | `e785b43bd2a24cf74d807479b5719e5f1b5e762027e41c4a69af07a655531549` |
| Campo CASES estratto dal sorgente come dato, senza eseguirlo | `cb24657c443010573cf85a54f9991e4288b46054094fd3069fe3d917a63a56f0` |

Ho letto `README_REVIEW.md`, `REVIEW_REQUEST.md`, la proof note, l'addendum e integralmente i tre programmi pertinenti prima delle esecuzioni. Ho consultato il PersonalContext canonico, iniziando da `00_README.md`, poi `projects/ringmin.md`, e le preferenze operative pertinenti; inoltre il protocollo corrente `RINGMIN_REVIEW_PROTOCOL.md` su GitHub. La voce Drive che indicava il JSON Windows ancora da acquisire è superata dalla dichiarazione dell'utente e dal report effettivamente presente e verificato nello ZIP. Non è un'attività da ripetere.

Questa non è una revisione di commit: non ho verificato un nuovo HEAD, la sua ancestry, la CI hosted o una transizione di Registry. Gli SHA storici di repository riportati dalle fonti non sono sostituiti da nuove affermazioni sullo stato corrente. Non ho scritto su Drive, GitHub o Registry, né alterato manoscritti, checkpoint o sorgenti originali. Tutti i 15 file estratti risultano ancora identici byte per byte ai membri dello ZIP; sono verificati anche CRC e manifest. Gli hash identificano i dati, non ne dimostrano la correttezza matematica.

## 3. Finding P1 — manca l'esistenza di un testimone superiore per ciascun n

**Severità: alta; blocker per integrare i checker come gate di certificazione completo.**

### Localizzazione

- `source/ringmin_global_interval_crosscheck.py:107-114`: il loop su `row['upper_witnesses']` può essere vuoto. Non esiste un controllo di cardinalità positiva per riga.
- Stesso file, `115-120`: il controllo negativo usa soltanto il primo caso, n=3. Non rileva l'assenza di testimoni nei casi successivi.
- Stesso file, `121-123`: il riepilogo PASS non impone un testimone per ogni caso.
- `source/windows_receipt_check.py:81-102`: `geometry` inizializza i contatori a zero e ritorna con successo se la lista è vuota.
- Stesso file, `136-148`: `main` non impone `nw >= 1` dopo la verifica geometrica.

Il problema logico è preciso: dimostrare che **ogni testimone presente** è valido non dimostra che **esista un testimone**. La proprietà universale è vera anche per l'insieme vuoto.

### Riproduzione eseguita

Ho generato esclusivamente copie locali deliberate, lasciando intatti tutti gli originali. In entrambe le copie Windows/Linux ho sostituito la riga n=4 con:

```text
L = 0.5; U = 0.50000000001; upper_witnesses = []
```

Ho ricalcolato correttamente gli intervalli angolari ai nuovi estremi, la prova inferiore e il digest canonico. Le due copie alterate concordano fra loro. Il fingerprint del sorgente corrisponde tuttora al sorgente originale: proprio perché un campo che dichiara quel fingerprint non autentica l'esecuzione che avrebbe prodotto il JSON.

Risultato reale di entrambi gli eseguibili: exit code 0 e PASS. Il crosschecker riporta 12 casi ma soltanto 46 testimoni. Una seconda variante duplica il testimone valido di n=3 e torna a **47 testimoni complessivi**, lasciando comunque n=4 privo di testimone: entrambi accettano ancora. Pertanto nemmeno una futura guardia sul solo totale 47 correggerebbe il difetto.

### Il bound alterato è realmente falso

Pongo `u=50000000001/100000000000`. Per la coppia di raggi 1 e 2,

`q_12 = 2 / ((u+1)(u+2)) > 1/2`,

perché

`4 - (u+1)(u+2) = 2499999999599999999999 / 10000000000000000000000 > 0`.

Per u positivo, `q_ab = [a/(u+a)] [b/(u+b)]` cresce con ciascun raggio. Fra tutte le coppie distinte di 1,2,3,4, q_12 è il minimo. Quindi ogni separazione minima è `2 asin(sqrt(q_ab)) > pi/2`. I quattro gap di qualsiasi ordine ciclico dovrebbero tutti superare pi/2, ma devono sommare 2*pi: impossibile. La stessa incompatibilità vale per ogni raggio positivo <=u, per monotonicità. Esiste anche un margine stretto, quindi l'infimum supera u.

Il test numerico indipendente conferma inoltre una violazione per tutte le tre classi canoniche anche a questo falso U; il margine minimo intero è `389980756458987491138532080958344493997 / 2^128` radianti. La dimostrazione analitica precedente rende il controesempio indipendente da qualunque kernel numerico.

### Impatto e rimedio minimo

Non è un difetto del payload originale: lì tutte le dodici righe hanno testimoni validi. Il generatore controlla già ordini non vuoti e distinti in `source/ringmin_global_interval_replay.py:425-429`. È un difetto nell'accettazione di evidenze ricevute dai checker.

Il futuro verificatore completo deve richiedere **almeno un testimone cartesiano valido per ciascun n**, dopo aver verificato schema e copertura dei casi. Per la riproduzione esatta di questo pacchetto deve anche controllare gli insiemi attesi degli ordini e le cardinalità per riga. Il claim matematico del solo upper bound richiede uno o più testimoni per n, non necessariamente tutti i 47: mantenere questa distinzione.

Regressioni obbligatorie: caso privo di testimone; bracket falso con intervalli e digest ricalcolati; redistribuzione dei testimoni che preserva il totale 47. Devono fallire per ragioni matematiche/schema, non soltanto perché il digest non coincide con un valore storico hardcoded.

Evidenze: `tests/adversarial_run/adversarial_results.json`, sottocartelle `FALSE_n4_bracket_empty_witness` e `FALSE_n4_bracket_47_total_witnesses`, `tests/reviewer_analytic_counterexample.json`.

## 4. Finding P2 — binding di input e tracce dichiarate non completamente verificati

**Severità: media per provenance e contratto del verificatore; non confuta il bracket originale.**

Sostituendo con 64 zeri sia `lower_bound.dp_table_sha256` sia `lower_bound.pruning_and_skeleton_stream_sha256` a n=14 e ricalcolando i digest dei report, entrambi i checker accettano. Anche un `input_cases_sha256` azzerato passa entrambi.

Localizzazione: `source/ringmin_global_interval_crosscheck.py:98-106` confronta soltanto una selezione di statistiche, non questi digest; `source/windows_receipt_check.py:125-130` controlla uguaglianza delle due copie e hash del file script, ma non estrae CASES per verificare il binding del contenuto; `source/ringmin_global_interval_replay.py:264-275,456-460` emette i digest dichiarati.

Questo non implica che la DP ricalcolata sia scorretta: il crosschecker ricalcola effettivamente il lower proof. Significa che non si può dichiarare verificata tutta la provenance o ogni hash annidato soltanto perché i due comandi terminano con successo. Il mio controllo indipendente originale ricostruisce e confronta le tracce DP/pruning; inoltre estrae CASES via AST e confronta esattamente estremi e ordini con il certificato (`reviewer_verify.py:269-287`).

Rimedio minimo: esplicitare quali campi siano evidenza verificata e quali metadati non decisivi; verificare il binding degli input e, se si dichiarano controllati, ricostruire i digest delle tracce. In alternativa non attribuire a tali digest un significato di verifica che i checker non implementano.

Nota sui test: la funzione `verify(..., pinned=False)` del nuovo script controlla il contenuto matematico, non il digest CASES; per questo la mutazione del solo input hash passa quella funzione. Il binding del suo entrypoint `main` è separato e il confronto con il digest estratto dal sorgente è stato testato separatamente, con esito di rifiuto (`tests/reviewer_analytic_counterexample.json`).

## 5. Derivazione del modello e lower bound stretto

Per due cerchi esterni a,b, i centri distano R+a e R+b dall'origine. Per una differenza angolare diretta delta in [0,2*pi],

`distance^2 = (a-b)^2 + 4(R+a)(R+b) sin^2(delta/2)`.

La non sovrapposizione equivale a `phi_ab(R) <= delta <= 2*pi-phi_ab(R)`, dove

`phi_ab(R) = 2 asin sqrt(ab/((R+a)(R+b)))`.

R>0 e a,b>0 danno q in (0,1); si usa il ramo principale, con phi in (0,pi). Non si deve imporre artificialmente che ciascun gap diretto sia <=pi. Per qualunque sottoinsieme ordinato ciclicamente, i suoi gap positivi sommano 2*pi. Ne segue la condizione necessaria `sum(phi_edges)<=2*pi`, anche quando uno dei gap supera pi.

La prova usa il ciclo completo, il ciclo indotto togliendo 1 e quello togliendo 1 e 2, solo se restano almeno tre vertici. Non sostiene che queste condizioni siano sufficienti alla realizzabilità. Una violazione stretta di una sola condizione necessaria basta a escludere un ordine.

Ho verificato anche il passaggio da infeasibilità in L alla disuguaglianza stretta sull'infimum. Ogni phi è continua e strettamente decrescente in R>0. Una violazione stretta persiste in un intervallo a destra di L; ci sono finitissime classi d'ordine. Prendendo il minimo degli intervalli si esclude un intero intorno destro comune: non soltanto il singolo punto L.

Per rendere questo passaggio quantitativo, il nuovo audit calcola un epsilon razionale positivo per ciascun n. Infatti

`|phi'_ab(R)| = sqrt(q/(1-q)) [1/(R+a)+1/(R+b)]`.

Per R>=L, un maggiorante razionale è ottenuto sostituendo la radice con `max(1,q_L/(1-q_L))` e i denominatori con quelli in L. Se m è il minimo margine intero di foglie/pruning, S=2^128 e B_n è n volte il massimo di questi maggioranti per coppia, `epsilon=m/(2 S B_n)>0` conserva una violazione di almeno metà del margine per tutti gli ordini coperti. Tutti i dodici epsilon sono strettamente positivi e inferiori alla larghezza del bracket; i razionali esatti sono nel report indipendente. Non serve assumere che l'infimum sia raggiunto.

Riferimenti originali: `source/ringmin_global_interval_proof.md:83-115`; `source/ringmin_global_interval_replay.py:129-142`. Nuovo controllo: `reviewer_verify.py:111-174,235-259`.

## 6. Intervalli: generatore, checker alternativo e controllo ulteriore

### Generatore arcsin

`source/ringmin_global_interval_replay.py:59-126` lavora con interi/Fraction e conversione finale sulla griglia S=2^128. La radice quadrata è racchiusa con isqrt sulla griglia 2^192; l'ineguaglianza dei quadrati è verificata. Nella serie positiva dell'arcsin, il rapporto dei termini del polinomio in q è

`q (2k+1)^2 / ((2k+2)(2k+3)) < q`.

Il resto positivo è dunque al più il primo termine omesso diviso per 1-q. Moltiplicazione degli estremi e floor/ceil finale hanno il verso corretto. Il budget di termini produce un errore esplicito se insufficiente, non un PASS approssimato. Il dominio q<0.9 è controllato per gli input effettivi.

Per 2*pi il generatore usa Machin con serie alternate razionali esatte; nel termine sottratto gli estremi vengono correttamente scambiati. Non ho trovato un errore nel segno del resto o nell'arrotondamento.

### Checker aritmetico alternativo

Il nuovo `windows_receipt_check.py:33-79` non assume gli intervalli salvati. Usa

`phi = 4 atan(sqrt(q)/(1+sqrt(1-q)))`

e aritmetica fissa a 256 bit. Se x e y sono i floor scalati di sqrt(q), sqrt(1-q), gli estremi `x/(P+y+1)` e `(x+1)/(P+y)` hanno il verso corretto. L'atan è monotona; i termini assoluti sono racchiusi prima dell'accumulo alternato. Il primo termine omesso è usato con il segno corretto, includendo gli errori degli arrotondamenti intermedi.

L'identità alternativa `2*pi = 8(atan(1/2)+atan(1/3))` è corretta: le due arctan positive sommano un angolo nel primo quadrante, con tangente 1. La conferma della reale inclusione nelle tabelle memorizzate avviene a `131-145`.

**Questo checker colma effettivamente il precedente confine di fiducia sugli angoli.** Non è solo una seconda stampa di cifre e non importa il generatore. Resta distinto dalla DP, che non implementa. Il P1 riguarda invece il controllo esistenziale dei witness.

### Nuovo metodo del revisore: coseno

Ho scritto `reviewer_verify.py` senza importare programmi Ringmin o moduli del pacchetto. Verifica `cos(phi)=1-2q` direttamente agli estremi salvati, usando Taylor del coseno e arrotondamenti esterni su griglia 2^224. I due endpoint sono in (0,3), dove il coseno è strettamente decrescente perché pi>3. Dimostrare `cos(lo)>1-2q>cos(hi)` prova l'inclusione senza riutilizzare né asin né atan né sqrt.

Il codice non assume che i primi termini del coseno siano decrescenti per x>sqrt(2): controlla la decrescenza della coda dopo il cutoff, dove viene applicato il resto alternato. Verifica anche il segno del coseno agli estremi di tau/4, isolando pi/2. Sono confermati tutti i 908 intervalli L/U e l'intervallo di 2*pi.

Riferimenti delle sole identità di serie: NIST DLMF 4.24.1 (arcsin), 4.24.3 (atan), 4.19.2 (coseno). La validità degli arrotondamenti e il giudizio sul codice sono oggetto di questa revisione, non certificati dal riferimento bibliografico.

## 7. DP, pruning e reinserimento di 1

La DP originale conserva il costo minimo da un ultimo vertice v, visitando una volta tutti i vertici di M e tornando all'ancora n:

`H(empty,v)=w(v,n)`;

`H(M,v)=min_{u in M} [w(v,u)+H(M\{u},u)]`.

Ogni ricorrenza riduce M e include l'arco finale. Sommare il costo del prefisso a H è quindi il minimo costo intero fra tutti i suoi completamenti, non un costo euristico. Il pruning usa esclusivamente `bound > tau_hi`; poiché w sono lower endpoints degli angoli, quel confronto esclude davvero ogni completamento. Non entrano float64, heap Top-K, cap o checkpoint storici.

Il nuovo audit usa una DP forward dei cammini dall'ancora. Per pesi simmetrici, l'inversione del cammino ricostruisce il costo di completamento; ho verificato la simmetria richiesta prima di usarla. Ricalcola anche digest delle tabelle e tracce di pruning, non solo il costo alla radice.

Per n<=9 il controllo è una enumerazione canonica diretta. Per n>=10, eliminare il vertice distinguibile 1 associa a ogni ciclo completo uno scheletro su 2,...,n. Viceversa, l'inserimento di 1 nei suoi n-1 spigoli ricostruisce tutte e sole le classi complete. Fra gli spigoli c'è quello dall'ultimo vertice all'ancora. La riflessione non fissa uno scheletro con almeno tre etichette distinte, perciò elimina esattamente un orientamento per coppia. La simmetria dei costi impedisce che un orientamento sopravviva e il suo inverso sia escluso per un diverso costo totale.

I tuple inseriti nell'ultimo gap possono non soddisfare il vecchio test second<last. Non è un bug: nel nuovo audit li normalizzo per rotazione/riflessione prima del confronto di classi. Il controllo trova 246 tuple non canonici in quel senso a n=13 e 18.660 a n=14, senza duplicazione di classi.

| n | Classi complete coperte | Scheletri canonici espansi | Ordini completi espliciti |
|---|---:|---:|---:|
| 3-9, totale | 23.116 | non applicabile | 23.116 |
| 10 | 181.440 | 0 | 0 |
| 11 | 1.814.400 | 0 | 0 |
| 12 | 19.958.400 | 0 | 0 |
| 13 | 239.500.800 | 246 | 2.952 |
| 14 | 3.113.510.400 | 18.660 | 242.580 |
| Totale | 3.374.988.556 | 18.906 | 268.648 |

A n=10,11,12 il lower bound dello scheletro alla radice basta già a escludere tutto. A n=13,14 i restanti ordini sono esplicitamente verificati dopo ogni inserimento. La tabella non significa che siano stati enumerati individualmente 3,37 miliardi di ordini: il resto è coperto dalla partizione matematica in sottoalberi esclusi.

Riferimenti: generatore `145-179,199-275`; proof note `173-251`; nuovo audit `99-174`.

## 8. Testimoni cartesiani razionali

Per parametro razionale t e raggio esterno r, il centro è

`C_r=(U+r) ((1-t^2)/(1+t^2), 2t/(1+t^2))`.

La norma quadrata è esattamente `(U+r)^2`, dunque la tangenza centrale è esatta. Per ogni coppia verifico direttamente `||C_a-C_b||^2-(a+b)^2 > 0` mediante Fraction. Le approssimazioni trigonometriche del generatore servono a proporre t, non all'accettazione geometrica.

Ho ricostruito tutti i 47 witness: **540 tangenze centrali, 3.004 coppie esterne**, tutte valide. Ho controllato anche gli ordini polari con semipiani e prodotti vettoriali delle coordinate, anziché riutilizzare il solo ordinamento dei parametri stereografici. Sono verificate inoltre 6.008 disuguaglianze angolari dirette/wrap nelle posizioni scalate salvate.

L'identità alternativa dei checker, con numerator `(U+a)(U+b)(s-t)^2-ab(1+s^2)(1+t^2)`, è corretta: moltiplicata per `4/[(1+s^2)(1+t^2)]` restituisce esattamente il gap cartesiano quadrato.

Riferimenti: generatore `278-373,433-439`; crosschecker `22-32`; receipt `81-102`; audit `176-219`. Nessuna tolleranza float è necessaria a questi confronti. La fattibilità a U non prova che i 47 ordini siano esattamente ottimi.

## 9. Esecuzioni effettive e falsificazione

### Eseguito in questa revisione

- Verifica degli originali, dei manifest e dell'uguaglianza del payload Windows/Linux, inclusa la corrispondenza a CASES estratto dal sorgente.
- Esecuzione isolata dei due checker originali sul report Windows ricevuto; log e nuovo receipt in `tests/reviewer_crosscheck_original.txt`, `tests/reviewer_receipt_original.*`.
- Una nuova esecuzione Linux del generatore originale, senza checkpoint, con stesso digest del payload; log in `tests/reviewer_replay_original.txt`, report `tests/global_interval_replay_20260917T105239Z_da6352a5.json`. Non è un nuovo replay Windows.
- Verifica distinta con il nuovo algoritmo del revisore: `tests/reviewer_independent_verification.json`.
- Dieci mutazioni di certificati, con digest ricalcolati, e relativi log integrali.
- 36 istanze DP su grafi piccoli: 18 simmetriche e 18 asimmetriche; 1.926 stati non-root e 36 costi root confrontati con tutti i completamenti espliciti, incluso l'arco di ritorno.
- 22 test di soglia su n=4,...,9, forzando solo in una copia in memoria il ramo scheletri/pruning e confrontando l'insieme esatto delle classi inoltrate alle foglie con l'enumerazione diretta. Il callback delle foglie è uno spy: questi sono test strutturali, non prove di fattibilità.
- Mutante `>` -> `>=`: con n=6 e pesi tutti 1, soglia 5, il codice corretto mantiene 60 ordini espliciti; quello errato ne mantiene zero, pur passando l'identità fattoriale di copertura. L'oracolo indipendente rileva l'over-pruning. Il codice originale usa il confronto corretto.
- Mutante che omette l'ultimo gap di inserimento: rifiutato.
- 30 test del kernel atan contro somme Fraction di 512 termini con resto; 44 test del coseno contro somme Fraction di 160 termini con resto, coprendo cutoff pari/dispari; 20 test di angoli contro entrambi i kernel e il coseno; 12 rifiuti di domini non validi.

### Esiti delle mutazioni dei certificati

A = exit code 0; R = rifiuto. La colonna del crosschecker non va interpretata come verifica degli angoli, esclusa dal suo contratto.

| Mutazione | Crosschecker DP | Receipt aritmetico | Nuovo controllo matematico |
|---|---|---|---|
| n=4 senza witness superiore | A | A | R |
| Bracket falso n=4 e nessun witness | A | A | R |
| Come sopra, ma totale witness riportato a 47 | A | A | R |
| Lower endpoint angolare falso di una unità di griglia, prova derivata e hash ricalcolati | A | R | R |
| Intervallo angolare U falso | A | R | R |
| Due direzioni cartesiane collassate | R | R | R |
| Copertura dei casi n errata | R | R | R |
| Conteggio canonico dichiarato errato | A | R | R |
| Digest DP e pruning azzerati | A | A | R |
| Input cases digest azzerato | A | A | A nella funzione matematica; R nel binding separato agli input |

L'alterazione angolare di una sola unità di griglia è particolarmente utile: il checker alternativo la rifiuta anche dopo il ricalcolo delle parti derivate. Quindi il suo contributo aritmetico è effettivo, non una semplice corrispondenza di hash.

### Evidenze riportate dal pacchetto, non nuove mie esecuzioni

`KERNEL_REGRESSION.json`, `WINDOWS_SECOND_DP_CHECK.txt`, `WINDOWS_RECEIPT_CHECK.json` e `ringmin_bundle_review.json` sono report preesistenti. Li ho letti come evidenza storica, non li ho conteggiati come test scritti o eseguiti da me. I miei nuovi controlli possono ripetere obblighi analoghi, ma hanno log e algoritmi identificati separatamente.

Il report Windows dichiara l'ambiente Windows e la versione Python; ho verificato il file ricevuto, i suoi metadati e il suo contenuto, non autenticato forensicamente il sistema operativo che lo avrebbe prodotto. Le mie esecuzioni sono Linux. Gli audit storici dei pickle, la CI hosted e la storia dei Top-K non sono stati rieseguiti e non sono dipendenze della nuova prova.

## 10. Matrice claim-evidenza e limiti

| Obbligo | Evidenza sufficiente esaminata / ricostruita |
|---|---|
| Intervalli reali corretti | Derivazione arcsin + alternate atan + nuova inclusione via coseno dei 908 intervalli e tau |
| Tutti gli ordini esclusi a L | Ricorrenza esatta, partizione della visita, simmetria/riflessione, reinserimento completo, DP forward e test esaustivi piccoli |
| Disuguaglianza stretta sull'infimum | Margini positivi, continuità/monotonicità, numero finito di classi; ulteriore epsilon razionale uniforme per n |
| Configurazione esistente a U per ogni n | Witness presenti in tutte le righe originali e controlli cartesiani razionali su tutte le coppie |
| Identificazione del payload originale | Byte, manifest, payload Windows/Linux e binding CASES; distinti dalla dimostrazione |

Non sono giustificati: uguaglianza dell'ottimo con un numero decimale della tabella; esatta ottimalità dei 47 ordini; classificazione completa dei minimizzatori; unicità o rigidità dei contatti; quantificatori sui floating circles; risultati per n>14; asintotica; correttezza dei pruning float64 storici; journal-readiness complessiva.

Non ho eseguito una verifica formale Lean/Coq/Isabelle né un audit del compilatore/interprete o dell'hardware. Il nuovo codice del revisore resta codice da ispezionare, non un'autorità incontestabile. Ho verificato la logica dei kernel e fatto regressioni falsificabili, non un'esplorazione esaustiva di tutti gli input razionali possibili. Il fixed-order seam theorem non è stato risolto qui: non è necessario alla catena inferiore/feasibility diretta usata per questo solo bracket, ma il suo ruolo editoriale resta un tema distinto.

## 11. Estremi esatti giudicati supportati

| n | L_n | U_n |
|---:|---:|---:|
| 3 | 0.26086956521 | 0.26086956522 |
| 4 | 0.84445358956 | 0.84445358957 |
| 5 | 1.69549408120 | 1.69549408121 |
| 6 | 2.79491951889 | 2.79491951890 |
| 7 | 4.15318955374 | 4.15318955375 |
| 8 | 5.76779428458 | 5.76779428459 |
| 9 | 7.72672655261 | 7.72672655262 |
| 10 | 9.97990738586 | 9.97990738587 |
| 11 | 12.48872048718 | 12.48872048719 |
| 12 | 15.25887043044 | 15.25887043045 |
| 13 | 18.31756304721 | 18.31756304722 |
| 14 | 21.66539518221 | 21.66539518222 |

Ogni decimale della tabella denota un razionale esatto. Questa tabella è il perimetro del giudizio, non una tabella di valori esatti di R*.

## 12. Minimo task successivo

Un unico task di integrazione di un **verificatore completo e fail-closed del certificato finito**, con correzione P1 e regressioni, descritto operativamente in `MINIMAL_INTEGRATION_TASK.md`. Non serve riaprire recupero checkpoint, replay Windows o Stage A storico. Il prossimo gate è la review del commit esatto prodotto dal task, non una promozione automatica fondata su questo rapporto.

