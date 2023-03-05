from termcolor import colored
from models.govee import Govee
import json
import os
import time


with open('./config.json') as f:
    config: str = json.load(f)

    
    
def goveeFunc():
    
    goveeActive: bool = True
    
    govee_api_key: str = config["GOVEE_API_KEY"]
    
    g: object = Govee(govee_api_key)
    
    pid = os.getpid()
    
    while(goveeActive):
        print(colored("-------------------------------------------------------", "red"))
        print(colored('                    GOVEE ', "blue"))
        print(colored("-------------------------------------------------------", "red"))
        
        availableDevices: list[dict] = g.getDevices()
        
        print(colored("AVAILABLE DEVICES: ", "green"))        
        for i, d in enumerate(availableDevices):
            print(colored(f'{i + 1}.', "yellow"), colored(f'{d["deviceName"]}', 'cyan'))
        
        command: str = input(colored("Govee -> ", "yellow"))
        
        if(command.startswith('++')):
            c: str = command[2:]
            match c:
                case 'b':
                    print('Going Back...')
                    goveeActive = False
                    return
                case 'kill':
                    print('Killing Program')
                    os.kill(pid, 9)
                    return
                case _:
                    print('Not A valid Command')
                    continue
        
        match command.lower():
            case 'on':
                light: int = int(input('Enter Device Number: '))
                if(light == 999):
                    for d in availableDevices:
                        g.deviceOn(d["model"], d['device'])
                        time.sleep(1)
                    return
                try:
                    selectedLight = availableDevices[light - 1]
                    print(f'Turning On: {selectedLight["deviceName"]}')
                    g.deviceOn(selectedLight["model"], selectedLight["device"])
                    continue
                except:
                    print('Not a valid choice')
                    continue
            case 'off':
                light: int = int(input('Enter Device Number: '))
                if(light == 999):
                    for d in availableDevices:
                        g.deviceOff(d["model"], d['device'])
                        time.sleep(1)
                    return
                try:
                    selectedLight = availableDevices[light - 1]
                    print(f'Turning Off: {selectedLight["deviceName"]}')
                    g.deviceOff(selectedLight["model"], selectedLight["device"])
                    continue
                except:
                    print('Not a valid choice')
                    continue
            case 'devices':
                for d in availableDevices:
                    print(d)
            case _:
                print('Invalid Command..')
