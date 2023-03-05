from termcolor import colored
import os
from functions.goveeFunc import goveeFunc



    
    
def deviceControl() -> None:
    deviceControlActive: bool = True
    
    pid = os.getpid()
    
    while(deviceControlActive):
        print(colored("-------------------------------------------------------", "red"))
        print(colored('                    DEVICE CONTROL ', "blue"))
        print(colored("-------------------------------------------------------", "red"))
        
        command: str = input(colored("Device -> ", "yellow"))
        
        if(command.startswith('++')):
            c: str = command[2:]
            match c:
                case 'b':
                    print('Going Back...')
                    deviceControlActive = False
                    return
                case 'kill':
                    print('Killing Program')
                    os.kill(pid, 9)
                    return
                case _:
                    goveeFunc()
                    continue
                
        match command:
            case 'govee':
                goveeFunc()
                continue
            case _:
                print('Not a valid command....')