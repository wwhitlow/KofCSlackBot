import os
import time
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

if sc.rtm_connect():
    sc.rtm_send_message("D5FDFE517", "test")
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print "Connection Failed"
