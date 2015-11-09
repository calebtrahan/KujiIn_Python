def _fromUtf8(s): return s


import sys
import random
import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore
from pydub import AudioSegment

from main_const import *
from helpers import Help


class SessionAmbience():
    def __init__(self, mainprogram, mainwindow):
        self.gui = mainwindow
        self.main = mainprogram
        self.specificambienceavailable = self.checkforspecificambience()
        self.generalambienceavailable = self.checkforgeneralambience()
        self.ambienceoptions = [None, "specific", "General"]
        self.ambiencetype = self.ambienceoptions[0]
        self.ambienceduration = int()
        self.folderswithambience = list()

    def startupchecks(self):
        """Method To Check Ambience Files Using os.isfile()"""
        if str(SESSIONDATABASE) != str(TESTINGDATABASE):
            self.statusBar.showMessage("Performing Startup Checks...")
        error = int()
        for x, i in enumerate(self.cuts): # Check Ambience For >= 3 Files
            thisdirectory = os.path.join(AMBIENCEDIRECTORY, i["name"])
            listofambience = list()
            for r in os.listdir(thisdirectory):
                if r.endswith(".mp3"): listofambience.append(r)
            if len(listofambience) == 0:
                print("%s Has No Ambience" % i["name"])
                error += 1
            elif len(listofambience) < 3:
                print("%s Does Not Have Enough Ambience Files" % i["name"])
                error += 1
        count = 0
        while True: # Ramp Files
            if count == 2: break
            elif count == 1:
                path = os.path.join(RAMPDIRECTORY, "down")
                special = "zr"
            elif count == 0:
                path = os.path.join(RAMPDIRECTORY, "up")
                special = "ar"
            for m in range(0, 9):
                durations = [2, 3, 5]
                for u in durations:
                    file = "%s%s%s.mp3" % (special, m + 1, u)
                    if not os.path.isfile(os.path.join(path, file)):
                        error += 1
                        print("%s Is Missing" % os.path.join(path, file))
            count += 1
        if not error:
            if str(SESSIONDATABASE) != str(TESTINGDATABASE):
                self.gui.statusBar.showMessage("Startup Checks Passed", 2000)
        else:
            # TODO Add A Link To Google Drive Entrainment Files, With A QMessageBox
            self.gui.statusBar.showMessage("Startup Checks Failed. The Program Might Not Operate As Intended. "
                                       "Refer To The Terminal For Missing Files")

    def selectambiencetype(self):
        """Method To Select Ambience Type (General Or Specific)"""
        if self.specificambienceavailable or self.generalambienceavailable:
            self.typeofambienceDialog = QDialog(self.gui)
            self.typeofambienceDialog.setObjectName(_fromUtf8("typeofambienceDialog"))
            self.typeofambienceDialog.resize(423, 107)
            self.specifcdescription = QLabel(self.typeofambienceDialog)
            self.specifcdescription.setGeometry(QRect(30, 40, 161, 31))
            self.specifcdescription.setAlignment(Qt.AlignCenter)
            self.specifcdescription.setWordWrap(True)
            self.specifcdescription.setObjectName(_fromUtf8("specifcdescription"))
            self.specifcButton = QPushButton(self.typeofambienceDialog)
            self.specifcButton.setGeometry(QRect(10, 10, 201, 23))
            self.specifcButton.setObjectName(_fromUtf8("specifcButton"))
            self.generaldescription = QLabel(self.typeofambienceDialog)
            self.generaldescription.setGeometry(QRect(220, 40, 191, 31))
            self.generaldescription.setAlignment(Qt.AlignCenter)
            self.generaldescription.setWordWrap(True)
            self.generaldescription.setObjectName(_fromUtf8("generaldescription"))
            self.generalButton = QPushButton(self.typeofambienceDialog)
            self.generalButton.setGeometry(QRect(220, 10, 191, 23))
            self.generalButton.setObjectName(_fromUtf8("generalButton"))
            self.helpButton = QPushButton(self.typeofambienceDialog)
            self.helpButton.setGeometry(QRect(320, 80, 90, 23))
            self.helpButton.setObjectName(_fromUtf8("helpButton"))
            self.typeofambienceDialog.setWindowTitle("Select The Type Of Ambience To Add To The Session")
            self.specifcdescription.setText("Randomized Ambience For Each Specifc Cut")
            self.generaldescription.setText("General Ambience Played Through The Whole Session")
            self.specifcButton.setText("Specific To Each Cut")
            self.generalButton.setText("General For Whole Session")
            self.helpButton.setText("Help")
            QObject.connect(self.generalButton, SIGNAL(_fromUtf8("clicked()")), self.generalbuttonpressed)
            QObject.connect(self.specifcButton, SIGNAL(_fromUtf8("clicked()")), self.specificbuttonpressed)
            QObject.connect(self.helpButton, SIGNAL(_fromUtf8("clicked()")), self.typeofambiencehelp)
            ret = self.typeofambienceDialog.exec_()
            if ret == QDialog.Rejected:
                self.gui.AmbienceOption.setChecked(False)
        else:
            # Create A Dialog (I Didn't Find Any Ambience. Please Add Some)
                # Create Button "How Do I Do This?" Explaining How The User Can Add Ambience
            pass

    def typeofambiencehelp(self):
        Help.HelpDialogTemplate(self.gui, "Adding Ambience How-To", "ADDING AMBIENCE",
                           os.path.join(HELPFILESDIRECTORY, "addingambience.html"))

    def specificbuttonpressed(self):
        self.typeofambienceDialog.accept()
        specificambience = self.checkforspecificambience()
        if isinstance(specificambience, list):
            st = ""
            for x in specificambience:
                st += x
                if x != specificambience[-1]:
                    st += ", "
            self.addspecificambiencedialog = QDialog(self.gui)
            self.addspecificambiencedialog.resize(586, 124)
            self.label = QLabel(self.addspecificambiencedialog)
            self.label.setGeometry(QRect(40, 20, 491, 51))
            self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
            self.label.setWordWrap(True)
            self.label.setObjectName(_fromUtf8("label"))
            self.pushButton3 = QPushButton(self.addspecificambiencedialog)
            self.pushButton3.setGeometry(QRect(230, 80, 101, 23))
            self.pushButton3.setObjectName(_fromUtf8("pushButton"))
            self.pushButton_4 = QPushButton(self.addspecificambiencedialog)
            self.pushButton_4.setGeometry(QtCore.QRect(490, 80, 80, 23))
            self.pushButton_4.setObjectName(_fromUtf8("pushButton_2"))
            QObject.connect(self.pushButton3, SIGNAL(_fromUtf8("clicked()")), self.openspecificambiencedirectory)
            self.addspecificambiencedialog.setWindowTitle("Specific Ambience Notice")
            self.label.setText("Found No Ambience To Use With %s. Please Add Ambience To Each Of Their Directories In: "
                               "%s" % (st, AMBIENCEDIRECTORY))
            self.pushButton3.setText("TAKE ME THERE")
            self.pushButton_4.setText("BACK")
            self.addspecificambiencedialog.exec_()
            self.gui.AmbienceOption.setChecked(False)
            return False
        else:
            self.ambiencetype = self.ambienceoptions[1]
            self.gui.AmbienceOption.setChecked(True)
            return True

    def generalbuttonpressed(self):
        self.typeofambienceDialog.accept()
        generalambience = self.checkforgeneralambience()
        if not generalambience:
            self.gui.AmbienceOption.setChecked(False)
            self.addgeneralambiencedialog = QDialog(self.gui)
            self.addgeneralambiencedialog.resize(586, 124)
            self.label = QLabel(self.addgeneralambiencedialog)
            self.label.setGeometry(QRect(40, 20, 491, 51))
            self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
            self.label.setWordWrap(True)
            self.label.setObjectName(_fromUtf8("label"))
            self.pushButton3 = QPushButton(self.addgeneralambiencedialog)
            self.pushButton3.setGeometry(QRect(230, 80, 101, 23))
            self.pushButton3.setObjectName(_fromUtf8("pushButton"))
            self.pushButton_4 = QPushButton(self.addgeneralambiencedialog)
            self.pushButton_4.setGeometry(QRect(490, 80, 80, 23))
            self.pushButton_4.setObjectName(_fromUtf8("pushButton_2"))
            self.addgeneralambiencedialog.setWindowTitle("General Ambience Notice")
            self.label.setText("Please Add At Least 3 Ambience Files (The More The Better) To The General Ambience "
                               "Directory Located At: %s" % GENERALAMBIENCEDIRECTORY)
            QObject.connect(self.pushButton3, SIGNAL(_fromUtf8("clicked()")), self.opengeneralambiencedirectory)
            self.pushButton3.setText("TAKE ME THERE")
            self.pushButton_4.setText("BACK")
            self.addgeneralambiencedialog.exec_()
            return False
        else:
            self.ambiencetype = self.ambienceoptions[2]
            self.gui.AmbienceOption.setChecked(True)
            return True

    def opengeneralambiencedirectory(self):
        self.addgeneralambiencedialog.close()
        import subprocess
        if sys.platform == "win32":
            subprocess.check_call(['explorer', GENERALAMBIENCEDIRECTORY])
        elif sys.platform == "linux":
            subprocess.check_call(['dolphin', GENERALAMBIENCEDIRECTORY])
        elif sys.platform == "darwin":
            subprocess.check_call(['open', '--', GENERALAMBIENCEDIRECTORY])
        else:
            QMessageBox.critical(None, "Unsupported Operating System",
                                       "Cannot Open This File In Your System Because Your Isn't Supported. This Feature"
                                       "Only Works On Windows, Mac OS X And Linux",
                                       QMessageBox.Ok | QMessageBox.Default,
                                       QMessageBox.NoButton)
        return False

    def openspecificambiencedirectory(self):
        self.addspecificambiencedialog.close()
        import subprocess
        if sys.platform == "win32":
            subprocess.check_call(['explorer', GENERALAMBIENCEDIRECTORY])
        elif sys.platform == "linux":
            subprocess.check_call(['dolphin', GENERALAMBIENCEDIRECTORY])
        elif sys.platform == "darwin":
            subprocess.check_call(['open', '--', GENERALAMBIENCEDIRECTORY])
        else:
            QMessageBox.critical(None, "Unsupported Operating System",
                                       "Cannot Open This File In Your System Because Your Isn't Supported. This Feature"
                                       "Only Works On Windows, Mac OS X And Linux",
                                       QMessageBox.Ok | QMessageBox.Default,
                                       QMessageBox.NoButton)

    def checkforgeneralambience(self):
        """Method To Check If General Ambience Is As Long As Their Selected Session"""
        if os.listdir(GENERALAMBIENCEDIRECTORY):
            count = 0
            for r in os.listdir(GENERALAMBIENCEDIRECTORY):
                if r.endswith(".mp3"):
                    count += 1
            if count < 3:
                self.main.ambienceenabled = False
                return False
            else:
                self.main.ambienceenabled = True
                return True

    def checkforspecificambience(self):
        """Method To Check If There Are Ambience Files In Each Cut Folder, If Not, Disable Ambience Option"""
        cutsmissing = list()
        for x, i in enumerate(self.main.cuts):
            thisdirectory = os.path.join(AMBIENCEDIRECTORY, i["name"])
            count = 0
            for r in os.listdir(thisdirectory):
                if r.endswith(".mp3"):
                    size = os.stat(os.path.join(thisdirectory, r))
                    if size.st_size > 100000:
                        count += 1
            if count == 0:
                cutsmissing.append(i["name"])
        if len(cutsmissing) > 0:
            self.main.ambienceenabled = False
            return cutsmissing
        else:
            self.main.ambienceenabled = True
            return True

    @staticmethod
    def deletetempambience():
        [os.remove(os.path.join(TEMPDIRECTORY, 'Ambience', x)) for x in os.listdir(os.path.join(TEMPDIRECTORY, 'Ambience'))]


