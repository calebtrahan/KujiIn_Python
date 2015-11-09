from utils import Tools


def _fromUtf8(s): return s


import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

from main_const import *
from helpers import Help
from helpers import Database, Reference
from utils import Tools


class KujiDesign(QMainWindow):
    def __init__(self, mainprogram):
        QMainWindow.__init__(self)
        qss_file = open(STYLESHEET).read()
        self.setStyleSheet(qss_file)
        self.sessiondb = Database.SessionDatabase(self)
        self.main = mainprogram
        self.player = None
        self.resize(1170, 830)
        self.sessioncreated = False
        app_icon = QtGui.QIcon()
        app_icon.addFile(os.path.join(WORKINGDIRECTORY, "assets", "icons", "mainwinicon"), QtCore.QSize(16, 16))
        self.setWindowIcon(app_icon)
        self.initgui()

    def viewgoals(self):
        if self.sessiondb.goalsset:
            self.sessiondb.displaycurrentgoals()
        else:
            QMessageBox.information(None, "No Goals Set",
                                    "No Goals Set. Please Set A Goal",
                                    QMessageBox.Ok | QMessageBox.Default,
                                    QMessageBox.NoButton)

    def viewcompletedgoals(self):
        if self.sessiondb.completedgoalsset:
            self.sessiondb.displaycompletedgoals()
        else:
            QMessageBox.information(None, "No Goals Completed Yet",
                                    "Keep Up The Hard Work And You Will Achieve A Goal Soon...",
                                    QMessageBox.Ok | QMessageBox.Default,
                                    QMessageBox.NoButton)

    def howtousethisprogram(self):
        Help.KujiInHelp(self)

    def goalcompleted(self, goaltext):
        goalcompleteddialog = QDialog(self)
        goalcompleteddialog.resize(406, 235)
        goalcompleteddialog.setLayoutDirection(Qt.LeftToRight)
        goalcompleteddialog.setAutoFillBackground(False)
        goalcompleteddialog.setModal(False)
        self.goalcompletedtopLabel = QLabel(goalcompleteddialog)
        self.goalcompletedtopLabel.setGeometry(QRect(120, 10, 161, 20))
        self.goalcompletedtopLabel.setStyleSheet("font: 12pt \"Arial\";\n"
                                                 "color: rgb(152, 166, 168);")
        self.goalcompletedmiddleLabel = QLabel(goalcompleteddialog)
        self.goalcompletedmiddleLabel.setGeometry(QRect(30, 40, 341, 21))
        self.goalcompletedValue = QLabel(goalcompleteddialog)
        self.goalcompletedValue.setGeometry(QRect(90, 70, 211, 51))
        self.goalcompletedValue.setStyleSheet("border: 1px solid black;\n"
                                              "font: 75 18pt \"Arial\";\n"
                                              "color: rgb(152, 166, 168);")
        self.goalcompletedValue.setAlignment(QtCore.Qt.AlignCenter)
        self.goalcompletedbottomLabel = QtGui.QLabel(goalcompleteddialog)
        self.goalcompletedbottomLabel.setGeometry(QtCore.QRect(10, 130, 391, 51))
        self.goalcompletedbottomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalcompletedbottomLabel.setWordWrap(True)
        self.goalcompletedButton = QtGui.QPushButton(goalcompleteddialog)
        self.goalcompletedButton.setGeometry(QtCore.QRect(310, 200, 84, 30))
        goalcompleteddialog.setWindowTitle("Goal Completed")
        self.goalcompletedtopLabel.setText("GOAL COMPLETED!")
        self.goalcompletedmiddleLabel.setText("It Wasn\'t Easy, But You Stuck With It And Achieved Your Goal Of:")
        self.goalcompletedValue.setText(goaltext)
        self.goalcompletedbottomLabel.setText(
            "Celebrate In Your Success, And Achieve The Next Goal You Have Set. Anything Is Possible!")
        self.goalcompletedButton.setText("OK")
        QtCore.QObject.connect(self.goalcompletedButton, QtCore.SIGNAL("clicked()"), goalcompleteddialog.accept)
        goalcompleteddialog.exec_()
        # Test Here If A New Goal Is Set, If Not Ask User To Set One!

    def setgoalstatus(self):
        """Method To Set Goal Current, Percentage And Total On Startup And After A Session Is Finished"""
        currenttext, percent, totaltext = self.sessiondb.getgoalstatus()
        if None not in [currenttext, percent, totaltext]:
            self.currentgoalLabel.setText(currenttext)
            self.goalProgressBar.setValue(percent)
            self.goalLabel.setText(totaltext)

    def goalpacing(self):
        if self.sessiondb.goalsset:
            self.goalpacingDialog = QDialog(self)
            self.goalpacingDialog.resize(400, 258)
            self.goalpacingtopLabel = QtGui.QLabel(self.goalpacingDialog)
            self.goalpacingtopLabel.setGeometry(QtCore.QRect(10, 20, 371, 81))
            self.goalpacingtopLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.goalpacingtopLabel.setWordWrap(True)
            self.goalpacingtopLabel.setObjectName(_fromUtf8("goalpacingtopLabel"))
            self.horizontalLayoutWidget = QtGui.QWidget(self.goalpacingDialog)
            self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 110, 171, 41))
            self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
            self.goalpacingValuesLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
            self.goalpacingValuesLayout.setMargin(0)
            self.goalpacingValuesLayout.setObjectName(_fromUtf8("goalpacingValuesLayout"))
            self.goalpaincgValue = QtGui.QSpinBox(self.horizontalLayoutWidget)
            self.goalpaincgValue.setMaximum(7)
            self.goalpaincgValue.setObjectName(_fromUtf8("goalpaincgValue"))
            self.goalpacingValuesLayout.addWidget(self.goalpaincgValue)
            self.goalpacingdaysLabel = QtGui.QLabel(self.horizontalLayoutWidget)
            self.goalpacingdaysLabel.setObjectName(_fromUtf8("goalpacingdaysLabel"))
            self.goalpacingValuesLayout.addWidget(self.goalpacingdaysLabel)
            self.horizontalLayoutWidget_2 = QtGui.QWidget(self.goalpacingDialog)
            self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 190, 188, 41))
            self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
            self.goalpacingButtonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
            self.goalpacingButtonLayout.setMargin(0)
            self.goalpacingButtonLayout.setObjectName(_fromUtf8("goalpacingButtonLayout"))
            self.goalpacingcalculateButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
            self.goalpacingcalculateButton.setObjectName(_fromUtf8("goalpacingcalculateButton"))
            self.goalpacingButtonLayout.addWidget(self.goalpacingcalculateButton)
            self.goalpacingcancelButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
            self.goalpacingcancelButton.setObjectName(_fromUtf8("goalpacingcancelButton"))
            self.goalpacingButtonLayout.addWidget(self.goalpacingcancelButton)
            self.goalpacingDialog.setWindowTitle("Goal Pacing")
            self.goalpacingtopLabel.setText(
                "In Order To Calculate How Much You Need To Meditate To Reach Your Goals, I Need To Know How Many Days A Week You Will Be Meditating")
            self.goalpacingdaysLabel.setText("Days A Week")
            self.goalpacingcalculateButton.setText("CALCULATE")
            self.goalpacingcancelButton.setText("CANCEl")
            QtCore.QObject.connect(self.goalpacingcalculateButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                                   self.goalpacingDialog.accept)
            QtCore.QObject.connect(self.goalpacingcancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                                   self.goalpacingDialog.reject)
            ret = self.goalpacingDialog.exec_()
            if ret == QDialog.Accepted:
                if self.goalpaincgValue.value() != 0:
                    goalpacingtext = self.sessiondb.goalpacing(int(self.goalpaincgValue.value()))
                    self.statusBar.showMessage(goalpacingtext, 10000)
                else:
                    self.statusBar.showMessage(
                        "You Must Practice At Least Once A Week For Me To Calculate Your Goal Pacing", 3000)
        else:
            QtGui.QMessageBox.information(None, "No Goals Set",
                                          "You Must Set At Least One Goal In Order For Me To Calculate Goal Pacing For That Goal",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                          QtGui.QMessageBox.NoButton)

    def closeEvent(self, event):
        """Stuff To Do Right Before Gui Is Closed"""
        self.player = self.main.sessionplayer
        playing = (self.player.entrainmentObject.state() == Phonon.PlayingState)
        if playing:
            quit_msg = "End The Session Prematurely?"
            reply = QtGui.QMessageBox.question(self, 'Confirmation End Session Prematurely',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.player.entrainmentObject.pause()
                if self.AmbienceOption.isChecked():
                    self.player.ambienceObject.pause()
                self.statusBar.showMessage("Session Is Currently Paused")
                self.confirmationDialog2 = QtGui.QDialog(self)
                self.confirmationDialog2.resize(434, 319)
                self.prematureendingreason = QtGui.QTextEdit(self.confirmationDialog2)
                self.prematureendingreason.setGeometry(QtCore.QRect(10, 50, 411, 221))
                self.prematureendingreason.setObjectName(_fromUtf8("listView"))
                self.label2 = QtGui.QLabel(self.confirmationDialog2)
                self.label2.setGeometry(QtCore.QRect(10, 20, 411, 20))
                self.label2.setAlignment(QtCore.Qt.AlignCenter)
                self.horizontalLayoutWidget2 = QtGui.QWidget(self.confirmationDialog2)
                self.horizontalLayoutWidget2.setGeometry(QtCore.QRect(80, 280, 341, 32))
                self.horizontalLayoutWidget2.setObjectName(_fromUtf8("horizontalLayoutWidget"))
                self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget2)
                self.horizontalLayout.setMargin(0)
                self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
                self.CreateButton = QtGui.QPushButton(self.horizontalLayoutWidget2)
                self.CreateButton.setObjectName(_fromUtf8("pushButton_2"))
                self.horizontalLayout.addWidget(self.CreateButton)
                self.listofsessionsButton = QtGui.QPushButton(self.horizontalLayoutWidget2)
                self.listofsessionsButton.setObjectName(_fromUtf8("pushButton"))
                self.horizontalLayout.addWidget(self.listofsessionsButton)
                self.confirmationDialog2.setWindowTitle("Premature Ending")
                self.label2.setText("Enter The Reason You Are Ending The Session Early:")
                self.CreateButton.setText("End Session")
                self.listofsessionsButton.setText("Resume Session")
                QtCore.QObject.connect(self.CreateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.testprematureending)
                QtCore.QObject.connect(self.listofsessionsButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                                       self.confirmationDialog2.reject)
                result = self.confirmationDialog2.exec_()
                if result == QDialog.Rejected:
                    self.statusBar.showMessage("Resuming Session...")
                    self.player.entrainmentObject.play()
                    if self.AmbienceOption.isChecked():
                        self.player.ambienceObject.play()
                    event.ignore()
            else:
                event.ignore()
        else:
            quit_msg = "Really Exit?"
            reply = QtGui.QMessageBox.question(self, 'Message',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

    def testprematureending(self):
        if self.prematureendingreason.toPlainText():
            sessionexpectedlist = list()
            for x, i in enumerate(self.slidervalues):
                if i.value() != 0:
                    val = i.value()
                    cutname = self.main.cuts[x]["name"]
                    txt = "%s: %s " % (cutname, val)
                    sessionexpectedlist.append(txt)
            self.statusBar.showMessage("Writing Reason To Database...")
            reason = self.prematureendingreason.toPlainText()
            self.sessiondb.writeprematureending(self.player.cutplayingname, sessionexpectedlist, reason)
            self.confirmationDialog2.accept()
        else:
            QtGui.QMessageBox.information(None, "Reason Empty",
                                          "Reason Cannot Be Blank In Order To End The Session Early",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                          QtGui.QMessageBox.NoButton)

    def aboutthisprogram(self):
        """Dialog Displaying Info About This Program"""
        self.aboutdialog = QDialog(self)
        self.aboutdialog.setObjectName(_fromUtf8("aboutdialog"))
        self.aboutdialog.resize(433, 268)
        self.aboutcloseButton = QtGui.QPushButton(self.aboutdialog)
        self.aboutcloseButton.setGeometry(QtCore.QRect(324, 230, 90, 23))
        self.aboutcloseButton.setObjectName(_fromUtf8("aboutcloseButton"))
        self.aboutlabel = QtGui.QLabel(self.aboutdialog)
        self.aboutlabel.setGeometry(QtCore.QRect(20, 20, 391, 21))
        self.aboutlabel.setStyleSheet(_fromUtf8("font: 14pt \"Arial Black\";"))
        self.aboutlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutlabel.setObjectName(_fromUtf8("aboutlabel"))
        self.abouttext = QtGui.QTextBrowser(self.aboutdialog)
        self.abouttext.setGeometry(QtCore.QRect(20, 50, 391, 170))
        self.abouttext.setObjectName(_fromUtf8("abouttext"))
        self.aboutHowToUseButton = QtGui.QPushButton(self.aboutdialog)
        self.aboutHowToUseButton.setGeometry(QtCore.QRect(20, 230, 111, 23))
        self.aboutHowToUseButton.setObjectName(_fromUtf8("aboutHowToUseButton"))
        self.aboutdialog.setWindowTitle("About")
        self.aboutcloseButton.setText("Close")
        self.aboutlabel.setText("About The Kuji-In Program")
        self.abouttext.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">This program was developed to be an aid to the practitioners of the Kuji-In through the use of brainwave entrainment technology and optional user-selected soundhelpers files. </span></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">Program Development By Caleb Trahan (c) 2015 All Rights Reserved</span></p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p>\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">Program Written In </span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; text-decoration: underline; color:#f0651f;\">Python 3</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">, Designed With </span><span style=\" font-family:\'Sans Serif\'; font-size:10pt; text-decoration: underline; color:#f0651f;\">Qt 4</span><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\"></span> And pydub Used For Audio Manipulation</p>\n"
            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p></body></html>")
        self.aboutHowToUseButton.setText("Tutorials")
        QtCore.QObject.connect(self.aboutHowToUseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.aboutdialog.accept)
        QtCore.QObject.connect(self.aboutcloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.aboutdialog.reject)
        ret = self.aboutdialog.exec_()
        if ret == QDialog.Accepted:
            Help.KujiInHelp(self)

    def displaylistofsession(self):
        """Method To Display The List Of Sessions Practiced"""
        sessionlist = self.sessiondb.testifnosessions()
        if not sessionlist:
            QtGui.QMessageBox.information(None, "No Sessions",
                                          "No Sessions Practiced Yet",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                          QtGui.QMessageBox.NoButton)
        else:
            Database.DisplaySessionList(self, self.sessiondb)

    def displayprematureendings(self):
        """Method To Display List Of Sessions Ended Early, If Any"""
        a = Database.DisplayPrematureEndings(self, self.sessiondb)
        isprematureendings = a.testforprematureendings()
        if not isprematureendings:
            QtGui.QMessageBox.information(None, "No Premature Endings",
                                          "No Premature Endings, Excellent Work And Let's Keep It That Way!",
                                          QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                          QtGui.QMessageBox.NoButton)

    def calculatetotalsessiontime(self):
        self.totalMinutesDisplay.display(0)
        self.totalhoursDisplay.display(0)
        totaltime = int()
        for x, i in enumerate(self.slidervalues):
            if i.value() != 0:
                totaltime += i.value()
        if totaltime > 0:
            if totaltime >= 60:
                hours = math.floor(totaltime / 60)
                if hours != 0:
                    self.totalhoursDisplay.display(hours)
                    totaltime -= hours * 60
                    if totaltime != 0:
                        self.totalMinutesDisplay.display(totaltime)
            else:
                self.totalMinutesDisplay.display(totaltime)
        else:
            self.statusBar.showMessage("Nothing To Calculate. All Cuts Are Set To 0", 1000)

    def displaytotalprogress(self):
        rinlist = [self.rintotalhoursDisplay, self.rintotalminutesDisplay]
        kyolist = [self.kyototalhoursDisplay, self.kyototalminutesDisplay]
        tohlist = [self.tohtotalhoursDisplay, self.tohtotalminutesDisplay]
        shalist = [self.shatotalhoursDisplay, self.shatotalminutesDisplay]
        kailist = [self.kaitotalhoursDisplay, self.kaitotalminutesDisplay]
        jinlist = [self.jintotalhoursDisplay, self.jintotalminutesDisplay]
        retsulist = [self.retsutotalhoursDisplay, self.retsutotalminutesDisplay]
        zailist = [self.zaitotalhoursDisplay, self.zaitotalminutesDisplay]
        zenlist = [self.zentotalhoursDisplay, self.zentotalminutesDisplay]
        totallist = [rinlist, kyolist, tohlist, shalist, kailist, jinlist, retsulist, zailist, zenlist]
        for x, i in enumerate(totallist):
            self.sessiondb.calculatetotalminutesforindividualcut(x, i)
        return True

    def newgoaldialog(self):
        self.setgoalsdialog = QDialog(self)
        self.setgoalsdialog.setObjectName(_fromUtf8("setgoalsdialog"))
        self.setgoalsdialog.resize(434, 241)
        self.setgoaldialogtopLabel = QtGui.QLabel(self.setgoalsdialog)
        self.setgoaldialogtopLabel.setGeometry(QtCore.QRect(40, 30, 381, 16))
        self.setgoaldialogtopLabel.setObjectName(_fromUtf8("setgoaldialogtopLabel"))
        self.setgoaldialoggoalLabel = QtGui.QLabel(self.setgoalsdialog)
        self.setgoaldialoggoalLabel.setGeometry(QtCore.QRect(130, 70, 59, 15))
        self.setgoaldialoggoalLabel.setObjectName(_fromUtf8("setgoaldialoggoalLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.setgoalsdialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 90, 91, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.setgoalsdialoggoallayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.setgoalsdialoggoallayout.setMargin(0)
        self.setgoalsdialoggoallayout.setObjectName(_fromUtf8("setgoalsdialoggoallayout"))
        self.setgoaldialogvalue = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.setgoaldialogvalue.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.setgoaldialogvalue.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.setgoaldialogvalue.setObjectName(_fromUtf8("setgoaldialogvalue"))
        self.setgoalsdialoggoallayout.addWidget(self.setgoaldialogvalue)
        self.setgoaldialoghrslabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.setgoaldialoghrslabel.setObjectName(_fromUtf8("setgoaldialoghrslabel"))
        self.setgoalsdialoggoallayout.addWidget(self.setgoaldialoghrslabel)
        self.setgoaldialogDueDate = QtGui.QDateEdit(self.setgoalsdialog)
        self.setgoaldialogDueDate.setDateTime(QDateTime.currentDateTime())
        self.setgoaldialogDueDate.setCalendarPopup(True)
        self.setgoaldialogDueDate.setGeometry(QtCore.QRect(220, 100, 110, 22))
        self.setgoaldialogDueDate.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.setgoaldialogDueDate.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.setgoaldialogDueDate.setDisplayFormat(_fromUtf8(""))
        self.setgoaldialogDueDate.setObjectName(_fromUtf8("setgoaldialogDueDate"))
        self.setgoalduedateLabel = QtGui.QLabel(self.setgoalsdialog)
        self.setgoalduedateLabel.setGeometry(QtCore.QRect(240, 70, 61, 20))
        self.setgoalduedateLabel.setObjectName(_fromUtf8("setgoalduedateLabel"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.setgoalsdialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 180, 334, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.setdialogbuttonslayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.setdialogbuttonslayout.setMargin(0)
        self.setdialogbuttonslayout.setObjectName(_fromUtf8("setdialogbuttonslayout"))
        self.setgoaldialoggoallistButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.setgoaldialoggoallistButton.setObjectName(_fromUtf8("pushButton"))
        self.setdialogbuttonslayout.addWidget(self.setgoaldialoggoallistButton)
        self.setgoaldialogAcceptButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.setgoaldialogAcceptButton.setObjectName(_fromUtf8("setgoaldialogAcceptButton"))
        self.setdialogbuttonslayout.addWidget(self.setgoaldialogAcceptButton)
        self.setgoaldialogCancelButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.setgoaldialogCancelButton.setObjectName(_fromUtf8("setgoaldialogCancelButton"))
        self.setdialogbuttonslayout.addWidget(self.setgoaldialogCancelButton)
        self.setgoalsdialog.setWindowTitle("Set A New Goal")
        currenthours = self.sessiondb.calculatetotalhours()
        self.setgoaldialogtopLabel.setText("You Have Practiced For %s Hours. Please Set A New Goal:" % currenthours)
        self.setgoaldialoggoalLabel.setText("GOAL")
        self.setgoaldialoghrslabel.setText("hrs")
        self.setgoalduedateLabel.setText("Due Date")
        self.setgoaldialogAcceptButton.setText("Set This Goal")
        self.setgoaldialoggoallistButton.setText("Current Goals")
        self.setgoaldialogCancelButton.setText("Cancel")
        QtCore.QObject.connect(self.setgoaldialogAcceptButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.checkgoals)
        QtCore.QObject.connect(self.setgoaldialoggoallistButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.viewgoals)
        QtCore.QObject.connect(self.setgoaldialogCancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.setgoalsdialog.reject)
        self.setgoalsdialog.exec_()

    def checkgoals(self):
        goaldate = self.setgoaldialogDueDate.dateTime().toPyDateTime()
        goalhours = int(self.setgoaldialogvalue.value())
        valueisgood = self.sessiondb.checknewgoals(goaldate, goalhours)
        if isinstance(valueisgood, bool):
            self.statusBar.showMessage("Adding Goal...")
            self.sessiondb.insertgoal(goaldate, goalhours)
            self.setgoalsdialog.accept()
            self.setgoalstatus()
            self.statusBar.showMessage("Goal Successfully Added", 3000)
        else:
            QtGui.QMessageBox.critical(None, "Error Adding Goal",
                                       valueisgood,
                                       QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                       QtGui.QMessageBox.NoButton)
            return

    def setsignalsandslots(self):
        """Signals And Slot Bindings For Main GUI"""
        QtCore.QObject.connect(self.preSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.preDisplay_2.display)
        QtCore.QObject.connect(self.rinSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.rinDisplay_2.display)
        QtCore.QObject.connect(self.kyoSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.kyoDisplay_2.display)
        QtCore.QObject.connect(self.tohSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.tohDisplay_2.display)
        QtCore.QObject.connect(self.shaSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.shaDisplay_2.display)
        QtCore.QObject.connect(self.kaiSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.kaiDisplay_2.display)
        QtCore.QObject.connect(self.jinSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.jinDisplay_2.display)
        QtCore.QObject.connect(self.retsuSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.retsuDisplay_2.display)
        QtCore.QObject.connect(self.zaiSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.zaiDisplay_2.display)
        QtCore.QObject.connect(self.zenSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.zenDisplay_2.display)
        QtCore.QObject.connect(self.postSlider_2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")),
                               self.postDisplay_2.display)
        QtCore.QObject.connect(self.CreateButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.main.createsession)
        QtCore.QObject.connect(self.listofsessionsButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.displaylistofsession)
        QtCore.QObject.connect(self.AmbienceOption, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")),
                               self.main.ambiencecheckboxchecked)
        QtCore.QObject.connect(self.ReferenceDisplayOption, QtCore.SIGNAL(_fromUtf8("stateChanged(int)")),
                               self.main.referenceboxchecked)
        QtCore.QObject.connect(self.prematureendingsbutton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.displayprematureendings)
        QtCore.QObject.connect(self.PlayButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.main.playsession)
        QtCore.QObject.connect(self.PauseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.main.pausesession)
        QtCore.QObject.connect(self.StopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.main.stopsession)
        QtCore.QObject.connect(self.exportButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.main.exportsession)
        QtCore.QObject.connect(self.calculateTotalSessionTimeButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.calculatetotalsessiontime)
        QtCore.QObject.connect(self.viewgoalsButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.viewgoals)
        QtCore.QObject.connect(self.completedgoalsButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.viewcompletedgoals)
        QtCore.QObject.connect(self.setgoalButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.newgoaldialog)
        QtCore.QObject.connect(self.goalpacingButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.goalpacing)
        QtCore.QObject.connect(self.changeallvaluesButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.changeallvalues)
        # self.setnewmaxslidervalue()
        self.displaytotalprogress()

    def changeallvalues(self):
        """Method With A Dialog To Set All Values To _____"""
        self.changevaluesdialog = QtGui.QDialog(self)
        self.changevaluesdialog.setObjectName(_fromUtf8("changevaluedialog"))
        self.changevaluesdialog.resize(395, 130)
        self.changevaluesdialog.setMinimumSize(QtCore.QSize(0, 100))
        self.changeValueTopLabel = QtGui.QLabel(self.changevaluesdialog)
        self.changeValueTopLabel.setGeometry(QtCore.QRect(70, 30, 131, 20))
        self.changeValueTopLabel.setObjectName(_fromUtf8("changeValueTopLabel"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.changevaluesdialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 337, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.changeValueLayout2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.changeValueLayout2.setMargin(0)
        self.changeValueLayout2.setObjectName(_fromUtf8("changeValueLayout2"))
        self.changeValuecheckbox = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.changeValuecheckbox.setObjectName(_fromUtf8("changeValuecheckbox"))
        self.changeValueLayout2.addWidget(self.changeValuecheckbox)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.changeValueLayout2.addWidget(self.pushButton)
        self.StopButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.StopButton.setObjectName(_fromUtf8("pushButton_2"))
        self.changeValueLayout2.addWidget(self.StopButton)
        self.changeValuespinbox = QtGui.QSpinBox(self.changevaluesdialog)
        self.changeValuespinbox.setGeometry(QtCore.QRect(210, 30, 51, 20))
        # self.changeValuespinbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.changeValuespinbox.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.changeValuespinbox.setObjectName(_fromUtf8("changeValuespinbox"))
        self.changeValueminuteslabel = QtGui.QLabel(self.changevaluesdialog)
        self.changeValueminuteslabel.setGeometry(QtCore.QRect(270, 20, 91, 39))
        self.changevaluesdialog.setWindowTitle("Change All Values")
        self.changeValueTopLabel.setText("Change All Values To:")
        self.changeValuecheckbox.setText("Include Pre And Post")
        self.changeValueminuteslabel.setText("minute(s)")
        self.pushButton.setText("OK")
        self.StopButton.setText("Cancel")
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.changevaluesdialog.accept)
        QtCore.QObject.connect(self.StopButton, QtCore.SIGNAL("clicked()"), self.changevaluesdialog.reject)
        ret = self.changevaluesdialog.exec_()
        if ret == QDialog.Accepted:
            value = self.changeValuespinbox.value()
            if self.changeValuecheckbox.isChecked():
                for x, i in enumerate(self.slidervalues):
                    i.setValue(value)
            else:
                for x, i in enumerate(self.slidervalues):
                    if x not in [0, 10]:
                        i.setValue(value)

    def initgui(self):
        """Method To Setup Gui Bindings"""
        self.centralwidget = self
        self.centralwidget.setObjectName(_fromUtf8("Kuji-In Session Creator"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 821))
        # self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        # self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
######## Creating Session Top Cutname Labels
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(36, 80, 716, 51))
        self.DurationLabels_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.setMargin(0)
        self.preLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.preLabel_2)
        self.rinLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.rinLabel_2)
        self.kyoLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.kyoLabel_2)
        self.tohLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.tohLabel_2)
        self.shaLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.shaLabel_2)
        self.kaiLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.kaiLabel_2)
        self.jinLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.jinLabel_2)
        self.retsuLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.retsuLabel_2)
        self.zaiLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.zaiLabel_2)
        self.zenLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.zenLabel_2)
        self.postLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.addWidget(self.postLabel_2)
        creatingsessiontopcutnamelabels = [
            self.preLabel_2, self.rinLabel_2, self.kyoLabel_2, self.tohLabel_2, self.shaLabel_2, self.kaiLabel_2,
            self.jinLabel_2, self.retsuLabel_2, self.zaiLabel_2, self.zenLabel_2, self.postLabel_2
        ]
        for i in creatingsessiontopcutnamelabels:
            i.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
                                    "border-top: 1px solid black;\n"
                                    "border-left: 1px solid black;\n"
                                    "border-right: 1px solid black;"))
            i.setAlignment(QtCore.Qt.AlignCenter)
