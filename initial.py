from win10toast import ToastNotifier
import random
from termcolor import cprint
import os

os.system('cls')
cprint('ENTER THE SOFTWARE ACTIVATION CODE SENT TO YOU: ','red',attrs=['bold'])

toast=ToastNotifier()
activation_code=random.randint(1000,15000)
toast.show_toast('KISSING BUG','Your Activation Code is '+str(activation_code),icon_path='bug.ico')

<<<<<<< HEAD
user_input=input("==>")
=======
user_input=input()
>>>>>>> origin/main

if int(user_input)==int(activation_code):
    os.system('cls')
    os.system('python Kissing_Bug.py')
else:
    cprint('Authentication Failed, Please Try Again.','red',attrs=['bold'])
    exit()