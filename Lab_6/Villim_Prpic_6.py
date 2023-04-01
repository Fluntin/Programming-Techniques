# Villim Prpic
# 2023-03-30
# DD100N

#Programmet läser in husdjur från en textfil.
#Det ger användaren flera valmöjligheter.
#För varje husdjur kan användaren välja att klappa det eller mata det.
#Efter en action ändras siffrorna.
#Ändringarna sparas i textfilen.
#En användare kan välja att visa husdjursnamn och status för varje behov.
#--------------------------------------------------------------------

import os
import os.path

#--------------------------------------------------------------------
# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
#--------------------------------------------------------------------
# 1. Skapa en klass som representerar ett husdjur som har minst tre attribut (t.ex. namn, hunger och klappbehov). 
#    Du väljer själva vilken datatyp du vill att attributen ska ha. Definiera en konstruktor för klassen.
#
# 2. Definiera:
#    en __str__-metod (eller/och  en __repr__-metod) och
#    en __lt__-metod där du själv får välja vilket/vilka attribut du vill sortera efter.
#
# 3. Definiera minst två metoder till (t.ex. klappa() och mata()). 
#    Se till att dessa metoderna ändrar värdet attributen på något sätt.
#--------------------------------------------------------------------
class Husdjur :
    
    #Denna metod är en konstruktor för klassen Husdjur. Den tar emot tre inparametrar.
    #Metoden sätter dessa värden som egenskaper för den aktuella instansen av klassen Husdjur.
    def __init__(self, name, hunger=0, klappbehov=0):
        self.name = name
        self.hunger = hunger
        self.klappbehov = klappbehov

    #Denna metod för klassen Husdjur som definierar hur en instans av klassen ska representeras
    #som en sträng när den skrivs ut med funktionen print()
    #Metoden tar inte emot några inparametrar utöver self
    #Metoden returnerar en sträng som innehåller information om husdjuret
    def __str__(self):
        return f"{self.name}, Hunger: {self.hunger}, Klappbehov: {self.klappbehov}"

    #Denna metod för klassen Husdjur som definierar hur två instanser av klassen ska jämföras när de sorteras.
    #Tar emot två inparametrar self, som är en referens till den första instansen och other som är referens till den andra instansen av klassen som ska jämföras.
    #Returnerar en boolesk värdering som indikerar resultatet av jämförelsen.
    def __lt__(self, other):
        return self.name < other.name

    def klappa(self):
        self.klappbehov -= 1
        print(f"Du klappar {self.name}.")

    def mata(self):
        self.hunger -= 1
        print(f"Du mattar {self.name}.")

#-------------------------------------------------------------------- 
#Denna metod heter load_husdjur() och dess syfte är att läsa in information om husdjur från en textfil, 
#skapa objekt för varje husdjur baserat på den informationen, och returnera en lista med dessa objekt.

def load_husdjur():
    #Dina husdjurs-objekt ska vara lagrade i en lista.
    husdjur_lista = list()
    
    husdjurfil = "pets.txt"  # Filnamnet för textfilen där resultaten sparas
    
    try:
        with open(husdjurfil, "r") as file:
            for line in file:
                pet_info = line.strip().split(",")
                pet = Husdjur(pet_info[0], int(pet_info[1]), int(pet_info[2]))
                husdjur_lista.append(pet)
    
    #Om filen pets.txt inte kunde hittas, kommer funktionen att skriva ut ett felmeddelande och returnera en tom lista.         
    except FileNotFoundError:
        print("Error: File not found.")
        husdjur_lista = list()
        
    return husdjur_lista
#--------------------------------------------------------------------
#Denna funktion/metod heter save_husdjur() och dess syfte är att spara informationen om husdjur till en textfil.
#Funktionen tar emot två inparametrar: file_path, som är en sträng som representerar sökvägen till textfilen, 
#och pets, som är en lista med Husdjur-objekt som innehåller informationen som ska sparas.
#Funktionen returnerar ingenting.

def save_husdjur(file_path, pets):
    with open(file_path, "w") as file:
        for pet in pets:
            file.write(f"{pet.name},{pet.hunger},{pet.klappbehov}\n")
