import datetime
import os
import random
from slackclient import SlackClient
import sqlite3
import sys
import time


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

methodDict = {}

#helpMessage apparently crashes the slack client...
helpMsg = "The slack bot searches for keywords in your messages for replies. You can ask it various questions such as when are the meetings, what are today's Rosary mysteries, or who is the Grand Knigt. As well as various other useful information including Knight's mass sign up link, meeting minutes, and prayer requests that brothers have added. Try more help for a complete list of commands"
meetingMsg = "Meetings are the First Thursday of every month at 7pm in the Classroom at the CC(if you don't know where that is start in the basement and someone should be able to help you)! Please remember to bring your Membership Card and Rosary!!!!!!!"
#minutesMessage also does not work...
minutesMsg = "Minute Meetings found at this link: "
massMsg = "Sign up to help with mass at https://docs.google.com/spreadsheets/d/1s_lssu3mIT8ErbePxntWEJnuZR4RhUVaRMEYTUJ1R64/edit?usp=sharing The Knight's Mass is every Third Sunday of the month!"
#                                                                                                                                                                                           spacing here is to force new line break
requestMsg = "This Slack bot is in continuous development. If you have an idea or believe something should be changed feel free to message '@will' on Slack or message the bot with keyword request and \n\"<Request here in strings>\""
calendarMsg = "Public Calendar for all events for the Fraternal year can be found at this link https://calendar.google.com/calendar/embed?src=ekacorqf8u5djofr8egll3il4s%40group.calendar.google.com&ctz=America/New_York"

joyfulMsg = "The Joyful Mysteries Are:\n1. The Anunciation\n2. The Visitation\n3. The Nativity\n4.The Presentation of Jesus in the Temple\n5. The Finding of Jesus in the Temple"
sorrowfulMsg = "The Sorrowful Mysteries Are:\n1. The Agony of Jesus in the Garden\n2. The Sourging at the Pillar\n3. The Crowning with Thorns\n4. Jesus Carrying the Cross\n5. The Crucifixion of our Lord"
gloriousMsg = "The Glorious Mysteries Are:\n1. The Resurrection of Jesus Christ\n2. The Acension of Jesus to Heaven\n3. The Descent of the Holy Spirit at Pentecost\n4. The Assumption of Mary into Heaven\n5. Mary is Crowned as Queen of Heaven and Earth"
luminousMsg = "The Luminous Mysteries Are:\n1. The Baptism in the Jordan\n2. The Wedding at Cana\n3. The Proclamation of the Kingdom of God\n4. The Transiguration\n5. The Institution of the Eucharist"

THWg = "TO HELL WITH GEORGIA!!!"
pissOnThem = "Piss on Them!!!"