class CreateGeneralAmbience(QThread):
    def __init__(self, cutsinsession):
        QThread.__init__(self)
        self.cutsinsession = cutsinsession
        # self.sessionlength = sessionlength
        self.totallist = list() # Used This To Check If An Ambience File Has Been Used
        # self.totalambiencelength = float()
        self.ambienceingeneralfolder = list()
        self.finalambience = list()
        self.ambiencesoundobjects = None
        self.done = False
        self.settoexit = False

    @staticmethod
    def getgeneralambience():
        print("Started Getting General Ambience")
        ambiencelist = list()
        for r in os.listdir(GENERALAMBIENCEDIRECTORY):
            if r.endswith(".mp3"):
                file = os.path.join(GENERALAMBIENCEDIRECTORY, r)
                # t = AudioSegment.from_mp3(file)
                # self.totalambiencelength += len(t)
                ambiencelist.append(file)
        return ambiencelist

    def run(self):
        self.ambienceingeneralfolder = self.getgeneralambience()
        [os.remove(os.path.join(TEMPDIRECTORY, 'Ambience', x)) for x in os.listdir(os.path.join(TEMPDIRECTORY, 'Ambience'))]
        for x, i in enumerate(self.cutsinsession):
            while True:
                self.currentlength = 0
                if i["name"] in ["Presession", "Postsession"]:
                    fileduration = int(i["ramp"]) * 60
                    if int(i["duration"]) != 0:
                        fileduration += int(i["duration"]) * 60
                else:
                    fileduration = int(i["duration"]) * 60
                fileduration *= 1000
                count = 0
                templistfortesting = list()
                while True:
                    num = random.randrange(0, len(self.ambienceingeneralfolder))
                    nextsoundfile = os.path.join(GENERALAMBIENCEDIRECTORY, self.ambienceingeneralfolder[num])
                    if self.totallist:
                        if len(self.totallist) < len(self.ambienceingeneralfolder):
                            if nextsoundfile in self.totallist:
                                continue
                        elif len(self.totallist) >= len(self.ambienceingeneralfolder):
                            if len(self.totallist) >= 10:
                                if str(nextsoundfile) in [self.totallist[-1], self.totallist[-2], self.totallist[-3],
                                                          self.totallist[-4], self.totallist[-5], self.totallist[-6]]:
                                    continue
                            elif len(self.totallist) >= 6:
                                if str(nextsoundfile) in [self.totallist[-1], self.totallist[-2], self.totallist[-3]]:
                                    continue
                            elif str(nextsoundfile) in [self.totallist[-1], self.totallist[-2]]:
                                    continue
                        self.totallist.append(nextsoundfile)
                    else:
                        self.totallist.append(nextsoundfile)
                    sound = AudioSegment.from_mp3(nextsoundfile)
                    length = len(sound)
                    templistfortesting.append(nextsoundfile)
                    self.currentlength += length
                    if int(self.currentlength + 10000) >= int(fileduration):
                        timetoplay = int(fileduration) - self.currentlength
                        finalsound = sound[:timetoplay]
                        finalsound = finalsound.fade_out(10000)
                        if count == 0:
                            exportthis = finalsound
                        else: exportthis += finalsound
                        break
                    else:
                        if count == 0 and x != (len(self.cutsinsession) - 1):
                            exportthis = sound
                        else: exportthis += sound
                    count += 1
                print(i["name"])
                for j in templistfortesting:
                    print("\t %s" % j)
                exportfilename = os.path.join(TEMPDIRECTORY, "Ambience", i["name"] + "Ambience.mp3")
                exportthis.fade_in(10000)
                exportthis.export(exportfilename, format="mp3")
                completedfile = self.testsession(exportfilename, fileduration)
                if completedfile is not None:
                    self.finalambience.append(exportfilename)
                    self.emit(SIGNAL("asignal"))
                    break
                else:
                    continue

    @staticmethod
    def testsession(filetotest, fileduration):
        try:
            filesize = os.stat(filetotest)
            if filesize.st_size < 100000:
                return None
            exportfile = AudioSegment.from_mp3(filetotest)
            exportfileminuteslength = math.floor((len(exportfile) / 1000) / 60)
            filedurationminuteslength = math.floor((fileduration / 1000) / 60)
            if exportfileminuteslength != filedurationminuteslength:
                with open(ERRORFILES, "a") as file:
                    file.writelines(filetotest)
                return None
            else:
                return filetotest
        except Exception as e:
            print(e)
            return None


