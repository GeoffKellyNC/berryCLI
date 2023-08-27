from termcolor import colored
from models.OpenAiChat import AiChat
from functions.kill import kill
import json
import os


def userSelectModel() -> str:
    print(colored(''))


def gptChat(aiToken):
    
    gptChatActive: bool = True

    while gptChatActive:
        print(colored('------------------------------------------------------', 'yellow'))
        print(colored('            GPT CHAT', 'red'))
        print(colored('------------------------------------------------------', 'yellow'))


