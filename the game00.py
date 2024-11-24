import random
import time  #så att inte alla text kommer samma tid
import os
import sys # jag behövde nånting så att alla text kommer inte till sammans. 
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write("\n")  
    sys.stdout.flush()
def clear_terminal(): #tabort text som behövs inte längre
    if os.name == 'nt':
        os.system('cls')

welcome_asicii="""
 ██╗       ██╗ ███████╗ ██╗      ██╗      █████╗   █████╗   ███╗   ███╗ ███████╗   ████████╗ █████╗
 ██║  ██╗  ██║ ██╔════╝ ██║      ██║      ██╔══██  ██╔══██╗ ████╗ ████║ ██╔════╝   ╚══██╔══╝██╔══██╗
 ╚██╗████╗██╔╝ █████╗   ██║      ██║      ██║      ██║  ██║ ██╔████╔██║ █████╗        ██║   ██║  ██║
  ████╔═████║  ██╔══╝   ██║      ██║      ██║  ██╗ ██║  ██║ ██║╚██╔╝██║ ██╔══╝        ██║   ██║  ██║
  ╚██╔╝ ╚██╔╝  ███████╗ ███████╗ ███████╗ ╚█████╔╝ ╚█████╔╝ ██║ ╚═╝ ██║ ███████╗      ██║   ╚█████╔╝
   ╚═╝   ╚═╝   ╚══════╝ ╚══════╝ ╚══════╝ ╚════╝    ╚════╝  ╚═╝     ╚═╝ ╚══════╝      ╚═╝    ╚════╝

 █████╗  ██████╗  ███████╗ ███╗  ██╗   █████╗     █████╗  ███╗  ██╗ ████████╗ ██╗  █████╗  ██████╗
██╔══██  ██╔══██╗ ██╔════╝ ████╗ ██║  ██╔══██╗   ██╔══██╗ ████╗ ██║ ╚══██╔══╝ ██║ ██╔══██  ██╔
███████  ██████╔╝ █████╗   ██╔██╗██║  ███████║   ███████║ ██╔██╗██║    ██║    ██║ ██║      ╚█████╗
██╔══██  ██╔══██╗ ██╔══╝   ██║╚████║  ██╔══██║   ██╔══██║ ██║╚████║    ██║    ██║ ██║  ██╗ ╚═══██╗
██║  ██  ██║  ██║ ███████╗ ██║ ╚███║  ██║  ██║   ██║  ██║ ██║ ╚███║    ██║    ██║ █████╔╝  ██████
╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚══╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═╝  ╚══╝    ╚═╝    ╚═╝ ╚════╝   ╚═════╝
"""

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
def setup_menu():
    print_slow("Welcome to the Arena Antics !")
    print_slow("\n1. Start Game")
    print_slow("\n2. Exit")

    while True:  # början 
        choice = input("\nChoose an option (1 or 2): ")
        if choice == "1":
            print("Starting game:")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            clear_terminal()
            print(welcome_asicii)
            time.sleep(1)
            time.sleep(0.5)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            clear_terminal()
            input("choose your gender: ").lower
        
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            
            break  
        elif choice == "2":
            print_slow("Exiting game:")
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            print_slow(".")
            time.sleep(1)
            exit()  
        else:
            print_slow("Invalid choice. Try again.")
#välja dificult level            
my_hp = 20
opps_hp = 20
def difficulty_level():
    my_hp = 20
    opps_hp = 20
    clear_terminal()
    print_slow("Choose difficulty level: ")
    print_slow("\n1: Easy\n2: Medium\n3: Hard")
#om du väljer easy du ska ha 5 mer hälspoang och minus tio for din opps
#om du väljer medium duka ha 5 mer hälsopoang men ingen minus for din opps
#om du väjer hard ingenting ska ändras med HP
    while True:
            difficulty_choice = int(input("Choose a number (1, 2, or 3): "))
            if difficulty_choice == 1:
                my_hp += 5
                opps_hp -= 10
                print_slow(f"Easy mode selected. Your HP is now: {my_hp}, opponent's HP is now: {opps_hp}.")
                time.sleep(5)
                break  
            elif difficulty_choice == 2:
                my_hp += 5
                print_slow(f"Medium mode selected. Your HP is now: {my_hp}. opps hp is {opps_hp}")
                time.sleep(5)
                break
            elif difficulty_choice == 3:
                print_slow("Hard mode selected. No changes to yours or your opps HP.")
                time.sleep(5)
                break
            else:
                print_slow("Invalid choice. Please choose one of the options.")
    clear_terminal()
    print_slow(f"Chosen difficulty level: {difficulty_choice}")
    print_slow(f"My HP is : {my_hp}")
    print_slow(f"Opponent's HP is : {opps_hp}")
    return difficulty_choice, my_hp, opps_hp

setup_menu()
difficulty_level()
print_slow("Du är en modig gladiator i arenan Arena Antics\nDin motståndare, Cassia, är stark och farlig. Publiken skriker och hejar medan du gör dig redo för strid\nDu måste slåss smart och välja rätt attacker. Varje träff gör dig närmare segenr eller nederlaget\nKommer du att vinnna och bli en hjälte, eller förlora du och lämna arenan i skam? Kämpa hårt, \ntänk snabbt och visa att du är den bästa gladiator.\nArenan väntar, och det är dags att börja!\n")

