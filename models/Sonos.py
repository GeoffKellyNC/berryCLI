from soco import SoCo


class Sonos:
    def __init__(self, ip: str) -> None:
        self._speaker = SoCo(ip)
    
    
    @property
    def getCurrentVolume(self) -> int:
        return self._speaker.volume
    
    @property
    def getName(self)-> str:
        return self._speaker.player_name
    
    def setVolume(self, newVol: int) -> int:
        self._speaker.volume = newVol
        return newVol