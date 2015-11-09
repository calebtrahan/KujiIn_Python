import os

from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

from main_const import HELPFILESDIRECTORY


class KujiInHelp(QDialog):
    def __init__(self, gui):
        QDialog.__init__(self, gui)
        self.gui = gui
        self.resize(343, 396)
        self.helptopLabel = QtGui.QLabel(self)
        self.helptopLabel.setGeometry(QtCore.QRect(40, 0, 271, 31))
        self.helptopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.helptopLabel.setObjectName("helptopLabel")
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 29, 271, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.helpbuttonsLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.helpbuttonsLayout.setMargin(0)
        self.helpbuttonsLayout.setObjectName("helpbuttonsLayout")
        self.helpcreatingsessionsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpcreatingsessionsButton.setObjectName("helpcreatingsessionsButton")
        self.helpbuttonsLayout.addWidget(self.helpcreatingsessionsButton)
        self.helpaddingambienceButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpaddingambienceButton.setObjectName("helpaddingambienceButton")
        self.helpbuttonsLayout.addWidget(self.helpaddingambienceButton)
        self.helpreferencefilesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpreferencefilesButton.setObjectName("helpreferencefilesButton")
        self.helpbuttonsLayout.addWidget(self.helpreferencefilesButton)
        self.helpplayingsessionsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpplayingsessionsButton.setObjectName("helpplayingsessionsButton")
        self.helpbuttonsLayout.addWidget(self.helpplayingsessionsButton)
        self.helpexportingsessionsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpexportingsessionsButton.setObjectName("helpexportingsessionsButton")
        self.helpbuttonsLayout.addWidget(self.helpexportingsessionsButton)
        self.helpgoalsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpgoalsButton.setObjectName("helpgoalsButton")
        self.helpbuttonsLayout.addWidget(self.helpgoalsButton)
        self.helpContactingMeButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpContactingMeButton.setObjectName("helpContactingMeButton")
        self.helpbuttonsLayout.addWidget(self.helpContactingMeButton)
        self.helpcloseButton = QtGui.QPushButton(self)
        self.helpcloseButton.setGeometry(QtCore.QRect(250, 360, 84, 30))
        self.helpcloseButton.setObjectName("helpcloseButton")
        self.setWindowTitle("Help")
        self.helptopLabel.setText("TUTORIALS")
        self.helpcreatingsessionsButton.setText("Creating Sessions")
        self.helpaddingambienceButton.setText("Adding Ambience")
        self.helpreferencefilesButton.setText("Reference Files")
        self.helpplayingsessionsButton.setText("Playing Sessions")
        self.helpexportingsessionsButton.setText("Exporting Sessions")
        self.helpgoalsButton.setText("Goals")
        self.helpContactingMeButton.setText("Contacting Me")
        self.helpcloseButton.setText("Close")
        QtCore.QObject.connect(self.helpcreatingsessionsButton, QtCore.SIGNAL("clicked()"), self.creatingsessions)
        QtCore.QObject.connect(self.helpaddingambienceButton, QtCore.SIGNAL("clicked()"), self.addingambience)
        QtCore.QObject.connect(self.helpreferencefilesButton, QtCore.SIGNAL("clicked()"), self.referencefiles)
        QtCore.QObject.connect(self.helpgoalsButton, QtCore.SIGNAL("clicked()"), self.goals)
        QtCore.QObject.connect(self.helpcloseButton, QtCore.SIGNAL("clicked()"), self.accept)
        QtCore.QObject.connect(self.helpplayingsessionsButton, QtCore.SIGNAL("clicked()"), self.playingsessions)
        QtCore.QObject.connect(self.helpexportingsessionsButton, QtCore.SIGNAL("clicked()"), self.exportingsessions)
        QtCore.QObject.connect(self.helpContactingMeButton, QtCore.SIGNAL("clicked()"), self.contactingme)
        self.exec_()

    def creatingsessions(self):
        HelpDialogTemplate(self.gui, "Creating Session How-To", "CREATING SESSIONS",
                           os.path.join(HELPFILESDIRECTORY, "creatingsession.html"))

    def addingambience(self):
        HelpDialogTemplate(self.gui, "Adding Ambience How-To", "ADDING AMBIENCE",
                           os.path.join(HELPFILESDIRECTORY, "addingambience.html"))

    def referencefiles(self):
        HelpDialogTemplate(self.gui, "Reference Files How-To", "REFERENCE FILES",
                           os.path.join(HELPFILESDIRECTORY, "referencefiles.html"))

    def playingsessions(self):
        HelpDialogTemplate(self.gui, "Playing Sessions How-To", "PLAYING SESSIONS",
                           os.path.join(HELPFILESDIRECTORY, "playingsessions.html"))

    def exportingsessions(self):
        HelpDialogTemplate(self.gui, "Exporting Sessions How-To", "EXPORTING SESSIONS",
                           os.path.join(HELPFILESDIRECTORY, "exportingsessions.html"))

    def goals(self):
        HelpDialogTemplate(self.gui, "Goals How-To", "GOALS",
                           os.path.join(HELPFILESDIRECTORY, "goals.html"))

    def contactingme(self):
        self.gui.contactme()


class HelpDialogTemplate(QDialog):
    def __init__(self, gui, windowtitle, topic, htmlfile):
        QDialog.__init__(self, gui)
        self.resize(806, 591)
        self.setStyleSheet("background-color:#212526;")
        self.label = QtGui.QLabel(self)
        self.label.setStyleSheet("color: #98A6A8;")
        self.label.setGeometry(QtCore.QRect(30, 10, 741, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.setGeometry(QtCore.QRect(30, 40, 741, 501))
        self.textBrowser.setStyleSheet("color: #98A6A8; background-color: rgb(42, 52, 53)")
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(690, 550, 84, 30))
        self.pushButton.setStyleSheet("color: #98A6A8; background-color: rgb(53, 63, 68);")
        self.setWindowTitle(windowtitle)
        self.label.setText(topic)
        self.pushButton.setText("Close")
        helpdisplay = open(htmlfile, "r", errors='ignore').read()
        self.textBrowser.insertHtml(helpdisplay)
        self.textBrowser.moveCursor(QtGui.QTextCursor.Start)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.accept)
        self.exec_()