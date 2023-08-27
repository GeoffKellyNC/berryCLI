from termcolor import colored
from models.Berry import Berry
from functions.turboChat import turboChat
from functions.recipeFunc import recipeFunc
from functions.kill import kill
import json
import os




def gpt() -> None:
    
    gptActive: bool = True
    
    while gptActive:
        print(colored('------------------------------------------------------', 'yellow'))
        print(colored('            GPT', 'red'))
        print(colored('------------------------------------------------------', 'yellow'))
        with open('./config.json') as f:
            config = json.load(f)
        
        aiToken: str = config["OPEN_AI_KEY"]
        
        berry: object = Berry(aiToken)
        
        command: str = input(colored('GPT -> ', "cyan", "on_black"))
        
        if(command.startswith("++")):
            c: str = command[2:]
            match c:
                case 'b':
                    gptActive = False
                    return
                case 'kill':
                    kill()
                    return
                case 'md':
                    currentEngine: str = berry._getEngine()
                    print(f'You are currently using {currentEngine}')
                    continue
                case 'cx':
                    context = berry._getContext()
                    print(context)
                    continue
                case 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case _:
                    print('Invalid Command.')
                    
        match command:
            case 'turbo':
                turboChat()
                continue
            case 'recipe':
                recipeFunc()
                continue
            case 'chat':
                gptChat(aiToken)
            case _:
                print('Invalid Command..')
                continue
        
        
        
        
        
        
            
    