import random # 
import time  #så att inte alla text kommer samma tid
import os

def clear_terminal(): #tabort text som behövs inte längre
    if os.name == 'nt':
        os.system('cls')

print("Du är gladiatorn Guts, nu ska du slåss mot gladiatorn Griffith. \nNi befinner er på en romersk arena omgivna av en förväntansfull publik. \nNi har inga vapen eller rustning utan du är klädd enbart i ett par korta läderbyxor,\nett par pälsstövlar och armband gjorda av läder.\nDin bara bronsfärgade bringa lyses upp av den starka solen.\npubliken som sitter runt omkring er ser förväntansfulla ut. \nGriffith ser ut att göra sig redo att gå till anfall. \nStriden kan börja.")
time.sleep(0.8)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.3)
print(".")

print("Press enter to continue ")
input("")
time.sleep(1)
print(".")
time.sleep(1)
print(".")

clear_terminal()

def setup_menu():
    print("Welcome to the Gladiator Game!")
    print("1. Start Game")
    print("2. Exit")
    choice = input("Choose an option? 1 or 2:  ")
    if choice == "2":
        exit()

    print("Choose Your Gladiator:")
    print("1. Fast Gladiator (higher dodge chance)")
    print("2. Defensive Gladiator (higher health, better blocking)")
    print("3. Balanced Gladiator (average stats)")
    gladiator_choice= input("Choose your gladiator: ")
    print("\nChoose your gladiator's gender:")
    print("1. Male")
    print("2. Female")
    gender_choice = input("Choose gender (1-2): ")
    time.sleep(0.8)
    print(".")
    time.sleep(0.8)
    print(".")
    clear_terminal()

    return gladiator_choice, gender_choice 
setup_menu()
    

guts_hp = 4
griffith_hp = 4
print("Du har just nu " + str(guts_hp) + " hälsopoäng kvar.")

print("Griffith har " + str(griffith_hp) + " hälsopoäng kvar.")

val = ("slag", "kast", "spark")
rankings = {
    "slag": "spark",  # slag beats spark
    "spark": "kast",  # spark beats kast
    "kast": "slag"    # kast beats slag
}
#ascii om du förlurar eller vinnar

lose_ascii="""


$$\     $$\  $$$$$$\  $$\   $$\       $$\       $$$$$$\   $$$$$$\  $$$$$$$$\       $$\       $$\       $$\ 
\$$\   $$  |$$  __$$\ $$ |  $$ |      $$ |     $$  __$$\ $$  __$$\ $$  _____|      $$ |      $$ |      $$ |
 \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |     $$ /  $$ |$$ /  \__|$$ |            $$ |      $$ |      $$ |
  \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |\$$$$$$\  $$$$$\          $$ |      $$ |      $$ |
   \$$  /   $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ | \____$$\ $$  __|         \__|      \__|      \__|
    $$ |    $$ |  $$ |$$ |  $$ |      $$ |     $$ |  $$ |$$\   $$ |$$ |                                    
    $$ |     $$$$$$  |\$$$$$$  |      $$$$$$$$\ $$$$$$  |\$$$$$$  |$$$$$$$$\       $$\       $$\       $$\ 
    \__|     \______/  \______/       \________|\______/  \______/ \________|      \__|      \__|      \__|  
    
    
    """

win_ascii=""" 


                                                   __                  __        __        __ 
                                                  /  |                /  |      /  |      /  |
 __    __   ______   __    __        __   __   __ $$/  _______        $$ |      $$ |      $$ |
/  |  /  | /      \ /  |  /  |      /  | /  | /  |/  |/       \       $$ |      $$ |      $$ |
$$ |  $$ |/$$$$$$  |$$ |  $$ |      $$ | $$ | $$ |$$ |$$$$$$$  |      $$ |      $$ |      $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ | $$ | $$ |$$ |$$ |  $$ |      $$/       $$/       $$/ 
$$ \__$$ |$$ \__$$ |$$ \__$$ |      $$ \_$$ \_$$ |$$ |$$ |  $$ |       __        __        __ 
$$    $$ |$$    $$/ $$    $$/       $$   $$   $$/ $$ |$$ |  $$ |      /  |      /  |      /  |
 $$$$$$$ | $$$$$$/   $$$$$$/         $$$$$/$$$$/  $$/ $$/   $$/       $$/       $$/       $$/ 
/  \__$$ |                                                                                    
$$    $$/                                                                                     
 $$$$$$/        
     

 """


while guts_hp > 0 and griffith_hp > 0:
    guts = input("Vilket väljer du: slag, spark eller kast? ").lower()

    if guts not in val:
        print("Ogiltigt val.")
        continue 

    griffith = random.choice(val)
    
    print("GRIFFITH valde:", griffith)
    print("Du valde:", guts)
    clear_terminal()

    if guts == griffith:
        print("Ni valde samma. Båda missar. ni båda backar och gör er redo att att slå igen.")

    elif rankings[guts] == griffith:
        if guts == "slag":
            print("Du slår Griffith i ansiktet. Griffith förlorar 2 hälsopoäng.")
        elif guts == "spark":
            print("Du sparkar Griffith i magen. Griffith förlorar 2 hälsopoäng.")
        elif guts == "kast":
            print("Du kastar Griffith i golvet. Griffith förlorar 2 hälsopoäng.")
        griffith_hp -= 2
      
   
    else:
        if griffith == "slag":
            print("Griffith slår dig. Du förlorar 2 hälsopoäng.")
        elif griffith == "spark":
            print("Griffith sparkar dig i revbenen. Du förlorar 2 hälsopoäng.")
        elif griffith == "kast":
            print("Griffith kastar dig i golvet. Du förlorar 2 hälsopoäng.")
        guts_hp -= 2
        

    print("Du har just nu " + str(guts_hp) + " hälsopoäng kvar.")
    print("Griffith har " + str(griffith_hp) + " hälsopoäng kvar.")

    if griffith_hp <= 0:
        print("Striden är över! JAG VAN WHOOOOOO!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(win_ascii)
        break


    if guts_hp <= 0:
        print("Striden är slut, Griffith vann!")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(lose_ascii)
        
        break


