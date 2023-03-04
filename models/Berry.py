import openai
from termcolor import colored
import requests


class Berry:
    def __init__(self, key):
        self.apiKey = key
        self._engine = ""
        self._baseURL = 'https://api.openai.com/v1/'
        self._tokensUsed = 0
        self._headers = {"Authorization": f"Bearer {self.apiKey}"}
        
    
    def addHeader(self,key: str, value: str) -> None:
        self._headers[key] = value
        return
         
    def getEngines(self):
        try:
            engineRes = requests.get(self._baseURL + 'models', headers = self._headers)
            engineRes.raise_for_status()
            engineData = engineRes.json()
            return engineData["data"]
        except requests.exceptions.HTTPError as e:
            print(f'HTTP ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return
    
    def engineInfo(self, engineId):
        try:
            openAiRes = requests.get(self._baseURL + f'models/{engineId}', headers = self._headers)
            openAiRes.raise_for_status()
            engineData = openAiRes.json()
            print(engineData)
            return
        except requests.exceptions.HTTPError as e:
            print(f'HTTP ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return
        
            