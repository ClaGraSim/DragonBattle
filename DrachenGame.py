import random


###Schadensmodel###
###Heiltrank=1###
###Ausweichen+Feurer=0.5###
###Ausweichen+Biss=0###
###Ausweichen+Klaue=1###

#Verstecken#
###Verstecken+Feuer=1###
###Verstecken+Biss=0.5###
###Verstecken+Klaue=0###

#Deckung#
###Deckung+Biss=1###
###Deckung+Feuer=0###
###Deckung+Klaue=0.5###
s={}
s["Feuer"]={"Ducken":0,"Ausweichen":0.5,"Verstecken":1,"Heiltrank":1}
s["Biss"]={"Ducken":0.5,"Ausweichen":0,"Verstecken":1,"Heiltrank":1}
s["Klaue"]={"Ducken":1,"Ausweichen":0,"Verstecken":1,"Heiltrank":1}
b="EnderDragon"
bhp=50
g="Goblin"
ghp=30
DrachenAction=["Feuer",
               "Klaue",
               "Biss"]
maxschaden=2
runde=0
krit=0.2
menuA=["Beenden",
      "Ultimativer Angriff",
      "Normaler Angriff"]
ducken=False
ausweichen=False
verstecken=False
menuB=["Beenden",
      "Ausweichen",
      "Verstecken",
      "Heiltrank",
      "Ducken"]
      



while bhp > 0 and ghp > 0:
    runde = runde + 1
    print("AU!!!",b,"hat noch",bhp,"leben übrig")
    while True:
        for x in menuA:
            print(menuA.index(x),x)
        x=input()
        if x < "0" or x > "6" or len(x)>1:
            print("Falsche Eingabe!!!!")
            continue
        else:
            print("OK")
            break
    if x =="0":
        break
  
    elif x =="1":
        print("Du versuchst den ULTIMATIVEN ANGRIFF")
        treffer=random.random()
        if treffer < krit:
            print("HURAAA!!!")
            schaden=maxschaden*3
            print(b,"erleidet",schaden,"schaden")
            bhp=bhp-schaden
        else:
            print("Angriff fehlgeschlagen")
    elif x=="2":
        print("Goblin greift an! Runde:",runde)
        schaden=random.randint(0,maxschaden)
        print(b,"erleidet",schaden,"schaden")
        bhp=bhp-schaden 
    #Drache schlägt zurück
    ducken=False
    ausweichen=False
    verstecken=False
    while True:
        for x in menuB:
            print(menuB.index(x),x)
        x=input()
        if x < "0" or x > "6" or len(x)>1:
            print("Falsche Eingabe!!!!")
            continue
        else:
            print("Gut!")
            break
        

    if x =="0":
        break
    elif x=="3":
        print ("Du bekommst 5 Herzen zurück")
        ghp=ghp+5
        print("Du bist Geheilt und hast jetzt", ghp,"Herzen")
    elif x =="4":
        ducken=True
    elif x =="1":
        ausweichen=True
    elif x =="2":
        verstecken=True
    
    action=random.choice(DrachenAction)
    if action == "Feuer":
        print("Der Drache spukt Feurer")
    elif action == "Klaue":
        print("Der Drache schlägt nach dir")
    elif action == "Biss":
        print("Der Drache schnappt nach dir")
    #Schadensberechnung#
    schaden=s[action][menuB[int(x)]] * random.randint(2,4)
    if schaden ==0:
        print("Das war clever!")
    else:
        print("Schlechte Idee")
    ghp=ghp-schaden
    print("Du erleidest schaden:",schaden)
    print("Du hast noch",ghp,"Leben")
    print("<3"*int(ghp))
    
    
        
         
        
    
    
    

        

