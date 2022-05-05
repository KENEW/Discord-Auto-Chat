import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_TOKEN = os.environ.get('Discord_Auth_Token')
DISCORD_ENDPOINT = os.environ.get('Chanel_End_Point')

CHAT_MIN_TIME = os.environ.get('Chat_Min_Time')
CHAT_MAX_TIME = os.environ.get('Chat_Max_Time')

def generateRandomNumber():
    return random.randint(int(CHAT_MIN_TIME), int(CHAT_MAX_TIME))

def sendChannelMessage(message):
    payload = {
        'content': message
    }

    header = {
        'authorization': AUTH_TOKEN

    }

    r = requests.post(DISCORD_ENDPOINT,
                      data=payload, headers=header)



def getChannelMessages():

    header = {
        'authorization': AUTH_TOKEN

    }

    r = requests.get(DISCORD_ENDPOINT,
                     headers=header)

    return [element['content'] for element in r.json()]


messageList = ['Test1', 'Test2', 'Test3']

def getRandomMessage():
    return messageList[random.randint(0, len(messageList) - 1)]

def getCycleMessage(id):
    return messageList[id]

loopNum = -1

if loopNum < 0 :
    while True:
        for i in range(0, len(messageList)) :
            messages = getCycleMessage(i)
            print(messages)
            sendChannelMessage(messages)
            time.sleep(generateRandomNumber())
else:
    for j in range(0, len(loopNum)) :
        for i in range(0, len(messageList)) :
            messages = getCycleMessage(i)
            print(messages)
            sendChannelMessage(messages)
            time.sleep(generateRandomNumber())