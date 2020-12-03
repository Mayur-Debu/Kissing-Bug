import loading
import pikepdf
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

cprint("                                                        █████████████████████████████████████████████", 'blue')
cprint("                                                        █▄─▄▄─█▄─▄█▄─█─▄█▄─▄▄─█████▄─▄▄─█▄─▄▄▀█▄─▄▄▄█", 'blue')
cprint("                                                        ██─▄▄▄██─███─▄▀███─▄█▀██████─▄▄▄██─██─██─▄▄██", 'blue')
cprint("                                                        █▄▄▄███▄▄▄█▄▄█▄▄█▄▄▄▄▄█████▄▄▄███▄▄▄▄██▄▄▄███", 'blue')

cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

cprint('Welcome to PIKE PDF. This software will help you remove the encryption from your pdf file.', 'yellow',
       attrs=['bold'])

try:
    cprint('\nPath to the .pdf file: ', 'cyan', attrs=['bold'])
    encryptedFilePath = input()
    encryptedFilePath = encryptedFilePath.replace('\\', '\\\\')  # Convert the user input path to absolute path

    cprint('\nPassword to turn off the encryption: ')
    encryptedFilePassword = input()

    pdfFile = pikepdf.open(encryptedFilePath, encryptedFilePassword)  # Turning off the encryption

except FileNotFoundError:
    cprint('Error 404: FILE NOT FOUND.', 'red', attrs=['bold'])
    choice = input('Do you want to retry? (y/n): ')
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python pdf_password_remover.py')
    else:
        os.system('cls')
        os.system('python Kissing_Bug.py')

loading.animate()

try:
    cprint('\nPath to the save the decrypted .pdf file: ', 'cyan', attrs=['bold'])
    decryptedFilePath = input()
    decryptedFilePath = decryptedFilePath.replace('\\', '\\\\')  # Convert the user input path to absolute path

    pdfFile.save(decryptedFilePath)  # Saving the decrypted .pdf

except FileExistsError:
    cprint('File Already Exists.','red',attrs=['bold'])
    choice = input('Do you want to retry? (y/n): ')
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python pdf_password_remover.py')
    else:
        os.system('cls')
        os.system('python Kissing_Bug.py')

except NotADirectoryError:
    cprint('No Such Directory Exists.','red',attrs=['bold'])
    choice = input('Do you want to retry? (y/n): ')
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python pdf_password_remover.py')
    else:
        os.system('cls')
        os.system('python Kissing_Bug.py')

except FileNotFoundError:
    cprint('File Not Found OR File Name Not Specified','red',attrs=['bold'])
    choice = input('Do you want to retry? (y/n): ')
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python pdf_password_remover.py')
    else:
        os.system('cls')
        os.system('python Kissing_Bug.py')