### Creating Session Slider
        self.sessionslidersLayout = QtGui.QWidget(self.frame)
        self.sessionslidersLayout.setGeometry(QtCore.QRect(10, 130, 761, 331))
        self.DurationSliders_2 = QtGui.QHBoxLayout(self.sessionslidersLayout)
        self.DurationSliders_2.setContentsMargins(-1, -1, 0, -1)
        self.preSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.preSlider_2)
        self.rinSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.rinSlider_2)
        self.kyoSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.kyoSlider_2)
        self.tohSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.tohSlider_2)
        self.shaSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.shaSlider_2)
        self.kaiSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.kaiSlider_2)
        self.jinSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.jinSlider_2)
        self.retsuSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.retsuSlider_2)
        self.zaiSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.zaiSlider_2)
        self.zenSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.zenSlider_2)
        self.postSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.DurationSliders_2.addWidget(self.postSlider_2)
        creatingsessionsliders = [
            self.preSlider_2, self.rinSlider_2, self.kyoSlider_2, self.tohSlider_2, self.shaSlider_2, self.kaiSlider_2,
            self.jinSlider_2, self.retsuSlider_2, self.zaiSlider_2, self.zenSlider_2, self.postSlider_2
        ]
        for i in creatingsessionsliders:
            i.setMaximum(90)
            i.setSingleStep(5)
            i.setPageStep(5)
            i.setOrientation(QtCore.Qt.Vertical)
            i.setTickPosition(QtGui.QSlider.TicksBothSides)
        self.toptotalsLabel = QtGui.QLabel(self.frame)
        self.toptotalsLabel.setGeometry(QtCore.QRect(280, 40, 221, 21))
        self.toptotalsLabel.setStyleSheet(_fromUtf8("font: 14pt \"Arial Black\";\n"
                                                    "color: #98A6A8;"))
        self.toptotalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toptotalsLabel.setObjectName(_fromUtf8("toptotalsLabel"))
