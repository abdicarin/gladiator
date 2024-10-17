import random
import time
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

print ("Du är gladiatorn Guts, nu ska du slåss mot gladiatorn Griffith. \nNi befinner er på en romersk arena omgivna av en förväntansfull publik. \nNi har inga vapen eller rustning utan du är klädd enbart i ett par korta läderbyxor,\n ett par pälsstövlar och armband gjorda av läder.\nDin bara bronsfärgade bringa lyses upp av den starka solen.\npubliken som sitter runt omkring er ser förväntansfulla ut. \nGriffith ser ut att göra sig redo att gå till anfall. \nStriden kan börja.")
print("Press enter to continue ")
input("")
time.sleep(1)
print(".")
time.sleep(1)

clear_terminal()

print("Du har 10 hälsopoäng kvar, Griffith har 10 hälsopoäng kvar")

guts_hp=10
griffith_hp=10

moves= "slag", "kast", "spark"

while guts_hp>0 and griffith_hp>0:
    guts= input("Vilket väljer du: slag, spark eller kast? ")
    guts=guts.lower()

    rankings = {
        "slag": "spark",  # slag beats spark
        "spark": "kast",  # spark beats kast
        "kast": "slag"    # kast beats slag
}
    
    clear_terminal()

    if guts not in moves:
        print("Ogiltigt val.")
        continue
    



    griffith = random.choice(moves)
    print("griffith valde:", griffith)
    print("Du valde:", guts)
    time.sleep(1)
    print(".")
    if guts == griffith:
        print("Ni valde samma. Båda missar. Ni stirrar på varandra med lömsk blick.")
    elif rankings[guts] == griffith:
        print("Du kastar din fiende i golvet. Fienden förlorar 2 hälsopoäng.")
        
        print("Du sparkar din fiende i golvet. Fienden förlorar 2 hälsopoäng.")

        griffith_hp-= 2
    else:
        print("Fienden kastar dig i golvet. Du förlorar 2 hälsopoäng.")
        guts_hp-= 2

    print("Du har just nu " + str(guts_hp) + " hälsopoäng kvar.")
    print("Din fiende har " + str(griffith_hp) + " hälsopoäng kvar.")

    if griffith_hp <= 0:
        print("Striden är över! JAG VAN WHOOOOOO!")
        break

    if guts_hp<= 0:
        print("Striden är slut, fienden vann!")
        break