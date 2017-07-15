import os
from slackclient import SlackClient

SLACK_TOKEN='insert-here-slack-token'

slack_client = SlackClient(SLACK_TOKEN)

def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='raspitempbot',
        icon_emoji=':space_invader:'
    )
    

if __name__ == '__main__':
    channels = list_channels()
    for channel in channels:
        if channel['name'] == 'general':
            send_message(channel['id'], "Hello " +
                         channel['name'] + "! It worked!")
    print('-----')
else:
    print("Unable to authenticate.")