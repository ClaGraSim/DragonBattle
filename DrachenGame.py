import random


###Schadensmodell###
###Heiltrank=1###
###Ausweichen+Feuer=0.5###
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
def cleverinput(miz=0,maz=5,default=0):
    while True:
        r=input("?")
        if r =="":
            return default
        if r.isdigit():
            r=int(r)
            if r <miz or r>maz:
                print("BLÖDESTE ZAHL EVER")
                continue
            return r



while bhp > 0 and ghp > 0:
    runde = runde + 1
    print("AU!!!",b,"hat noch",bhp,"Leben übrig")
    #while True:
    for x in menuA:
        print(menuA.index(x),x)
    x=cleverinput(miz=0,maz=5,default=0)
    
            
    if x ==0:
        break
  
    elif x ==1:
        print("Du versuchst den ULTIMATIVEN ANGRIFF")
        treffer=random.random()
        if treffer < krit:
            print("HURRAAA!!!")
            schaden=maxschaden*3
            print(b,"erleidet",schaden,"Schaden")
            bhp=bhp-schaden
        else:
            print("Angriff fehlgeschlagen")
    elif x==2:
        print("Goblin greift an! Runde:",runde)
        schaden=random.randint(0,maxschaden)
        print(b,"erleidet",schaden,"Schaden")
        bhp=bhp-schaden 
    #Drache schlägt zurück
    
    
    for x in menuB:
            print(menuB.index(x),x)
    x=cleverinput(miz=0,maz=6,default=0)
        

    if x ==0:
        break
    elif x==3:
        print ("Du bekommst 5 Herzen zurück")
        ghp=ghp+5
        print("Du bist geheilt und hast jetzt", ghp,"Herzen")
   
    
    action=random.choice(DrachenAction)
    if action == "Feuer":
        print("Der Drache spuckt Feuer")
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
    print("Du erleidest Schaden:",schaden)
    print("Du hast noch",ghp,"Leben")
    print("<3"*int(ghp))
    
    
        
         
        
    
    
    

        

