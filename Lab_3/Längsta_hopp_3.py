# -*- coding: utf-8 -*-
"""
This is the third code for course DD100N written on 2022-02-27
The code allows user to input names of students and values of jumps, and then use a menu 
for some basic commands.
"""

hoppDict = {}
ANTAL_ELEVER=3
ANTAL_HOPP=3

for i in range(ANTAL_ELEVER):
    print("vänligen ange studentens namn: ")
    name=input()
    hoppList=[]
    for j in range(ANTAL_HOPP):
        print("Hoppets värde: ")
        hopp=float(input())
        hoppList.append(hopp)
        
    hoppDict[name]=hoppList

menuSwitch=1

while menuSwitch==True:
    print("1. Visa alla resultat")
    print("2. Visa längsta hopp för varje elev")
    print("3. Visa hur långt det sista hoppet var för varje elev")
    print("4. Avsluta program")
    val=int(input())
    
    if val==1:
      for name in hoppDict.keys():
          print(name, "hoppade", hoppDict[name] , "meter.")
          
    elif val==2:
        for name in hoppDict.keys():
            hoppList=hoppDict[name]
            print(name , " hoppade som längst", max(hoppList), "meter.")
                
    
    elif val==3:
        for name in hoppDict.keys():
            hoppList=hoppDict[name]
            print(name ,"hoppade" , hoppList[-1] ," meter i sista hoppet.")
        
    elif val==4:
        menuSwitch=False
        print("Välkommen åter!")
    else:
        print("Välj ett giltigt alternativ.")
