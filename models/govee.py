from termcolor import colored
import requests
import json


class Govee:
    def __init__(self, key):
        self._apiKey = key
        self._baseURL = 'https://developer-api.govee.com/v1/devices'
        self._headers = { "Govee-API-Key": self._apiKey, "Content-Type": "application/json"}
        
        
    def getDevices(self) -> list[str]:
        try:
            goveeRes = requests.get(self._baseURL, headers = self._headers)
            goveeRes.raise_for_status()
            deviceData = goveeRes.json()
            
            devices = []
            
            for d in deviceData["data"]["devices"]:
                devices.append(d)
                
            return devices
            
        except requests.exceptions.HTTPError as e:
            print(f"HTTP ERROR: {e}")
            return
        except requests.exceptions.RequestException as e:
            print(f"Error Occurred: {e}")
            return
        
    def deviceOn(self, model: str, mac: str) -> None:
        try:
            body = {
                "device": mac,
                "model": model,
                "cmd": {
                    "name": "turn",
                    "value": "on"
                }
            }
            
            json_body = json.dumps(body)
            
            goveeRes = requests.put(f'{self._baseURL}/control', headers = self._headers, data = json_body)
            goveeRes.raise_for_status()
            
            res = goveeRes.json()
            
            print(res)
            
        except requests.exceptions.HTTPError as e:
            print(f'HTTP ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return
        
    def deviceOff(self, model: str, mac: str) -> None:
        try:
            body = {
                "device": mac,
                "model": model,
                "cmd": {
                    "name": "turn",
                    "value": "off"
                }
            }
            
            json_body = json.dumps(body)
            
            goveeRes = requests.put(f'{self._baseURL}/control', headers = self._headers, data = json_body)
            goveeRes.raise_for_status()
            
            res = goveeRes.json()
            
            print(res)
            
        except requests.exceptions.HTTPError as e:
            print(f'HTTP ERROR: {e}')
            return
        except requests.exceptions.RequestException as e:
            print(f'Error Occurred: {e}')
            return
        
        