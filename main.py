from commands.help import helpCommand
from models.Berry import Berry
from functions.gpt import gpt
from functions.pokeFunc import pokeFunc
from functions.deviceControl import deviceControl
from functions.config import configure
from functions.kill import kill
from functions.fileDelete import delete_files_in_folders
from termcolor import colored
import json
import os


print(colored('------------------------------------------------------', 'yellow'))
print(colored('            BERRY CLI TOOLS', 'red'))
print(colored('------------------------------------------------------', 'yellow'))

with open('./config.json') as f:
    config: dict = json.load(f)
    
running: bool = True

openai_api_key: str = config['OPEN_AI_KEY']



def main() -> None:
    print('Done')
    
    global running
    global openai_api_key
    
    berry: object = Berry(openai_api_key)
    
    while running:
        _iPrompt: str = input('HOME -> ')
        
        if(_iPrompt.startswith('++')):
            command = _iPrompt[2:]
            match command:
                case 'kill':   
                    print(colored('Killing Program!', 'red'))
                    kill()
                    return
                case 'ts':
                    print('TEST WORKED!')
                    continue
                case 'h':
                    helpCommand()
                    continue
                case 'ns':
                    print('Current Name Space for Berry CLI')
                    print(dir())
                    continue
                case 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case 'om':
                    models = berry.getEngines()
                    for model in models:
                        if model["owned_by"] == 'openai':
                            print(model['id'])
                            continue
                        else:
                            pass
                    continue
                case 'omi':
                    engine: str = input('Enter Model ID: ')
                    engineData: dict = berry.engineInfo(engine)
                    continue
                case _:
                    print('Not a valid Command.')
                
        
        match _iPrompt:
            case "gpt":
                gpt()
                continue
            case "poke":
                pokeFunc()
                continue
            case "device":
                deviceControl()
                continue
            case "config":
                configure()
                continue
            case "test":
                delete_files_in_folders()
                continue
            case _:
                print('Not a valid Command!')
                
    
    
    
if __name__ == '__main__':
    main()