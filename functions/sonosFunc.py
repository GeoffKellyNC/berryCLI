from models.Sonos import Sonos
import soco
from termcolor import colored
from functions.kill import kill
import os
# from typing import set




def sonosFunc() -> None:
    
    sonosActive: bool = True
    

        
    while(sonosActive):
        print(colored("-------------------------------------------------------", "red"))
        print(colored('                    SONOS ', "blue"))
        print(colored("-------------------------------------------------------", "red"))
        
        speaker = Sonos('192.168.50.222')
        
        print('Devices: ' + speaker.getName)

        command: str = input('SONOS -> ')
    
        if(command.startswith('++')):
            c: str = command[2:]
            match c: 
                case 'b':
                    print('Going Back...')
                    sonosActive = False
                    return
                case 'kill':
                    print(colored('Killing Program!', 'red'))
                    kill()
                    return
                case 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case _:
                    print('Not a valid Command sys')
                    continue
        
        match command:
            case 'volume':
                currentVol = speaker.getCurrentVolume
                print(f'Current Volume: {currentVol}')
                continue
            case 'volume set':
                newVol: int = int(input(f'{speaker.getName} set volume -> '))
                speaker.setVolume(newVol)
                print(f'New speaker Volume: {newVol}')
                continue