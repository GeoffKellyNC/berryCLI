from termcolor import colored
import requests
import json

class AiChat:
    def __init__(self, key, model) -> None:
        self._apiKey = key
        self._baseURL = 'https://api.openai.com/v1/chat/completions'
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._apiKey}"
        }
        self._model = model

    def chat(self, message) -> None:
        data = {
            "model": self._model,
            "messages": [{"role": "user", "content": message}]
        }
        try:
            response = requests.post(self._baseURL, headers=self._headers, data=json.dumps(data))
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("Something went wrong: ",err)
        else:
            print('Response: ', response) #! DEBUG
            return response.json()
