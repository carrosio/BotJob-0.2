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

wait_time = 90

while True:
    
    time.sleep(1)
    i = i + 1
    print("Seconds Remaning: ",(wait_time - i),"s.")
    if i >= wait_time:
        break
    
    