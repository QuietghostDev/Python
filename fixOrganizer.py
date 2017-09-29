###Just a little refresher on programming and Python

###Parsing and compiling earth nav data for navigational fixes

def openFile(fileName, mode): #Openning the file
	return open(fileName, mode)

def writeLine(string, file): #Writing to the file
	file.write(string + '\n')

def dataOrg(fileLine, fixDictLst): #Organizing fix data into list of dictionaries
	fileLineLst = fileLine.split()
	fixDict = {'lat':float(fileLineLst[0]),'long':float(fileLineLst[1]),'name':fileLineLst[2],'airp':fileLineLst[3],'reg':fileLineLst[4]}
	fixDictLst.append(fixDict)
	return fixDictLst

def readFile(file): #Reading the file
	fixDictLst = []
	fileLineLst = file.readlines()
	del fileLineLst[0:3]
	del fileLineLst[-1]
	for fileLine in fileLineLst:
		fixDictLst = dataOrg(fileLine, fixDictLst)
	return fixDictLst

def writeFile(fixDictLst, file): #Loop to write file
	for fixDict in fixDictLst:
		fixDictStr = stringify(fixDict)
		writeLine(fixDictStr, file)

def stringify(fixDict): #Reads dict type, returns string
		fixDictStr = 'Fix ' + fixDict['name'] + '\n\tLatitude: ' + str(fixDict['lat']) + '\tLongitude: ' + str(fixDict['long']) + '\n\tAirport: ' + fixDict['airp'] + '\n\tRegion: ' + fixDict['reg']
		return fixDictStr

def sortList(fixDictLst, sortMode):
	if sortMode in ('name','lat','long','airp','reg'):
		fixDictLst.sort(key = lambda l: l[sortMode])
		return fixDictLst
	else:
		print "Unable to reconize " + sortMode
		return fixDictLst

def main(): #Main
	file = openFile('C:\Users\Nigel\Desktop\FlightSim\X-Plane 11\Custom Data\earth_fix.dat','r')
	fixDictLst = readFile(file)
	file.close()
	sortMode = raw_input('Enter sorting mode:\n')
	fixDictLst = sortList(fixDictLst, sortMode)
	fileName = raw_input('Enter file and directory to save to:\n')
	file = openFile(fileName,'w')
	writeFile(fixDictLst, file)
	print "Done!"
	raw_input()

main()
