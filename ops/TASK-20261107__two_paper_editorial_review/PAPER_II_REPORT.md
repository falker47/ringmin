# Paper II — Rapporto di revisione editoriale

## Identità, perimetro e criteri

Fonte revisionata: `paper_assets/paper_ii_journal/main.tex`, candidato separato
sulla teoria asintotica. Baseline:
`7d257221d9034ca5f895f062e45e782d8e77b6c2` (3 novembre 2026).
La revisione è una proposta locale successiva, non una modifica del preprint
arXiv:2609.13630 o del candidato originale. La data nel manoscritto è mantenuta
come richiesto dal perimetro di conservazione dei metadati; questa nota identifica
la proposta editoriale del 7 novembre. Modalità STRICT.

Sono stati letti integralmente il manoscritto, il README del pacchetto e le
indicazioni pertinenti in `EDITORIAL_REQUIREMENTS.md`, `EDITORIAL_CHECKLIST.md`,
`REVIEW_COVERAGE.md` e `CLAIM_PROOF_MAP.md`. Restano le scelte di formato già
adottate: 11 pt, numeri di pagina e di riga, intestazioni coerenti. Questo non
attesta la conformità a una nuova rivista. Nessuna sede è scelta qui.

La richiesta associa S2 e Proposizione 7; il pacchetto identifica invece S1
come supplemento della Proposizione 7 e S2 come supplemento delle costruzioni
superiori. Per rispettare entrambi i possibili riferimenti, sono protetti
integralmente S1, S2 e tutta la sezione 6 del main. Non è stata ripetuta né
interferita alcuna revisione matematica indipendente.

Sono conservati formule, enunciati, definizioni, dimostrazioni, ragionamenti
matematici anche fuori dagli ambienti `proof`, valori numerici, citazioni,
bibliografia, metadati e acknowledgment sull'assistenza AI. Le sole aggiunte
sono spiegazioni del ruolo di passaggi già presenti. I giudizi sulla leggibilità
sono valutazioni editoriali; i controlli di invarianza sono fatti ingegneristici,
non nuove prove o certificazioni.

## Problemi trovati e interventi

I numeri di riga seguenti si riferiscono al sorgente revisionato. Il diff contro
la baseline rende visibile ogni intervento; non vi è riscrittura delle prove.

| Posizione | Problema prima | Intervento e ragione |
|---|---|---|
| Abstract, riga 32 | Un unico blocco passa da problema e risultato a riduzione, concatenazione, LP, due endpoint e limiti. | Separati quattro momenti: risultato; metodo; bounds espliciti; limiti. Tutte le formule e le qualificazioni sono mantenute. |
| Introduzione, riga 62 | «All outer circles are tangent ...» introduce direttamente un vincolo, prima di formulare la domanda di minimizzazione. | «We seek the smallest central circle ...» esplicita il problema; i raggi consecutivi iniziano da uno. Nessun nuovo modello è introdotto. |
| Introduzione, riga 72 | Il risultato principale arrivava dopo due paragrafi di storia dei manoscritti. | Una breve presentazione della crescita asintotica e dei programmi finiti precede ora quella storia; citazioni e loro ordine restano uguali. |
| Introduzione, riga 93 | «Our main result ... true global leading coefficient» ripeteva l'annuncio e concentrava il percorso in una sola frase. | Il paragrafo ha ora la funzione di guida alla prova: modello angolare, retta, concatenazione, parole finite. Eliminato l'enfatico «true». |
| Sezione 2, riga 146 | La definizione del problema sulla retta seguiva il raggio di catena senza un raccordo esplicito. | Anticipato il ruolo del problema ausiliario e il successivo confronto attraverso il costo di chiusura. Definizione e argomenti intatti. |
| Sezione 3, riga 207 | La sezione iniziava immediatamente con il teorema di esistenza. | Spiegato in tre righe perché concatenazione a costo limitato e riassegnazione ai raggi prescritti sono i due ingredienti. |
| Sezione 4, riga 248 | Il passaggio dall'esistenza alla quantizzazione cominciava direttamente con la notazione. | Esplicitate le due approssimazioni e il loro ruolo nei due termini della larghezza del bracket. |
| Sezione 4.2, riga 277 | Le parole e il vincolo di bilanciamento comparivano senza una spiegazione intuitiva locale. | Una parola è presentata come parte consecutiva di un ordine; il bilanciamento riguarda una distribuzione di parole, non ogni singola parola. |
| Sezione 5, riga 347 | La descrizione continua dei blocchi iniziava con i parametri prima di ricordare lo scopo. | Esplicitato che si cercano upper bounds e che occorre recuperare permutazioni effettive con tutti i vincoli di coppia. |
| Sezione 7, riga 546 | «claim--lemma--hypothesis--proof--verification map» e «No task-log reconstruction is a proof prerequisite» appesantivano la descrizione del pacchetto. | Sostituiti con frasi ordinarie sulla mappa delle dipendenze e sull'autonomia delle fonti di prova. |

