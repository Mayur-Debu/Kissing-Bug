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


def importError():
    cprint('\nERROR WHILE IMPORTING !!!', 'red', attrs=['bold'])
    cprint('Contact The Developer: https://github.com/Mayur-Debu/Kissing-Bug \n')
    exit()


try:
    while True:
        cprint('1: PDF Decryter.', 'yellow')
        cprint('2: Detect Malware.', 'yellow')
        cprint('3: Sars-coV Virus Builder.', 'yellow')
        cprint('4: Pyrated Windows Activator.', 'yellow')
        cprint('5: Saycheese Spy.', 'yellow')
        cprint('6: Camera Hacker.', 'yellow')
        cprint('7: KeyLogger.', 'yellow')
        cprint('8: Exit the software.', 'yellow')

        choice = int(input('Enter your choice:'))

        if choice == 1:
            try:
                os.system('cls')
                os.system('python pdf_password_remover.py')
            except OSError:
                os.system('clear')
                os.system('python3 pdf_password_remover.py')
            except ImportError:
                importError()
                break

        elif choice == 2:
            try:
                os.system('cls')
                os.system('python Detect_Malware.py')
            except OSError:
                os.system('clear')
                os.system('python3 Detect_Malware.py')
            except ImportError:
                importError()
                break

        elif choice == 3:
            try:
                os.system('cls')
                os.system('python Sars_cov.py')
            except OSError:
                os.system('clear')
                os.system('python3 Sars_cov.py')
            except ImportError:
                importError()
                break

        elif choice == 4:
            try:
                os.system('cls')
                os.system('python Win_Activator.py')
            except OSError:
                os.system('clear')
                os.system('python3 Win_Activator.py')
            except ImportError:
                importError()

        elif choice == 5:
            try:
                cprint("Make sure you're running this function on LINUX.", 'red', attrs=['bold'])
                print()
                current_working_directory = os.getcwd()
                os.chdir('saycheese')
                os.system('bash saycheese.sh')
                os.chdir(current_working_directory)
            except OSError:
                os.system('clear')
                os.system('python3')
            except ImportError:
                importError()


        elif choice == 6:
            try:
                pass
            except OSError:
                os.system('clear')
                os.system('python3 ')
            except ImportError:
                importError()

        elif choice == 7:
            try:
                pass
            except OSError:
                os.system('clear')
                os.system('python3')
            except ImportError:
                importError()

        elif choice == 8:
            exit()

except ValueError:
    cprint('\nError 404! Requested service not found', 'red', attrs=['bold'])
