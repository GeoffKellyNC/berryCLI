from termcolor import colored
from models.berryTurbo import BerryTurbo
import json

turboActive: bool = False

with open('./config.json') as f:
    config: str = json.load(f)

def turboChat(running: bool) -> None:
    global turboActive
    turboActive = True
    print('NOW CHATTING WITH TURBO CHAT MODEL')
    openai_api_key: str = config['OPEN_AI_KEY']
        
    berry: object = BerryTurbo(openai_api_key)
    
    while(turboActive):
        
        print(colored('-----------------------------------------------', "yellow"))
        prompt: str = input(colored('USER -> ', "cyan", "on_black"))
        
        if(prompt.startswith('++')):
            match prompt:
                case '++b':
                    turboActive = False
                    return
                case '++md':
                    currentEngine: str = berry._getEngine()
                    print(f'You are currently using {currentEngine}')
                    continue
                case '++cx':
                    context = berry._getContext()
                    print(context)
                    continue
                case '++h':
                    print('This will eventually show you a turbo chat specific help.')
                    continue
                case '++tu':
                    tokensUsed: int = berry.getTokensUsed()
                    print(f"So far this session you have used {tokensUsed} tokens")
                    continue
                case '++kill':
                    print(colored('Killing Program!', 'red'))
                    running = False
                    return
                case _:
                    print('Not A Valid Choice')
        
        
        aiRes: dict = berry.askTurbo(prompt)
        
        print(colored(aiRes["response"], "light_green"),colored(f'- T: {aiRes["usage"]["total_tokens"]}', "cyan"), colored(f'-ST: {aiRes["sessionTokenTotal"]}'))