Esempi prima/dopo non contenenti formule:

- Prima: «Our main result is an effective characterization of the true global
  leading coefficient.» Dopo: l'annuncio del risultato è anticipato e il
  paragrafo successivo comincia «Sections ... develop the proof of the effective
  characterization.» Le due funzioni, annuncio e percorso, sono riconoscibili.
- Prima: la sezione sulle parole bilanciate iniziava con «Fix ...».
  Dopo: «A word records a short consecutive piece of an ordering.» La notazione
  originale segue immediatamente e senza cambiamenti.
- Prima: «No task-log reconstruction is a proof prerequisite.»
  Dopo: «These sources contain the proofs without requiring reconstruction
  from task logs.» Il contenuto documentario resta identico.

## Copertura dell'intero manoscritto

| Parte esaminata | Esito della lettura editoriale |
|---|---|
| Frontespizio, metadati, parole chiave e MSC | Conservati; nessuna informazione personale o dichiarazione inventata. |
| Abstract | Organizzazione locale migliorata; simboli e portata conservati. |
| Sezione 1, problema, storia e letteratura | Domanda e risultato anticipati; confronto con Paper I, shelf packing, disk-contact recognition e difference constraints conservato. Nessuna attribuzione o novità modificata. |
| Sezione 2, confronto angolare e problema sulla retta | Un raccordo aggiunto; tutte le definizioni, formule, proprietà e prove conservate. |
| Sezione 3, esistenza | Un'introduzione funzionale aggiunta; teorema e prova conservati. |
| Sezione 4.1, tipi finiti | Motivazione fornita all'inizio della sezione 4; derivazione fuori dagli ambienti formali conservata integralmente. |
| Sezione 4.2, LP bilanciati | Spiegazione della funzione delle parole; vincoli, teorema e prova intatti. |
| Sezione 4.3, certificati e computabilità | Già distingue bene scoperta numerica, verifica razionale e complessità. Nessuna modifica. |
| Sezione 5, costruzioni superiori | Aggiunto solo il paragrafo iniziale; definizioni continue, teorema, prova, parametri impliciti e derivazione del guadagno conservati. |
| Sezione 6, endpoint inferiore e Proposizione 7 | Letta per coerenza narrativa, lasciata integralmente invariata e fuori dalla revisione matematica. |
| Sezione 7, riproducibilità e questioni aperte | Alleggerita la descrizione delle fonti; distinzioni fra controlli finiti, prove universali, computabilità ed efficienza mantenute. |
| Acknowledgment e bibliografia | Conservati integralmente. La disclosure AI resta visibile e veritiera nei limiti già documentati. |

## Scelte con possibile rilievo semantico

Queste aggiunte sono esplicitamente segnalate per una facile ispezione del diff:

- L'apertura ripete in parole il dominio già definito nell'abstract: minore
  raggio centrale, tangente esternamente a tutti i cerchi, senza sovrapposizioni,
  raggi interi consecutivi a partire da uno. Non autorizza altri insiemi di raggi.
