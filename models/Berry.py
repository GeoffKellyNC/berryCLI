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