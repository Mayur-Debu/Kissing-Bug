import os
import getpass
from termcolor import colored, cprint

os.system('cls')

# welcome screen of the tool
print('\n\n')

cprint("██╗░░██╗██╗░██████╗░██████╗██╗███╗░░██╗░██████╗   ░██████╗░██╗░░░██╗░██████╗░ ", 'blue',
       attrs=['bold', 'blink'])
cprint("██║░██╔╝██║██╔════╝██╔════╝██║████╗░██║██╔════╝   ░██╔══██╗██║░░░██║██╔════╝░ ", 'blue',
       attrs=['bold', 'blink'])
cprint("█████═╝░██║╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗   ░██████╦╝██║░░░██║██║░░███╗░", 'blue',
       attrs=['bold', 'blink'])
cprint("██╔═██╗░██║░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗  ░██╔══██╗██║░░░██║██║░░╚██╗ ", 'blue',
       attrs=['bold', 'blink'])
cprint("██║░╚██╗██║██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ░██████╦╝╚██████╔╝╚██████╔╝ ", 'blue',
       attrs=['bold', 'blink'])
cprint("╚═╝░░╚═╝╚═╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝   ░╚═════╝░░╚═════╝░░╚═════╝░ ", 'blue',
       attrs=['bold', 'blink'])

print('\n\n')

# User of the hacker/cracker
dev = colored('Smart Monk-E', 'red', attrs=['bold'])
github = colored('https://github.com/Mayur-Debu/Kissing-Bug',
                 'red', attrs=['bold'])
current_hacker = getpass.getuser()
current_hacker = colored(current_hacker, 'green', attrs=['bold'])

print(f'Developer: {dev}')
print(f'Want to contribute? {github}')
print(f'Currently Logged in as: {current_hacker}')


def importError():
    '''Function stating call of action when error is generated.'''

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
        cprint('6: KeyLogger.', 'yellow')
        cprint('7: Exit the software.', 'yellow')

        choice = int(input('Enter your choice:'))

        # PDF decrypter
        if choice == 1:
            try:
                os.system('cls')
                os.system('python pdf_password_remover.py')

            except ImportError:
                importError()
                break

        #  Detect Malware
        elif choice == 2:
            try:
                os.system('cls')
                os.system('python Detect_Malware.py')

            except ImportError:
                importError()
                break

        # Sars_coV virus builder
        elif choice == 3:
            try:
                os.system('cls')
                os.system('python Sars_cov.py')

            except ImportError:
                importError()
                break

        # windows activator
        elif choice == 4:
            try:
                os.system('cls')
                os.system('python Win_Activator.py')

            except ImportError:
                importError()
                break

        # saycheese module
        elif choice == 5:
            try:
                current_working_directory = os.getcwd()
                os.chdir('saycheese')
                os.system('bash saycheese.sh')
                os.chdir(current_working_directory)

            except ImportError:
                importError()
                break

            else:
                # Printing the Exception if the module is executed on windows Operating System.
                print()
                cprint(
                    '----------------------------------------------------------------------------------------------------------------------------------',
                    'blue', attrs=['bold'])

                cprint('I see you are running this on your window\'s OS.\n\n',
                       'green', attrs=['bold'])
                cprint('Follow the instruction to execute the saycheese module on the window\'s.', 'yellow',
                       attrs=['bold'])

                cprint(
                    'Step 1: Open Settings app and go to Update & Security -> For Developers and choose the “Developer Mode” radio button.\n\n',
                    'yellow', attrs=['bold'])

                cprint('Step 2: Then go to the Control Panel -> Programs and click “Turn Windows feature on or off”.\n'
                       'Enable “Windows Subsystem for Linux(Beta)”. When you click OK, you will be prompted to reboot.\n '
                       'Click “Restart Now” to reboot your PC.\n\n', 'yellow', attrs=['bold'])

                cprint('Step 3: After rebooting, head to Start and search for “bash”.\n '
                       'Run the “bash.exe” file.\n'
                       'When you run it for first time, you’ll need to accept the terms of service as “Bash on Ubuntu for Windows” will be downloaded from the Windows Store.\n'
                       ' You will be asked for a Username and Password for the Ubuntu environment.\n'
                       ' Please store them somewhere as the password is required to run commands as sudo.', 'yellow',
                       attrs=['bold'])

                cprint(
                    '----------------------------------------------------------------------------------------------------------------------------------',
                    'blue', attrs=['bold'])

                print()
                cprint('1: Reload.')
                cprint('2: Exit.')
                user_choice = input(f'{current_hacker}$ > ')
                try:
                    if user_choice == '1':
                        os.system('cls')
                        os.system('python Kissing_Bug.py')
                    else:
                        exit()

                except (OSError, TypeError, NameError):
                    os.system('clear')
                    os.system('python3 kissingBug.py')

        # Keylogger
        elif choice == 6:
            try:
                os.system('cls')
                current_working_directory = os.getcwd()
                os.chdir('Keylogger')
                os.chdir('Keylogger_Source_Code')
                os.system('python Keylogger.py')
                os.chdir(current_working_directory)

            except ImportError:
                importError()

        # final exiting option
        elif choice == 7:
            exit()

except (ValueError, TypeError):
    cprint('\nError 404! Requested service not found', 'red', attrs=['bold'])
    os.system('cls')
    os.system('python Kissing_Bug.py')
