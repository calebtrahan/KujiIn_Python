import os
# DIRECTORIES
WORKINGDIRECTORY = os.getcwd()
# SOUND
SOUNDDIRECTORY = str(os.path.join(WORKINGDIRECTORY, "assets", "audio"))
ALERTFILE = str(os.path.join(SOUNDDIRECTORY, "Alert.mp3"))
ALERTSILENCE = str(os.path.join(SOUNDDIRECTORY, "AlertSilence.mp3"))
TEMPDIRECTORY = str(os.path.join(SOUNDDIRECTORY, "temp"))
MAINCUTDIRECTORY = str(os.path.join(SOUNDDIRECTORY, "entrainment"))
RAMPDIRECTORY = str(os.path.join(MAINCUTDIRECTORY, "ramp"))
PREDIRECTORY = MAINCUTDIRECTORY
POSTDIRECTORY = MAINCUTDIRECTORY
AMBIENCEDIRECTORY = str(os.path.join(SOUNDDIRECTORY, "ambience"))
GENERALAMBIENCEDIRECTORY = str(os.path.join(AMBIENCEDIRECTORY, "General"))
REFERENCEFILESMAINDIRECTORY = str(os.path.join(WORKINGDIRECTORY, "assets", 'referencetext'))
ERRORFILES = str(os.path.join(WORKINGDIRECTORY, "errorfiles.txt"))
HELPFILESDIRECTORY = str(os.path.join(WORKINGDIRECTORY, "assets", "html", "helpfiles"))
TESTINGDATABASE = str(os.path.join(WORKINGDIRECTORY, "testingdatabase.db"))
# realdatabase = str(os.path.join(workingdirectory, "sessiondatabase2.db"))
REALDATABASE = str(os.path.join(WORKINGDIRECTORY, "assets", "database", "sessiondatabase.db"))
SESSIONDATABASE = REALDATABASE
#  sessiondatabase = testingdatabase
# if str(sessiondatabase) == str(testingdatabase): print("Testing Database Selected")
# elif str(sessiondatabase) == str(realdatabase): print("Real Session Database Selected")
STYLESHEET = os.path.join(WORKINGDIRECTORY, "assets", "styles", "styles.qss")
WELCOMEMESSAGE = os.path.join(WORKINGDIRECTORY, "assets", "html", "welcomemessage.html")