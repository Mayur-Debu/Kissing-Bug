import os
from termcolor import cprint, colored
import prettytable as pt

os.system('cls')

cprint('DISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
       attrs=['bold'])
try:
    file = open('Code_Files\Application_Bomber.txt', 'r', encoding='utf-8')
    virusCode = file.read()
    sentence = colored(virusCode, 'cyan')
    width = 127
    t = pt.PrettyTable()
    t.field_names = [colored('APPLICATION BOMBER CODE', 'red', attrs=['bold'])]
    [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
    print(t)
    file.close()
except FileNotFoundError:
    cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

while True:
    cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
    cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
    cprint('3. Edit Code', 'yellow', attrs=['bold'])
    cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
    cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

    choice = int(input())

    if choice == 1:
        try:
            os.rename('Code_Files\Application_Bomber.txt', 'Code_Files\Application_Bomber.bat')
        except Exception as e:
            cprint(e, 'red', attrs=['bold'])
    elif choice == 2:
        try:
            os.system('BatToExe.exe')
        except Exception as e:
            cprint(e, 'red', attrs=['bold'])
    elif choice == 3:
        try:
            os.system("Code_Files\\Application_Bomber.txt")
            cprint('File Edited', 'cyan', attrs=['bold'])
        except Exception as e:
            cprint(e, 'red', attrs=['bold'])
    elif choice == 4:
        exit()