#--------------------------------------------------------------------            
#Denna metod skriver ut en lista med alla husdjur som finns i en given lista av Husdjur-objekt.
#Funktionen tar emot en inparameter: pets, som är en lista med Husdjur-objekt som ska skrivas ut.
#Funktionen returnerar ingenting.

def list_husdjur(pets):
    if not pets:
        print("Inga husdjur i lista.")
    else:
        pets.sort()
        for i, pet in enumerate(pets):
            print(f"{i+1}. {pet}")
#--------------------------------------------------------------------
#Denna metod söker efter en viss husdjur i en given lista av Husdjur-objekt.

#Funktionen tar emot två inparametrar: 
#pets, som är en lista med Husdjur-objekt att söka igenom, 
#name, som är en sträng som representerar namnet på husdjuret som ska sökas efter.

#Funktionen returnerar antingen det sökta Husdjur-objektet eller None.

def hitta_husdjur(pets, name):
    for pet in pets:
        if pet.name.lower() == name.lower():
            return pet
    return None

#--------------------------------------------------------------------
#   4. Skapa ett objekt av klassen och prova att det går att skriva ut husdjurens värden med print().
#    print("Prova att det går att skriva ut husdjurens värden med print():")
#   husdjur0=Husdjur("Selma",3,3)
#    print(husdjur0)
#    print("Nice!\n")
#--------------------------------------------------------------------
#   5. Skapa nu flera olika husdjur och lägg dem i en lista. 
#      Sortera listan och  skriv en slinga som skriver ut alla husdjur.
#
#    husdjur_lista=list()
#    husdjur_lista.append(husdjur0)
#    
#    husdjur1 = Husdjur("Pooper", hunger=3, klappbehov=3)
#    husdjur_lista.append(husdjur1)
#    
#    husdjur2 = Husdjur("Hegel", hunger=1, klappbehov=2)
#    husdjur_lista.append(husdjur2)
#    
#    husdjur3 = Husdjur("Marx", hunger=100, klappbehov=0)
#    husdjur_lista.append(husdjur3)
#    
#    husdjur_lista.sort()
#    for husdjur in husdjur_lista:
#        print(husdjur)
#     

#--------------------------------------------------------------------

def main():
    
# Läsa in data från textfilen
    file_path = "pets.txt"
    husdjur_lista = load_husdjur()
    print("\n")
    print("Välkommen till PetRobo!")

# Huvudloop som låter användaren interagera med programmet.
# Loopen fortsätter att köras tills användaren väljer att avsluta programmet

    while True:
        print("\n")
        print("Vad kan jag stå till tjänst med?")
        print("1. Lista husdjur och deras status")
        print("2. Leta upp djur")
        print("3. Avsluta")

        choice = input()
        print("\n")

        if choice == "1":
            list_husdjur(husdjur_lista)
            
        elif choice == "2":
            name = input("Vilket djur vill du att jag letar upp? ")
            husdjur = hitta_husdjur(husdjur_lista, name)
            if husdjur:
                print(f"Hittade  {husdjur.name} under soffan, vad ska jag göra nu?")
                while True:
                    print(f"1. Klappa {husdjur.name}")
                    print(f"2. Mata {husdjur.name}")
                    print("3. Tillbaka till huvudmenyn")
                    action = input()
                    if action == "1":
                        print(f"Klappar {husdjur.name}")
                        husdjur.klappa()
                        print("Vad ska jag göra nu?")
                    elif action == "2":
                        print(f"Mattar {husdjur.name}")
                        husdjur.mata()
                        print("Vad ska jag göra nu?")
                    elif action == "3":
                        break
                    else:
                        print("Invalid val.")
            else:
                print(f"Tyvärr kunde jag inte hitta {name}.")


        elif choice == "3":
            #Programmet ska skriva till samma textfil en gång, strax innan det att programmet avslutas.
            save_husdjur(file_path, husdjur_lista)
            print("Programmet avslutas. Tack för att du använder PetRobo!")
            break
        else:
            print("Invalid val")
            print("\n")

main()