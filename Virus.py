import os
from termcolor import cprint, colored
import prettytable as pt


# -------------------------------------------------Antivirus Hacker -----------------------------------------------------
def virus_A():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Antivirus_Hacker.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Antivirus Hacker', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Antivirus_Hacker.txt', 'Antivirus_Hacker.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Antivirus_Hacker.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_A()


# -------------------------------------------------Application Bomber-----------------------------------------------------
def virus_B():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Application_Bomber.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('APPLICATION BOMBER', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])
    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Application_Bomber.txt', 'Application_Bomber.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Application_Bomber.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_B()


# -------------------------------------------------Delete Registry keys -----------------------------------------------------
def virus_C():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Delete_key_registry_files.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Registry Key Eraser', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Delete_key_registry_files.txt', 'Delete_key_registry_files.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Delete_key_registry_files.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_C()


# -------------------------------------------------Internet Jammer -----------------------------------------------------
def virus_D():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Disable_Internet.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Internet Jammer', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Disable_Internet.txt', 'Disable_Internet.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Disable_Internet.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_D()


# -------------------------------------------------Endless Keydown -----------------------------------------------------
def virus_E():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Endless_Enter.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Endless KeyDown', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Endless_Enter.txt', 'Endless_Enter.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Endless_Enter.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_E()


# -------------------------------------------------Folder Flooder -----------------------------------------------------
def virus_F():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Folder_Flooder.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Folder Flooder', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Folder_Flooder.txt', 'Folder_Flooder.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Folder_Flooder.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_F()


# -------------------------------------------------CD Popper -----------------------------------------------------
def virus_G():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Popping_CD_Drive.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('CD Popper', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Popping_CD_Drive.txt', 'Popping_CD_Drive.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Popping_CD_Drive.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_G()


# -------------------------------------------------Background Process Producer -----------------------------------------------------
def virus_H():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Unlimited_BG_Process_Creator.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Background Process Producer', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Unlimited_BG_Process_Creator.txt', 'Unlimited_BG_Process_Creator.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Unlimited_BG_Process_Creator.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_H()


# -------------------------------------------------User Flooder -----------------------------------------------------
def virus_I():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/User_Account_Flooder.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('User Flooder', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('User_Account_Flooder.txt', 'User_Account_Flooder.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("User_Account_Flooder.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_I()


# -------------------------------------------------Windows Hacker -----------------------------------------------------
def virus_J():
    cprint("\n===========================================================================================================================================================", 'red')
    cprint('\nDISCLAIMER: Once you convert the virus to .bat (batch) file, you can\'t edit it again.\n', 'yellow',
           attrs=['bold'])

    cprint('!!! THIS IS THE MOST DANGEROUS VIRUS THIS CAN COST YOUR WHOLE OS !!!', 'red', attrs=['bold'])
    cprint("===========================================================================================================================================================\n", 'red')

    try:
        file = open('Viruses/Code_Files/Windows_Hacker.txt', 'r', encoding='utf-8')
        virusCode = file.read()
        sentence = colored(virusCode, 'cyan')
        width = 127
        t = pt.PrettyTable()
        t.field_names = [colored('Windows Hacker', 'red', attrs=['bold'])]
        [t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
        print(t)
        file.close()
    except FileNotFoundError:
        cprint('Already Converted to Batch File.', 'red', attrs=['bold'])

    try:
        while True:
            cprint('\n1. Get .bat File (Batch)', 'yellow', attrs=['bold'])
            cprint('2. Get .exe File (Executables)', 'yellow', attrs=['bold'])
            cprint('3. Edit Code', 'yellow', attrs=['bold'])
            cprint('4. Not Sure What to do?', 'yellow', attrs=['bold'])
            cprint('\nMake Your Choice: ', 'cyan', attrs=['bold'])

            choice = int(input())

            if choice == 1:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.rename('Windows_Hacker.txt', 'Windows_Hacker.bat')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 2:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system('BatToExe.exe')
                    os.chdir(currentWorkingDirectory)
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 3:
                try:
                    currentWorkingDirectory = os.getcwd()
                    os.chdir('Viruses\\Code_Files')
                    os.system("Windows_Hacker.txt")
                    os.chdir(currentWorkingDirectory)
                    cprint('File Edited', 'red', attrs=['bold'])
                except Exception as e:
                    cprint(e, 'red', attrs=['bold'])
            elif choice == 4:
                os.system('python Sars_cov.py')
    except ValueError:
        cprint('\nError 404! Requested Service not found.', 'red', attrs=['bold'])
        virus_J()