- L'annuncio anticipato ripete il risultato dell'abstract e dei Teoremi 4 e 5.
  Non introduce una valutazione numerica efficace in senso di complessità.
- Il raccordo alla concatenazione descrive soltanto gli ingredienti della prova
  già presente. Il costo limitato non viene trasformato in un risultato nuovo.
- Le due approssimazioni nella sezione 4 rinviano ai due contributi già distinti
  nella prova. Il bilanciamento è deliberatamente attribuito alla distribuzione
  delle parole, per non suggerire che ogni parola sia bilanciata.
- L'introduzione della sezione 5 richiama la necessità del recupero geometrico:
  non attribuisce fattibilità alle sole marginali né ottimalità ai quattro blocchi.

## Ambiguità e decisioni lasciate aperte

1. **Riferimento dei bounds nell'introduzione, riga 97.** La frase mantenuta
   «The lower and upper bounds converge to the same constant with a prescribed
   error» segue il percorso dei programmi finiti, ma nelle frasi successive
   compaiono gli endpoint espliciti. Candidata non applicata:
   «The bounds from the finite-word programs converge to the same constant
   with a prescribed error.» L'autore deve confermare che il referente inteso
   sia esclusivamente il Teorema 5; non si deve suggerire la convergenza degli
   endpoint espliciti della costruzione e della Proposizione 7.
2. **Simboli degli endpoint nell'abstract, righe 48–51.** Sono introdotti prima
   delle definizioni nelle sezioni 5–6. La revisione conserva la formula per
   rispettare il blocco sulle espressioni matematiche. Possibile futura frase:
   «Together these arguments give explicit lower and upper bounds for the
   constant; neither endpoint is asserted sharp.» Richiede la decisione
   dell'autore sull'eventuale rimozione della formula dall'abstract e il controllo
   che resti adeguatamente rappresentato il contributo degli endpoint.
3. **Lessico “genuine labels”, abstract e sezione 3.** È corretto nel percorso
   seguito ma specialistico per un primo lettore. Una candidata futura è
   «reassignment to the prescribed integer radii». Prima di una sostituzione
   sistematica occorre controllare, punto per punto, quando “labels” designi
   i raggi originali e quando i marchi normalizzati; nessuna sostituzione
   automatica è stata applicata.
4. **Disclosure AI.** L'acknowledgment esistente è preservato. I nomi degli
   strumenti storici, le porzioni coinvolte e le attestazioni personali rimangono
   questioni dell'autore già censite nell'EDITORIAL_CHECKLIST; questa revisione
   non inventa dettagli né attenua l'assistenza ricevuta.
5. **Data del frontespizio.** Rimane 3 novembre per conservare i metadati; il
   dossier distingue esplicitamente questa proposta del 7 novembre. Un cambio
   della data nella versione destinata all'esterno resta decisione dell'autore.

## Controlli svolti e limiti

Controllo locale Python tra la baseline Git e il main revisionato, exit 0:
279 frammenti matematici ordinati identici; 13 ambienti formali identici;
ordine delle citazioni, intera sezione 6, acknowledgment e bibliografia identici.
Il controllo è testuale, non un parser LaTeX completo e non una verifica matematica.
Il diff completo del main è stato letto; `git diff --check --
paper_assets/paper_ii_journal/main.tex` termina con exit 0 senza output.
I risultati dei build, del controllo globale dei file protetti e delle altre
verifiche del task sono registrati separatamente in EVIDENCE.md.

## Valutazione prima/dopo

Prima, il manoscritto aveva una struttura matematica compatta e già distingueva
le classi di evidenza, ma chiedeva al lettore di ricavare da solo il motivo dei
passaggi fra modelli e approssimazioni. Dopo, domanda, risultato e funzione
degli strumenti sono visibili prima dei dettagli tecnici. La maggiore
leggibilità dipende da raccordi brevi e dalla divisione dell'abstract, non da
una semplificazione delle prove. Restano da valutare con l'autore le cinque
questioni sopra; non si attribuisce alla revisione alcuna accettazione scientifica.
