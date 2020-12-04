import os
p_ID = input('enter PID: ')
command="taskkill /pid "+p_ID+" /F"
print(command)

