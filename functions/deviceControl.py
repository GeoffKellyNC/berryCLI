from termcolor import colored
from functions.goveeFunc import goveeFunc
from functions.lifexFunc import lifexFunc
from functions.sonosFunc import sonosFunc
from functions.kill import kill


    
    
def deviceControl() -> None:
    deviceControlActive: bool = True
    
    
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
                    kill()
                    return
                case _:
                    print('Not A valid Command...')
                    continue
                
        match command:
            case 'govee':
                goveeFunc()
                continue
            case 'lifex':
                lifexFunc()
                continue
            case 'sonos':
                sonosFunc()
                continue
            case _:
                print('Not a valid command....')