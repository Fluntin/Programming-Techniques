# 2023-03-19
# DD100N

#Programmet håller reda på tävlingar. En användare kan lägga till spelare och poäng. 
#Programmet sparar dem i en separat fil och läser sedan filen för att få resultaten. 
#Programmet kontrollerar också eventuella fel och har möjlighet att skriva ut en ordnad lista över resultaten.

import os
# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#--------------------------------------------------------------------
def main():
    
    # Inparameter: None
    # Returvärde: None
    
    # Huvudprogrammet som körs när programmet startas. 
    # Läser in tidigare resultat och huvudmenyn.
    
    clear_screen()
    print("\n")
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
            clear_screen()
            print("Resultattavlan är sparad. Hejdå!")
            break
        else:
            print("Felaktigt val, försök igen!")


 #--------------------------------------------------------------------   
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
        #Om file resultat.txt inte existerar.
        resultat = list()
    return resultat

#--------------------------------------------------------------------
def write_result(resultat):
    
    # Inparameter: resultat (en lista av tupler med namn och poäng)
    # Returvärde: None
    
    # Funktion för att skriva ut resultattavlan sorterad efter poäng.
    
    if len(resultat) == 0:
        clear_screen()
        print("Inga resultat hittades.")
    else:
        resultat = sorted(resultat, key=lambda person: person[1], reverse=True)
        clear_screen()
        print("Just nu är ställningen följande:")
        for i, result in enumerate(resultat):
            namn, poäng = result
            place=i+1
            print(f"{place}. {namn} {poäng} poäng")

#--------------------------------------------------------------------
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
        
        poäng = input("Vilken poäng fick spelaren? ")
        
        # Kontrollera att poängen är rimlig, användaren behöver dock bara mata in totalpoängen (inte poängen för varje pil).
        if poäng.isdigit() and (0 <= int(poäng) <= 50):
            resultat.append((namn, int(poäng)))
            print(f"{namn} har nu lagts till i resultatlistan med {poäng} poäng!")
            break
        else:
            poäng = input("Det där var inte en rimlig poäng. Försök igen. Vilken poäng fick spelaren? ")

#--------------------------------------------------------------------
def spara_resultat(resultat):
    
    # Inparameter: resultat (en lista av tupler med namn och poäng)
    # Returvärde: None
    
    # Funktion för att spara resultatlistan till filen resultatfil.
    
    resultatfil = "resultat.txt"  # Filnamnet för textfilen där resultaten sparas
    with open(resultatfil, "w") as fil:
        for result in resultat:
            namn, poäng = result
            fil.write(f"{namn},{poäng}\n")


if __name__ == "__main__":
    main()
