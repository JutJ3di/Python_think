from procedure import *


while True:
    print('''
    Benvenuto al programma calcolatrice!
    Creata da: Hermo
    Di seguito un elenco delle varie funzioni disponibili:

    -Per effettuare un'Addizione, seleziona 1;
    -Per effettuare una Sottrazione, seleziona 2;
    -Per effettuare una Moltiplicazione, seleziona 3;
    -Per effettuare una Divisone, seleziona 4;
    -Per effettuare un Calcolo Esponenziale, seleziona 5;
    -Per effettuare la radice,primi 6;
    -Per effettuare la potenza premi 7;
    -Per uscire dal programma puoi digitare ESC;
    ''')

    scelta = input('Inserisci il numero corrispondente all\'operazione selezionata --->  ')
    if scelta == "1":
        add()
    elif scelta == "2":
        sott()
    elif scelta == "3":
        molt()    
    elif scelta == "4":
        div()
    elif scelta == "5":
        esp()
    elif scelta == "6":
        rad()
    elif scelta == "7":
        pot()
    elif scelta == "ESC":
        print('''L'applicazione verrà ora chiusa!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break

    loop = input('\nDesideri continuare ad usare l\'applicazione? S/N ')
    if loop == "S" or loop == "s":
        print('''Sto tornando al Menù principale!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        continue
    else:
        print('''Grazie e arrivederci!

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++''')
        break