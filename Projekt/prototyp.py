# 168 Minröjning
# Villim Prpic
# DD100N
# 2023-04-16

"""
Programmet "168 Minröjning" är ett spel.
Spelet innebär att man slumpmässigt placerar minor på en matris och låter användaren 
navigera genom matrisen genom att avslöja innehållet i varje cell.
Om en mina avslöjas avslutas spelet.
Om en cell är tom visar spelet antalet intilliggande minor. 
Spelet kan vinnas genom att antingen avslöja alla tomma celler eller flagga alla minor.
"""

# Algoritm för minröjningsspel:
# 1. Generera en tom spelplan av given storlek.
# 2. Placera ut det angivna antalet minor slumpmässigt på spelplanen.
# 3. Låt användaren välja en cell att avslöja.
# 4. Om cellen innehåller en mina, avsluta spelet.
# 5. Om cellen är tom, avslöja intilliggande celler tills celler med intilliggande minor avslöjas.
# 6. Upprepa steg 3-5 tills spelet är slut.
# 7. Om alla tomma celler har avslöjats eller alla minor har flaggats, vinner användaren.
# 8. Visa resultatet och fråga om användaren vill spela igen eller avsluta.

class Main:
"""
Representerar huvudprogrammet för spelet.
Frågar användaren efter deras namn, storleken på spelbrädet och antalet minor innan spelet startar.
"""

    def __init__(self):
        """
        Skapar en ny instans av huvudprogrammet.
        """

    def spela(self):
        """
        Startar spelet och hanterar varje omgång av spelet tills spelet är slut. 
        Returnerar resultatet av spelet.
        """

    def visa_highscore(self):
        """
        Visar highscore-listan för tidigare spelare.
        """

    def spara_highscore(self, resultat):
        """
        Sparar det nya spelets resultat i highscore-listan om det är tillräckligt bra för att vara med bland de topp 10.
        
        parameter: resultat(str) - Resultatet av det nya spelet som ska sparas.
        """

    def avsluta(self):
        """
        Avslutar programmet.
        """

class Mechanism :
    """ 
    En klass som hanterar logiken för programmet:
    """ 

    def __init__(self, storlek, antal_minor):
    """ 
    grid: en matris som representerar minfältet där "M" motsvarar en mina och 
            siffrorna motsvarar antalet intilliggande minor.
            
    ubtern_grid: en matris som representerar det synliga spelbrädet. 
                   Värdena är som standard satta till "*" och avslöjas när den motsvarande cellen i "grid" klickas på.
                   
    storlek: storleken på spelbrädet.
    
    antal_minor: antalet minor i spelet.
    """

    def generera_grid(self, storlek, antal_minor):
        """
        genererar en matris som representeras av en 2d-sträng-array och lägger 
        till minor och antal intilliggande minor.

        parametrar: storlek(int), antal_minor(int)
        return: grid( 2-dimensional string array )
        """

    def placera_mina(self, grid, antal_minor):
        """
        Placerar ett specificerat antal minor slumpmässigt på spelbrädet.

        parametrar: grid(str[]), antal_minor(int)
        return: grid( 2-dimensional string array ) som innehåller minor
        """

    def kontrollera_grannar(self, func, grid, x, y):
        """
        Kontrollerar alla intilliggande celler och hanterar dem enligt den specificerade funktionsparametern. 

        parametrar: func(method), grid(str[]), x(int), y(int)
        return: En sträng från funktionsparametern, om cellen inte är en mina returneras "M"
        """

    def räkna_grannar(self, grid, x, y, count):
        """
        Ökar räkningen om cellen innehåller en mina.

        parametrar: grid(str[]), x (int), y (int), count(int)
        return: den ökade räkningen
        """

    def avslöja_grannar(self, grid, x, y, count):
        """
        Avslöjar cellen om den inte är en mina eller en avslöjad nolla.

        parametrar: grid(str[]), x (int), y (int), count(int)
        return: den oförändrade räkningen
        """

    def avslöja(self, x, y):
        """
        Avslöjar cellen och, om det är en "0", avslöjar också dess intilliggande celler och 
        kontrollerar sedan om spelet är slut. 

        parametrar: x(int), y (int)
        return: spelresultaten om spelet är slut, annars returneras den uppdaterade dolda matrisen.
        """

    def generera_dold_grid(self, stor)
        """
        Genererar den dolda matrisen, dvs. den matris som visas för spelaren.

        parametrar: storlek(int)
        return: grid( 2-dimensional string array )
        """


    def sätt_flagga(self, pos):
        """
        Sätter en flagga på cellen, om den inte redan har en, och tar bort flaggan om den redan är satt. 
        Returnerar den uppdaterade dolda matrisen.

        parametrar: pos(int[])
        return: updaterad grid( 2-dimensional string array )
        """

    def kontrollera_flaggor(self):
        """
        Kontrollerar om alla minor har flaggats. 

        parametrar:
        return: Returnerar True om spelet är vunnet, annars False.
        """

    def kontrollera_avslut(self, kontrollerad_cell):
        """
        Kontrollerar om spelet är slut och om spelaren vann eller förlorade. Returnerar resultatet av spelet.

        parametrar: kontrollerad_cell(str)
        return: resultat(str)
        """
    
    def räkna_poäng(self):
        """
        Räknar antalet avslöjade celler och skalar det enligt spelbrädets storlek och antalet minor. 

        parametrar: pos(int[])
        return: poängen(int)
        """
        
    def spara_poäng(self, poäng):
        """
        Jämför poängen med de tidigare resultaten och lägger till det om det kommer bland topp 10.
    
        parametrar: score(str)
        return: None
        """

    def hämta_highscore(self):
        """
        Laddar highscore från en textfil och returnerar en strängarray med de tidigare resultaten.

        parametrar:
        return: en str-array med de tidigare resultaten.
        """