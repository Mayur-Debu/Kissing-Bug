import pikepdf
from termcolor import cprint
from password_remover import loading

cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================\n",
    'red')

cprint("                                                        █████████████████████████████████████████████", 'cyan')
cprint("                                                        █▄─▄▄─█▄─▄█▄─█─▄█▄─▄▄─█████▄─▄▄─█▄─▄▄▀█▄─▄▄▄█", 'cyan')
cprint("                                                        ██─▄▄▄██─███─▄▀███─▄█▀██████─▄▄▄██─██─██─▄▄██", 'cyan')
cprint("                                                        █▄▄▄███▄▄▄█▄▄█▄▄█▄▄▄▄▄█████▄▄▄███▄▄▄▄██▄▄▄███", 'cyan')

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



cprint('\nPath to the .pdf file: ', 'cyan', attrs=['bold'])
encryptedFilePath = input()
encryptedFilePath = encryptedFilePath.replace('\\', '\\\\')  # Convert the user input path to absolute path

cprint('\nPassword to turn off the encryption: ')
encryptedFilePassword = input()

pdfFile = pikepdf.open(encryptedFilePath, encryptedFilePassword)  # Turning off the encryption

loading.animate()

cprint('\nPath to the save the decrypted .pdf file: ', 'cyan', attrs=['bold'])
decryptedFilePath = input()
decryptedFilePath = decryptedFilePath.replace('\\', '\\\\')  # Convert the user input path to absolute path

pdfFile.save(decryptedFilePath)  # Saving the decrypted .pdf
