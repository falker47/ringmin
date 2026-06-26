# Il problema della collana di cerchi tangenti

**Una guida semplice, non tecnica, alla mia ricerca su cerchi di raggi 1, 2, ..., n attorno a un cerchio centrale minimo.**

Questa guida spiega l'idea senza entrare nei dettagli del paper. L'obiettivo è rendere chiaro il problema, perché non è solo un disegno geometrico, quale struttura matematica compare, e che cosa è stato effettivamente certificato.

---

## 1. Il puzzle di partenza

Immagina di avere un cerchio centrale, di raggio ancora da scegliere, che chiamiamo **R**. Attorno a questo cerchio vuoi disporre una serie di cerchi esterni, tutti di dimensioni diverse:

- un cerchio di raggio 1;
- un cerchio di raggio 2;
- un cerchio di raggio 3;
- e così via, fino a un cerchio di raggio **n**.

Tutti i cerchi esterni devono toccare il cerchio centrale dall'esterno e non devono sovrapporsi tra loro.

> **Domanda chiave**  
> In quale ordine devo disporre i cerchi esterni per rendere il cerchio centrale il più piccolo possibile?

A prima vista sembra un puzzle geometrico. La parte interessante è capire perché un ordine possa essere migliore di un altro.

---

## 2. Lo spazio angolare: perché l'ordine conta

Ogni cerchio esterno tocca il cerchio centrale. Il suo centro non sta esattamente sulla stessa circonferenza degli altri: un cerchio di raggio **i** ha il centro a distanza **R+i** dal centro principale. Pero' tutti i centri possono essere descritti con un angolo attorno al centro.

Se due cerchi esterni sono vicini nell'ordine, devono avere abbastanza distanza angolare per non sovrapporsi. Quindi ogni coppia di cerchi consecutivi **consuma** un certo angolo attorno al centro:

- due cerchi piccoli consumano poco angolo;
- due cerchi grandi consumano più angolo;
- un cerchio piccolo vicino a uno grande consuma una quantita' intermedia.

Il giro completo attorno al cerchio centrale misura sempre **360 gradi**, cioe' **2π radianti**. Per chiudere la collana, la somma degli angoli richiesti dai cerchi consecutivi deve arrivare a quel giro completo.

Qui entra in gioco **R**:

- se il cerchio centrale è grande, i cerchi esterni sono più lontani dal centro e gli angoli richiesti diventano più piccoli;
- se il cerchio centrale è piccolo, i cerchi esterni sono più stretti attorno al centro e gli angoli richiesti diventano più grandi.

Quindi minimizzare il raggio centrale significa cercare l'ordine dei cerchi che riesce a chiudere il giro usando lo spazio angolare nel modo più efficiente possibile.

---

## 3. Il collegamento inatteso: il commesso viaggiatore

A questo punto la geometria incontra l'ottimizzazione combinatoria.

Esiste un problema classico chiamato **Travelling Salesman Problem**, o **problema del commesso viaggiatore**. Dice così: date alcune città e le distanze tra ogni coppia di città, qual è il giro più breve che visita tutte le città una volta sola e poi torna al punto di partenza?

Nel mio problema:

- le **città** sono i cerchi di raggio 1, 2, ..., n;
- il **costo** di mettere due cerchi vicini non è una distanza stradale, ma l'angolo minimo necessario per farli stare vicini senza sovrapporsi;
- scegliere l'ordine dei cerchi significa scegliere un ciclo che passa da tutti i cerchi.

Quindi la domanda diventa simile a questa: qual è il ciclo di cerchi che minimizza la somma degli angoli tra vicini?

---

## 4. La scorciatoia: anti-Monge e Supnick

Il problema del commesso viaggiatore, in generale, è difficile: se gli oggetti aumentano, il numero di ordini possibili cresce molto rapidamente.

Nel mio caso, però, la tabella dei costi non è casuale. La tabella che dice quanto angolo consuma ogni coppia di cerchi ha una struttura regolare chiamata **anti-Monge**.

In modo intuitivo, anti-Monge significa che i costi seguono una regolarita' forte: non sono numeri sparsi a caso, ma dipendono in modo ordinato dalle dimensioni dei cerchi.

Qui entra **Supnick**.

Supnick è associato a un risultato classico sul commesso viaggiatore in casi speciali. L'idea, detta senza formalismi, è questa: quando la matrice dei costi ha una struttura regolare del tipo giusto, non serve provare tutte le permutazioni. Si può riconoscere direttamente un ordine ottimale della catena.

Nel mio problema la matrice degli angoli ha proprio questa struttura. Quindi l'ordine ottimale della catena non è un'intuizione grafica: viene spiegato dalla struttura **Supnick/anti-Monge**.

> **Primo contributo**  
> Ho collegato il problema geometrico a una struttura di ottimizzazione combinatoria. L'ordine "a piramide" della catena è giustificato da Supnick e dalla struttura anti-Monge della matrice degli angoli.

---

## 5. La geometria reale: quando la catena si rompe

Fin qui sembrerebbe tutto risolto. Ma c'è una seconda difficolta'.

L'equazione della catena controlla solo i cerchi consecutivi: il primo con il secondo, il secondo con il terzo, e così via. Nella figura reale, però, anche due cerchi non vicini nell'ordine potrebbero finire per sovrapporsi.