######## Values Below Sliders On Session Creator
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 470, 721, 41))
        self.CutDurationDisplays_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.setMargin(0)
        self.preDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.preDisplay_2)
        self.rinDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.rinDisplay_2)
        self.kyoDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.kyoDisplay_2)
        self.tohDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.tohDisplay_2)
        self.shaDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.shaDisplay_2)
        self.kaiDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.kaiDisplay_2)
        self.jinDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.jinDisplay_2)
        self.retsuDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.retsuDisplay_2)
        self.zaiDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.zaiDisplay_2)
        self.zenDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.addWidget(self.zenDisplay_2)
        self.postDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        lcdvaluesbelowsliders = [
            self.preDisplay_2, self.rinDisplay_2, self.kyoDisplay_2, self.tohDisplay_2, self.shaDisplay_2,
            self.kaiDisplay_2, self.jinDisplay_2, self.retsuDisplay_2, self.zaiDisplay_2, self.zenDisplay_2,
            self.postDisplay_2
        ]
        for i in lcdvaluesbelowsliders:
            i.setNumDigits(3)
        self.CutDurationDisplays_2.addWidget(self.postDisplay_2)
######## CutName Labels On Total Progress Display
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 80, 91, 432))
        self.totalprogressLabels = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.totalprogressLabels.setMargin(0)
        self.rintotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.rintotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.rintotalLabel)
        self.kyototalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.kyototalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.kyototalLabel)
        self.tohtotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.tohtotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.tohtotalLabel)
        self.shatotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.shatotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.shatotalLabel)
        self.kaitotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.kaitotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.kaitotalLabel)
        self.jintotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.jintotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.jintotalLabel)
        self.retsutotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.retsutotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.retsutotalLabel)
        self.zaitotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.zaitotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalprogressLabels.addWidget(self.zaitotalLabel)
        self.zentotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.zentotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        cutnamelabels = [
            self.rintotalLabel, self.kyototalLabel, self.tohtotalLabel, self.shatotalLabel, self.kaitotalLabel,
            self.jintotalLabel, self.retsutotalLabel, self.zaitotalLabel, self.zentotalLabel
        ]
        for i in cutnamelabels:
            i.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
                                       "border-left: 1px solid black;\n"
                                       "border-top: 1px solid black;\n"
                                       "border-bottom: 1px solid black;"))
        self.totalprogressLabels.addWidget(self.zentotalLabel)
