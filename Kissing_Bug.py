import os
import getpass
from termcolor import colored, cprint

os.system('cls')
cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

cprint(
    "                                           ██╗░░██╗██╗░██████╗░██████╗██╗███╗░░██╗░██████╗   ░██████╗░██╗░░░██╗░██████╗░",
    'blue', attrs=['bold', 'blink'])
cprint(
    "                                           ██║░██╔╝██║██╔════╝██╔════╝██║████╗░██║██╔════╝   ░██╔══██╗██║░░░██║██╔════╝░",
    'blue', attrs=['bold', 'blink'])
cprint(
    "                                           █████═╝░██║╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗   ░██████╦╝██║░░░██║██║░░███╗░",
    'blue', attrs=['bold', 'blink'])
cprint(
    "                                           ██╔═██╗░██║░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗  ░██╔══██╗██║░░░██║██║░░╚██╗",
    'blue', attrs=['bold', 'blink'])
cprint(
    "                                           ██║░╚██╗██║██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ░██████╦╝╚██████╔╝╚██████╔╝",
    'blue', attrs=['bold', 'blink'])
cprint(
    "                                           ╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝   ░╚═════╝░░╚═════╝░░╚═════╝░",
    'blue', attrs=['bold', 'blink'])

cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

dev = colored('Smart Monk-E', 'red', attrs=['bold'])
github = colored('https://github.com/Mayur-Debu/Kissing-Bug', 'red', attrs=['bold'])
current_hacker = getpass.getuser()
current_hacker = colored(current_hacker, 'green', attrs=['bold'])

print(f'Developer: {dev}')
print(f'Want to contribute? {github}')
print(f'Currently Logged in as: {current_hacker}')

cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

while True:
    cprint('1: PDF Decryter.', 'yellow')
    cprint('2: Detect Malware.', 'yellow')
    cprint('3: Exit the software.', 'yellow')

    choice = int(input('Enter your choice:'))
    if choice == 1:
        try:
            os.system('cls')
            os.system('python pdf_password_remover.py')
        except ImportError:
            cprint('\nERROR WHILE IMPORTING !!!', 'red', attrs=['bold'])
            cprint('Contact The Developer: https://github.com/Mayur-Debu/Kissing-Bug \n')
            break
    elif choice == 2:
        try:
            os.system('cls')
            os.system('python Detect_Malware.py')
        except ImportError:
            cprint('\nERROR WHILE IMPORTING !!!', 'red', attrs=['bold'])
            cprint('Contact The Developer: https://github.com/Mayur-Debu/Kissing-Bug \n')
            break

    elif choice == 3:
        exit()
