import math

def pot():
    print('\nHai Scelto: Potenza\n')
    a = float(input('Inserisci il Primo Numero -> '))
    b = float(input('Inserisci il Secondo Numero -> '))
    print('Il risultato della Potenza è: ' + str(math.pow(a,b)))


def rad():
    print('\nHai Scelto: Radice\n')
    a = float(input('Inserisci il Numero -> '))
    print('Il risultato della Radice è: ' + str(math.sqrt(a)))


def add():
    print('\nHai scelto: Addizione\n')
    a = float(input('Inserisci il Primo Numero -> '))
    b = float(input('Inserisci il Secondo Numero -> '))
    print('Il risultato della Somma è: ' + str(a))



def sott():
    print('\nHai Scelto: Sottrazione\n')
    a = float(input('Inserisci il Primo Numero -> '))
    b = float(input('Inserisci il Secondo Numero -> '))
    print('Il risultato della Sottrazione è: ' + str(a - b))

def molt():
    print('\nHai scelto: Moltiplicazione\n')
    a = float(input('Inserisci il Primo Numero -> '))
    b = float(input('Inserisci il Secondo Numero -> '))
    print('Il risultato della Moltiplicazione è: ' + str(a * b))

def div():       
    print('\nHai scelto: Divisione\n')
    a = float(input('Inserisci il Primo Numero -> '))
    b = float(input('Inserisci il Secondo Numero -> '))
    try:
        ris = a/b
        print('Il risultato della Divisione è: ' + str(ris))
    except ZeroDivisionError:
        print("errore non puoi dividere per 0")    

def esp():
    print('\nHai scelto: Calcolo Esponenziale\n')
    a = float(input('Inserisci la Base -> '))
    b = float(input('Inserisci l\'Esponente -> '))
    print('Il risultato del Calcolo Esponenziale è: ' + str(a ** b))

