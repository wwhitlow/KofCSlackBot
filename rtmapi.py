import datetime
import os
import random
import sys
from slackclient import SlackClient
#Imports messages from another python file
from messages import *
import time

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)


def parseMessage():
    if "help" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], helpMessage)
    if "meeting" in lowercaseString or "business" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], meetingMessage)
    if "mass" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], massMessage)
    if "calendar" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], calendarMessage)
    if "rosary" in lowercaseString or "mystery" in lowercaseString or "mysteries" in lowercaseString:
        date = datetime.datetime.today().weekday()
        print date
        if (date == 0 or date == 5):
            sc.rtm_send_message(message[u'channel'], joyfulMessage)
        elif (date == 1 or date == 4):
            sc.rtm_send_message(message[u'channel'], sorrowfulMessage)
        elif (date == 2 or date == 6):
            sc.rtm_send_message(message[u'channel'], gloriousMessage)
        else:
            sc.rtm_send_message(message[u'channel'], luminousMessage)

    if "russian roulette" in lowercaseString:
        pull = random.randint(1,6)
        if (pull % 6 == 0):
            sc.rtm_send_message(message[u'channel'], "BANG! You died :disappointed:")
        else:
            sc.rtm_send_message(message[u'channel'], "Did you die? Click the link to find out\n gifs.com/gif/russian-roulette-click-wj1qEM")
    if "dice roll" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], "Dice Value: " + str(random.randint(1,6)))
    if "random number" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], "True Random Number " + str(random.randint(-sys.maxint, sys.maxint)))
    if "coin flip" in lowercaseString:
        coin = random.randint(0,1)
        if (coin):
            sc.rtm_send_message(message[u'channel'], "Heads")
        else:
            sc.rtm_send_message(message[u'channel'], "Tails")

    if "who" in lowercaseString and "deputy grand knight" in lowercaseString or " dgk" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsDGKMessage)

    elif "who" in lowercaseString and "grand knight" in lowercaseString or " gk" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsGKMessage)

    if "who" in lowercaseString and "treasurer" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsTreasurerMessage) 
    
    if "who" in lowercaseString and "chancellor" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsChancellorMessage) 
    
    if "who" in lowercaseString and "warden" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsWardenMessage) 
    
    if "who" in lowercaseString and "advocate" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsAdvocateMessage) 
    
    if "who" in lowercaseString and "recorder" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsRecorderMessage) 
    
    if "who" in lowercaseString and "outside guard" in lowercaseString or " og" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsOutsideGuardMessage) 
    
    if "who" in lowercaseString and "inside guard" in lowercaseString or " ig" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsInsideGuardMessage) 
    
    if "who" in lowercaseString and "trustee" in lowercaseString:
        if "1st" in lowercaseString or "first" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIs1stTrusteeMessage) 
        elif "2nd" in lowercaseString or "second" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIs2ndTrusteeMessage) 
        elif "3rd" in lowercaseString or "third" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIs3rdTrusteeMessage) 


if sc.rtm_connect():
    #Starts scanning loop
    while True:
        json = sc.rtm_read()
        if len(json) == 1:
            message = json[0]
            #print message have Andrew DM bot to see what stays constant
            #Confirms that the api response contains text from a user to parse
            #print message
            if u'text' in message.keys() and u'channel' in message.keys():
                #Message in lowercase to ignore funky spelling
                lowercaseString = message[u'text'].lower()
                #Checks to see if lackeybot is mentioned in the text
                if "lackeybot" in lowercaseString or "@u5gqdkhn2" in lowercaseString or message[u'channel'][0] == "D":
                    #Searches for keywords in messages
                    if "request" in lowercaseString:
                        if "prayer" in lowercaseString:
                            sc.rtm_send_message(message[u'channel'], requestMessage)
                        elif "feature" in lowercaseString:
                            if '"' in lowercaseString:
                                request = lowercaseString.split('"')
                                sc.rtm_send_message(message[u'channel'], "Your request has been recorded and forwarded to '@will' current developer")
                                sc.rtm_send_message("D5FDFE517", "New Feature Idea: " + request[1])
                            else:
                                sc.rtm_send_message(message[u'channel'], requestMessage)
                        else:
                            sc.rtm_send_message(message[u'channel'], "Sorry couldn't parse request make sure to differentiate between a prayer and feature request")
                    else:
                        parseMessage()
        time.sleep(1)
else:
    print "Connection Failed"