class CreateSpecificAmbience(QThread):
    def __init__(self, cutsinsession):
        QThread.__init__(self)
        self.cutsinsession = cutsinsession
        self.finalambience = list()
        self.ambiencesoundobjects = None
        # self.done = False
        self.settoexit = False

    @staticmethod
    def deletespecificambientfiles():
        [os.remove(os.path.join(TEMPDIRECTORY, 'Ambience', x)) for x in os.listdir(os.path.join(TEMPDIRECTORY, 'Ambience'))]

    def run(self):
        self.deletespecificambientfiles()
        for x, i in enumerate(self.cutsinsession):
            errorfiles = list()
            while True:
                if self.settoexit:
                    self.deletespecificambientfiles()
                    break
                self.currentlength = 0
                if i["name"] in ["Presession", "Postsession"]:
                    fileduration = int(i["ramp"]) * 60
                    if int(i["duration"]) != 0:
                        fileduration += int(i["duration"]) * 60
                else:
                    fileduration = int(i["duration"]) * 60
                fileduration *= 1000
                thisdirectory = os.path.join(AMBIENCEDIRECTORY, i["name"])
                listofambience = list()
                for r in os.listdir(thisdirectory):
                    if r.endswith(".mp3"):
                        listofambience.append(r)
                count = 0
                troubleshootinglist = list()
                while True:
                    num = random.randrange(0, len(listofambience))
                    nextsoundfile = os.path.join(thisdirectory, listofambience[num])
                    if troubleshootinglist:
                        if len(troubleshootinglist) < len(listofambience):
                            if nextsoundfile in troubleshootinglist:
                                continue
                        elif len(troubleshootinglist) >= len(listofambience):
                            if len(listofambience) >= 6:
                                if str(nextsoundfile) in [str(troubleshootinglist[-1]), str(troubleshootinglist[-2]),
                                                          str(troubleshootinglist[-3])]:
                                    continue
                            elif str(nextsoundfile) in [str(troubleshootinglist[-1]), str(troubleshootinglist[-2])]:
                                    continue
                        troubleshootinglist.append(nextsoundfile)
                    else:
                        troubleshootinglist.append(nextsoundfile)
                    if nextsoundfile in errorfiles:
                        continue
                    else:
                        sound = AudioSegment.from_mp3(nextsoundfile)
                        length = len(sound)
                        self.currentlength += length
                    if int(self.currentlength + 10000) >= int(fileduration):
                        timetoplay = int(fileduration) - self.currentlength
                        finalsound = sound[:timetoplay]
                        finalsound = finalsound.fade_out(10000)
                        if count == 0:
                            exportthis = finalsound
                        else: exportthis += finalsound
                        break
                    else:
                        if count == 0 and x != (len(self.cutsinsession) - 1):
                            exportthis = sound
                        else: exportthis += sound
                    count += 1
                exportfilename = os.path.join(TEMPDIRECTORY, "Ambience", i["name"] + "Ambience.mp3")
                exportthis.fade_in(10000)
                exportthis.export(exportfilename, format="mp3")
                completedfile = self.testsession(exportfilename, fileduration)
                if completedfile is not None:
                    self.finalambience.append(exportfilename)
                    self.emit(SIGNAL("asignal"))
                    break
                else:
                    continue
        # self.emit(SIGNAL("done"))
        # self.done = True

    @staticmethod
    def testsession(filetotest, fileduration):
        try:
            filesize = os.stat(filetotest)
            if filesize.st_size < 100000:
                return None
            exportfile = AudioSegment.from_mp3(filetotest)
            exportfileminuteslength = math.floor((len(exportfile) / 1000) / 60)
            filedurationminuteslength = math.floor((fileduration / 1000) / 60)
            if exportfileminuteslength != filedurationminuteslength:
                with open(ERRORFILES, "a") as file:
                    file.writelines(filetotest)
                return None
            else:
                return filetotest
        except Exception as e:
            print(e)
            return None