whoIsGKMessage = "The Grand Knight for this Fraternal Year is Will Whitlow(@will on slack). Feel free to message him on Slack, call/text at 706-302-7470, or email at wwhitlow@gatech.edu"
whoIsDGKMessage = "The Deputy Grand Knight for this Fraternal Year is Andrew Lewis(@alewis on slack). Feel free to message him on Slack or email at aklew12@gmail.com"
whoIsTreasurerMessage = "The Treasurer for this Fraternal Year is Clay Newman(@clay.newman on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIsChancellorMessage = "The Chancellor for this Fraternal Year is Justin Tamayo(@justin on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIsWardenMessage = "The Warden for this Fraternal Year is Tony D'Arienzo(@tstark on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIsAdvocateMessage = "The Advocate for this Fraternal Year is Joshua Rhodes(not on slack :disappointed:). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIsRecorderMessage = "The Recorder for this Fraternal Year is Chris Larkins(@calarkins on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIsInsideGuardMessage = "The Inside Guard for this Fraternal Year is Jeffrey Jacob(@jjacob on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIsOutsideGuardMessage = "The Outside Guard for this Fraternal Year is Andres Rodriguez(@andres.rodriguez on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIs1stTrusteeMessage = "The 1st Year Trustee for this Fraternal Year is Andrew Renuart(@arenuart3 on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIs2ndTrusteeMessage = "The 2nd Year Trustee for this Fraternal Year is Mitchell Tuck(not on slack :disappointed:). Feel free to message him on Slack or email at i don't have it :disappointed:"
whoIs3rdTrusteeMessage = "The 3rd Year Trustee for this Fraternal Year is Zach Basel(@zbasel12 on slack). Feel free to message him on Slack or email at i don't have it :disappointed:"

whoIsProLifeDirector = "The Pro-life Director for this Fraternal Year is Nick Korzik(not on slack). Feel free to message him on Slack or email at I don't have it :disappointed:"
whoIsChurchDirector = "The Church Director for this Fraternal Year is Rafael Murphy(not on slack). Feel free to message him on Slack or email at I don't have it :dissappointed:"
whoIsCommunityDirector = "The Community Director for this Fraternal Year is Chris Larkins(@calarkins on slack). Feel free to message him on Slack or email at I don't have it :disappointed:"
whoIsCouncilDirector = "The Council Director for this Fraternal Year is Dan Theriault(@dtheriault on slack). Feel free to message him on Slack or email at I don't have it :dissappointed:"
whoIsYouthDirector = "The Youth Director for this Fraternal Year is Ian Sebastian(@e-n on slack). Feel free to message him on Slack or email at I don't have it :disappointed:"
whoIsFamilyDirector = "TBD"

#sc.rtm_connect()

def helpMessage(channel):
    sc.rtm_send_message(channel, helpMsg)

methodDict['help'] = helpMessage

def minutesMessage(channel):
    sc.rtm_send_message(channel, minutesMsg)

methodDict['minutes'] = minutesMessage

def meetingMessage(channel):
    sc.rtm_send_message(channel, meetingMsg)

methodDict['meeting'] = meetingMessage

def massMessage(channel):
    sc.rtm_send_message(channel, massMsg)

methodDict['mass'] = massMessage

def requestMessage(channel):
    sc.rtm_send_message(channel, requestMsg)

methodDict['request'] = requestMessage

def calendarMessage(channel):
    sc.rtm_send_message(channel, calendarMsg)

methodDict['calendar'] = calendarMessage

def joyfulMessage(channel):
    sc.rtm_send_message(channel, joyfulMsg)

methodDict['joy'] = joyfulMessage

def sorrowfulMessage(channel):
    sc.rtm_send_message(channel, sorrowfulMsg)

methodDict['sorrow'] = sorrowfulMessage

def gloriousMessage(channel):
    sc.rtm_send_message(channel, gloriousMsg)

methodDict['glorious'] = gloriousMessage

def luminousMessage(channel):
    sc.rtm_send_message(channel, luminousMsg)

methodDict['luminous'] = luminousMessage

def THWgMsg(channel):
    sc.rtm_send_message(channel, THWgMessage)

methodDict["what's the good word"] = THWgMsg

def pissOnThemMsg(channel):
    sc.rtm_send_message(channel, pissOnThemMessage)

methodDict['how about them dawgs'] = pissOnThemMsg

def GKMessage(channel):
    sc.rtm_send_message(channel, whoIsGKMessage)

methodDict['grand knight'] = GKMessage

def DGKMessage(channel):
    sc.rtm_send_message(channel, whoIsDGKMessage)

methodDict['deputy grand knight'] = DGKMessage

def treasurerMessage(channel):
    sc.rtm_send_message(channel, whoIsTreasurerMessage)

methodDict['treasurer'] = treasurerMessage

def chancellorMessage(channel):
    sc.rtm_send_message(channel, whoIsChancellorMessage)

methodDict['chancellor'] = chancellorMessage

def wardenMessage(channel):
    sc.rtm_send_message(channel, whoIsWardenMessage)

methodDict['warden'] = wardenMessage

def advocateMessage(channel):
    sc.rtm_send_message(channel, whoIsAdvocateMessage)

methodDict['advocate'] = advocateMessage

def recorderMessage(channel):
    sc.rtm_send_message(channel, whoIsRecorderMessage)

methodDict['recorder'] = recorderMessage

def insideGuardMessage(channel):
    sc.rtm_send_message(channel, whoIsInsideGuardMessage)

methodDict['inside guard'] = insideGuardMessage

def outsideGuardMessage(channel):
    sc.rtm_send_message(channel, whoIsOutsideGuardMessage)

methodDict['outside guard'] = outsideGuardMessage

def firstTrusteeMessage(channel):
    sc.rtm_send_message(channel, whoIs1stTrusteeMessage)

methodDict['first year trustee'] = firstTrusteeMessage

def secondTrusteeMessage(channel):
    sc.rtm_send_message(channel, whoIs2ndTrusteeMessage)

methodDict['second year trustee'] = secondTrusteeMessage

def thirdTrusteeMessage(channel):
    sc.rtm_send_message(channel, whoIs3rdTrusteeMessage)

methodDict['third year trustee'] = thirdTrusteeMessage

def proLifeDirectorMessage(channel):
    sc.rtm_send_message(channel, whoIsProLifeDirector)

methodDict['prolife'] = proLifeDirectorMessage

def churchDirectorMessage(channel):
    sc.rtm_send_message(channel, whoIsChurchDirector)

methodDict['church'] = churchDirectorMessage

def communityDirectorMessage(channel):
    sc.rtm_send_message(channel, whoIsCommunityDirector)

methodDict['community'] = communityDirectorMessage

def councilDirectorMessage(channel):
    sc.rtm_send_message(channel, whoIsCouncilDirector)

methodDict['council'] = councilDirectorMessage

def youthDirectorMessage(channel):
    sc.rtm_send_message(channel, whoIsYouthDirector)

methodDict['youth'] = youthDirectorMessage

def familyDirectorMessage(channel):
    sc.rtm_send_message(channel, whoIsFamilyDirector)

methodDict['family'] = familyDirectorMessage