######## Hours LCD Numbers On Total Progress Display
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(880, 80, 66, 432))
        self.totalhoursLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.totalhoursLayout.setMargin(0)
        self.rintotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.rintotalhoursDisplay)
        self.kyototalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.kyototalhoursDisplay)
        self.tohtotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.tohtotalhoursDisplay)
        self.shatotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.shatotalhoursDisplay)
        self.kaitotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.kaitotalhoursDisplay)
        self.jintotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.jintotalhoursDisplay)
        self.retsutotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.retsutotalhoursDisplay)
        self.zaitotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.totalhoursLayout.addWidget(self.zaitotalhoursDisplay)
        self.zentotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        lcdhoursdisplays = [
            self.rintotalhoursDisplay, self.kyototalhoursDisplay,self.tohtotalhoursDisplay, self.shatotalhoursDisplay,
            self.kaitotalhoursDisplay, self.jintotalhoursDisplay, self.retsutotalhoursDisplay, self.zaitotalhoursDisplay,
            self.zentotalhoursDisplay
        ]
        for i in lcdhoursdisplays:
            i.setNumDigits(4)
            i.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
                                      "border-top: 1px solid black;\n"
                                      "border-bottom: 1px solid black;"))
        self.totalhoursLayout.addWidget(self.zentotalhoursDisplay)
