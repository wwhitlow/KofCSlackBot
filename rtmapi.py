import datetime
#Imports messages from another python file
from messages import *
import os
import random
from slackclient import SlackClient
import sqlite3
import sys
import time

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

date = datetime.datetime.today()

    
def parseMessage():
    if "help" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], helpMsg)

    if "meeting" in lowercaseString or "business" in lowercaseString:
        if "minutes" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], minutesMsg)
        else:
            sc.rtm_send_message(message[u'channel'], meetingMessage)

    if "mass" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], massMessage)

    if "calendar" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], calendarMessage)

    if "rosary" in lowercaseString or "mystery" in lowercaseString or "mysteries" in lowercaseString:
        weekday = date.weekday()
        if (weekday == 0 or weekday == 5):
            sc.rtm_send_message(message[u'channel'], joyfulMessage)
        elif (weekday == 1 or weekday == 4):
            sc.rtm_send_message(message[u'channel'], sorrowfulMessage)
        elif (weekday == 2 or weekday == 6):
            sc.rtm_send_message(message[u'channel'], gloriousMessage)
        else:
            sc.rtm_send_message(message[u'channel'], luminousMessage)

    if "what's the good word" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], THWg)
    if "how about them dawgs" in lowercaseString or "how about them dogs" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], pissOnThem)

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

    if "who" in lowercaseString and "director" in lowercaseString:
        if "pro" in lowercaseString and "life" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIsProLifeDirector)
        elif "church" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIsChurchDirector)
        elif "community" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIsCommunityDirector)
        elif "council" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIsCouncilDirector)
        elif "youth" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIsYouthDirector)
        elif "family" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIsFamilyDirector)


if sc.rtm_connect():
    #Starts scanning loop
    while True:
        json = sc.rtm_read()
        if len(json) == 1:
            message = json[0]
            #print message have Andrew DM bot to see what stays constant
            #Confirms that the api response contains text from a user to parse
            if u'text' in message.keys() and u'channel' in message.keys():
                #print message
                #Message in lowercase to ignore funky spelling
                lowercaseString = message[u'text'].lower()
                #Checks to see if lackeybot is mentioned in the text
                if "lackeybot" in lowercaseString or "@u5gqdkhn2" in lowercaseString or message[u'channel'][0] == "D" and message[u'user'] != "U5GQDKHN2":
                    #Searches for keywords in messages
                    #minutesMessage(message[u'channel'])
                    methodDict['minutes'](message[u'channel'])
                    if "request" in lowercaseString or "requests" in lowercaseString:
                        if "prayer" in lowercaseString:
                            conn = sqlite3.connect('kofcDb.db')
                            c = conn.cursor()
                            if "delete" in lowercaseString or "remove" in lowercaseString and '"' in lowercaseString:
                                rm = message[u'text'].split('"')
                                rf = (message[u'user'], rm[1],)
                                c.execute("DELETE FROM requests WHERE user_id = ? AND prayer_intention = ?", rf)
                                conn.commit()
                                sc.rtm_send_message(message[u'channel'], "Delete Command Run!")
                            elif "add" in lowercaseString:
                                request = message[u'text'].split('"')
                                pR = (message[u'user'], request[1], date.now(),)
                                c.execute("INSERT INTO requests VALUES (?,?,?)", pR)
                                conn.commit()
                            elif "list" in lowercaseString:
                                c.execute('SELECT * FROM requests')
                                requests = c.fetchall()
                                msg = "List of Prayer Requests Submitted by the Council:"
                                for req in requests:
                                    msg =  msg + "\n" + req[1]
                                sc.rtm_send_message(message[u'channel'], msg)
                            else:
                                sc.rtm_send_message(message[u'channel'], requestMessage)
                            conn.close()
                        elif "feature" in lowercaseString:
                            if '"' in lowercaseString:
                                request = message[u'text'].split('"')
                                sc.rtm_send_message(message[u'channel'], "Your request has been recorded and forwarded to '@will' current developer")
                                sc.rtm_send_message("D5FDFE517", "New Feature Idea: " + request[1])
                            else:
                                sc.rtm_send_message(message[u'channel'], requestMessage)
                        else:
                            sc.rtm_send_message(message[u'channel'], "Sorry couldn't parse request make sure to differentiate between a prayer and feature request")
                    elif "degree" in lowercaseString:
                        if "list" in lowercaseString:
                            degreeConn = sqlite3.connect('kofcDb.db')
                            dlist = degreeConn.cursor()
                            upcoming = "Upcoming "
                            if "first" in lowercaseString or "1st" in lowercaseString:
                                dlist.execute('SELECT * FROM  first_degrees')
                                first = dlist.fetchall()
                                upcoming = upcoming + "First Degrees:"
                                for f in first:
                                    upcoming = upcoming + "\n" + f[0]
                            elif "second" in lowercaseString or "2nd" in lowercaseString:
                                dlist.execute('SELECT * FROM  second_degrees')
                                second = dlist.fetchall()
                                upcoming = upcoming + "Second Degrees:"
                                for s in second:
                                    upcoming = upcoming + "\n" + s[0]
                            elif "third" in lowercaseString or "3rd" in lowercaseString:
                                dlist.execute('SELECT * FROM  third_degrees')
                                third = dlist.fetchall()
                                upcoming = upcoming + "Third Degrees:"
                                for t in third:
                                    upcoming = upcoming + "\n" + t[0]
                            else:
                                dlist.execute('SELECT * FROM  first_degrees')
                                first = dlist.fetchall()
                                upcoming = upcoming + "First Degrees:"
                                for f in first:
                                    upcoming = upcoming + "\n" + f[0]
                                dlist.execute('SELECT * FROM  second_degrees')
                                second = dlist.fetchall()
                                upcoming = upcoming + "Second Degrees:"
                                for s in second:
                                    upcoming = upcoming + "\n" + s[0]
                                dlist.execute('SELECT * FROM  third_degrees')
                                third = dlist.fetchall()
                                upcoming = upcoming + "Third Degrees:"
                                for t in third:
                                    upcoming = upcoming + "\n" + t[0]
                    else:
                        parseMessage()
        time.sleep(1)
else:
    print("Connection Failed")
