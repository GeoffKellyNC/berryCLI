from  termcolor import colored
from functions.kill import kill
import json



def update(propName, newValue):

    with open('./config.json', 'r') as f:
        config = json.load(f)

    if propName in config:
        config[propName] = newValue
        with open('config.json', 'w') as f:
            json.dump(config, f)
            print(f'Successfully updated {propName} with {newValue} in config.json')
    else:
        print(f'{propName} not found in config.json')
        
def addConfig(property_name, value):
    with open('config.json', 'r') as f:
        config = json.load(f)

    if property_name in config:
        print(f'{property_name} already exists in config.json')
        return
    else:
        config[property_name] = value
        with open('config.json', 'w') as f:
            json.dump(config, f)
            print(f'Successfully added {property_name} with {value} to config.json')
            return
        
def removeConfig(property_name):
    with open('config.json', 'r') as f:
        config = json.load(f)

    if property_name in config:
        del config[property_name]
        with open('config.json', 'w') as f:
            json.dump(config, f)
            print(f'Successfully removed {property_name} from config.json')
    else:
        print(f'{property_name} not found in config.json')


def configure():
    
    print(colored('------------------------------------------------------', 'yellow'))
    print(colored('            UPDATE CONFIG', 'red'))
    print(colored('------------------------------------------------------', 'yellow'))
    
    configActive = True
    
    while (configActive):
        with open('./config.json') as f:
            config: dict = json.load(f)
            
        keyTypes = []
    
        for key in config:
            keyTypes.append(key)
            continue
        
        print('--------- Available Config Properties')
        
        for i,n in enumerate(keyTypes):
            print(colored(f'{i + 1}.', "yellow"), colored(f'{n}', 'cyan'))
            continue
        
        command: str = input('Config -> ')
        
        if(command.startswith('++')):
            c: str = command[2:]
            
            match c:
                case 'b':
                    print('Going Back....')
                    configActive = False
                    return
                case 'kill':
                    kill()
                    return
                case _:
                    print('Not a valid command')
                    continue
                
        match command:
            case 'edit':
                selection = int(input('Enter Property Number -> '))
                selectedProp = keyTypes[selection - 1]
                print(f'You have selected {selectedProp}')
                newValue: str = input('Enter New Value -> ')
                print(f'Updating {selectedProp} to {newValue}')
                update(selectedProp, newValue)
                continue
            
            case 'add':
                newProp: str = input('Enter property Name ->  ')
                newValue: str = input(f'Enter Value fof {newProp} -> ')
                print(f'Adding {newProp}-:-{newValue} to config')
                addConfig(newProp, newValue)
                continue
            
            case 'del':
                selection: int = int(input('Enter Property Number to remove -> '))
                prop = keyTypes[selection - 1]
                areSure: str = input(f'Are you sure you want to delete {prop} -> ')
                
                if(areSure == 'no'):
                    continue
                else:
                    removeConfig(prop)
                    continue            
            case _:
                print('Not a valid Command')
                
                
    