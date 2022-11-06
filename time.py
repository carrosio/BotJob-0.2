import time
from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


i = 0


while True:
   
    time.sleep(1)
    i = i + 1
    print("Seconds Remaning: ",(90 - i),"s.")
    if i >= 90:
        break
    