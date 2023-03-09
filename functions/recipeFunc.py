from termcolor import colored
from models.Berry import Berry
from functions.kill import kill
import json
import os


def recipeFunc() -> None:
    print(colored('------------------------------------------------------', 'yellow'))
    print(colored('            GPT-3.5-TURBO MODEL', 'red'))
    print(colored('------------------------------------------------------', 'yellow'))
    
    
    recipeActive: bool = True
    
    while recipeActive:
        
        with open('./config.json') as f:
            config = json.load(f)
        
        openai_api_key: str = config["OPEN_AI_KEY"]
        
        berry = Berry(openai_api_key, 'gpt-3.5-turbo' )
        
        modifier: str = input("Recipe Modifier -> ")
        
        if(modifier.startswith('++')):
            command = modifier[2:]
            match command:
                case 'b':
                    recipeActive = False
                    return
                case 'cx':
                    context = berry._getContext()
                    print(context)
                    continue
                case 'h':
                    print('This will eventually show you a turbo chat specific help.')
                    continue
                case 'tu':
                    tokensUsed: int = berry.getTokensUsed()
                    print(f"So far this session you have used {tokensUsed} tokens")
                    continue
                case 'clear':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
                case 'kill':
                    print(colored('Killing Program!', 'red'))
                    kill()
                    return
                case _:
                    print('Not a valid Command.')
                    return
        
        match modifier:
            case 'g':
                general = True
                itemList: list[str] = []
                while general:
                    item: str = input('Enter Item: ')
                    if(item == 'done'):
                        print('Generating Recipe...')
                        print(itemList)
                        aiRes = berry.getRecipes(itemList, 'g')
                        print(colored('Berry -> ', 'red'),colored(aiRes["response"], "yellow"),colored(f'- T: {aiRes["usage"]["total_tokens"]}', "cyan"), colored(f'-ST: {aiRes["sessionTokenTotal"]}'), colored(f'-$:{aiRes["sessionPrice"]:.6f}','cyan'))
                        general = False
                        continue
                    itemList.append(item)
                    continue
                    
                        
                    
        




