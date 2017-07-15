import os
from slackclient import SlackClient

SLACK_TOKEN='insert-here-slack-token'

slack_client = SlackClient(SLACK_TOKEN)




def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='raspitempbot',
        icon_emoji=':space_invader:'
    )
    

if __name__ == '__main__':
    send_message('test_python', "Hello World!")
