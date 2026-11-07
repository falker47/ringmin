# Paper II — Controllo visivo del PDF

Revisione locale del 7 novembre 2026, modalità STRICT. Classificazione:
controllo editoriale e ingegneristico dell'impaginazione, non verifica matematica.
È stata applicata la skill PDF per il rendering e l'ispezione delle pagine.

## Oggetti ispezionati

Il PDF revisionato è quello prodotto dal build locale del task:
`reproducibility/.work/editorial_20261107/revised/paper_ii/main.pdf`.
Conta 9 pagine, SHA-256:
`deda77d01c02d33c7f921b9fedc13db78f7ebe6deda3c25cac7c683f1c929766`.

Per confronto dei cambi pagina è stata usata la baseline compilata nello stesso
task: `reproducibility/.work/editorial_20261107/baseline/paper_ii/main.pdf`.
Conta anch'essa 9 pagine, SHA-256:
`44644a088d813f9b6272fbb20fd5dd5610581c7781aa4b1df1163216174cd0b1`.

Ambiente di rendering: Python bundled 3.12.14, pypdfium2 5.14.0, Pillow 12.3.0.
Due esecuzioni Python via stdin, entrambe exit 0: prima tutte le nove pagine
revisionate, poi le pagine 2, 3, 5, 6 della baseline. Ogni pagina è stata
renderizzata con `PdfPage.render(scale=2)`, convertita tramite `to_pil()` e
salvata come PNG di 1224 x 1584 pixel (144 dpi). Le immagini temporanee sono in
`reproducibility/.work/editorial_20261107/visual/paper_ii/`, esclusa dal commit.
Tutte le tredici immagini sono state effettivamente aperte con `view_image`.
Non è stato usato il solo testo estratto come controllo dell'impaginazione.

## Ispezione di tutte le pagine revisionate

| Pagina | Righe PDF visibili | Contenuto e controllo |
|---|---|---|
| 1 | 1–34 | Frontespizio completo; abstract articolato in paragrafi, parole chiave, MSC e apertura del problema leggibili. Titolo e formule inline non escono dai margini. |
| 2 | 35–76 | Letteratura, guida al percorso, sezione 2, equazioni (1) e (2). Numeri di equazione separati dal testo. Il finale della Definizione 1 prosegue a pagina 3: osservazione specifica sotto. |
| 3 | 77–109 | Finale della definizione, ricorrenza (3), Lemmi 2–3, squeeze (4), apertura della sezione 3 e Teorema 4 con (5). Formule e simboli QED leggibili; la prova prosegue a pagina 4 senza sovrapposizioni. |
| 4 | 110–144 | Continuazione della prova, (6), nuova motivazione della sezione 4, tipi finiti, (7), parole bilanciate e LP (8). Il display su due righe resta integro e il suo numero è allineato. |
| 5 | 145–180 | Teorema 5 con riquadro (9), prova, sezione 4.3, sezione 5 e primo display dei blocchi. Il riquadro non invade numeri di riga o testo. La descrizione dei blocchi prosegue a pagina 6. |
| 6 | 181–218 | Costo (10), Teorema 6 e prova completa fino al rinvio a S2. Disequazioni lunghe, sommatorie e numeri di riga rimangono separati e leggibili. |
| 7 | 219–249 | Parametri impliciti, bracket razionali, (11), inizio della sezione 6 e definizioni dell'endpoint inferiore. Integrali, frazioni e indici non risultano troncati. Nessun contenuto matematico è stato rivalutato. |
| 8 | 250–291 | Proposizione 7, enclosure decimale, outline protetto e sezione 7. Le cifre del display sono leggibili; il QED e il titolo successivo hanno spazio sufficiente. |
| 9 | 292–317 | Acknowledgment AI visibile all'inizio pagina e otto voci bibliografiche complete. DOI, URL, identificativo del commit S1 e nome del PDF S2 sono leggibili e dentro i margini. |

Numeri di pagina 1–9 e numeri di riga sono visibili e coerenti. Non sono stati
osservati testo troncato, collisioni fra testo/formule/numerazione, caratteri
sostituiti da quadrati, riferimenti visualizzati come `??` o pagine bianche
aggiuntive. Si tratta di un'osservazione sui rendering esaminati, non di una
certificazione universale del PDF in ogni visualizzatore.

## Confronto dei cambi pagina e osservazione residua

Le pagine 2, 3, 5 e 6 della baseline sono state aperte per confrontare i punti
in cui il nuovo testo introduttivo sposta definizioni e costruzioni.
La Definizione 1 era tutta a pagina 2 nella baseline; nella revisione la sua
ultima frase, sui marchi nulli e sulla notazione della sequenza, è all'inizio
di pagina 3. Il contenuto resta integro e la continuità è riconoscibile, ma
il cambio pagina è meno compatto sul piano tipografico. È registrato come
piccolo compromesso di impaginazione, non come errore matematico o di
compilazione. Non è stata alterata la definizione per forzare una nuova pagina.

Il passaggio fra pagine 5 e 6 nella descrizione dei blocchi avviene dopo un
display completo; non spezza una formula. La baseline aveva già una divisione
della successiva prova fra quelle pagine. Il nuovo riquadro del Teorema 5
all'inizio di pagina 5 e la bibliografia interamente a pagina 9 sono leggibili.

## Limiti e risultato

Controllate visivamente tutte le 9 pagine revisionate e 4 pagine della baseline.
Nessuna modifica al PDF, al main, a S1/S2 o ai relativi checkpoint è stata fatta
durante questa ispezione. Il rendering non esegue TeX, non controlla la validità
delle prove e non attesta la correttezza degli endpoint. Esiti dei build e
confronto degli avvisi appartengono a EVIDENCE.md; non sono sostituiti da questo
controllo. Rimane la sola osservazione tipografica sulla Definizione 1 riportata
sopra, da considerare nella lettura finale dell'autore.