########    'Hours' And 'Minutes' Labels On Total Progress
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(946, 80, 55, 432))
        self.totalhoursLabels = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.totalhoursLabels.setMargin(0)
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_11)
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_15)
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_18)
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_17)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_16)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_13)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_12)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.totalhoursLabels.addWidget(self.label_10)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(1000.5, 80, 66, 432))
        self.totalminutesLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.totalminutesLayout.setMargin(0)
        self.rintotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.rintotalminutesDisplay)
        self.kyototalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.kyototalminutesDisplay)
        self.tohtotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.tohtotalminutesDisplay)
        self.shatotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.shatotalminutesDisplay)
        self.kaitotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.kaitotalminutesDisplay)
        self.jintotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.jintotalminutesDisplay)
        self.retsutotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.retsutotalminutesDisplay)
        self.zaitotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.zaitotalminutesDisplay)
        self.zentotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.totalminutesLayout.addWidget(self.zentotalminutesDisplay)
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(1064, 80, 71, 432))
        self.totalminuteslabelsLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.setMargin(0)
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_19)
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_23)
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_22)
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_21)
        self.label_25 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_25)
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_20)
        self.label_26 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_26)
        self.label_24 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_24)
        self.label_27 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.totalminuteslabelsLayout.addWidget(self.label_27)
        descriptionlabelslist = [
            self.label_10, self.label_11, self.label_12, self.label_13, self.label_14, self.label_15, self.label_16,
            self.label_17, self.label_18, self.label_19, self.label_20, self.label_21, self.label_22, self.label_23,
            self.label_24, self.label_25, self.label_26, self.label_27
        ]
        minuteslcdlist = [
            self.rintotalminutesDisplay, self.kyototalminutesDisplay, self.tohtotalminutesDisplay,
            self.shatotalminutesDisplay, self.kaitotalminutesDisplay, self.jintotalminutesDisplay,
            self.retsutotalminutesDisplay, self.zaitotalminutesDisplay, self.zentotalminutesDisplay
        ]
        for i in minuteslcdlist:
            i.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n" # Styles For LCDDisplay
                                     "border-top: 1px solid black;\n"
                                     "border-bottom: 1px solid black;"))
            i.setNumDigits(4)
        for i in descriptionlabelslist:
            i.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
                                      "border-right: 1px solid black;\n"
                                      "border-top: 1px solid black;\n"
                                      "border-bottom: 1px solid black;\n"))
            i.setAlignment(QtCore.Qt.AlignCenter)
