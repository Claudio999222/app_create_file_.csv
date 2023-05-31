
### **Questa applicazione ci permette di creare un dataset pandas e poi di creare un file csv con il dataset se non esiste, nel caso sia un inserimento successivo al primo aggiungerà solo i valori inseriti al data.csv file già esistente nella cartella.**

_**Questo file ci permette di inserire i seguenti dati:**_

*   _Mansione_
*   _Turno_
*   _KG-00000000000 (sarebbe il Nome Della commessa)_
*   _Sales Order_
*   _Marcatura KG (una commessa e' composta da da piu marcature)_
*   _Marcatura (Marcatura di ogni singolo pezzo)_
*   _Pezzi (Numero dei Pezzi)_
*   _Cognome dell operaio_

### I dati di “Mansione” e “Turno” sono selezionabili tramite un menu a tendina

### I dati di “KG-00000000000” sono un input e possono essere inseriti in quasi tutti i modi ad esempio:

*   _00000000_
*   _kG00000000_
*   _kG-00000000_
*   _Kg-00000000_
*   _g-00000000_
*   _k-00000000_

_ed il risultato finale di input Sara' semper KG-00000000000, se inseriamo un valore diverse da questo ad esempio una parole apparira un pop up di errore_

### I dati di Sales Order sono un input e possono essere inseriti in quest modo :

*   3 lettere ed il restante da numeri perche' i nostri sales order sono compost in questo modo “aal123456789, apl123456789” 

In caso non si rispetti quest sintassi apparira un pop up di errore

### I dati di “Marcatura” sono un input e possono essere inseriti in quest modo :

*   2 lettere e uno score piu 3 numeri e 2 lettere
*   2 lettere piu 3 numeri e 2 lettere
*   2 lettere e uno score piu 3 numeri e 1 lettere
*   2 lettere  piu 3 numeri e 1 lettere
*   2 lettere e uno score piu 3 numeri
*   2 lettere piu 3 numeri
*   1 lettere e uno score piu 3 numeri e 2 lettere
*   1 lettere piu 3 numeri e 2 lettere
*   1 lettere e uno score piu 3 numeri e 1 lettere
*   1 lettere  piu 3 numeri e 1 lettere
*   1 lettere e uno score piu 3 numeri
*   1 lettere piu 3 numeri
*   3 numeri e 2 lettere
*   3 numeri e 1 lettere
*   3 numeri

In agni caso ad esempio i caratteri di uscita nel csv saranno AB-302bc  e cosi via le lettere maiuscole o minuscole nell inserimento non contano vengono impostate poi dal programma.In caso non si rispetti quest sintassi apparira un pop up di errore

### I dati di “Pezzi” e “Marcatura KG”  sono un input e possono essere inseriti in quest modo :

*   4 numeri per i pezzi 
*   3 numeri per Marcatura KG

In caso non si rispetti quest sintassi apparira un pop up di errore

### I dati di “Cognome”  sono un input e possono essere inseriti in quest modo :

*   la prima lettera Maiuscola e le altere minuscule se il cognome e' composto da una sola parola
*   se nel cognome sono presenti due parole verranno convertite in maiuscole l'iniziale di entrambe le parole 

Non possono essere inseriti numeri. In caso non si rispetti quest sintassi apparira un pop up di errore

### Sotto a “KG-0000000000”, “Sales Order”, “Marcatura KG”, “Cognome” sono presenti delle check box che permettono di bloccare la cella con il testo presente in essa perche' Quando si premera' il pulsante asporta che trasformera questi dati  in un dataset nel csv i dati in input verranno cancellati . E apparira un pop up che confermera il corretto caricamento dei nostri dati