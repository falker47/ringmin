# Paper I - controllo visivo

PDF revisionato: paper_assets/journal_dcg/ringmin_dcg.pdf.
SHA-256: c1a693f28e37bdfc0c0b2724a18204d71dc41a14adc4fd9d83b46009e6ed711c.

Tutte le 19 pagine sono state renderizzate con PDFium (pypdfium2, scala 1.5)
e ispezionate in cinque tavole di quattro pagine, con ulteriore lettura del
render singolo di pagina 9 dopo la correzione dell'overfull.
Ambiente rendering: Python bundled, pypdfium2 e Pillow; immagini conservate
solo nell'area ignorata reproducibility/.work/editorial_20261107/visual/paper_i.

- Pagine 1-4: titolo, abstract, introduzione, equazioni e primi enunciati leggibili.
- Pagine 5-8: passaggi di certificazione, tabelle razionali e copertura senza
  sconfinamenti o sovrapposizioni visibili.
- Pagine 9-12: tabella floating, limiti, comando di riproduzione, dati archivio,
  dichiarazioni AI e avvio dell'appendice leggibili. La frase accorciata sul
  risultato storico del verificatore rientra ora nella misura di pagina.
- Pagine 13-19: appendici, formule, tabelle di confronto razionale e bibliografia
  senza elementi troncati o collisioni osservate.

La bibliografia occupa la fine di pagina 18 e parte di pagina 19; il commit
d'archivio segue il richiamo fra pagine 9 e 10. Queste interruzioni restano
leggibili; non sono stati introdotti comandi di impaginazione o modifiche alle
parti matematiche. Il conteggio resta 19 pagine, come nel build iniziale.

Questo e un controllo visivo di impaginazione, non una verifica cifra per cifra
dei dati e non una nuova revisione delle dimostrazioni. Invarianza delle sorgenti
protette, avvisi LaTeX e numerazione sono verificati separatamente.
