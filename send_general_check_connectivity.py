from slackclient import SlackClient

SLACK_TOKEN='insert-here-slack-token'

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
        send_message('test_python', "My test message is here 2!")
    else:
        print("Unable to authenticate.")
