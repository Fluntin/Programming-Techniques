# -*- coding: utf-8 -*-
"""
This is the second code for course DD100N written on 2022-02-13
The code allows user to choose conversions from the menu or exit the program.
"""



switch=0

def Selection_Menu():
    print("Välkommen till Konverteraren!")
    print("Välj en av följande konverteringar:")
    print("1. Grader Celsius till grader Fahrenheit")
    print("2. Meter till amerikanska mil")
    print("3. Liter till gallon")
    print("4. Avsluta")


while switch==0 :
     Selection_Menu()  
     val = int(input("Vad väljer du?:"))
     
                    
     if val==1:
         celsius = float(input("Ange grader i Celsius:"))
         print(celsius ,"grader Celsius motsvarar ", celsius*1.8+32 , "Grader Ferenheit.") 
         print()
              
     elif val==2:
         meter = float(input("Ange antal meter:"))
         print(meter ,"meter motsvarar ", meter/1609.3 , "amerikanska mil.") 
         print()
         
     elif val==3:
         liter=float(input("Ange antal liter:"))
         print(liter ,"liter motsvarar ", liter/3.785 , "gallon.") 
         print()  
         
     elif val==4:
         print("Välkommen åter!")
         switch=1
     else:
         print("Använd ett av alternativen som erbjuds av menyn.")
