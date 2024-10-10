import random
import time
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

print ("Du är gladiatorn Guts, nu ska du slåss mot gladiatorn Griffith. \nNi befinner er på en romersk arena omgivna av en förväntansfull publik. \nNi har inga vapen eller rustning utan du är klädd enbart i ett par korta läderbyxor, ett par pälsstövlar och armband gjorda av läder.\nDin bara bronsfärgade bringa lyses upp av den starka solen.\npubliken som sitter runt omkring er ser förväntansfulla ut. \nGriffith ser ut att göra sig redo att gå till anfall. \nStriden kan börja.")
print("Press enter to continue ")
input("")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)

clear_terminal()

guts_hp=10
griffith_hp=10
moves= "slag", "kast", "spark"
while guts_hp>0 and griffith_hp>0:
    my_choice= input("slag", "kast", "spark")



 
 