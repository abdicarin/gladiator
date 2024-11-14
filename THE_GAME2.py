import random
import time 
import sys # jag behövde nånting så att alla text kommer inte till sammans. 
import os
# saker att göra 
# första menu
# välja difficult level
# välja din gäadiator 
# stamina system
# mer ascii art
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02) 
        
    print()

welcome_asicii="""
 ██╗       ██╗ ███████╗ ██╗      ██╗      █████╗   █████╗   ███╗   ███╗ ███████╗   ████████╗ █████╗
 ██║  ██╗  ██║ ██╔════╝ ██║      ██║      ██╔══██  ██╔══██╗ ████╗ ████║ ██╔════╝   ╚══██╔══╝██╔══██╗
 ╚██╗████╗██╔╝ █████╗   ██║      ██║      ██║      ██║  ██║ ██╔████╔██║ █████╗        ██║   ██║  ██║
  ████╔═████║  ██╔══╝   ██║      ██║      ██║  ██╗ ██║  ██║ ██║╚██╔╝██║ ██╔══╝        ██║   ██║  ██║
  ╚██╔╝ ╚██╔╝  ███████╗ ███████╗ ███████╗ ╚█████╔╝ ╚█████╔╝ ██║ ╚═╝ ██║ ███████╗      ██║   ╚█████╔╝
   ╚═╝   ╚═╝   ╚══════╝ ╚══════╝ ╚══════╝ ╚════╝    ╚════╝  ╚═╝     ╚═╝ ╚══════╝      ╚═╝    ╚════╝

 █████╗  ██████╗  ███████╗ ███╗ ██╗   █████╗    █████╗  ███╗  ██╗████████╗██╗  █████╗  ██████╗
██╔══██  ██╔══██╗ ██╔════╝ ████╗ ██║  ██╔══██╗  ██╔══██╗ ████╗ ██║╚══██╔══╝██║ ██╔══██  ██╔
███████  ██████╔╝ █████╗   ██╔██╗██║  ███████║  ███████║ ██╔██╗██║   ██║   ██║ ██║      ╚█████╗
██╔══██  ██╔══██╗ ██╔══╝   ██║╚████║  ██╔══██║  ██╔══██║ ██║╚████║   ██║   ██║ ██║  ██╗ ╚═══██╗
██║  ██  ██║  ██║ ███████╗ ██║ ╚███║  ██║  ██║  ██║  ██║ ██║ ╚███║   ██║   ██║ █████╔╝ ██████
╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚══╝  ╚═╝╚═╝    ╚═╝  ╚═╝ ╚═╝  ╚══╝   ╚═╝   ╚═╝ ╚════╝  ╚═════╝
"""
def clear_terminal():# ta bort gamla frågar
    if os.name == 'nt':
        os.system('cls')

def setup_menu():
    print_slow("Welcome to the Gladiator Game!")
    print_slow("1. Start Game")
    print_slow("2. Exit")

    while True:  # början 
        choice = input("Choose an option (1 or 2): ")
        if choice == "1":
            print("Starting game:")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            print(welcome_asicii)
            time.sleep(1)
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            
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

def difficulty_level():
    my_hp = 50
    opps_hp = 50
    clear_terminal()
    print_slow("Choose difficulty level: ")
    print_slow("1: Easy\n2: Medium\n3: Hard")

    while True: 
            difficulty_choice = int(input("Choose a number (1, 2, or 3): "))
            if difficulty_choice == 1:
                my_hp += 20
                opps_hp -= 10
                print_slow("Easy mode selected. Your HP increased by 20, opponent's HP decreased by 10.")
                time.sleep(5)
                break  
            elif difficulty_choice == 2:
                my_hp += 10
                print_slow("Medium mode selected. Your HP increased by 10.")
                time.sleep(5)
                break
            elif difficulty_choice == 3:
                print_slow("Hard mode selected. No changes to HP.")
                time.sleep(5)
                break
            else:
                print_slow("Invalid choice. Please choose one of the options.")
    clear_terminal()
    print_slow(f"Chosen difficulty level: {difficulty_choice}")
    print_slow(f"My HP: {my_hp}")
    print_slow(f"Opponent's HP: {opps_hp}")
    return difficulty_choice, my_hp, opps_hp

def select_gladiator():
    print_slow("Choose Your Gladiator:")
    print_slow("1. Dimachaerius (tvåsvärdskämpe) - had little armor and fought with two swords\nFast Gladiator (higher dodge chance)") #stats för a fast gladiator???
    print_slow("2. Secutor (förföljaren) - heavily armed gladiator\n   Defensive Gladiator") #stats för defensiva gladiator ???
    print_slow("3. Gladiatrix - a female gladiator")# stats för female????

    gladiator_choice = ""
    while gladiator_choice not in ("1", "2", "3"):
        gladiator_choice = input("Choose your gladiator (1, 2, or 3): ")
        if gladiator_choice not in ("1", "2", "3"):
            print_slow("Invalid choice. Try again.")

    print_slow(f"You chose gladiator option {gladiator_choice}.")
    return gladiator_choice


# kallar alla funktione
setup_menu()
difficulty_level()
select_gladiator()






# print("Du har just nu " + str(guts_hp) + " hälsopoäng kvar.")
# time.sleep(1)
# print("Din opps har " + str(griffith_hp) + " hälsopoäng kvar.")
# time.sleep(1)


# while True:  
#     opps -= random.choice([0, 1])

    # print("\nDu har just nu " + str(my_hp) + " hälsopoäng kvar.")
#     time.sleep(1)
#     print("din opps har " + str(opps_hp) + " hälsopoäng kvar.")
#     time.sleep(1)

#     # vad ska hända om du vinner eller om din opps vinner
#     if opps_hp <= 0:
#         print("Striden är över! JAG VAN WHOOOOOO!")
#         time.sleep(1)
#         print(win_ascii)
#         break

#     if my_hp <= 0:
#         print("Striden är slut, din opps vann!")
#         time.sleep(1)
#         print(lose_ascii)
#         break

