# Revisione editoriale di Paper I

Data: 7 novembre 2026. Modalita: STRICT. Valutazione editoriale, non nuova
verifica matematica o approvazione per la pubblicazione.

## Identita e base

Il sorgente revisionato e `paper_assets/journal_dcg/ringmin_dcg.tex`, titolo
*Minimum central circles: chain order, seam obstructions, and exact finite
certification*. La richiesta lo identifica con DAM DA21348. Il nome storico
`journal_dcg` non determina la rivista corrente. Il testo e separato da Paper II,
dai depositi arXiv e dal pacchetto storico `paper_assets/dcg_submission/`.

Confronto con `7d257221d9034ca5f895f062e45e782d8e77b6c2` nel nuovo branch
`codex/ringmin-editorial-review`. Nessuna modifica al checkout originale.
Le righe sotto si riferiscono al sorgente, prima e dopo questa revisione.

## Problemi trovati e interventi applicati

| Posizione / funzione | Riga base | Riga rivista | Scelta editoriale |
|---|---:|---:|---|
| Abstract: spiegazione della catena | 34 | 34 | Il termine specialistico precedeva la sua funzione. Ora la frase specifica che vengono imposti solo i vincoli consecutivi; anti-Monge, ordine minimizzante e trasferimento alla radice restano distinti. |
| Abstract: portata e antecedente | 43 | 46 | Un nuovo paragrafo separa i risultati a ordine fissato dalla certificazione globale. "It" diventa "The certificate", evitando che l'indipendenza dal pruning sembri riferita solo al testimone superiore. |
| Introduzione: percorso dei contributi | 80 | 84 | Tre paragrafi distinguono ordinamento/formulazione, seam e certificato. Enunciati riassunti, attribuzione a Supnick e dominio restano identici. |
| Modello: apertura | 126 | 133 | Rimossa la ripetizione poco naturale "central center"; coordinate e definizioni invariate. |
| Ordine canonico: avvio della definizione | 187 | 195 | Rimosso "unambiguous", un giudizio sul testo che non aiuta a eseguire la costruzione. La regola operativa rimane integra. |
| Certificato: ruolo dei due argomenti | 305 | 313 | Ogni lato del bracket ha ora una propria frase e uno scopo esplicito. Restano l'indipendenza dei due argomenti, l'esclusione leggermente sopra il limite inferiore e il testimone al limite superiore. |
| Sigla DP | 384 | 393 | Espansa la sigla alla prima occorrenza; ricorrenza, complessita e analisi della copertura non cambiano. |
| Floating: raggio della testimonianza | 530 | 540 | "Illustrate the quantifier issue sharply" diventa un richiamo concreto al raggio specificato. Tutti i quantificatori e i limiti successivi restano identici. |
| Riproduzione: istruzione e resoconto | 565 | 575 | Il comando e introdotto da un verbo operativo. Un capoverso separa le istruzioni ripetibili dal risultato storico; comando, ambiente e conteggi restano invariati. |

Esempi essenziali:

- "The adjacent-chain relaxation has an angular kernel ..." diventa
  "We first study the adjacent-chain relaxation, which imposes only the
  constraints between consecutive circles. Its angular kernel ...".
- "The finite proof has two independent mathematical obligations: exclude ...,
  and exhibit ..." diventa "The finite certificate requires two independent
  arguments. For the lower bound, ... For the upper bound, ...".
- "The new upper witnesses illustrate the quantifier issue sharply" diventa
  "The upper witnesses show why the radius must be specified".

L'abstract passa da 184 a 193 parole contando i segmenti separati da spazi
nel sorgente LaTeX. L'aumento serve a spiegare il rilassamento; non aggiunge
risultati. Il certificato conserva il suo dominio finito e la sua larghezza
esatta, e le soglie seam restano risultati a ordine fissato.

## Controllo del significato delle modifiche

Le modifiche potenzialmente piu sensibili sono rese esplicite nel diff:

1. La spiegazione del rilassamento nell'abstract riprende l'oggetto gia
   definito nelle sezioni 2 e 4. Non identifica ottimo della catena e ottimo
   geometrico: la frase sui vincoli per ogni coppia rimane visibile.
2. "Global infimum" richiama precisamente la definizione introduttiva;
   non introduce una pretesa di raggiungimento dell'infimo.
3. "The certificate" risolve l'antecedente del vecchio "It"; la sezione 6
   esclude gia il pruning storico come premessa di entrambi gli argomenti.
4. "Two independent arguments" conserva il requisito precedente. Non indica
   due implementazioni indipendenti: il passaggio sull'origine del verificatore
   nella sezione 10 rimane invariato.
5. La frase sui floating riporta l'attenzione al raggio della costruzione;
   non rende esistenziale o universale una conclusione prima solo numerica.
