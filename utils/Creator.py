def _fromUtf8(s): return s


import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
from pydub import *

from helpers import Entrainment, Ambience
from main_const import *


class SessionCreator():
    def __init__(self, main, gui, player):
        self.gui = gui
        self.main = main
        self.player = player
        self.percentsessioncreated = float()

    def displayupdate(self):
        """Method To Display Updates To Statusbar While Creating Session"""
        percent = 100 / self.itemstocreate
        self.percentsessioncreated += percent
        msg = "Creating Session (" + str(int(self.percentsessioncreated)) + "%)"
        self.gui.statusBar.showMessage(msg)

    def sessionprechecks(self):
        # Dialog Here To Test (Making Sure Everything Is In Place To Create Your Session. Please Wait...)
        self.checksdialog = QDialog(self.gui)
        self.checksdialog.resize(502, 114)
        self.label = QLabel(self.checksdialog)
        self.label.setGeometry(QRect(30, 50, 421, 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.checksdialog.setWindowTitle("Dialog")
        self.label.setText("Making Sure Everything Is In Place To Create Your Session. Please Wait...")
        self.creationchecks = ChecksBeforeSessionCreation(self.gui, self.main)
        self.creationchecks.start()
        #  QObject.connect(self.creationchecks,SIGNAL("started"),self.sessioncreationupdates,Qt.QueuedConnection)
        QObject.connect(self.creationchecks,SIGNAL("done"),self.precheckscomplete,Qt.QueuedConnection)
        self.checksdialog.exec_()

    def precheckscomplete(self):
        if self.creationchecks.good:
            self.checksdialog.accept()
            self.confirmationtocreatesession()
        else:
            self.checksdialog.reject()
            self.gui.statusBar.showMessage("Session Creation Cancelled Because The Session Creation Checks Failed")

    def confirmationtocreatesession(self):
        """Method To Display A Dialog To Verify Selected Option"""
        # Add TOH Check Here
        for i in self.main.cutsinsession:
            if i["number"] == 3:
                if i["duration"] < 3:
                    QtGui.QMessageBox.critical(None, "TOH Is Too Short",
                                               "Toh Uses A Special Ramp, And As Such, If It Is In The Session, "
                                               "It Must Be Practiced For At Least 3 Minutes",
                                               QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                               QtGui.QMessageBox.NoButton)
                    self.main.resetsession()
                    return False
        ###
        self.confirmationDialog2 = QDialog(self.gui)
        self.confirmationDialog2.resize(395, 550)
        self.confirmationDialog2.setStyleSheet(_fromUtf8("background-color:#212526;"))
        self.sessionpartsListView = QtGui.QListWidget(self.confirmationDialog2)
        self.sessionpartsListView.setGeometry(QtCore.QRect(30, 80, 341, 281))
        self.sessionpartsListView.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(42, 52, 53);"))
        self.sessionpartsListView.setObjectName(_fromUtf8("sessionpartsListView"))
        self.topLabel = QtGui.QLabel(self.confirmationDialog2)
        self.topLabel.setGeometry(QtCore.QRect(20, 20, 361, 20))
        self.topLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"font: 12pt \"Arial Black\";"))
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.confirmationDialog2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 500, 231, 37))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.buttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonLayout.setMargin(0)
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        self.createButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.createButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.buttonLayout.addWidget(self.createButton)
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.buttonLayout.addWidget(self.cancelButton)
        self.toplabel2 = QtGui.QLabel(self.confirmationDialog2)
        self.toplabel2.setGeometry(QtCore.QRect(20, 50, 361, 20))
        self.toplabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabel2.setObjectName(_fromUtf8("toplabel2"))
        self.ambienceLabel = QtGui.QLabel(self.confirmationDialog2)
        self.ambienceLabel.setGeometry(QtCore.QRect(90, 400, 101, 20))
        self.ambienceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ambienceLabel.setObjectName(_fromUtf8("ambienceLabel"))
        self.AmbienceStatus = QtGui.QLabel(self.confirmationDialog2)
        self.AmbienceStatus.setGeometry(QtCore.QRect(220, 400, 71, 19))
        self.AmbienceStatus.setObjectName(_fromUtf8("AmbienceStatus"))
        self.referencefilesLabel = QtGui.QLabel(self.confirmationDialog2)
        self.referencefilesLabel.setGeometry(QtCore.QRect(80, 430, 111, 20))
        self.referencefilesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.referencefilesLabel.setObjectName(_fromUtf8("referencefilesLabel"))
        self.ReferenceFilesActual = QtGui.QLabel(self.confirmationDialog2)
        self.ReferenceFilesActual.setGeometry(QtCore.QRect(220, 430, 58, 19))
        self.ReferenceFilesActual.setObjectName(_fromUtf8("ReferenceFilesActual"))
        self.totalsessiontimeLabel = QtGui.QLabel(self.confirmationDialog2)
        self.totalsessiontimeLabel.setGeometry(QtCore.QRect(80, 460, 121, 19))
        self.totalsessiontimeLabel.setObjectName(_fromUtf8("totalsessiontimeLabel"))
        self.TotalSessionTimeActual = QtGui.QLabel(self.confirmationDialog2)
        self.TotalSessionTimeActual.setGeometry(QtCore.QRect(220, 460, 151, 20))
        self.TotalSessionTimeActual.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TotalSessionTimeActual.setObjectName(_fromUtf8("TotalSessionTimeActual"))
        self.confirmationDialog2.setWindowTitle("Confirmation To Create Session")
        self.topLabel.setText("Create This Session?")
        self.createButton.setText("Create")
        self.cancelButton.setText("Cancel")
        self.toplabel2.setText("Your Session Parts:")
        self.ambienceLabel.setText("Ambience:")
        # self.AmbienceStatus.setText("Enabled")
        self.referencefilesLabel.setText("Reference Files:")
        # self.ReferenceFilesActual.setText("Disabled")
        self.totalsessiontimeLabel.setText("Total Session Time:")
        self.TotalSessionTimeActual.setText("9 Hours And 99 Minutes")
        count = 1
        for i, x in enumerate(self.main.cutsinsession):
            if x["name"] != "Alert":
                item = QtGui.QListWidgetItem()
                num = "%s) " % count
                if x["name"] in ["Presession", "Postsession"]:
                    if int(x["duration"]) != 0:
                        item.setText(num + str(x["name"]) + " (" + str(x["duration"]) + " Mins. + 2 Min. Ramp)")
                    else:
                        item.setText(num + str(x["name"]) + " (" + str(x["ramp"]) + " Mins. (Ramp Only)")
                else:
                    if int(x["duration"]) == int(self.main.cutinvocationduration):
                        item.setText(num + str(x["name"]) + " (" + str(x["duration"]) + " Mins. (Invocation)")
                    else:
                        item.setText(num + str(x["name"]) + " ( " + str(x["duration"]) + " Mins.)")
                count += 1
                self.sessionpartsListView.addItem(item)
        if self.totalduration > 60:
            hours = math.trunc(self.totalduration / 60)
            minutes = self.totalduration % 60
        else:
            hours = False
            minutes = self.totalduration
        # item = QtGui.QListWidgetItem()
        # item.setText("")
        # self.sessionpartsListView.addItem(item)
        # ambienceitem = QtGui.QListWidgetItem()
        if self.gui.AmbienceOption.isChecked():
            self.AmbienceStatus.setText("Enabled")
        else:
            self.AmbienceStatus.setText("Disabled")
        if self.gui.ReferenceDisplayOption.isChecked():
            self.ReferenceFilesActual.setText("Enabled")
        else:
            self.ReferenceFilesActual.setText("Disabled")
        if hours is not False:
            if hours > 1:
                self.TotalSessionTimeActual.setText(str(hours) + " Hours And " + str(minutes) + " Minutes")
            else:
                self.TotalSessionTimeActual.setText(str(hours) + " Hour And " + str(minutes) + " Minutes")
        else:
            self.TotalSessionTimeActual.setText(str(minutes) + " Minutes")
        # item = QtGui.QListWidgetItem()
        # now = datetime.datetime.now()
        # sessionendtime = now + datetime.timedelta(minutes=int(self.totalduration))
        # sessionendtime = sessionendtime.strftime('%I:%M %p')
        # item.setText("If You Start Now, Your Session Will End At About %s" % sessionendtime)
        # self.prematureendingreason.addItem(item)
        self.sessionpartsListView.show()
        QtCore.QObject.connect(self.createButton, QtCore.SIGNAL("clicked()"), self.createbuttonpressed)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancelbuttonpressed)
        self.confirmationDialog2.exec_()

    def createbuttonpressed(self):
        self.confirmationDialog2.accept()
        SessionCreationDialog(self.gui, self, self.main)

    def cancelbuttonpressed(self):
        self.confirmationDialog2.accept()
        self.gui.statusBar.showMessage("Session Creation Cancelled")

    def createsession(self):
        """Method To Actually Create Session"""
        playing = (self.player.entrainmentObject.state() == Phonon.PlayingState)
        paused = (self.player.entrainmentObject.state() == Phonon.PausedState)
        if playing or paused:
            quit_msg = "A Session Is Already Created And Loaded. Overwrite?"
            reply = QtGui.QMessageBox.question(self.gui, 'Confirmation To Overwrite Created Session',
                             quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.player.entrainmentObject.stop()
                self.player.entrainmentObject.clearQueue()
                if self.player.AmbienceOption.isChecked():
                    self.player.ambienceObject.stop()
                    self.player.ambienceObject.clearQueue()
                self.main.deletetempfiles()
                self.gui.statusBar.showMessage("Previous Session Deleted")
            else:
                return
        else:
            if self.main.sessioncreated:
                msg = "Overwrite Created Session?"
                reply = QtGui.QMessageBox.question(self.gui, 'Overwrite Session',
                                 msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    self.main.deletetempfiles()
                else:
                    return
            self.main.sessioncreated = False
            cutsinsession = False
            for u in self.gui.slidervalues:
                if u.value() != 0:
                    cutsinsession = True
            if cutsinsession is True:
                self.main.resetsession()
                self.totalduration = int()
                self.gui.statusBar.show()
                for x, i in enumerate(self.gui.slidervalues):
                    if i.value() != 0:
                        cuttochange = self.main.cuts[x]
                        cuttochange["duration"] = int(i.value())
                        self.main.cutsinsession.append(cuttochange)
                        self.totalduration += i.value()
                    elif x == 0 or x == 10:
                        if i.value() == 0:
                            cuttochange = self.main.cuts[x]
                            self.main.cutsinsession.append(cuttochange)
                    if x == 0 or x == 10:
                        self.totalduration += 2
                testcut = self.main.cutsinsession[1]
                if int(testcut["number"]) != 1: # Test If Cuts Start With RIN
                    displaylist = str()
                    for x, i in enumerate(self.main.cuts): # Append Each Cut Before Rin To A List To Display In Dialog:
                        if testcut["number"] > i["number"]:
                            if i["number"] != 0:
                                displaylist += i["name"]
                                if i["number"] < (testcut["number"] - 1):
                                    displaylist += ", "
                    print("Displaylist Is: %s" % displaylist)
                    quit_msg = "The First Cut You Selected Is Not RIN, And As Such %s Might Not Have " \
                               "The Energy It Needs.\n\n Would You Like To Work On Each Cut Up Until %s?\n\nSelecting" \
                               " \"No\" Will Continue Creating The Session Starting With %s." % \
                               (testcut["name"], testcut["name"], testcut["name"])
                    reply = QtGui.QMessageBox.question(self.gui, 'Add Invocation Cuts',
                                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        custominvocationcutdurationdialog = QDialog(self.gui)
                        custominvocationcutdurationdialog.resize(400, 213)
                        self.custominvocationtopLabel = QtGui.QLabel(custominvocationcutdurationdialog)
                        self.custominvocationtopLabel.setGeometry(QtCore.QRect(90, 10, 221, 16))
                        self.custominvocationcutsLabel = QtGui.QLabel(custominvocationcutdurationdialog)
                        self.custominvocationcutsLabel.setGeometry(QtCore.QRect(11, 30, 381, 20))
                        self.custominvocationcutsLabel.setAlignment(QtCore.Qt.AlignCenter)
                        self.horizontalLayoutWidget = QtGui.QWidget(custominvocationcutdurationdialog)
                        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 60, 160, 80))
                        self.custominvocationLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
                        self.custominvocationLayout.setMargin(0)
                        self.custominvocationValue = QtGui.QSpinBox(self.horizontalLayoutWidget)
                        self.custominvocationLayout.addWidget(self.custominvocationValue)
                        self.custominvocationminLabel = QtGui.QLabel(self.horizontalLayoutWidget)
                        self.custominvocationLayout.addWidget(self.custominvocationminLabel)
                        self.custominvocationaddButton = QtGui.QPushButton(custominvocationcutdurationdialog)
                        self.custominvocationaddButton.setGeometry(QtCore.QRect(160, 170, 131, 30))
                        self.custominvocationcancelButton = QtGui.QPushButton(custominvocationcutdurationdialog)
                        self.custominvocationcancelButton.setGeometry(QtCore.QRect(300, 170, 84, 30))
                        custominvocationcutdurationdialog.setWindowTitle("Set Cut Invocation Duration")
                        self.custominvocationtopLabel.setText("How Long Would You Like To Work On (Invoke):")
                        self.custominvocationcutsLabel.setText("Cuts Here")
                        self.custominvocationminLabel.setText("min")
                        self.custominvocationaddButton.setText("ADD TO SESSION")
                        self.custominvocationcancelButton.setText("CANCEL")
                        QtCore.QObject.connect(self.custominvocationaddButton, QtCore.SIGNAL("clicked()"), custominvocationcutdurationdialog.accept)
                        QtCore.QObject.connect(self.custominvocationcancelButton, QtCore.SIGNAL("clicked()"), custominvocationcutdurationdialog.reject)
                        opt = custominvocationcutdurationdialog.exec_()
                        if opt == QDialog.Accepted:
                            self.main.cutinvocationduration = int(self.custominvocationValue.value())
                            invocationcuts = int(testcut["number"] - 1)
                            for i in range(0, int(invocationcuts)):
                                nextinvocationcut = self.main.cuts[i + 1]
                                nextinvocationcut["duration"] = int(self.main.cutinvocationduration)
                                self.main.cutsinsession.insert((i + 1), self.main.cuts[i + 1])
                                self.gui.slidervalues[i + 1].setValue(self.main.cutinvocationduration)
                                self.totalduration += int(self.main.cutinvocationduration)
                        else:
                            quit_msg = "Still Create Session?"
                            reply = QtGui.QMessageBox.question(self.gui, 'Still Create Session?',
                                             quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                            if reply == QMessageBox.No:
                                self.main.resetsession()
                                self.gui.statusBar.showMessage("Session Creation Cancelled", 5000)
                                return False
                nonsequentialcuts = list()
                lastcutnumber = int()
                for t, o in enumerate(self.main.cuts):
                    if t not in [0, 10]:
                        if o in self.main.cutsinsession:
                            lastcutnumber = o["number"]
                for i in range(0, lastcutnumber):
                    if i != 0 and i <= lastcutnumber:
                        if i > self.main.cutsinsession[1]["number"]:
                            if self.main.cuts[i + 1] not in self.main.cutsinsession:
                                nonsequentialcuts.append(self.main.cuts[i + 1])
                nonsequentialdisplaylist = str()
                if nonsequentialcuts:
                    for r in nonsequentialcuts:
                            nonsequentialdisplaylist += "\t" + r["name"]
                            if r != nonsequentialcuts[-1]:
                                nonsequentialdisplaylist += "\n"
                    esm = "You Can End The Session At Any Cut (Even RIN), But All Cuts Before The Last Cut With A " \
                          "Non-Zero Value Must Connect"
                    quit_msg = "The Cuts You Have Selected Are Not Sequential And As Such The Session Cannot Be" \
                               " Created Without Each Cut Connecting To Each Other (%s)\n\nThe Cuts I Am Missing Are:\n\n%s\n\n " \
                               "You Can Either:" \
                               "\n\nClick 'Yes' And I Will Ask You For A Value To Fill In The Above Cuts With" \
                               "\n\n\tOR\n\nClick 'No' And Return To The " \
                               "Main Program So You Can Connect Them Yourself." % \
                               (esm, nonsequentialdisplaylist)
                    reply = QtGui.QMessageBox.question(self.gui, 'Fix Non-Sequential Cuts',
                                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QMessageBox.Yes:
                        nonsequentialcutsdialog = QDialog(self.gui)
                        nonsequentialcutsdialog.resize(400, 213)
                        self.nonsquentaialcutstopLabel = QtGui.QLabel(nonsequentialcutsdialog)
                        self.nonsquentaialcutstopLabel.setGeometry(QtCore.QRect(90, 10, 221, 16))
                        self.nonsequentialcutsLabel = QtGui.QLabel(nonsequentialcutsdialog)
                        self.nonsequentialcutsLabel.setGeometry(QtCore.QRect(11, 30, 381, 20))
                        self.nonsequentialcutsLabel.setAlignment(QtCore.Qt.AlignCenter)
                        self.nonsequentialLayout = QtGui.QWidget(nonsequentialcutsdialog)
                        self.nonsequentialLayout.setGeometry(QtCore.QRect(130, 60, 160, 80))
                        self.nonsequentiallayout2 = QtGui.QHBoxLayout(self.nonsequentialLayout)
                        self.nonsequentiallayout2.setMargin(0)
                        self.nonsequentialValue = QtGui.QSpinBox(self.nonsequentialLayout)
                        self.nonsequentiallayout2.addWidget(self.nonsequentialValue)
                        self.nonsequentialminLabel = QtGui.QLabel(self.nonsequentialLayout)
                        self.nonsequentiallayout2.addWidget(self.nonsequentialminLabel)
                        self.nonsequentialaddButton = QtGui.QPushButton(nonsequentialcutsdialog)
                        self.nonsequentialaddButton.setGeometry(QtCore.QRect(160, 170, 131, 30))
                        self.nonsequentialcancelButton = QtGui.QPushButton(nonsequentialcutsdialog)
                        self.nonsequentialcancelButton.setGeometry(QtCore.QRect(300, 170, 84, 30))
                        nonsequentialcutsdialog.setWindowTitle("Set Invocation Duration")
                        self.nonsquentaialcutstopLabel.setText("How Long Would You Like To Invoke:")
                        self.nonsequentialcutsLabel.setText(nonsequentialdisplaylist)
                        self.nonsequentialminLabel.setText("min")
                        self.nonsequentialaddButton.setText("ADD TO SESSION")
                        self.nonsequentialcancelButton.setText("CANCEL")
                        QtCore.QObject.connect(self.nonsequentialaddButton, QtCore.SIGNAL("clicked()"), nonsequentialcutsdialog.accept)
                        QtCore.QObject.connect(self.nonsequentialcancelButton, QtCore.SIGNAL("clicked()"), nonsequentialcutsdialog.reject)
                        opt = nonsequentialcutsdialog.exec_()
                        if opt == QDialog.Accepted:
                            if self.nonsequentialValue.value() != 0:
                                for l in range(0, lastcutnumber):
                                    if self.main.cuts[l] not in self.main.cutsinsession:
                                        insertindex = int()
                                        for k in range(0, len(self.main.cutsinsession)):
                                            if l > k: insertindex = k; break
                                        self.main.cuts[l]["duration"] = int(self.nonsequentialValue.value())
                                        self.gui.slidervalues[l].setValue(int(self.nonsequentialValue.value()))
                                        self.main.cutsinsession.insert(insertindex, self.main.cuts[l])
                                from operator import itemgetter
                                newlist = sorted(self.main.cutsinsession, key=itemgetter('number'))
                                self.main.cutsinsession = newlist
                                print("Cuts In Session After:")
                                for x in self.main.cutsinsession:
                                    print(x)
                                self.confirmationtocreatesession()
                            else:
                                self.main.resetsession()
                                self.gui.statusBar.showMessage("Session Creation Cancelled (Value Must Not Be 0)")
                        else:
                            self.main.resetsession()
                            self.gui.statusBar.showMessage("Session Creation Cancelled (Cuts Must Be Sequential)")
                            return False
                    else:
                        self.main.resetsession()
                        self.gui.statusBar.showMessage("Session Creation Cancelled (Cuts Must Be Sequential)")
                        return False
                else:
                    #self.sessionprechecks()
                    self.confirmationtocreatesession()
            else:
                QtGui.QMessageBox.information(None, "Please Select At Least One Cut",
                                           "At Least One Cut Must Have A Value Greater Than 0 In Order To Create A "
                                           "Session (Not Including Pre And Post)",
                                           QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                           QtGui.QMessageBox.NoButton)


class SessionCreationDialog(QDialog):
    def __init__(self, maingui, creator, mainprogram):
        QDialog.__init__(self, maingui)
        self.percentsessioncreated = int()
        self.creator = creator
        self.totalshittodo = int()
        self.resize(400, 93)
        self.main = mainprogram
        self.main.sessioncreated = False
        self.gui = maingui
        self.createsessionProgressBar = QtGui.QProgressBar(self)
        self.createsessionProgressBar.setGeometry(QtCore.QRect(20, 20, 361, 23))
        self.createsessionCancelButton = QtGui.QPushButton(self)
        self.createsessionCancelButton.setGeometry(QtCore.QRect(300, 50, 84, 30))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 60, 200, 16))
        self.setWindowTitle("Creating Session")
        self.label.setText("(This May Take A While)")
        self.createsessionCancelButton.setText("Cancel")
        self.createsessionProgressBar.setValue(0)
        QtCore.QObject.connect(self.createsessionCancelButton, QtCore.SIGNAL("clicked()"), self.cancelsessioncreation)
        QtCore.QObject.connect(self.createsessionProgressBar, QtCore.SIGNAL("valueChanged(int)"), self.seeifsessiondone)
        self.exec_()

    def cancelsessioncreation(self):
        self.close()

    def seeifsessiondone(self):
        if math.floor(self.percentsessioncreated) == 100 or math.ceil(self.percentsessioncreated) == 100:
            self.main.sessioncreated = True
            if self.gui.AmbienceOption.isChecked():
                self.main.createdsessionhasmabience = True
            self.gui.statusBar.showMessage("Your Session Has Been Successfully Created!")
            self.gui.CreateButton.setText('Re-Create')
            self.accept()

    def callthreads(self):
        self.percentsessioncreated = int()
        self.totalshittodo = len(self.main.cutsinsession)
        ambienceoption = self.gui.AmbienceOption.isChecked()
        if ambienceoption: self.totalshittodo *= 2
        self.main.entrainmentplayer = Entrainment.CreateEntrainmentMp3(self.main.cutsinsession, self.main.cutinvocationduration)
        if ambienceoption:
            if self.main.ambience.ambiencetype == "specific":
                self.main.ambienceplayer = Ambience.CreateSpecificAmbience(self.main.cutsinsession)
            elif self.main.ambience.ambiencetype == "General":
                self.main.ambienceplayer = Ambience.CreateGeneralAmbience(self.main.cutsinsession)
            QObject.connect(self.main.ambienceplayer,SIGNAL("asignal"),self.sessioncreationupdates,Qt.QueuedConnection)
        else:
            self.main.ambienceplayer = None
        self.main.entrainmentplayer.start()
        if self.main.ambienceplayer: self.main.ambienceplayer.start()
        self.gui.statusBar.showMessage("Creating Your Session...")
        QObject.connect(self.main.entrainmentplayer,SIGNAL("asignal"),self.sessioncreationupdates,Qt.QueuedConnection)

    def sessioncreationupdates(self):
        percent = 100 / self.totalshittodo
        self.percentsessioncreated += percent
        self.createsessionProgressBar.setValue(int(self.percentsessioncreated))

    def showEvent(self, QShowEvent):
        self.callthreads()

    def closeEvent(self, QCloseEvent):
        self.main.entrainmentplayer.settoexit = True
        if self.gui.AmbienceOption.isChecked():
            self.main.ambienceplayer.settoexit = True
        self.gui.statusBar.showMessage("Session Creation Cancelled", 3000)
        self.accept()


class ChecksBeforeSessionCreation(QThread):
    def __init__(self, gui, main):
        QThread.__init__(self, gui)
        self.good = False
        self.gui = gui
        self.main = main

    def run(self):
        good = self.main.entrainment.checkentrainment()
        if good:
            if self.main.ambienceenabled:
                if self.main.ambience.ambiencetype == "General":
                    print("Checking General Ambience")
                    sessionduration = int()
                    for x, i in enumerate(self.gui.slidervalues):
                        if int(i.value()) != 0:
                            sessionduration += int(i.value())
                    sessionduration += 4
                    ambienceduration = int()
                    for k in os.listdir(os.path.join(AMBIENCEDIRECTORY, "General")):
                        print("Testing %s" % k)
                        if k.endswith('mp3'):
                            t = AudioSegment.from_mp3(os.path.join(AMBIENCEDIRECTORY, "General", k))
                            ambienceduration += math.floor((len(t) / 60) / 1000)
                    if ambienceduration < sessionduration:
                        quit_msg = "Not Enough Ambience To Cover The Entire Length Of The Session In Unique Ambience. Loop Ambience" \
                                   "Randomly? (Selecting No Will Disable Ambience For Now)"
                        reply = QtGui.QMessageBox.question(self.gui, 'Confirmation To Loop Ambience',
                                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                        if reply != QtGui.QMessageBox.Yes:
                            self.good = True
                        else:
                            self.good = False
                    else:
                        self.good = True
                    self.emit(SIGNAL("done"))
                elif self.main.ambience.ambiencetype == "specific":
                    print("Checking Specific Ambience")
                    cutsnotlongenough = list()
                    for i in self.main.cutsinsession:
                        print("Testing %s" % i['name'])
                        lengthtotest = int(i["duration"])
                        if i["name"] in ["Presession", "Postsession"]:
                            lengthtotest += 2
                        ambienceduration = int()
                        for x in os.listdir(os.path.join(AMBIENCEDIRECTORY, str(i["name"]))):
                            if x.endswith('.mp3'):
                                file = AudioSegment.from_mp3(os.path.join(AMBIENCEDIRECTORY, str(i["name"]), x))
                                ambienceduration += math.floor((len(file) / 60) / 1000)
                        if ambienceduration < lengthtotest:
                            cutsnotlongenough.append(i["name"])
                    if cutsnotlongenough:
                        quit_msg = "The Following Cut's Ambience Is Not As Long As The Practice Time: \n %s\n" \
                                   "Would You Like Me To Loop The Ambience Files In Each Of These Cuts " \
                                   "Randomly? (Selecting No Will Disable Ambience For Now) " % str(cutsnotlongenough)
                        reply = QtGui.QMessageBox.question(self.gui, 'Confirmation To Loop Ambience',
                                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                        if reply != QtGui.QMessageBox.Yes:
                            self.good = True
                        else:
                            self.good = False
                    else:
                        self.good = True
                    self.emit(SIGNAL("done"))
            else:
                self.emit(SIGNAL("done"))
        else:
            self.good = False
            self.emit(SIGNAL("done"))