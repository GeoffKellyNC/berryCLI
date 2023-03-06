from functions.kill import kill



def commandHandler(command, activator):
    if not command.startswith('++'):
        return
    else:
        c: str = command[2:]
        match c:
            case 'b':
                print('Going Back...')
                activator = False
                return activator
            case 'kill':
                print('Killing Program')
                kill()
                return
            case _:
                print('Not A valid Command')
                return