6. L'espansione di DP e un cambiamento terminologico all'interno della
   descrizione del metodo; nessun passaggio dell'argomento o bound e modificato.

Queste sono valutazioni di equivalenza editoriale, ispezionabili parola per
parola; non una nuova dimostrazione dei risultati citati.

## Copertura della lettura

Sono stati letti l'intero main e l'intera appendice seam inclusa:

- Abstract e sezione 1: migliorati definizione informale, ritmo e transizioni;
  contesto bibliografico e attribuzioni preservati.
- Sezioni 2-3: corretti solo due incipit; notazione, kernel, gerarchia e
  costruzione del ciclo restano invariati.
- Sezioni 4-5: lasciate integre. Il percorso da vincoli diretti a seam,
  persistenza, casi piccoli e uguaglianza e gia esplicito.
- Sezione 6: migliorato solo l'avvio e sciolta DP; le sottosezioni tecniche
  restano integre quanto a ragionamento, formule, algoritmi e quantificatori.
- Sezione 7: conservata integralmente; la distinzione fra bracket razionale,
  numero di testimoni e conteggio delle classi e gia leggibile.
- Sezioni 8-9: ritoccata una frase di transizione sui testimoni; definizione di
  floating, interpretazione numerica, limiti e questioni aperte preservati.
- Sezione 10: distinta l'istruzione eseguibile dal resoconto storico.
- Dichiarazioni, appendici A e B e bibliografia: lette e preservate integralmente.
  La disclosure AI resta veritiera, visibile e senza attenuazioni.

## Questioni lasciate alla decisione dell'autore

Non e stata individuata una nuova ambiguita matematica concreta che richieda
una correzione del risultato. Restano due questioni di presentazione/versione:

1. La sezione 10 conserva date, baseline interno e la frase "this manuscript
   has not been submitted to Discrete & Computational Geometry". La richiesta
   identifica Paper I come DAM DA21348; la frase storica non dice che non sia
   stato presentato altrove. Non viene riscritta una cronologia editoriale da
   indizi. Formulazione candidata, solo dopo conferma dell'autore:
   "The archived snapshot and the later internal review baseline identify
   different revisions; neither constitutes journal peer review."
   La sostituzione eliminerebbe informazione storica: decidere quali eventi
   vadano mantenuti nel manoscritto e verificare il record editoriale corrente.
2. "At and slightly above" all'inizio della sezione 6 e precisato dal buffer
   razionale nella sezione 6.4. L'espressione non e una lacuna della prova.
   Se l'autore desidera un rimando immediato, candidata separata:
   "The positive radius buffer is established in Section 6.4."
   Verificare il rimando e che il buffer continui a valere per tutte le classi
   coperte in ogni eventuale revisione matematica. Non applicato per evitare
   ritocchi superflui alla spiegazione della prova.

## Diff e verifiche

Diff completo riproducibile dalla radice del worktree:

```text
git diff 7d257221d9034ca5f895f062e45e782d8e77b6c2 -- paper_assets/journal_dcg/ringmin_dcg.tex
```

Il controllo locale editoriale confronta 265 segmenti matematici nell'ordine
originale; gli ambienti di enunciato, prova, tabella e bibliografia e il testo
dalle dichiarazioni alla fine restano identici. `git diff --check` sul sorgente
ha restituito exit 0 senza output. Un primo controllo preliminare ha
erroneamente interpretato la spaziatura autore `\\[3pt]` come apertura di una
formula; e fallito prima di scrivere, poi e stato corretto e rieseguito.
Il coordinatore ha rilevato nel primo build rivisto un nuovo overfull box
(52.93068pt) nel capoverso sul resoconto storico. La frase introduttiva e stata
abbreviata in "The manuscript's local Python 3.14.3 run returned": conserva
soggetto, ambiente, esito e natura storica senza spezzature tipografiche forzate.
Le posizioni del sorgente nella tabella non cambiano. Compilazione finale,
confronto degli avvisi e ispezione PDF sono registrati dal coordinatore nel
dossier; questo rapporto non presume l'esito della ricompilazione.

## Valutazione prima/dopo

Prima: manoscritto preciso e attento alla portata delle conclusioni, ma
l'abstract introduceva presto termini specialistici e il paragrafo dei
contributi chiedeva di seguire quattro fili senza pause. Alcune frasi parlavano
della qualita o della funzione del testo in modo astratto.

Dopo: il rilassamento ha una spiegazione immediata, i contributi si leggono
per blocchi, i due lati del certificato hanno un ruolo esplicito e il passaggio
ai floating richiama il raggio della testimonianza. La densita tecnica di
prove e appendici rimane, per scelta, invariata. L'autore deve valutare il diff
e la presentazione della cronologia; la revisione non attesta accettazione
matematica o idoneita a una specifica rivista.
