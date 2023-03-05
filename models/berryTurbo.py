import openai
from termcolor import colored


class BerryTurbo:
    def __init__(self, apiKey) -> None:
        self._apiKey = apiKey
        self._engine = "gpt-3.5-turbo"
        self._baseURL = 'https://api.openai.com/v1/'
        self._context = [{"role": "system", "content": "You are a cool hip young ai."} ]
        self._tokensUsed = 0;
        
    def _getEngine(self) -> str:
        return self._engine
    
    def _addToContext(self, response: dict) -> None:
        self._context.append(response)
        return
        
    def _getContext(self) -> list:
        return self._context
    
    def _updateUsedTokens(self, newTokens) -> None:
        self._tokensUsed = newTokens
        
    def getTokensUsed(self) -> int:
        return self._tokensUsed
    
    def increaseTokens(self, newTokens) -> int:
        newTotal: int = self._tokensUsed + newTokens
        self._updateUsedTokens(newTotal)
        return newTotal
        
    
    def askTurbo(self, prompt: str) -> None:
        openai.api_key: str = self._apiKey
        
        self._addToContext({"role": "user", "content": prompt})
        
        message: list[dict[str,str]] = self._getContext()
        
        completion: dict = openai.ChatCompletion.create(model = self._engine, messages = message)
        
        aiRes = completion.choices[0].message
        
        self._addToContext({"role": "assistant", "content": aiRes["content"]})
        
        totalTokensSession = self.increaseTokens(completion.usage["total_tokens"])
        
        return {
                "response": aiRes["content"], 
                "usage": completion.usage,
                "sessionTokenTotal": totalTokensSession
                }
        
        
        
    
    
        