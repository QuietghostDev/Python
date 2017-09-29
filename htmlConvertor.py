''' +=======================================================+
    Nigel Hamilton
    HTML -> .ics file convertor
    v 1.0, 2/27/16
    +=======================================================+
'''
import os
import time

def getFileName():
    fileName = raw_input("Enter directory for .ics file\n")
    htmlFile = raw_input("Enter HTML file directory to read\n")
    if (fileName[-4:] != ".ics"):
        fileName += ".ics"
    return fileName,htmlFile

def writeFile(fileName,htmlFile,name,desc):
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
                writeEvent(fileOpen,dateList,eventString)
            if ("<a href='#' onclick=\"setCourse(" in htmlString[i+8]):
                eventLoc = htmlString[i+8]
                eventString = eventLoc[eventLoc.index(">")+1:eventLoc.rindex("</a>")]
                writeEvent(fileOpen,dateList,eventString)
    fileOpen.write("END:VCALENDAR")

def writeEvent(fileOpen,date,event):
    currentTime = time.localtime()
    timeList = list(currentTime)
    timeList[1] = addZero(str(timeList[1])) #Month
    timeList[2] = addZero(str(timeList[2])) #Day
    timeList[3] = addZero(str(timeList[3])) #Hour
    timeList[4] = addZero(str(timeList[4])) #Minute
    timeList[5] = addZero(str(timeList[5])) #Second
    fillerTime = str(timeList[0]) + timeList[1] + timeList[2] + "T" + timeList[3] + timeList[4] + timeList[5]
    #Begin Event
    fileOpen.write("BEGIN:VEVENT\n")
    #Event Start
    fileOpen.write("DTSTART;VALUE=DATE:" + date[2] + date[1] + date[0] + "\n")
    #Event End
    fileOpen.write("DTEND;VALUE=DATE:" + date[2] + date[1] + date[3] + "\n")
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

def tryFile(htmlFile):
    try:
        htmlOpen = open(htmlFile,'r')
        htmlOpen.close()
        return True
    except (IOError):
        return False
    
def calNameDesc():
    name = raw_input("Name your calendar: ")
    desc = raw_input("Give your calendar a description: ")
    return name,desc
    
def main():
    fileName,html = getFileName()
    calName,calDesc = calNameDesc()
    if (tryFile(html)):
        writeFile(fileName,html,calName,calDesc)
        print "Done! Your file can be found at: " + os.path.dirname(fileName)
    else:
        print "HTML file was not found, did not convert."

main()
