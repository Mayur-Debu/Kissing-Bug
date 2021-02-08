from gtts import gTTS
import os
import loading
import prettytable as pt
from termcolor import colored, cprint

os.system('cls')
cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')
cprint(
    "                                             ▒█░░▒█ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ █░░░█ █▀▀ 　 █▀▀█ █▀▀ ▀▀█▀▀ ░▀░ ▀█░█▀ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ ",
    'blue', attrs=['bold'])
cprint(
    "                                             ▒█▒█▒█ ▀█▀ █░░█ █░░█ █░░█ █▄█▄█ ▀▀█ 　 █▄▄█ █░░ ░░█░░ ▀█▀ ░█▄█░ █▄▄█ ░░█░░ █░░█ █▄▄▀ ",
    'blue', attrs=['bold'])
cprint(
    "                                             ▒█▄▀▄█ ▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀▀ ░▀░▀░ ▀▀▀ 　 ▀░░▀ ▀▀▀ ░░▀░░ ▀▀▀ ░░▀░░ ▀░░▀ ░░▀░░ ▀▀▀▀ ▀░▀▀",
    'blue', attrs=['bold'])
cprint(
    "\n===========================================================================================================================================================",
    'red')
cprint(
    "===========================================================================================================================================================",
    'red')

try:
    os.system('start info.mp3')
except FileNotFoundError:
    mytext = 'Hi I apologize for the inconvenience, I request you to follow the below given steps to activate your windows. Cherrs !!! '
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("info.mp3")
    os.system("start info.mp3")

# Remaining Driver Code
loading.scripLoading()
print()
sentence = colored('Step 1: Copy the script from this link==> https://github.com/Mayur-Debu/Win_Activator .\n '
                   'Step 2: Paste in notepad. \n'
                   'Step 3: Save it with .bat extension [<filename>.bat]. \n'
                   'Step 4: Run as administrator, that\'s it!!!', 'cyan', attrs=['bold'])
width = 160
t = pt.PrettyTable()
t.field_names = [colored('INSTRUCTIONS', 'red', attrs=['bold'])]
[t.add_row([sentence[i:i + width]]) for i in range(0, len(sentence), width)]
print(f'\n{t}')
