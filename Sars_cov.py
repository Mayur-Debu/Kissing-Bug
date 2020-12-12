from termcolor import cprint
import os

cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

cprint("                                           ░██████╗░█████╗░██████╗░░██████╗░░░░░░░█████╗░░█████╗░██╗░░░██╗",
       'blue')
cprint("                                           ██╔════╝██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗██╔══██╗██║░░░██║",
       'blue')
cprint("                                           ╚█████╗░███████║██████╔╝╚█████╗░█████╗██║░░╚═╝██║░░██║╚██╗░██╔╝",
       'blue')
cprint("                                           ░╚═══██╗██╔══██║██╔══██╗░╚═══██╗╚════╝██║░░██╗██║░░██║░╚████╔╝░",
       'blue')
cprint("                                           ██████╔╝██║░░██║██║░░██║██████╔╝░░░░░░╚█████╔╝╚█████╔╝░░╚██╔╝░░",
       'blue')
cprint("                                           ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░░░░░╚════╝░░╚════╝░░░░╚═╝░░░",
       'blue')

cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

cprint('Welcome to SARS-CoV. This software will help you make viruses.\n', 'cyan', attrs=['bold'])

while True:
    cprint('A: Antivirus Hacker', 'yellow', attrs=['bold'])
    cprint('B: Application Bomber', 'yellow', attrs=['bold'])
    cprint('C: Registry Key Eraser', 'yellow', attrs=['bold'])
    cprint('D: Internet Jammer', 'yellow', attrs=['bold'])
    cprint('E: Endless KeyDown', 'yellow', attrs=['bold'])
    cprint('F: Folder Flooder', 'yellow', attrs=['bold'])
    cprint('G: CD Popper', 'yellow', attrs=['bold'])
    cprint('H: Background Process Producer', 'yellow', attrs=['bold'])
    cprint('I: User Flooder', 'yellow', attrs=['bold'])
    cprint('J: Windows Hacker (BRUTAL)', 'yellow', attrs=['bold'])

    cprint('Enter the alphabets in \'CAPITAL\'s\' only: ', 'cyan', attrs=['bold'])
    choice = input()

    if choice == "A":
        cwd=os.getcwd()
        os.chdir("Viruses")
        os.system('python A.py')
        os.chdir(cwd)
        os.system('initial.py')
    elif choice == "B":
        pass
    elif choice == "C":
        pass
    elif choice == "D":
        pass
    elif choice == "E":
        pass
    elif choice == "F":
        pass
    elif choice == "G":
        pass
    elif choice == "H":
        pass
    elif choice == "I":
        pass
    elif choice == "J":
        pass
    else:
        cprint('\nPlease enter only \'CAPITAL\' letter.', 'red', attrs=['bold'])