########
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(790, 17, 491, 61))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.topsessionLabel = QtGui.QLabel(self.frame)
        self.topsessionLabel.setGeometry(QtCore.QRect(796, 36, 335, 31))
        self.topsessionLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
                                                     "font: 14pt \"Arial Black\";"))
        self.topsessionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topsessionLabel.setObjectName(_fromUtf8("topsessionLabel"))
        # self.horizontalLayout.addWidget(self.topsessionLabel)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(784, 517, 361, 50))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.listofsessionsButton = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.listofsessionsButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.listofsessionsButton)
        self.prematureendingsbutton = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.prematureendingsbutton.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_4.addWidget(self.prematureendingsbutton)
        # self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayoutWidget2 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget2.setGeometry(QtCore.QRect(30, 585, 310, 31))
        self.horizontalLayoutWidget2.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.AmbienceOption = QtGui.QCheckBox(self.horizontalLayoutWidget2)
        self.AmbienceOption.setObjectName(_fromUtf8("AmbienceOption"))
        self.horizontalLayout_2.addWidget(self.AmbienceOption)
        self.ReferenceDisplayOption = QtGui.QCheckBox(self.horizontalLayoutWidget2)
        self.ReferenceDisplayOption.setObjectName(_fromUtf8("ReferebceDisplayOption"))
        self.horizontalLayout_2.addWidget(self.ReferenceDisplayOption)
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 760, 311, 33))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget1 = QtGui.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(390, 580, 349, 41))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.actionsbuttonsLayout = QtGui.QHBoxLayout(self.widget1)
        self.actionsbuttonsLayout.setMargin(0)
        self.actionsbuttonsLayout.setObjectName(_fromUtf8("actionsbuttonsLayout"))
        self.CreateButton = QtGui.QPushButton(self.widget1)
        self.CreateButton.setObjectName(_fromUtf8("CreateButton"))
        self.actionsbuttonsLayout.addWidget(self.CreateButton)
        self.exportButton = QtGui.QPushButton(self.widget1)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.actionsbuttonsLayout.addWidget(self.exportButton)
        self.sessionPlayerFrame = QtGui.QFrame(self.frame)
        self.sessionPlayerFrame.setGeometry(QtCore.QRect(20, 640, 722, 165))
        self.sessionPlayerFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.sessionPlayerFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.sessionPlayerFrame.setObjectName(_fromUtf8("sessionPlayerFrame"))
        self.widget1 = QtGui.QWidget(self.sessionPlayerFrame)
        self.widget1.setGeometry(QtCore.QRect(20, 40, 311, 33))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.PlayButton = QtGui.QPushButton(self.widget1)
        self.PlayButton.setObjectName(_fromUtf8("PlayButton"))
        self.horizontalLayout_3.addWidget(self.PlayButton)
        self.PauseButton = QtGui.QPushButton(self.widget1)
        self.PauseButton.setObjectName(_fromUtf8("PauseButton"))
        self.horizontalLayout_3.addWidget(self.PauseButton)
        self.StopButton = QtGui.QPushButton(self.widget1)
        self.StopButton.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.StopButton)
        self.EntrainmentVolumeSlider = Phonon.VolumeSlider(self.sessionPlayerFrame)
        self.EntrainmentVolumeSlider.setGeometry(QtCore.QRect(2, 120, 150, 20))
        self.EntrainmentVolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.EntrainmentVolumeSlider.setObjectName(_fromUtf8("EntrainmentVolumeSlider"))
        fonttop = QtGui.QFont()
        fonttop.setPointSize(14)
        self.sessionPlayertopLabel = QtGui.QLabel(self.sessionPlayerFrame)
        self.sessionPlayertopLabel.setFont(fonttop)
        # self.sessionPlayertopLabel.setGeometry(QtCore.QRect(310, 10, 91, 16))
        self.sessionPlayertopLabel.setGeometry(QtCore.QRect(2, 10, 718, 20))
        self.sessionPlayertopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sessionPlayertopLabel.setObjectName(_fromUtf8("sessionPlayertopLabel"))
        self.EntrainmentVolumeTopLabel = QtGui.QLabel(self.sessionPlayerFrame)
        self.EntrainmentVolumeTopLabel.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.EntrainmentVolumeTopLabel.setObjectName(_fromUtf8("EntrainmentVolumeTopLabel"))
        self.AmbienceVolumeTopLabel = QtGui.QLabel(self.sessionPlayerFrame)
        self.AmbienceVolumeTopLabel.setGeometry(QtCore.QRect(220, 90, 111, 16))
        self.AmbienceVolumeTopLabel.setObjectName(_fromUtf8("AmbienceVolumeTopLabel"))
        self.AmbienceVolumeSlider = Phonon.VolumeSlider(self.sessionPlayerFrame)
        self.AmbienceVolumeSlider.setGeometry(QtCore.QRect(186, 120, 150, 20))
        self.AmbienceVolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AmbienceVolumeSlider.setObjectName(_fromUtf8("AmbienceVolumeSlider"))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.currentlyPlayingtopLabel = QtGui.QLabel(self.sessionPlayerFrame)
        self.currentlyPlayingtopLabel.setFont(font)
        self.currentlyPlayingtopLabel.setGeometry(QtCore.QRect(390, 30, 131, 21))
        self.currentlyPlayingtopLabel.setObjectName(_fromUtf8("currentlyPlayingtopLabel"))
        self.CutPlayingName = QtGui.QLabel(self.sessionPlayerFrame)
        self.CutPlayingName.setFont(font)
        self.CutPlayingName.setGeometry(QtCore.QRect(550, 30, 151, 20))
        self.CutPlayingName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CutPlayingName.setObjectName(_fromUtf8("CutPlayingName"))
        self.thiscutprogressDescriptionLabel = QtGui.QLabel(self.sessionPlayerFrame)
        self.thiscutprogressDescriptionLabel.setFont(font)
        self.thiscutprogressDescriptionLabel.setGeometry(QtCore.QRect(390, 60, 171, 21))
        self.thiscutprogressDescriptionLabel.setObjectName(_fromUtf8("thiscutprogressDescriptionLabel"))
        self.CutPlayingProgressActual = QtGui.QLabel(self.sessionPlayerFrame)
        self.CutPlayingProgressActual.setFont(font)
        self.CutPlayingProgressActual.setGeometry(QtCore.QRect(540, 60, 161, 20))
        self.CutPlayingProgressActual.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.CutPlayingProgressActual.setObjectName(_fromUtf8("CutPlayingProgressActual"))
        self.TotalSessionProgressDescriptionLabel = QtGui.QLabel(self.sessionPlayerFrame)
        self.TotalSessionProgressDescriptionLabel.setFont(font)
        self.TotalSessionProgressDescriptionLabel.setGeometry(QtCore.QRect(390, 90, 181, 21))
        self.TotalSessionProgressDescriptionLabel.setObjectName(_fromUtf8("TotalSessionProgressDescriptionLabel"))
        self.TotalSessionPlayingProgressActual = QtGui.QLabel(self.sessionPlayerFrame)
        self.TotalSessionPlayingProgressActual.setFont(font)
        self.TotalSessionPlayingProgressActual.setGeometry(QtCore.QRect(540, 90, 161, 20))
        self.TotalSessionPlayingProgressActual.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalSessionPlayingProgressActual.setObjectName(_fromUtf8("TotalSessionPlayingProgressActual"))
        self.OpenThisCutsReferenceFilesButton = QtGui.QPushButton(self.sessionPlayerFrame)
        self.OpenThisCutsReferenceFilesButton.setGeometry(QtCore.QRect(534, 126, 170, 31))
        self.OpenThisCutsReferenceFilesButton.setObjectName(_fromUtf8("OpenThisCutsReferenceFilesButton"))
        self.goalsFrame = QtGui.QFrame(self.frame)
        self.goalsFrame.setGeometry(QtCore.QRect(750, 570, 411, 237))
        self.goalsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.goalsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.goalsFrame.setObjectName(_fromUtf8("goalsFrame"))
        self.layoutWidget2 = QtGui.QWidget(self.goalsFrame)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 50, 361, 100))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.goalsVLayout = QtGui.QVBoxLayout(self.layoutWidget2)
        self.goalsVLayout.setObjectName(_fromUtf8("goalsVLayout"))
        self.goallabelsLayout = QtGui.QHBoxLayout()
        self.goallabelsLayout.setObjectName(_fromUtf8("goallabelsLayout"))
        self.currenttopLabel = QtGui.QLabel(self.layoutWidget2)
        self.currenttopLabel.setStyleSheet(_fromUtf8("border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.currenttopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currenttopLabel.setObjectName(_fromUtf8("currenttopLabel"))
        self.goallabelsLayout.addWidget(self.currenttopLabel)
        self.goaltopLabel = QtGui.QLabel(self.layoutWidget2)
        self.goaltopLabel.setStyleSheet(_fromUtf8("border-top: 1px solid black;\n"
"border-right: 1px solid black;\n"
"border-left: 1px solid black;"))
        self.goaltopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goaltopLabel.setObjectName(_fromUtf8("goaltopLabel"))
        self.goallabelsLayout.addWidget(self.goaltopLabel)
        self.goalsVLayout.addLayout(self.goallabelsLayout)
        self.goalactualLayout = QtGui.QHBoxLayout()
        self.goalactualLayout.setObjectName(_fromUtf8("goalactualLayout"))
        self.currentgoalLabel = QtGui.QLabel(self.layoutWidget2)
        self.currentgoalLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.currentgoalLabel.setBaseSize(QtCore.QSize(0, 0))
        self.currentgoalLabel.setStyleSheet(_fromUtf8("border-left: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.currentgoalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentgoalLabel.setObjectName(_fromUtf8("currentgoalLabel"))
        self.goalactualLayout.addWidget(self.currentgoalLabel)
        self.goalLabel = QtGui.QLabel(self.layoutWidget2)
        self.goalLabel.setMinimumSize(QtCore.QSize(100, 0))
        self.goalLabel.setStyleSheet(_fromUtf8("border-right: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.goalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalLabel.setObjectName(_fromUtf8("goalLabel"))
        self.goalactualLayout.addWidget(self.goalLabel)
        self.goalsVLayout.addLayout(self.goalactualLayout)
        self.goalProgressBar = QtGui.QProgressBar(self.layoutWidget2)
        self.goalProgressBar.setProperty("value", 24)
        self.goalProgressBar.setObjectName(_fromUtf8("goalProgressBar"))
        self.goalsVLayout.addWidget(self.goalProgressBar)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.goalsFrame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 152, 181, 81))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.goalsButtonLayoutLeft = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.goalsButtonLayoutLeft.setObjectName(_fromUtf8("goalsButtonLayoutLeft"))
        self.setgoalButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.setgoalButton.setObjectName(_fromUtf8("setgoalButton"))
        self.goalsButtonLayoutLeft.addWidget(self.setgoalButton)
        self.viewgoalsButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.viewgoalsButton.setObjectName(_fromUtf8("viewgoalsButton"))
        self.goalsButtonLayoutLeft.addWidget(self.viewgoalsButton)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.goalsFrame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(210, 152, 181, 81))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.goalsButtonLayoutRight = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.goalsButtonLayoutRight.setObjectName(_fromUtf8("goalsButtonLayoutRight"))
        self.goalpacingButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.goalpacingButton.setObjectName(_fromUtf8("goalpacingButton"))
        self.goalsButtonLayoutRight.addWidget(self.goalpacingButton)
        self.completedgoalsButton = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.completedgoalsButton.setObjectName(_fromUtf8("completedgoalsButton"))
        self.goalsButtonLayoutRight.addWidget(self.completedgoalsButton)
        self.progresstopLabel = QtGui.QLabel(self.goalsFrame)
        self.progresstopLabel.setGeometry(QtCore.QRect(60, 20, 290, 21))
        self.progresstopLabel.setMinimumSize(QtCore.QSize(290, 0))
        self.progresstopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.progresstopLabel.setStyleSheet(_fromUtf8("font: 14pt \"Arial Black\";\n"
                                                    "color: #98A6A8;"))
        self.progresstopLabel.setObjectName(_fromUtf8("progresstopLabel"))
        self.statusBar = QtGui.QStatusBar(self)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Status Bar Is Still There")
        self.menuBar = QtGui.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuBar.setStyleSheet("""
            QMenuBar {background-color:#212526; color: #98A6A8;}
            QMenuBar::item {background-color:#212526; color: #98A6A8; selection-color: #212526}
            QMenuBar::item:selected {color: #212526; background-color: #d7801a;}
        """)
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.setMenuBar(self.menuBar)
        self.actionExit = QtGui.QAction(self)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(self.close)
        self.actionChange_AlertFile = QtGui.QAction(self)
        self.actionChange_AlertFile.setObjectName(_fromUtf8("actionCheck_Integrity"))
        self.actionChange_AlertFile.triggered.connect(self.changealertfile)
        self.actionAddAmbience = QtGui.QAction(self)
        self.actionAddAmbience.setObjectName(_fromUtf8("actionadd_ambience"))
        self.actionAddAmbience.triggered.connect(self.addambiencefiles)
        self.actionEditAmbience = QtGui.QAction(self)
        self.actionEditAmbience.setObjectName(_fromUtf8("actionedit_ambience"))
        self.actionEditAmbience.triggered.connect(self.editambiencefiles)
        self.actionEditReferenceFiles = QtGui.QAction(self)
        self.actionEditReferenceFiles.triggered.connect(self.editreferencefiles)
        self.actionHowToUseThisProgram = QAction(self)
        self.actionHowToUseThisProgram.triggered.connect(self.howtousethisprogram)
        self.actionAboutThisProgram = QtGui.QAction(self)
        self.actionAboutThisProgram.triggered.connect(self.aboutthisprogram)
        self.actioncontactMe = QtGui.QAction(self)
        self.actioncontactMe.triggered.connect(self.contactme)
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionAddAmbience)
        self.menuTools.addAction(self.actionEditAmbience)
        self.menuTools.addAction(self.actionChange_AlertFile)
        self.menuTools.addAction(self.actionEditReferenceFiles)
        self.menuHelp.addAction(self.actionHowToUseThisProgram)
        self.menuHelp.addAction(self.actionAboutThisProgram)
        self.menuHelp.addAction(self.actioncontactMe)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        QtCore.QObject.connect(self.PlayButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.statusBar.clearMessage)
        self.horizontalLayoutWidget_8 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(250, 520, 271, 51))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.totalsessiondisplayLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.totalsessiondisplayLayout.setMargin(0)
        self.totalsessiondisplayLayout.setObjectName(_fromUtf8("totalsessiondisplayLayout"))
        self.totalhoursDisplay = QtGui.QLCDNumber(self.horizontalLayoutWidget_8)
        self.totalhoursDisplay.setObjectName(_fromUtf8("totalhoursDisplay"))
        self.totalsessiondisplayLayout.addWidget(self.totalhoursDisplay)
        self.totalhoursLabel = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.totalhoursLabel.setObjectName(_fromUtf8("totalhoursLabel"))
        self.totalsessiondisplayLayout.addWidget(self.totalhoursLabel)
        self.totalMinutesDisplay = QtGui.QLCDNumber(self.horizontalLayoutWidget_8)
        self.totalMinutesDisplay.setObjectName(_fromUtf8("totalMinutesDisplay"))
        self.totalsessiondisplayLayout.addWidget(self.totalMinutesDisplay)
        self.totalminutesLabel = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.totalminutesLabel.setObjectName(_fromUtf8("totalminutesLabel"))
        self.totalsessiondisplayLayout.addWidget(self.totalminutesLabel)
        self.calculateTotalSessionTimeButton = QtGui.QPushButton(self.frame)
        self.calculateTotalSessionTimeButton.setGeometry(QtCore.QRect(540, 530, 201, 23))
        self.calculateTotalSessionTimeButton.setObjectName(_fromUtf8("calculateTotalSessionTimeButton"))
        self.changeallvaluesButton = QtGui.QPushButton(self.frame)
        self.changeallvaluesButton.setGeometry(QtCore.QRect(30, 530, 201, 23))
        self.changeallvaluesButton.setObjectName(_fromUtf8("changeallvaluesButton"))
        self.setWindowTitle("MainWindow")
        self.preLabel_2.setText("PRE")
        self.rinLabel_2.setText("RIN")
        self.kyoLabel_2.setText("KYO")
        self.tohLabel_2.setText("TOH")
        self.shaLabel_2.setText("SHA")
        self.kaiLabel_2.setText("KAI")
        self.jinLabel_2.setText("JIN")
        self.retsuLabel_2.setText("RETSU")
        self.zaiLabel_2.setText("ZAI")
        self.zenLabel_2.setText("ZEN")
        self.postLabel_2.setText("POST")
        self.toptotalsLabel.setText("Create New Session")
        self.rintotalLabel.setText("RIN")
        self.kyototalLabel.setText("KYO")
        self.tohtotalLabel.setText("TOH")
        self.shatotalLabel.setText("SHA")
        self.kaitotalLabel.setText("KAI")
        self.jintotalLabel.setText("JIN")
        self.retsutotalLabel.setText("RETSU")
        self.zaitotalLabel.setText("ZAI")
        self.zentotalLabel.setText("ZEN")
        self.label_11.setText("Hours")
        self.label_14.setText("Hours")
        self.label_15.setText("Hours")
        self.label_18.setText("Hours")
        self.label_17.setText("Hours")
        self.label_16.setText("Hours")
        self.label_13.setText("Hours")
        self.label_12.setText("Hours")
        self.label_10.setText("Hours")
        self.label_19.setText("Minutes")
        self.label_23.setText("Minutes")
        self.label_22.setText("Minutes")
        self.label_21.setText("Minutes")
        self.label_25.setText("Minutes")
        self.label_20.setText("Minutes")
        self.label_26.setText("Minutes")
        self.label_24.setText("Minutes")
        self.label_27.setText("Minutes")
        self.changeallvaluesButton.setText("Change All Values To...")
        self.topsessionLabel.setText("Total Progress")
        self.listofsessionsButton.setText("View Practiced Sessions")
        self.prematureendingsbutton.setText("View Premature Endings")
        self.AmbienceOption.setText("Ambience In Session?")
        self.ReferenceDisplayOption.setText("Display Reference?")
        self.CreateButton.setText("Create Session")
        self.exportButton.setText("Export Session")
        self.PlayButton.setText("Play")
        self.PauseButton.setText("Pause")
        self.StopButton.setText("Stop")
        self.sessionPlayertopLabel.setText("Session Player")
        self.EntrainmentVolumeTopLabel.setText("Entrainment Volume")
        self.AmbienceVolumeTopLabel.setText("Ambience Volume")
        self.currentlyPlayingtopLabel.setText("Currently Playing:")
        self.CutPlayingName.setText("No Session Playing")
        self.thiscutprogressDescriptionLabel.setText("Progress:")
        self.CutPlayingProgressActual.setText("No Session Playing")
        self.TotalSessionProgressDescriptionLabel.setText("Total Session Progress:")
        self.TotalSessionPlayingProgressActual.setText("No Session Playing")
        self.OpenThisCutsReferenceFilesButton.setText("No Cut Playing")
        self.setgoalButton.setText("New Goal")
        self.goalpacingButton.setText("Goal Pacing")
        self.viewgoalsButton.setText("View Goals")
        self.completedgoalsButton.setText("Completed Goals")
        self.totalminutesLabel.setText("Minutes")
        self.totalhoursLabel.setText("Hours")
        self.calculateTotalSessionTimeButton.setText("Calculate Total Session Time")
        self.currenttopLabel.setText("Current")
        self.goaltopLabel.setText("Goal")
        self.progresstopLabel.setText("Goal Progress")
        self.setgoalstatus()
        if not self.sessiondb.goalsset:
            self.goalProgressBar.setValue(0)
            self.currentgoalLabel.setText("No Goal Set")
            self.goalLabel.setText("No Goal Set")
        self.menuFile.setTitle("File")
        self.menuTools.setTitle("Tools")
        self.menuHelp.setTitle("Help")
        self.actionExit.setText("Exit")
        self.actionChange_AlertFile.setText("Change Alert File")
        self.actionAddAmbience.setText("Add Ambience To Program")
        self.actionEditAmbience.setText("Edit Program's Ambience")
        self.actionEditReferenceFiles.setText("Edit Reference Files")
        self.actionAboutThisProgram.setText("About")
        self.actionHowToUseThisProgram.setText("Tutorials")
        self.actioncontactMe.setText("Contact Me")
        self.slidervalues = [self.preSlider_2, self.rinSlider_2, self.kyoSlider_2, self.tohSlider_2, self.shaSlider_2,
                             self.kaiSlider_2,
                             self.jinSlider_2, self.retsuSlider_2, self.zaiSlider_2, self.zenSlider_2,
                             self.postSlider_2]
        self.setsignalsandslots()

    def changealertfile(self):
        Tools.ChangeAlertFile(self)

    def editreferencefiles(self):
        Reference.EditReferenceFiles(self)

    def addambiencefiles(self):
        Tools.AddAmbienceFiles(self)

    def editambiencefiles(self):
        Tools.EditAmbienceFiles(self)

    def contactme(self):
        self.contactmedialog = QDialog(self)
        self.contactmedialog.resize(387, 206)
        self.contactmetextBrowser = QtGui.QTextBrowser(self.contactmedialog)
        self.contactmetextBrowser.setGeometry(QtCore.QRect(10, 10, 371, 161))
        self.contactmeOKButton = QtGui.QPushButton(self.contactmedialog)
        self.contactmeOKButton.setGeometry(QtCore.QRect(300, 180, 80, 23))
        self.contactmedialog.setWindowTitle("Contact Me")
        self.contactmetextBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:9pt;\">This program has been a project for me for a couple of years now, and it\'s grown from a basic terminal application to a full-fledged program (now over 4,000 lines of code). Seeing as I\'m the sole developer, chances are, I may have made a few mistakes, and sometimes programs don\'t work as expected. If this happens, please attach your log.txt file (in the program\'s directory) and shoot me an email at calebtrahan@gmail.com. I\'ll do my best to get back to you, and resolve the problem ASAP.</span></p></body></html>")
        self.contactmeOKButton.setText("OK")
        QtCore.QObject.connect(self.contactmeOKButton, QtCore.SIGNAL("clicked()"), self.contactmedialog.accept)
        self.contactmedialog.exec_()


