from colorama import Fore, Style, init
import os
import sys

init(autoreset=True)

text = """
░▒▓███████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░        ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓██████▓▒░  ░▒▓███████▓▒░  
"""

option1 = """
Nuker >> The Invite Code for the nuker is https://discord.com/oauth2/authorize?client_id=1278453727031857204&permissions=8&integration_type=0&scope=bot, Sometimes, The servers will be down, So you may have to host it on your machine, The code for the nuker will be avaliable on github at https://github.com/sawyerschat/nyxus.py/tree/main
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def display_text():
    clear_screen()
    print(Fore.MAGENTA + text)
    print(Style.RESET_ALL)
def display_options():
    print(Fore.CYAN + "[1] Nuker")
    print(Fore.CYAN + "[2] Raider")
    print(Fore.CYAN + "[3] Selfbot")
    print(Fore.CYAN + "[4] Member Boost")
    print(Style.RESET_ALL)
def main():
    display_text()
    display_options()
    choice = input("select option: ")
    if choice == '1':
        print("nan1")
    elif choice == '2':
        print("nan2")
    elif choice == '3':
        print("nan3")
    elif choice == '4':
        print("nan4")
    else:
        print("wrong option")

if __name__ == "__main__":
    main()
