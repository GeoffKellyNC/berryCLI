from termcolor import colored
from models.lifex import Lifex
from functions.kill import kill
import json



with open('./config.json') as f:
    config = json.load(f)
    
    
def lifexFunc() -> None:
    
    lifexActive: bool = True
    
    LIFEX_API_KEY: str = config["LIFEX_API_KEY"]
    
    l: object = Lifex(LIFEX_API_KEY)
    
    while(lifexActive):
        print(colored("-------------------------------------------------------", "red"))
        print(colored('                    LIFEX ', "blue"))
        print(colored("-------------------------------------------------------", "red"))
        
        availableDevices: list[dict] = l.getDevices()
        
        for i, d in enumerate(availableDevices):
            print(colored(f'{i+1}.', "yellow"), colored(f'{d["label"]}', "cyan"))
        
        command: str = input(colored("Lifex -> ", "yellow"))
        
        
        if(command.startswith('++')):
            c: str = command[2:]
            match c: 
                case 'b':
                    print('Going Back...')
                    lifexActive = False
                    return
                case 'kill':
                    print(colored('Killing Program!', 'red'))
                    kill()
                    return
                case _:
                    print('Not a valid Command sys')
                    continue
        
        match command.lower():
            case 'off':
                device: int =  int(input('Enter Device Number: '))
                try:
                    selectedDevice = availableDevices[device - 1]
                    print(f'Turning off {selectedDevice["label"]}')
                    l.turnOff(selectedDevice["id"])
                    continue
                except:
                    print('Not a valid choice')
                    continue
            case 'on':
                device: int =  int(input('Enter Device Number: '))
                try:
                    selectedDevice = availableDevices[device - 1]
                    print(f'Turning on {selectedDevice["label"]}')
                    l.turnOn(selectedDevice["id"])
                    continue
                except:
                    print('Not a valid choice')
                    continue
            case _:
                print('Invalid Command...')