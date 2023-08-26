# Datum: 2022-03-13
# Kurskod: DD100N

#Programmet för att spela luffarschacksspelet.
#Tar in två namn på spelare, visar ett spelfält, tillåter inmatning och kontrollerar det.
#För att rita ut spelplanen används Box Drawing Characters": https://en.wikipedia.org/wiki/Box-drawing_character

import random
import sys

def skrivUtSpelplan(spelplan): #Funktionen skriver ut en spelplan med avsedda symboler för rader och kolumner.
    print('      A     B      C  ')
    print('  ┏━━━┳━━━┳━━━┓')
    radRäknare = 0
    for rad in spelplan:
        radRäknare += 1
        print(str(radRäknare) +' ┃', end=' ')
        for ruta in rad:
            print(' ' + ruta, end='  ')
            print('┃', end=' ')
        print()
        if radRäknare < 3:          #Efter sista raden vill vi inte göra detta
            print('  ┣━━━╋━━━╋━━━┫')
    print('  ┗━━━┻━━━┻━━━┛')          #Utan istället detta


def kontrolleraRader(spelplan):
    """Kontrollerar om det finns tre likadana tecken på någon rad och returnerar då True, annars False
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    
    for i in range(3):
        if ' ' not in [spelplan[i][0], spelplan[i][1], spelplan[i][2]]:
            if spelplan[i][0] == spelplan[i][1] == spelplan[i][2]:
                return True
            
    return False


def kontrolleraKolumner(spelplan):
    """Funktionen kontrollerar om samma symbol upptar alla tre fälten i en specifik kolumn.
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    
    for i in range(3):
        if ' ' not in [spelplan[0][i] , spelplan[1][i] , spelplan[2][i]]:
            if spelplan[0][i] == spelplan[1][i] == spelplan[2][i]:
                return True
           
    return False


def kontrolleraDiagonaler(spelplan):
    """Funktionen kontrollerar om samma symbol upptar alla tre fälten i var och en av diagonalerna
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    
    if ' ' not in [spelplan[0][0], spelplan[1][1], spelplan[2][2]] and spelplan[0][0] == spelplan[1][1] == spelplan[2][2]:
        return True
    elif ' ' not in [spelplan[0][2], spelplan[1][1], spelplan[2][0]] and spelplan[0][2] == spelplan[1][1] == spelplan[2][0]:
        return True
    else:
        return False


def finnsVinnare(spelplan):
    """Funktionen anropar tre andra kontrollfunktioner (rad, kolumn och diagonal) och baserat på resultaten kontrollera om någon av dem utser en vinnare.
    Inparameter: spelplan (matris)
    Returvärde: True om det finns vinnare annars False (booleskt värde)
    """
    
    if kontrolleraKolumner(spelplan) or kontrolleraDiagonaler(spelplan) or kontrolleraRader(spelplan):
        return True
    else:
        return False


def oavgjort(spelplan):
    """Om alla fält på spelfältet har fyllts returnerar funktionen true.
    Inparameter: spelplan (matris)
    Returvärde: True eller False (booleskt värde)
    """
    
    for rad in spelplan:
        for element in rad:
            if element ==' ':
                return False
    return True


def tolkaInmatning(inmatning):
    """Funktionerna översätter A B och C till siffror. Det kraschar programmet om en spelare använder en annan symbol än A,B,C
    Inparameter: inmatning (string)
    Returvärde: rad, kolumn (int)
    """
    
    bokstav = inmatning[0].upper() #Använder .upper() för att göra om alla inmatade bokstäver till versaler
    rad = int(inmatning[1])-1
    if bokstav == 'A':
        kolumn = 0
    elif bokstav == 'B':
        kolumn = 1
    elif bokstav == 'C':
        kolumn = 2
    """else:
        sys.exit("Error message")"""   
    return rad, kolumn

def tur ():
    """Radomiserar vem som går först.
    Inparameter: ingen
    Returvärde: random (int)
    """
    return random.randint(0,1)
    
    

def spela(spelarNamn1, spelarNamn2):
    """Tar in spelarnamn, randomiserar vem som går först, utser X och O till varje spelare.
    Inparameter: spelarNamn1, spelarNamn2 (string)
    Returvärde:ingen
    """
    
    
    print("Då kör vi!")
    print("Ange de koordinater du vill lägga på på formatet A1, B3 osv.")
    spelplan = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #Tom spelplan.

    spelarLista = [spelarNamn1, spelarNamn2]
    vemsTur = tur()
    
    
    while finnsVinnare(spelplan) == False:
        vemsTur = (vemsTur+1)% 2 #vemsTur ska aldrig bli 2, utan börja om igen på 0, %-är modul dvs resten vid heltals division.
        
        
        skrivUtSpelplan(spelplan)
        
        if vemsTur == 0:
            markör = 'X'
        else:
            markör = 'O'
            
        inmatning = input(str(spelarLista[vemsTur]) + "s tur att spela: ") #
        
        rad,kolumn = tolkaInmatning(inmatning)
        
        if spelplan[rad][kolumn]==' ':
            spelplan[rad][kolumn] = markör
            
        if oavgjort(spelplan) == True and finnsVinnare(spelplan) == False:
            skrivUtSpelplan(spelplan)
            print("Det blev oavgjort!")
            break
        
    if not oavgjort(spelplan) or finnsVinnare(spelplan) == True:
        skrivUtSpelplan(spelplan)
        print("Grattis " + str(spelarLista[vemsTur]) + " du vann!")


def huvudfunktion():
    """Tar in spelarnamn, randomiserar vem som går först, utser X och O till varje spelare.
    Inparameter:ingen
    Returvärde:ingen
    """
    
    print("Hej och väkommen till Tre-i-rad!")
    spelarNamn1 = input("Vad heter spelare 1? ")
    spelarNamn2 = input("Vad heter spelare 2? ")
    spela(spelarNamn1, spelarNamn2)

huvudfunktion()
