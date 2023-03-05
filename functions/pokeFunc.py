from termcolor import colored
from models.poke import Poke
import json
import os

with open('./config.json') as f:
    config: str = json.load(f)
    
def pokeFunc() -> None:
    pokeActive = True
    
    poke_api_key: str = config["POKEMON_RAPID_API_KEY"]
    
    p: object = Poke(poke_api_key)
    
    pid = os.getpid()
    
    while(pokeActive):
        print(colored("-------------------------------------------------------", "red"))
        print(colored('                    POKEMON TOOLS ', "blue"))
        print(colored("-------------------------------------------------------", "red"))
        
        command = input(colored("Poke -> ", "yellow"))
        
        if(command.startswith('++')):
            c: str = command[2:]
            match c: 
                case 'b':
                    print('Going Back...')
                    pokeActive = False
                    return
                case 'kill':
                    print(colored('Killing Program!', 'red'))
                    os.kill(pid,9)
                    return
                case _:
                    print('Not a valid Command')
        
        match command:
            case 'ditto':
                p.currentDittos()
                continue
            case "cp":
                pokemon: str = input('Enter Pokemon: ')
                p.maxCP(pokemon.strip().lower())
                continue
            case _:
                print("Not a valid command")