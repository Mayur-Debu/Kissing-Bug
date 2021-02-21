from win10toast import ToastNotifier
import random
from termcolor import cprint, colored
import os
import prettytable as pt

os.system('cls')

# Generating a pretty table.
sentence = colored('Make sure, you run this application as administrator.', 'cyan', attrs=['bold'])
width = 127
t = pt.PrettyTable()
t.field_names = [colored('NOTE', 'red', attrs=['bold'])]
[t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
print(t)
cprint(f'ENTER THE SOFTWARE ACTIVATION CODE SENT TO : ', 'red', attrs=['bold'])

# Toast Notification Sent to your desktop.
toast = ToastNotifier()
activation_code = random.randint(1000, 15000)
toast.show_toast('KISSING BUG', f' Your Activation Code is ' + str(activation_code), icon_path='bug.ico')

user_input = input()

if int(user_input) == int(activation_code):
    os.system('cls')
    os.chdir("Source_Code")
    os.system('python Kissing_Bug.py')
else:
    cprint('Resend? (y/n): ', 'cyan', attrs=['bold'])
    choice = input()
    if choice == 'y' or choice == 'Y':
        os.system('python initial.py')
    else:
        exit()
