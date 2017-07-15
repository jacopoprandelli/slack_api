'''
project: every 5 second generate random number between 1 and 10
if number > 6 then send a slack notification with the number
'''

from slackclient import SlackClient
from time import sleep
from datetime import datetime
from random import randint
import os

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)


def check_connectivity():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return True
    else:
        return False


def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='pythonbot',
        icon_emoji=':robot_face:'
    )


if __name__ == '__main__':
    connected = check_connectivity()
    if connected:
        msgNum = 1
        while True:
            randNum = randint(1, 10)
            currTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if randNum > 6:
                message = "number %s was randomly generated at %s. This is message number %s" % (randNum, currTime, msgNum)
                send_message('test_python', message)
                msgNum += 1
                sleep(5)
            else:
                print(randNum)
                sleep(5)
    else:
        print("Unable to authenticate.")
