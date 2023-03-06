from termcolor import colored
import requests
import json




class Lifex:
    def __init__(self, key):
        self._apiKey: str = key
        self._baseURL: str = 'https://api.lifx.com/v1/lights/'
        self._headers: dict = {"Authorization": f"Bearer {self._apiKey}" }
        
        
    def getDevices(self) -> list[dict]:
        try:
            lifexRes: list[dict] = requests.get(f"{self._baseURL}/all", headers = self._headers) 
            lifexRes.raise_for_status()
            
            deviceData: list[dict] = lifexRes.json()
            
            return deviceData
            
        except requests.exceptions.HTTPError as e:
            print(f'HTTPS ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return
        
    def turnOff(self,lightId) -> None:
        try:
            payload = {"power": "off",}
            lifexRes = requests.put(f"{self._baseURL}/id:{lightId}/state/", data = payload, headers = self._headers)
            lifexRes.raise_for_status()
            res = lifexRes.json()
            print(res)
        except requests.exceptions.HTTPError as e:
            print(f'HTTPS ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return
        
    def turnOn(self,lightId) -> None:
        try:
            payload = {"power": "on",}
            lifexRes = requests.put(f"{self._baseURL}/id:{lightId}/state/", data = payload, headers = self._headers)
            lifexRes.raise_for_status()
            res = lifexRes.json()
            print(res)
        except requests.exceptions.HTTPError as e:
            print(f'HTTPS ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return