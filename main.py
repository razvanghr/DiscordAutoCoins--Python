# for requests / pip install requests
import requests , random , time


def sendData(message , authorization , channel_url):
    json = {
        'content': message
    }
    header = {
        'Authorization': authorization
    }
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_url}/messages', data=json, headers=header)


# Input your data... /
sleep_time = int(input('Sleep time: '))
game_value = int(input('Value to gambling: '))
authorization = input('Input your AuthorizationKey: ')
channel_url = int(input('Input channelId: '))

messages = [f'!work',f'!roulette {game_value}',f'!dice {game_value}',f'!guess 100']


# Random Number Generator!
def randomNumbers():
    for i in range(5):
        randomInt = random.randint(0, 100)
        sendData(randomInt , authorization , channel_url)
        time.sleep(5)

def setupData():
    while(True):
        for message in messages:
            sendData(message , authorization , channel_url)
            if message == f'!guess 100':
                time.sleep(5)
                randomNumbers()
            time.sleep(10)

    time.sleep(sleep_time)


setupData()

# Ravan Ghilea
# For any information or issues,
# Github: https://github.com/razvanghr
# Discord : zaRazvi#8730