time.sleep(5)
time.sleep(1)
print_slow(".")
time.sleep(1)
print_slow(".")
time.sleep(1)
print_slow(".")
time.sleep(1)
print_slow(".")
attack_info = {
    "light attack": {"beats": "combo attack", "damage": "1-2"},
    "heavy attack": {"beats": "light attack", "damage": "3-4"},
    "combo attack": {"beats": "heavy attack", "damage": "2-3"},
    "headbutt": {"beats": "light attack", "damage": "3-4"},
    "knee strike": {"beats": "headbutt", "damage": "3-4"},
    "chest kick stomp": {"beats": "knee strike", "damage": "3-4"},
}
# Prints attack information foe spelare

for attack, info in attack_info.items():
    print(f"- {attack.title()}: Damage {info['damage']} (Beats: {info['beats'].title()})")


print_slow("\nPress enter to continue ")
input(" ")
time.sleep(1)
print_slow(".")
time.sleep(1)
print_slow(".")
val = ("light attack", "heavy attack", "combo attack", "headbutt", "chest kick stomp", "knee strike")
#which attacks beats which
rankings = {
    "light attack": "combo attack",  
    "heavy attack": "light attack",  
    "combo attack": "heavy attack",  
    "headbutt": "light attack",      
    "Knee Strike": "headbutt",       
    "Chest Kick Stomp": "Knee Strike",  
}
clear_terminal()
while my_hp > 0 and opps_hp > 0:
    my_move = input("Vilket väljer du: light attack, heavy attack, combo attack, headbutt, Chest Kick Stomp, Knee Strike: ").lower()

    if my_move not in val:
        print("Ogiltigt val.")
        continue
    #hur cassia ska välja sin attack
    cassia = random.choice(val)
    print_slow(f"Du valde: {my_move}")
    print_slow(f"CASSIA valde: {cassia}")
    time.sleep(3)

    
    if my_move == "light attack":
        damage = random.randint(1, 2)
        print_slow(f"Du slår Cassia i ansiktet. Cassia förlorar {damage} hälsopoäng.")
    elif my_move == "heavy attack":
        damage = random.randint(3, 4)
        print_slow(f"Du sparkar Cassia i magen. Cassia förlorar {damage} hälsopoäng.")
    elif my_move == "combo attack":
        damage = random.randint(2, 3)
        print_slow(f"Du kastar Cassia i golvet. Cassia förlorar {damage} hälsopoäng.")
    elif my_move == "headbutt":
        damage = random.randint(3, 4)
        print_slow(f"Du slår Cassia med en kraftig headdbutt. Cassia förlorar {damage} hälsopoäng.")
    elif my_move == "chest kick stomp":
        damage = random.randint(3, 4)
        print_slow(f"Du sparkar Cassia i bröstet och trampar på honom. Cassia förlorar {damage} hälsopoäng.")
    elif my_move == "knee strike":
        damage = random.randint(3, 4)
        print_slow(f"Du slår Cassia med en snabb knee strike. Cassia förlorar {damage} hälsopoäng.")

    opps_hp -= damage  
    time.sleep(1)

   
    if cassia == "light attack":
        damage = random.randint(1, 2)
        print_slow(f"Cassia slår dig. Du förlorar {damage} hälsopoäng.")
    elif cassia == "heavy attack":
        damage = random.randint(3, 4)
        print_slow(f"Cassia sparkar dig i revbenen. Du förlorar {damage} hälsopoäng.")
    elif cassia == "combo attack":
        damage = random.randint(2, 3)
        print_slow(f"Cassia kastar dig i golvet. Du förlorar {damage} hälsopoäng.")
    elif cassia == "headbutt":
        damage = random.randint(3, 4)
        print_slow(f"Cassia slår dig med en kraftig headbutt. Du förlorar {damage} hälsopoäng.")
    elif cassia == "chest kick stomp":
        damage = random.randint(3, 4)
        print_slow(f"Cassia sparkar dig i bröstet och trampar på dig. Du förlorar {damage} hälsopoäng.")
    elif cassia == "knee strike":
        damage = random.randint(3, 4)
        print_slow(f"Cassia slår dig med en snabb knee strike. Du förlorar {damage} hälsopoäng.")

    my_hp -= damage 

    time.sleep(1)
    print_slow("Du har just nu " + str(my_hp) + " hälsopoäng kvar.")
    print_slow("Cassia har " + str(opps_hp) + " hälsopoäng kvar.")
    time.sleep(5)
    #vad ska hända i slutet av spelet om du vinner eller förlorar
    clear_terminal()
    if opps_hp <= 0:
        print_slow("Striden är över! DU VAN WHOOOOOO!")
        time.sleep(1)
        print_slow(".")
        time.sleep(1)
        print_slow(".")
        time.sleep(1)
        print_slow(".")
        time.sleep(1)
        print(win_ascii)
        break
    if my_hp <= 0:
        print_slow("Striden är slut, Cassia vann!")
        time.sleep(1)
        print_slow(".")
        time.sleep(1)
        print_slow(".")
        time.sleep(1)
        print_slow(".")
        time.sleep(1)
        print(lose_ascii)
        break