Da **n=8** succede un fenomeno inatteso: la collana ideale non è più realizzabile nel modo più semplice. Il cerchio più piccolo, quello di raggio 1, può restare tangente al cerchio centrale, ma non riesce più a funzionare come anello della catena principale tra due cerchi più grandi.

In pratica viene espulso dalla catena principale. Per questo lo chiamo **cerchio flottante**.

Per valori più grandi di n, anche il cerchio di raggio 2 può diventare flottante. I dati suggeriscono una cascata: man mano che il sistema cresce, i cerchi più piccoli vengono progressivamente spinti fuori dalla catena principale.

> **Secondo contributo**  
> Ho descritto il breakdown della collana: l'ordine ottimale della catena è importante, ma la geometria completa può rompere quella catena e produrre cerchi flottanti.

---

## 6. Il controllo di coerenza: tutte le coppie, non solo i vicini

Per trovare la vera configurazione ottimale non basta controllare i vicini. Bisogna controllare **tutte le coppie di cerchi**.

Il metodo è questo:

1. assegno a ogni cerchio un angolo, cioe' una posizione attorno al centro;
2. per ogni coppia di cerchi calcolo la distanza angolare minima necessaria per non sovrapporsi;
3. ottengo un sistema di vincoli del tipo: "questi due cerchi devono essere separati almeno da questo angolo";
4. verifico se esiste una scelta degli angoli che soddisfa tutti i vincoli contemporaneamente.

Se i vincoli sono compatibili, la configurazione è realizzabile. Se si contraddicono, quell'ordine o quel raggio centrale sono impossibili.

Tecnicamente questa parte è modellata come un sistema di vincoli angolari, equivalente a un **Simple Temporal Network**. Intuitivamente è un controllo di coerenza geometrica: posso davvero mettere tutti i cerchi attorno al centro senza sovrapporli?

---

## 7. Che cosa significa "ottimo globale certificato"

Per i casi da **n=3** fino a **n=14**, il lavoro certifica l'ottimo globale. Questo significa una cosa precisa: per ciascuno di quei valori di n è stata trovata la miglior configurazione possibile, non solo una configurazione buona.

Il punto difficile è che gli ordini possibili sono tantissimi. Per **n=14**, gli ordini ciclici distinti sono dell'ordine dei miliardi.

La certificazione funziona così:

1. **Limiti inferiori.** Per ogni ordine si calcola un limite ottimistico: un valore sotto il quale quell'ordine non potra' mai scendere. Se questo limite è già peggiore della miglior soluzione trovata, l'ordine viene scartato con certezza.
2. **Verifica geometrica completa.** Gli ordini ancora competitivi vengono controllati con tutti i vincoli angolari tra coppie di cerchi.
3. **Verificatore indipendente.** I risultati vengono ricontrollati con un verificatore separato, ad alta precisione, per ridurre il rischio di errori numerici o bug del solver principale.

Quindi il metodo non dice solo: "ho trovato questa configurazione". Dice anche: "tutte le altre configurazioni sono state controllate oppure escluse perché non possono batterla".

> **Terzo contributo**  
> Ho certificato gli ottimi globali per i primi casi non banali, da n=3 a n=14, con codice e dati riproducibili.

---

## 8. Il rapporto con la teoria dei circle packings

Questo problema si collega anche alla teoria classica dei **circle packings**, cioe' l'impacchettamento di cerchi tangenti.

Un riferimento naturale è il teorema di Descartes, che riguarda quattro cerchi mutuamente tangenti: se conosci tre curvature, puoi ricavare la quarta. La curvatura, in questo contesto, è essenzialmente l'inverso del raggio.

Daniel Mathews mi ha fatto notare che, in linea di principio, equazioni di circle packing più generali potrebbero essere usate per trovare il raggio centrale. Pero' sarebbe un calcolo molto pesante, per due motivi:

- la teoria classica spesso parte da uno schema di contatti già fissato, mentre qui l'ordine dei cerchi deve essere scelto;
- da un certo punto in poi compaiono cerchi flottanti, quindi anche lo schema di tangenza cambia.

Il mio metodo è più mirato per questo problema: prima isola la struttura dell'ordine con Supnick/anti-Monge, poi verifica la geometria completa con i vincoli angolari.

---

## 9. I tre contributi in una pagina

1. **Contributo teorico**  
   Ho collegato la geometria dei cerchi al problema del commesso viaggiatore, mostrando che la catena ottimale è governata da Supnick e dalla struttura anti-Monge.

2. **Contributo geometrico**  
   Ho descritto il momento in cui la collana si rompe: da n=8 il cerchio più piccolo può diventare flottante, e il fenomeno sembra propagarsi.

3. **Contributo computazionale**  
   Ho certificato gli ottimi globali per n=3,...,14 con un metodo verificabile e dati riproducibili.

---

## In sintesi

> Ho studiato come disporre cerchi di raggi crescenti attorno a un cerchio centrale minimo. Ho mostrato che l'ordine ottimale della catena è regolato da una struttura Supnick/anti-Monge, ho descritto come la geometria reale rompa questa catena producendo cerchi flottanti, e ho certificato gli ottimi globali per i primi casi non banali.
