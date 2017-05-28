helpMessage = ""
meetingMessage = "Meetings are the First Thursday of every month at 7pm in the Classroom at the CC(if you don't know where that is start in the basement and someone should be able to help you)! Please remember to bring your Membership Card and Rosary!!!!!!!"
massMessage = "Sign up to help with mass at https://docs.google.com/spreadsheets/d/1s_lssu3mIT8ErbePxntWEJnuZR4RhUVaRMEYTUJ1R64/edit?usp=sharing The Knight's Mass is every Third Sunday of the month!"
#                                                                                                                                                                                           spacing here is to force new line break
requestMessage = "This Slack bot is in continuous development. If you have an idea or believe something should be changed feel free to message '@will' on Slack or message the bot with keyword request and \n\"<Request here in strings>\""
calendarMessage = "Public Calendar for all events for the Fraternal year can be found at this link https://calendar.google.com/calendar/embed?src=ekacorqf8u5djofr8egll3il4s%40group.calendar.google.com&ctz=America/New_York"

joyfulMessage = "The Joyful Mysteries Are:\n1. The Anunciation\n2. The Visitation\n3. The Nativity\n4.The Presentation of Jesus in the Temple\n5. The Finding of Jesus in the Temple"
sorrowfulMessage = "The Sorrowful Mysteries Are:\n1. The Agony of Jesus in the Garden\n2. The Sourging at the Pillar\n3. The Crowning with Thorns\n4. Jesus Carrying the Cross\n5. The Crucifixion of our Lord"
gloriousMessage = "The Glorious Mysteries Are:\n1. The Resurrection of Jesus Christ\n2. The Acension of Jesus to Heaven\n3. The Descent of the Holy Spirit at Pentecost\n4. The Assumption of Mary into Heaven\n5. Mary is Crowned as Queen of Heaven and Earth"
luminousMessage = "The Luminous Mysteries Are:\n1. The Baptism in the Jordan\n2. The Wedding at Cana\n3. The Proclamation of the Kingdom of God\n4. The Transiguration\n5. The Institution of the Eucharist"

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

whoIsProLifeDirector = "";
whoIsChurchDirector = "";
whoIsCommunityDirector = "";
whoIsYouthDirector = "";
whoIsFamilyDirector = "";


def parseMessage():
    if "help" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], helpMessage)
    if "meeting" in lowercaseString or "business" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], meetingMessage)
    if "mass" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], massMessage)
    if "calendar" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], calendarMessage)

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


    if "who" in lowercaseString and "deputy grand knight" in lowercaseString or " dgk " in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsDGKMessage)

    elif "who" in lowercaseString and "grand knight" in lowercaseString or " gk " in lowercaseString:
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
    
    if "who" in lowercaseString and "outside guard" in lowercaseString or " og " in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsOutsideGuardMessage) 
    
    if "who" in lowercaseString and "inside guard" in lowercaseString or " ig " in lowercaseString:
        sc.rtm_send_message(message[u'channel'], whoIsInsideGuardMessage) 
    
    if "who" in lowercaseString and "trustee" in lowercaseString:
        if "1st" in lowercaseString or "first" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIs1stTrusteeMessage) 
        elif "2nd" in lowercaseString or "second" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIs2ndTrusteeMessage) 
        elif "3rd" in lowercaseString or "third" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], whoIs3rdTrusteeMessage) 
