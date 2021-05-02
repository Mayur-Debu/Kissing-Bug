from loading import animateDecrypting
import pikepdf
from termcolor import cprint
import os

cprint("█████████████████████████████████████████████", 'blue')
cprint("█▄─▄▄─█▄─▄█▄─█─▄█▄─▄▄─█████▄─▄▄─█▄─▄▄▀█▄─▄▄▄█", 'blue')
cprint("██─▄▄▄██─███─▄▀███─▄█▀██████─▄▄▄██─██─██─▄▄██", 'blue')
cprint("█▄▄▄███▄▄▄█▄▄█▄▄█▄▄▄▄▄█████▄▄▄███▄▄▄▄██▄▄▄███", 'blue')

cprint('Welcome to PIKE PDF. This software will help you remove the encryption from your pdf file.', 'yellow',
       attrs=['bold'])

try:
    cprint('\nPath to the .pdf file: ', 'cyan', attrs=['bold'])

    encryptedFilePath = input()
    # Convert the user input path to absolute path
    encryptedFilePath = encryptedFilePath.replace('\\', '\\\\')
    cprint('\nPassword to turn off the encryption: ')
    encryptedFilePassword = input()
    # Turning off the encryption
    pdfFile = pikepdf.open(encryptedFilePath, encryptedFilePassword)

except (FileNotFoundError, ValueError):
    cprint('Error 404: FILE NOT FOUND.', 'red', attrs=['bold'])
    choice = input('Do you want to retry? (y/n): ')
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python pdf_password_remover.py')
    else:
        os.system('cls')
        os.system('python Kissing_Bug.py')

# Animation For Decryption
animateDecrypting()

try:
    cprint('\nPath to the save the decrypted .pdf file: ',
           'cyan', attrs=['bold'])

    decryptedFilePath = input()
    # Convert the user input path to absolute path
    decryptedFilePath = decryptedFilePath.replace('\\', '\\\\')
    # Saving the decrypted .pdf file
    pdfFile.save(decryptedFilePath)

except (FileExistsError, NotADirectoryError, FileNotFoundError):
    cprint('File Already Exists.', 'red', attrs=['bold'])
    choice = input('Do you want to retry? (y/n): ')
    if choice == 'y' or choice == 'Y':
        os.system('cls')
        os.system('python pdf_password_remover.py')
    else:
        os.system('cls')
        os.system('python Kissing_Bug.py')
