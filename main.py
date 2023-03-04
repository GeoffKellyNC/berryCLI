from commands.help import helpCommand
from models.Berry import Berry
from functions.turboChat import turboChat
from termcolor import colored
import json


print(colored('------------------------------------------------------', 'yellow'))
print(colored('           WELCOME TO BERRY CLI', 'red'))
print(colored('------------------------------------------------------', 'yellow'))

with open('./config.json') as f:
    config: str = json.load(f)
    
running: bool = True

openai_api_key: str = config['OPEN_AI_KEY']


def killAll():
    global running
    running = False
    return

def main() -> None:
    print('Done')
    
    global running
    global openai_api_key
    
    berry = Berry(openai_api_key)
    
    while running:
        _iPrompt: str = input('Command:')
        
        if(_iPrompt.startswith('++')):
            command = _iPrompt[2:]
            match command:
                case 'k':   
                    print(colored('Killing Program!', 'red'))
                    killAll()
                    return
                case 'ts':
                    print('TEST WORKED!')
                    continue
                case 'h':
                    helpCommand()
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
            case "tc":
                turboChat(running)
                continue
            case _:
                print('Not a valid Command!')
                
    
    
    
if __name__ == '__main__':
    main()