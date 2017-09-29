''' +=======================================================+
    Nigel Hamilton
    HTML -> .ics file convertor
    v 2.1, 2/27/16
    +=======================================================+
'''
import os
import time

def getFileName():
    fileName = input("Enter directory for .ics file\n")
    htmlFile = input("Enter HTML file directory to read\n")
    if (fileName[-4:] != ".ics"):
        fileName += ".ics"
    return fileName,htmlFile

def writeFile(fileName,htmlFile,name,desc):
    eventCount = 0
    #Open files:
    fileOpen = open(fileName,'w')
    htmlOpen = open(htmlFile,'r')
    htmlString = htmlOpen.readlines()
    htmlOpen.close()
    #Begin writing:
    fileOpen.write("BEGIN:VCALENDAR\nPRODID:-//Google Inc//Google Calendar 70.9054//EN\nVERSION:2.0\n\
CALSCALE:GREGORIAN\nMETHOD:PUBLISH\n")
    fileOpen.write("X-WR-CALNAME:" + name + "\n")
    fileOpen.write("X-WR-TIMEZONE:America/New_York\n")
    fileOpen.write("X-WR-CALDESC:" + desc + "\n")
    #Begin reading HTML here:
    for i in range(len(htmlString)):
        if ("<a href=\"javascript:onClick=document.forms[0].event.value=" in htmlString[i]):
            dateLoc = htmlString[i]
            dateString = dateLoc[dateLoc.index("'")+1:dateLoc.index(";")-1]
            dateList = dateString.split("-")
            dateList.append(str(eval(dateList[0])+1))
            dateList[1] = str(eval(dateList[1])+1)
            dateList[1] = addZero(dateList[1])
            dateList[0] = addZero(dateList[0])
            dateList[3] = addZero(dateList[3])
            if ("<font size=\"-1\">" in htmlString[i+2]):
                eventLoc = htmlString[i+2]
                eventString = eventLoc[eventLoc.index(">")+1:eventLoc.rindex("</font>")]
                writeEvent(fileOpen,dateList,eventString,["0","0 N"])
                eventCount += 1
            if ("<a href='#' onclick=\"setCourse(" in htmlString[i+8]):
                eventLoc = htmlString[i+8]
                eventString = eventLoc[eventLoc.index(">")+1:eventLoc.rindex("</a>")]
                timeLoc = htmlString[i+17]
                timeString = timeLoc[timeLoc.index(">")+1:timeLoc.rindex("</font>")]
                if (":" in timeString):
                    timeList = timeString.split(":")
                    timeList[0] = str(eval(timeList[0]))
                else:
                    timeLoc = htmlString[i+27]
                    timeString = timeLoc[timeLoc.index(">")+1:timeLoc.rindex("</font>")]
                    timeList = timeString.split(":")
                    timeList[0] = str(eval(timeList[0]))
                writeEvent(fileOpen,dateList,eventString,timeList)
                eventCount += 1
    fileOpen.write("END:VCALENDAR")
    return eventCount

def writeEvent(fileOpen,date,event,timeString):
    #Time Formating
    currentTime = time.localtime()
    timeList = list(currentTime)
    timeList[1] = addZero(str(timeList[1])) #Month
    timeList[2] = addZero(str(timeList[2])) #Day
    timeList[3] = addZero(str(timeList[3])) #Hour
    timeList[4] = addZero(str(timeList[4])) #Minute
    timeList[5] = addZero(str(timeList[5])) #Second
    if ("PM" in timeString[1]):
        timeString[0] = str(eval(timeString[0][:2])+12)
    if ("N" not in timeString[1]):
        timeString[1] = timeString[1][:1]
        if (eval(timeString[0]) > 23):
            timeString[0] = str(eval(timeString[0])-24)
        timeString[0] = addZero(timeString[0])
        timeString[1] = addZero(timeString[1])
        timeFormated = time.strptime(date[0] + " " + date[1] + " " + date[2] + " " + timeString[0] + " " + timeString[1],
                                     "%d %m %Y %H %M")
        #Coversion from local DD MM YYYY HH:mm to Unix time stamp
        timeUnix = time.mktime(timeFormated)
        #Conversion from Unix to GMT/UTC
        timeGMT = list(time.gmtime(timeUnix))
        timeGMT[1] = addZero(str(timeGMT[1]))
        timeGMT[2] = addZero(str(timeGMT[2]))
        timeGMT[3] = addZero(str(timeGMT[3]))
        timeGMT[4] = addZero(str(timeGMT[4]))
    #Filler time used for date created, last modified, and time stamp
    fillerTime = str(timeList[0]) + timeList[1] + timeList[2] + "T" + timeList[3] + timeList[4] + timeList[5]
    #Begin Event
    fileOpen.write("BEGIN:VEVENT\n")
    #Event Start
    if ("N" in timeString[1]):
        fileOpen.write("DTSTART;VALUE=DATE:" + date[2] + date[1] + date[0] + "\n")
        #Event End
        fileOpen.write("DTEND;VALUE=DATE:" + date[2] + date[1] + date[3] + "\n")
    else:
        fileOpen.write("DTSTART:" + str(timeGMT[0]) + str(timeGMT[1]) + str(timeGMT[2]) + "T" + str(timeGMT[3]) + str(timeGMT[4]) + "00Z\n")
        fileOpen.write("DTEND:" + str(timeGMT[0]) + str(timeGMT[1]) + str(timeGMT[2]) + "T" + str(timeGMT[3]) + str(timeGMT[4]) + "00Z\n")
    fileOpen.write("DTSTAMP:" + fillerTime + "Z\n")
    fileOpen.write("UID:\n")
    fileOpen.write("CREATED:" + fillerTime + "Z\n")
    fileOpen.write("DESCRIPTION:\n")
    fileOpen.write("LAST-MODIFIED:" + fillerTime + "Z\n")
    fileOpen.write("LOCATION:\nSEQUENCE:0\nSTATUS:CONFIRMED\n")
    #Event Name
    fileOpen.write("SUMMARY:" + event + "\n")
    fileOpen.write("TRANSP:OPAQUE\n")
    #End Event
    fileOpen.write("END:VEVENT\n")

def addZero(numString):
    if (eval(numString) < 10):
        numString = "0" + numString
    return numString

def tryFile(htmlFile,mode):
    try:
        htmlOpen = open(htmlFile,mode)
        htmlOpen.close()
        return True
    except (IOError):
        return False
    
def calNameDesc():
    name = input("Name your calendar: ")
    desc = input("Give your calendar a description: ")
    return name,desc
    
def main():
    fileName,html = getFileName()
    calName,calDesc = calNameDesc()
    if (tryFile(html,'r')):
        if (tryFile(fileName,'w')):
            eventCount = writeFile(fileName,html,calName,calDesc)
            if (eventCount == 0):
                print("\nWARNING: No events were found, this calendar is empty.")
                print("Make sure you are using a correctly formated HTML file.")
            print("\nDone! Your file can be found at: " + os.path.dirname(fileName))
            print("Successfully loaded",eventCount,"events!")
            input()
        else:
            print("Could not find directory " + os.path.dirname(fileName))
            input()
    else:
        print("HTML file was not found, did not convert.")
        input()

main()
