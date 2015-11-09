import os
import re
from PyQt4 import QtCore, QtGui
from helpers.Help import *
from main_const import *
# from py_w3c.validators.html.validator import HTMLValidator

class ReferenceFiles(object):
    def __init__(self, main, gui):
        self.main = main
        self.gui = gui
        self.variation = None
        self.options = ["html", "txt"]
        self.fullscreen = False
        self.automaticallyopen = False
        self.fullscreenwarningdisplayed = False
        self.checkreferencefiles()

    @staticmethod
    def checkreferencefiles():
        reftypes = ["html", "txt"]
        names = ["Presession", "Rin", "Kyo", "Toh", "Sha", "Kai", "Jin", "Retsu", "Zai", "Zen", "Postsession"]
        for w in reftypes:
            for t in names:
                filetocheck = os.path.join(REFERENCEFILESMAINDIRECTORY, w, str(t + "." + w))
                if not os.path.exists(filetocheck):
                    open(filetocheck, "w").close()

    def selectreferencetype(self, topmessage="Select A Reference File Variation"):
        self.referencetypedialog = QtGui.QDialog(self.gui)
        self.referencetypedialog.resize(423, 155)
        self.htmldescription = QtGui.QLabel(self.referencetypedialog)
        self.htmldescription.setGeometry(QtCore.QRect(30, 70, 161, 31))
        self.htmldescription.setAlignment(QtCore.Qt.AlignCenter)
        self.htmldescription.setWordWrap(True)
        self.txtdescription = QtGui.QLabel(self.referencetypedialog)
        self.txtdescription.setGeometry(QtCore.QRect(220, 70, 191, 31))
        self.txtdescription.setAlignment(QtCore.Qt.AlignCenter)
        self.txtdescription.setWordWrap(True)
        self.htmlButton = QtGui.QPushButton(self.referencetypedialog)
        self.htmlButton.setGeometry(QtCore.QRect(10, 40, 201, 23))
        self.txtButton = QtGui.QPushButton(self.referencetypedialog)
        self.txtButton.setGeometry(QtCore.QRect(220, 40, 191, 23))
        self.helpButton = QtGui.QPushButton(self.referencetypedialog)
        self.helpButton.setGeometry(QtCore.QRect(320, 120, 90, 23))
        self.fullScreenCheckBox = QtGui.QCheckBox(self.referencetypedialog)
        self.fullScreenCheckBox.setGeometry(QtCore.QRect(20, 120, 181, 20))
        self.topLabel = QtGui.QLabel(self.referencetypedialog)
        self.topLabel.setGeometry(QtCore.QRect(17, 0, 391, 31))
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setWordWrap(True)
        self.referencetypedialog.setWindowTitle("Reference File Variations")
        self.htmldescription.setText(".html Files Containing Formatted Reference Files")
        self.txtdescription.setText(".txt Files Containing Un-Formatted Reference Files")
        self.htmlButton.setText("HTML")
        self.txtButton.setText("Text")
        self.helpButton.setText("Help")
        self.fullScreenCheckBox.setText("Full Screen")
        self.topLabel.setText(topmessage)
        QtCore.QObject.connect(self.txtButton, QtCore.SIGNAL("clicked()"), self.textoptionpressed)
        QtCore.QObject.connect(self.htmlButton, QtCore.SIGNAL("clicked()"), self.htmloptionpressed)
        QtCore.QObject.connect(self.helpButton, QtCore.SIGNAL("clicked()"), self.helpbuttonpressed)
        return QDialog.Accepted == self.referencetypedialog.exec_()

    def textoptionpressed(self):
        self.variation = self.options[1]
        good = self.referencefilescheck()
        if good:
            # self.gui.ReferenceDisplayOption.setChecked(True)
            if self.fullScreenCheckBox.isChecked():
                self.fullscreen = True
            self.referencetypedialog.accept()
            self.gui.statusBar.showMessage("The Text Variation Of Your Reference Files Will Auto-Display On Session Playback", 5000)
        else:
            QtGui.QMessageBox.critical(None, "Cannot Add Reference Files",
                                       "All Of The .txt Files In The Reference Directory Are Empty. Please Add Content To"
                                       " Each Of The .txt Files (For Each Cut Name) In %s/" %
                                       str(os.path.join(REFERENCEFILESMAINDIRECTORY, self.variation)),
                                       QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                       QtGui.QMessageBox.NoButton)

    def htmloptionpressed(self):
        self.variation = self.options[0]
        good = self.referencefilescheck()
        if good:
            # self.gui.ReferenceDisplayOption.setChecked(True)
            if self.fullScreenCheckBox.isChecked():
                self.fullscreen = True
            self.referencetypedialog.accept()
            self.gui.statusBar.showMessage("The HTML Variation Of Your Reference Files Will Auto-Display On Session Playback", 5000)
        else:
            QtGui.QMessageBox.critical(None, "Cannot Add Reference Files",
                                       "All Of The .html Files In The Reference Directory Are Empty. Please Add Content To"
                                       " Each Of The .html Files (For Each Cut Name) In %s/" % self.main.referencefilesvalue,
                                       QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                       QtGui.QMessageBox.NoButton)

    def helpbuttonpressed(self):
        HelpDialogTemplate(self.gui, "Reference Files How-To", "REFERENCE FILES",
                           os.path.join(HELPFILESDIRECTORY, "referencefiles.html"))

    def referencefilescheck(self): # TODO Trigger The Content Check On All For Only If Auto-Cycle All Is Called
        filedirectory = os.path.join(REFERENCEFILESMAINDIRECTORY, self.variation)
        filesexist = int()
        for i in os.listdir(filedirectory):
            filetocheck = os.path.join(filedirectory, i)
            fileisgood = self.checkifreferencefilegood(filetocheck)
            if fileisgood:
                filesexist += 1
            else:
                print("This Isn't Good: " + filetocheck)
        if filesexist == len(os.listdir(filedirectory)): # All Files Have At Least 3 Lines With Working Characters
            return True
        elif filesexist > 0: # Some Files Have At Least 3 Lines With Working Characters
            quit_msg = "Some Reference Files Have Content And Some Are Empty. Add The Reference" \
                       " Files That Have Content (The Ones That Don't Will Be Displayed Blank)?"
            reply = QtGui.QMessageBox.question(self.gui, 'Add Partial Reference Files To Session',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                return True
            else:
                return False
        else: # No Files Have 3 Lines With Working Characters
            return False

    @staticmethod
    def checkifreferencefilegood(filewithpath):
        try:
            with open(filewithpath, "r", errors='ignore') as file:
                f = file.readlines()
                linesthataregood = int()
                for u in f: # Test Line If It Contains At Least 5 Alpha-Numeric Characters
                    if re.search('[a-zA-Z]{5}', u): # Change Back To 5
                        linesthataregood += 1
                    if linesthataregood >= 3:
                        return True
                return False
        except FileNotFoundError:
            print("I Couldn't File This File: %s" % filewithpath)
            return False

    def openreferencefile(self, cutname):
        if not self.gui.ReferenceDisplayOption.isChecked():
            self.selectreferencetype()
        if self.variation == self.options[0]:
            cut = os.path.join(REFERENCEFILESMAINDIRECTORY, str(self.variation), str(cutname) + ".html")
        else: # TXT
            cut = os.path.join(REFERENCEFILESMAINDIRECTORY, str(self.variation), str(cutname) + ".txt")
        if self.checkifreferencefilegood(cut):
            self.cutdialog = QDialog()
            self.cutdialog.setWindowTitle("%s's Reference File" % cutname)
            self.cutdialog.setStyleSheet("background-color:#212526;")
            app_icon = QtGui.QIcon()
            app_icon.addFile(os.path.join(WORKINGDIRECTORY, "assets", "icons", "mainwinicon"), QtCore.QSize(16, 16))
            self.cutdialog.setWindowIcon(app_icon)
            self.textBrowser = QtGui.QTextBrowser(self.cutdialog)
            if self.fullscreen:
                self.fullscreenconfirmation()
                self.cutdialog.showFullScreen()
                height = self.main.screenheight - 20
                width = self.main.screenwidth - 20
                self.textBrowser.setGeometry(QtCore.QRect(10, 10, width, height))
            else:
                height = self.main.screenheight - 200
                width = self.main.screenwidth - 200
                self.textBrowser.setGeometry(QtCore.QRect(10, 10, width, height))
            self.textBrowser.setStyleSheet("color: #98A6A8;\nbackground-color: rgb(42, 52, 53);")
            cutdisplay = open(cut, "r", errors='ignore').read()
            if self.variation == self.options[0]:
                self.textBrowser.insertHtml(cutdisplay)
            else:
                self.textBrowser.insertPlainText(cutdisplay)
            self.textBrowser.moveCursor(QtGui.QTextCursor.Start)
            self.textBrowser.show()
            self.cutdialog.show()

    def fullscreenconfirmation(self):
        if not self.fullscreenwarningdisplayed:
            msg = "For immersion, I stripped away all of the normal OS elements such as the top menu bar for fullscreen reference file display." \
                  "To exit this screen at any time, simply press the 'ESC' Key"
            QtGui.QMessageBox.information(None, "Fullscreen Reference Files Notice", msg, QtGui.QMessageBox.Ok |
                                          QtGui.QMessageBox.Default, QtGui.QMessageBox.NoButton)
            self.fullscreenwarningdisplayed = True

    def closereferencefile(self):
        try:
            self.cutdialog.close()
        except:
            pass


class EditReferenceFiles(QDialog):
    def __init__(self, parent, msg="No File Open"):
        QDialog.__init__(self, parent)
        self.resize(958, 751)
        self.referencetextEditor = QtGui.QTextEdit(self)
        self.referencetextEditor.setGeometry(QtCore.QRect(40, 180, 891, 511))
        self.acceptButton = QtGui.QPushButton(self)
        self.acceptButton.setGeometry(QtCore.QRect(760, 710, 85, 32))
        self.closeButton = QtGui.QPushButton(self)
        self.closeButton.setGeometry(QtCore.QRect(860, 710, 85, 32))
        self.LoadReferenceFileFrame = QtGui.QFrame(self)
        self.LoadReferenceFileFrame.setGeometry(QtCore.QRect(130, 20, 341, 141))
        self.LoadReferenceFileFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LoadReferenceFileFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.loadReferenceFileButton = QtGui.QPushButton(self.LoadReferenceFileFrame)
        self.loadReferenceFileButton.setGeometry(QtCore.QRect(240, 60, 85, 32))
        self.LoadReferenceFileLabel_1 = QtGui.QLabel(self.LoadReferenceFileFrame)
        self.LoadReferenceFileLabel_1.setGeometry(QtCore.QRect(10, 40, 71, 31))
        self.LoadReferenceFileLabel_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.referenceFileSelectComboBox = QtGui.QComboBox(self.LoadReferenceFileFrame)
        self.referenceFileSelectComboBox.setGeometry(QtCore.QRect(90, 40, 131, 30))
        self.versionSelectComboBox = QtGui.QComboBox(self.LoadReferenceFileFrame)
        self.versionSelectComboBox.setGeometry(QtCore.QRect(90, 90, 131, 30))
        self.versionselectLabel = QtGui.QLabel(self.LoadReferenceFileFrame)
        self.versionselectLabel.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.versionselectLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LoadReferenceFileTopLabel = QtGui.QLabel(self.LoadReferenceFileFrame)
        self.LoadReferenceFileTopLabel.setGeometry(QtCore.QRect(10, 10, 311, 20))
        self.LoadReferenceFileTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentlyEditingFrame = QtGui.QFrame(self)
        self.CurrentlyEditingFrame.setGeometry(QtCore.QRect(540, 20, 331, 141))
        self.CurrentlyEditingFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.CurrentlyEditingFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.CurrentlyEditingTopLabel = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.CurrentlyEditingTopLabel.setGeometry(QtCore.QRect(10, 20, 311, 20))
        self.CurrentlyEditingTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentlyEditingTopLabel.setStyleSheet("font: 12pt \"Arial Black\";\n")
        self.CutNameActual = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.CutNameActual.setGeometry(QtCore.QRect(170, 60, 141, 20))
        self.CutNameActual.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Label_CutName = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.Label_CutName.setGeometry(QtCore.QRect(50, 60, 111, 21))
        self.Label_CutName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Variation = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.Label_Variation.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.Label_Variation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.VariationNameActual = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.VariationNameActual.setGeometry(QtCore.QRect(170, 100, 141, 21))
        ####
        self.setWindowTitle("Reference File Editor")
        self.loadReferenceFileButton.setText("Load")
        self.LoadReferenceFileLabel_1.setText("Cut Name:")
        self.versionselectLabel.setText("Variation")
        self.LoadReferenceFileTopLabel.setText("Load Reference File:")
        self.CurrentlyEditingTopLabel.setText("Currently Editing")
        self.CutNameActual.setText("No File Loaded")
        self.VariationNameActual.setText("No File Loaded")
        self.Label_CutName.setText("Cut Name:")
        self.Label_Variation.setText("Variation:")
        self.acceptButton.setText("Accept")
        self.closeButton.setText("Close")
        QtCore.QObject.connect(self.loadReferenceFileButton, QtCore.SIGNAL("clicked()"), self.loadreferencefile)
        QtCore.QObject.connect(self.versionSelectComboBox, QtCore.SIGNAL("activated(int)"), self.loadvariation)
        QtCore.QObject.connect(self.acceptButton, QtCore.SIGNAL("clicked()"), self.acceptbuttonpressed)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), self.closebuttonpressed)
        #
        self.oldtext = str()
        self.newtext = str()
        self.name = str()
        self.option = str()
        self.currentfile = str()
        self.items = ["txt", "html"]
        self.versionSelectComboBox.addItems(self.items)
        self.names = ["Presession", "Rin", "Kyo", "Toh", "Sha", "Kai", "Jin", "Retsu", "Zai", "Zen", "Postsession"]
        self.referenceFileSelectComboBox.addItems(self.names)
        #
        self.exec_()

    def loadreferencefile(self):
        if self.isfilechanged():
            msg = "Would You Like To Save The Changes You Made To The %s Variation Of %s?" % (self.option, self.name)
            if self.confirmationdialog("Save Changes", msg):
                self.savetofile()
        self.name = self.referenceFileSelectComboBox.currentText()
        self.option = self.versionSelectComboBox.currentText()
        self.referencetextEditor.clear()
        self.VariationNameActual.setText(".%s" % self.option)
        self.CutNameActual.setText(self.name)
        self.currentfile = os.path.join(REFERENCEFILESMAINDIRECTORY, self.option, self.name + "." + self.option)
        if os.path.isfile(self.currentfile):
            try:
                self.oldtext = open(self.currentfile).read()
                self.referencetextEditor.insertPlainText(self.oldtext)
            except UnicodeDecodeError:
                self.referencetextEditor.insertPlainText("Could Not Read HTML File. Possible Illegal Characters In File?")
        else:
            print("%s Does Not Exist" % self.currentfile)

    def validatetext(self):
        # Check If 5 Numeric Characters On Each Line For 5 Lines
        with open(self.currentfile, "r", errors='ignore') as file:
            f = file.readlines()
            linesthataregood = int()
            for u in f: # Test Line If It Contains At Least 5 Alpha-Numeric Characters
                if re.search('[a-zA-Z]{5}', u): # Change Back To 5
                    linesthataregood += 1
                if linesthataregood >= 3:
                    return True
            return False

    def validatefragment(self, fragment):
        if re.search('[a-zA-Z]{5}', fragment):
            return True
        else:
            return False

    def validatehtml(self):
        """Method To Pass Fragment Into py_w3c To See If It Valid HTML"""
        # Refer To https://bitbucket.org/nmb10/py_w3c
        filetext = ""
        # validator = HTMLValidator()
        # validator.validate_fragment(filetext)

    def savetofile(self):
        open(self.currentfile, 'w').close() # Erase The File's Contents
        newfile = open(self.currentfile, 'w')
        newfile.write(self.referencetextEditor.toPlainText())

    def isfilechanged(self):
        if str(self.oldtext) != self.referencetextEditor.toPlainText():
            return True
        else:
            return False

    def acceptbuttonpressed(self):
        if self.isfilechanged():
            newtext = self.referencetextEditor.toPlainText()
            if self.validatefragment(newtext):
                msg = "Are You Sure You Want To Update This Reference File With This Text? This Cannot Be Undone."
                if self.confirmationdialog("Save To File", msg):
                    self.savetofile()
            else:
                msg = "The Text You Entered To Be Used For This Reference File Is Really Short. Still Save As " \
                      "Reference File?"
                if self.confirmationdialog("Short Message Text", msg):
                    self.savetofile()

    def loadvariation(self, index):
        # Test If There Have Been Any Changes, And If So Ask The User If They Want To Save Their Changes
        pass

    def confirmationdialog(self, toptitle, msg):
        reply = QtGui.QMessageBox.question(self, toptitle, msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            return True
        else:
            return False

    def closebuttonpressed(self):
        if self.isfilechanged():
            pass # Save The Changes To This File Before Exiting?
        else:
            self.reject()