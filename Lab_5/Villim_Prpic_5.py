# Villim Prpic
# 2023-03-19
# DD100N

#The program keeps track of competition. A user can add players and scores. The program saves them on a separate file and then reedds the file to get the results.
#The program also checks for eventual errors and has the ability to print out and ordered list of results."""

import os




def main():
    
    # Inparameter: None
    # Returvärde: None
    
    # Huvudprogrammet som körs när programmet startas. 
    # Läser in tidigare resultat och loopar genom huvudmenyn.
    
    print("Den årliga pilkastningstävlingen är i full gång!")
    resultat = read_results()  # Läs in tidigare resultat

    while True:
        print("\n")
        print("Huvudmeny")
        print("1. Se resultat")
        print("2. Mata in nytt resultat")
        print("3. Spara och avsluta")
        print("\n")
        val = input("Vad vill du göra?")

        if val == "1":
            write_result(resultat)
        elif val == "2":
            mata_in_resultat(resultat)
        elif val == "3":
            spara_resultat(resultat)
            print("Resultattavlan är sparad. Hejdå!")
            break
        else:
            print("Felaktigt val, försök igen!")

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def read_results():
    
    # Inparameter: None
    # Returvärde: Listan resultat med tidigare resultat från filen resultatfil.
    
    # Funktion för att läsa in resultat från fil och returnera en lista av tupler med namn och poäng.
    # Om filen inte finns eller är tom så returneras en tom lista.
    resultatfil = "resultat.txt"  # Filnamnet för textfilen där resultaten sparas
    try:
        with open(resultatfil, "r") as data:
            resultat = list()
            for line in data:
                namn, poäng = line.strip().split(",")
                resultat.append((namn, int(poäng)))
    except FileNotFoundError:
        resultat = list()
    return resultat


def write_result(resultat):
    # Inparameter: resultat (en lista av tupler med namn och poäng)
    # Returvärde: None
    # Funktion för att skriva ut resultattavlan sorterad efter poäng.
    
    if len(resultat) == 0:
        print("Inga resultat hittades.")
    else:
        #Ask if O(n) or O(n^2)?
        for i in range(0,len(resultat)):
            for j in range(i + 1, len(resultat)):
                if resultat[j][1] > resultat[i][1]:
                    resultat[i], resultat[j] = resultat[j], resultat[i]
        clear_screen()
        print("Just nu är ställningen följande:")
        for i, result in enumerate(resultat):
            namn, poang = result
            print(f"{i+1}. {namn} {poang} poäng")


def mata_in_resultat(resultat):
    # Inparameter: resultat (en lista av tupler med namn och poäng)
    # Returvärde: None
    # Funktion för att mata in nya resultat och lägga till dem i resultatlistan.
    clear_screen()
    namn = input("Vad heter spelaren? ")
    while True:
        exists = False
        for n, p in resultat:
            if namn.lower() == n.lower():
                exists = True
                break
        if not exists and namn:
            break
        namn = input("Nej det namnet är upptaget, försök igen. Vad heter spelaren? ")
    while True:
        
        poang = input("Vilken poäng fick spelaren? ")
        if poang.isdigit() and (0 <= int(poang) <= 50):
            resultat.append((namn, int(poang)))
            print(f"{namn} har nu lagts till i resultatlistan med {poang} poäng!")
            break
        else:
            poang = input("Det där var inte en rimlig poäng. Försök igen. Vilken poäng fick spelaren? ")


def spara_resultat(resultat):
    # Inparameter: resultat (en lista av tupler med namn och poäng)
    # Returvärde: None
    # Funktion för att spara resultatlistan till filen resultatfil.
    resultatfil = "resultat.txt"  # Filnamnet för textfilen där resultaten sparas
    with open(resultatfil, "w") as fil:
        for result in resultat:
            namn, poang = result
            fil.write(f"{namn},{poang}\n")


if __name__ == "__main__":
    main()