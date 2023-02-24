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


# define colors for the ai2.py file (the code is imported from the ai2.py file but being run here so  we need to define it here)
kolory = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]


# define smth (idk how to explain it)
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
    sleep(.3)
    print('1) Run')
    print('2) Help')
    print('3) Exit')
    choice =input('Enter Choice: ')
    choice = choice.strip()

    if choice == '1':
        run()
    elif choice == '2':
        slow_type('\nmsg me on dc:\nTheFilipcom4607#8475\nor open an issue on github')
        print('3...')
        sleep(1)
        print('2...')
        sleep(1)
        print('1...')
        sleep(1)
        print('Going back to home screen...')
        sleep(.4)
        clean()
        uwu()
    
    elif choice == '3':
        clean()
        exit()
        


# define slow_type function (i use this in this code to have this "slow type" effect)
def slow_type(text):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(0.05)
    print()




# define clean function (i use this in this code to clean the screen)
def clean():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
     
clean()

# define run function (i use this part to run the code from another file)
def run():
    for i in tqdm (range (600),
               desc="Loading…",
               ascii=False, ncols=75):
        time.sleep(0.001)
        # Opening the file "p.py" and reading its contents
    with open("ai2.py", "r") as file:
        code = file.read()

     # Executing the code
    exec(code)
    clean()
    print("""
    
    ██████╗ ██╗   ██╗███████╗██╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
    ██████╔╝ ╚████╔╝ █████╗  ██║
    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
    ██████╔╝   ██║   ███████╗██╗
    ╚═════╝    ╚═╝   ╚══════╝╚═╝
    """)
    sleep(3)
    clean()
    exit()


colorama.init(autoreset=True)


#! here the "define functions" part ends, now the "main" part starts 


print (Fore.CYAN + """████████╗██╗  ██╗███████╗███████╗██╗██╗     ██╗██████╗ 
╚══██╔══╝██║  ██║██╔════╝██╔════╝██║██║     ██║██╔══██╗
   ██║   ███████║█████╗  █████╗  ██║██║     ██║██████╔╝
   ██║   ██╔══██║██╔══╝  ██╔══╝  ██║██║     ██║██╔═══╝ 
   ██║   ██║  ██║███████╗██║     ██║███████╗██║██║     
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝╚═╝     
""")
sleep(0.3)
slow_type("Program Made by TheFilip\n")
sleep(.3)
print('1) Run')
print('2) Help')
print('3) Exit')
choice =input('Enter Choice: ')
choice = choice.strip()

if choice == '1':
    run()
elif choice == '2':
    slow_type('\nmsg me on dc:\nTheFilipcom4607#8475\nor open an issue on github\n')
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Going back to home screen...')
    sleep(.4)
    clean()
    uwu()

    
elif choice == '3':
    clean()
    print("""

    ██████╗ ██╗   ██╗███████╗██╗
    ██╔══██╗╚██╗ ██╔╝██╔════╝██║
    ██████╔╝ ╚████╔╝ █████╗  ██║
    ██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
    ██████╔╝   ██║   ███████╗██╗
    ╚═════╝    ╚═╝   ╚══════╝╚═╝
    """)
    sleep(3)
    clean()
    exit()

