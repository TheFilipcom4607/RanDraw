import turtle
import random
from os import system, name
from colorama import Fore, Back, Style
import colorama
from time import sleep
import os
import platform
import time
from tqdm import tqdm
kolory = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
def uwu():
    print (Fore.CYAN + """████████╗██╗  ██╗███████╗███████╗██╗██╗     ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝██╔════╝██║██║     ██║██╔══██╗
   ██║   ███████║█████╗  █████╗  ██║██║     ██║██████╔╝
   ██║   ██╔══██║██╔══╝  ██╔══╝  ██║██║     ██║██╔═══╝ 
   ██║   ██║  ██║███████╗██║     ██║███████╗██║██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝     
    """)
    sleep(0.3)
    print("Program Made by TheFilip\n")
    print('1) Run')
    print('2) Help')
    print('3) Exit')
    choice =input('Enter Choice: ')
    choice = choice.strip()

    if choice == '1':
        run()
    elif choice == '2':
        slow_type('\nmsg me on dc:\nTheFilipcom4607#8475\nor open an issue on github')
        sleep(3)
        clean()
        uwu()
    
    elif choice == '3':
        clean()
        exit()
        
def slow_type(text):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(0.05)
    print()

def clean():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
clean()

def run():
    for i in tqdm (range (101),
               desc="Loading…",
               ascii=False, ncols=75):
        time.sleep(0.01)
        # Opening the file "p.py" and reading its contents
    with open("ai2.py", "r") as file:
        code = file.read()

# Executing the code
    exec(code)
     
    print("Complete.")
    xd =input('Exit the program? y/n')
    if xd == 'y':
        clean()
        exit()
    elif xd == 'n':
        clean()
        print (Fore.CYAN + """████████╗██╗  ██╗███████╗███████╗██╗██╗     ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝██╔════╝██║██║     ██║██╔══██╗
   ██║   ███████║█████╗  █████╗  ██║██║     ██║██████╔╝
   ██║   ██╔══██║██╔══╝  ██╔══╝  ██║██║     ██║██╔═══╝ 
   ██║   ██║  ██║███████╗██║     ██║███████╗██║██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝     
    """)


    sleep(0.3)
    print("Program Made by TheFilip\n")
    print('1) Run')
    print('2) Help')
    print('3) Exit')
    choice =input('Enter Choice: ')
    choice = choice.strip()

    if choice == '1':
        run()
    elif choice == '2':
        slow_type('\nmsg me on dc:\nTheFilipcom4607#8475\nor open an issue on github')
        sleep(3)
        clean()
        uwu()
        
    elif choice == '3':
        clean()
        exit()

        

colorama.init(autoreset=True)





print (Fore.CYAN + """████████╗██╗  ██╗███████╗███████╗██╗██╗     ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝██╔════╝██║██║     ██║██╔══██╗
   ██║   ███████║█████╗  █████╗  ██║██║     ██║██████╔╝
   ██║   ██╔══██║██╔══╝  ██╔══╝  ██║██║     ██║██╔═══╝ 
   ██║   ██║  ██║███████╗██║     ██║███████╗██║██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝     
""")
sleep(0.3)
slow_type("Program Made by TheFilip\n")
print('1) Run')
print('2) Help')
print('3) Exit')
choice =input('Enter Choice: ')
choice = choice.strip()

if choice == '1':
    run()
elif choice == '2':
    slow_type('\nmsg me on dc:\nTheFilipcom4607#8475\nor open an issue on github')
    sleep(3)
    clean()
    uwu()

    
elif choice == '3':
    clean()
    exit()




