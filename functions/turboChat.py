from termcolor import colored
from models.Berry import Berry
import json
import os

turboActive: bool = False

with open('./config.json') as f:
    config: str = json.load(f)


def turboChat() -> None:
    print(colored('------------------------------------------------------', 'yellow'))
    print(colored('            GPT-3.5-TURBO MODEL', 'red'))
    print(colored('------------------------------------------------------', 'yellow'))
    
    
    global turboActive
    turboActive = True
    
    pid = os.getpid()
    
    print('NOW CHATTING WITH TURBO CHAT MODEL')
    openai_api_key: str = config['OPEN_AI_KEY']
        
    berry: object = Berry(openai_api_key, "gpt-3.5-turbo")
    
    while(turboActive):
        
        
        prompt: str = input(colored('TURBO -> ', "cyan", "on_black"))
        
        if(prompt.startswith('++')):
            command = prompt[2:]
            match command:
                case 'b':
                    turboActive = False
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
                    os.kill(pid,9)
                    return
                case _:
                    print('Not a valid Command.')
                    return
        
        
        aiRes: dict = berry.askTurbo(prompt)
        
        print('-----------------------------------------------------------------')
        print('-----------------------------------------------------------------')
        
        print(colored('Berry -> ', 'red'),colored(aiRes["response"], "yellow"),colored(f'- T: {aiRes["usage"]["total_tokens"]}', "cyan"), colored(f'-ST: {aiRes["sessionTokenTotal"]}'), colored(f'-$:{aiRes["sessionPrice"]:.6f}','cyan'))
        
        print('-----------------------------------------------------------------')
        print('-----------------------------------------------------------------')
        