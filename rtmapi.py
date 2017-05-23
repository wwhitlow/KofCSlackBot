import os
from slackclient import SlackClient
import time

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

helpMessage = ""
meetingMessage = "Meetings are the First Thursday of every month at 7pm! Please remember to bring your Membership Card and Rosary!!!!!!!"
massMessage = "Sign up to help with mass at https://docs.google.com/spreadsheets/d/1s_lssu3mIT8ErbePxntWEJnuZR4RhUVaRMEYTUJ1R64/edit?usp=sharing The Knight's Mass is every Third Sunday of the month!"
whoIsGKMessage = "The Grand Knight for this Fraternal Year is Will Whitlow('@will' on slack). Feel free to message him on Slack or email at wwhitlow@gatech.edu"
#                                                                                                                                                                                           spacing here is to force new line break
requestMessage = "This Slack bot is in continuous development. If you have an idea or believe something should be changed feel free to message '@will' on Slack or message the bot with keyword request and \n\"<Request here in strings>\""

if sc.rtm_connect():
    #Starts scanning loop
    while True:
        json = sc.rtm_read()
        if len(json) == 1:
            message = json[0]
            #print message have Andrew DM bot to see what stays constant
            #Confirms that the api response contains text from a user to parse
            if u'text' in message.keys():
                #Message in lowercase to ignore funky spelling
                lowercaseString = message[u'text'].lower()
                #Checks to see if lackeybot is mentioned in the text
                if "lackeybot" in lowercaseString or "@u5gqdkhn2" in lowercaseString:
                    #Searches for keywords in messages
                    if "help" in lowercaseString:
                        sc.rtm_send_message(message[u'channel'], helpMessage)
                    if "request" in lowercaseString:
                        sc.rtm_send_message(message[u'channel'], requestMessage)
                    if "meeting" in lowercaseString or "business" in lowercaseString:
                        sc.rtm_send_message(message[u'channel'], meetingMessage)
                    if "mass" in lowercaseString:
                        sc.rtm_send_message(message[u'channel'], massMessage)
                    if "who" in lowercaseString and "grand knight" in lowercaseString or "gk" in lowercaseString:
                        sc.rtm_send_message(message[u'channel'], whoIsGKMessage)
        time.sleep(1)
else:
    print "Connection Failed"
