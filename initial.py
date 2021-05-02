# from win10toast import ToastNotifier
import random
from termcolor import cprint, colored
import os
import prettytable as pt

# clearing the content on powershell before executing
os.system('cls')

# printing the instructions on the screen
instructionOnStartup = colored("Turn off Windows Defender and run as Administrator", 'cyan', attrs=['bold'])
widthOfTable = 127
tableObject = pt.PrettyTable()
tableObject.field_names = [colored("Instruction to the user", 'red', attrs=['bold'])]
[tableObject.add_row([instructionOnStartup[i:i + widthOfTable]]) for i in range(0, len(instructionOnStartup), widthOfTable)]
print(tableObject)

# sending the desktop notification to the user
notification = ToastNotifier()
activation_code = random.randint(1000, 15000)
notification.show_toast("KISSING BUG", f"Your software activation code is: " + str(activation_code), icon_path='bug.ico')

cprint(f"Enter the software activation code: ", 'red', attrs=['bold'])
user_input = input()

# authentication and authorized access
if int(user_input) == int(activation_code):
    os.system('cls')
    os.chdir("Source_Code")
    os.system('python Kissing_Bug.py')
else:
    cprint('Resend? (y/n): ', 'cyan', attrs=['bold'])
    choice = input()
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python initial.py')
    else:
        exit()
