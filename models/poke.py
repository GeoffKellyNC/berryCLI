from termcolor import colored
import requests



class Poke: 
    def __init__(self, key):
        self._apiKey = key
        self._baseURL = "https://pokemon-go1.p.rapidapi.com/"
        self._headers = {"X-RapidAPI-Key": self._apiKey,"X-RapidAPI-Host": "pokemon-go1.p.rapidapi.com"}
        
        
    def currentDittos(self) -> None:
        try:
            pokeRes = requests.get(self._baseURL + "possible_ditto_pokemon.json", headers = self._headers)
            pokeRes.raise_for_status()
            dittoData = pokeRes.json()
            for p in dittoData.values():
                print(p["name"])
        except requests.exceptions.HTTPError as e:
            print(f"HTTP ERROR: {e}")
            return
        except requests.exceptions.RequestException as e:
            print(f"Error Occurred: {e}")
            return
        
    def maxCP(self, pokemon):
        try:
            pokeRes = requests.get(self._baseURL + "pokemon_max_cp.json", headers = self._headers)
            pokeRes.raise_for_status()
            cpData = pokeRes.json()
            
            
            for p in cpData:
                if(p["pokemon_name"].lower() == pokemon):
                    maxCP: int = p["max_cp"]
                    print(f"The max CP for {pokemon} is {maxCP}")
                    return
                else:
                    continue
        except requests.exceptions.HTTPError as e:
            print(f"HTTP ERROR: {e}")
            return
        except requests.exceptions.RequestException as e:
            print(f"Error Occurred: {e}")
            return
        
        
        
        
        