from commands.help import helpCommand
from functions.turboChat import turboChat
from termcolor import colored


print(colored('------------------------------------------------------', 'yellow'))
print(colored('           WELCOME TO BERRY CLI', 'red'))
print(colored('------------------------------------------------------', 'yellow'))


running: bool = True

def killAll():
    running = False
    return

def main() -> None:
    print('Done')
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
                case _:
                    print('Not a valid Command')
                
        
        match _iPrompt:
            case "tc":
                turboChat(running)
                continue
            case _:
                print('Not a valid Command!')
                
    
    
    
if __name__ == '__main__':
    main()