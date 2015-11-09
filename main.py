# noinspection PyPackageRequirements
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtNetwork import QLocalSocket, QLocalServer

from helpers import Entrainment, Ambience, Database, Gui
from utils import Creator, Exporter, Player
from main_const import *
from helpers.Reference import *
from pydub import AudioSegment
from utils import Tools
# BUGS

# NEW/UPDATED FEATURES

    # TODO Write All Stdout To Log File
        # TODO Get This Working With Sys.excepthook (Started Before Kujiin() Class In main.py)
    # TODO If StartupChecks() Fail, Display A Dialog With A Link To Download Session Files (This Program Is Missing Some Files, And May Not Work Correctly)
# FINISHING TOUCHES
    # TODO Use py2exe or py2installer To Create A Windows Exectuable (And Maybe A Macintosh One Too?)


def logtologfile(text):
    with open(os.path.join(WORKINGDIRECTORY, "log.txt"), 'a') as file:
        file.writelines(text)


def myexceptionhook(typed, value, tback):
    logtologfile(value)
    sys.__excepthook__(typed, value, tback)


class QSingleApplication(QApplication):
    def singleStart(self, mainWindow):
        self.mainWindow = mainWindow
        # Socket
        self.m_socket = QLocalSocket()
        self.m_socket.connected.connect(self.connectToExistingApp)
        self.m_socket.error.connect(self.startApplication)
        self.m_socket.connectToServer(self.applicationName(), QIODevice.WriteOnly)

    def connectToExistingApp(self):
        if len(sys.argv)>1 and sys.argv[1] is not None:
            self.m_socket.write(sys.argv[1])
            self.m_socket.bytesWritten.connect(self.quit)
        else:
            QMessageBox.warning(None, self.tr("Already running"), self.tr("The Kuji-In Program Is Already Running."))
            QTimer.singleShot(0, self.quit)

    def startApplication(self):
        self.m_server = QLocalServer()
        if self.m_server.listen(self.applicationName()):
            self.m_server.newConnection.connect(self.getNewConnection)
            self.mainWindow.show()
        else:
            QMessageBox.critical(None, self.tr("Error"), self.tr("Error listening the socket."))

    def getNewConnection(self):
        self.new_socket = self.m_server.nextPendingConnection()
        self.new_socket.readyRead.connect(self.readSocket)

    def readSocket(self):
        f = self.new_socket.readLine()
        self.mainWindow.getArgsFromOtherInstance(str(f))
        self.mainWindow.activateWindow()
        self.mainWindow.show()

class StartupChecks(QDialog):
    def __init__(self, parent, main):
        QDialog.__init__(self, parent)
        self.resize(292, 65)
        self.main = main
        self.currentlyprocessingLabel = QtGui.QLabel(self)
        self.currentlyprocessingLabel.setGeometry(QtCore.QRect(0, 40, 291, 17))
        self.totalprocessingProgressBar = QtGui.QProgressBar(self)
        self.totalprocessingProgressBar.setGeometry(QtCore.QRect(0, 20, 291, 23))
        self.totalprocessingProgressBar.setValue(0)
        self.exec_()

    def alertfilechecker(self):
        if not os.path.exists(ALERTFILE):
            if os.path.exists(ALERTSILENCE): os.remove(ALERTSILENCE)
            QMessageBox.warning(None, "No Alert File Found", "An Alert File (Short Audible Warning That Informats You When"
                                                             "In Between Cuts That It's Time To Change To The Next Cut) "
                                                             "Is Necessary For This Program To Function.")
            while True:
                Tools.ChangeAlertFile(self, "Add Alert File")
                if os.path.exists(ALERTFILE) and os.path.exists(ALERTSILENCE):
                    break
                else:
                    continue
        elif not os.path.exists(ALERTSILENCE):
            alertfile = AudioSegment.from_mp3(ALERTFILE)
            alertsilence = AudioSegment.silent(len(alertfile))
            alertsilence.export(ALERTSILENCE, format="mp3")

    def checkifambienceisempty(self):
        directoriesnotempty = 0
        for i in self.main.cuts:
            directory = os.path.join(AMBIENCEDIRECTORY, i["name"])
            filecount = 0
            for i in os.listdir(directory):
                if i.endswith(".mp3"):
                    filecount += 1
            if filecount > 0:
                directoriesnotempty += 1
        generaldir = os.path.join(AMBIENCEDIRECTORY, "general")
        filecount = 0
        for i in os.listdir(generaldir):
            if i.endswith(".mp3"):
                filecount += 1
        if filecount > 0:
            directoriesnotempty += 1
        if directoriesnotempty == 0:
            quit_msg = "No Ambience At All Found. Add Some Now?"
            reply = QtGui.QMessageBox.question(self.main.gui, 'Ambience Missing',
                                               quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                Tools.AddAmbienceFiles(self.main.gui)

    def showEvent(self, QShowEvent):
        self.startupchecks()

    def startupchecks(self):
        self.currentlyprocessingLabel.setText("Currently Checking Necessary Sound Files...")
        self.recheckentrainment()
        self.totalprocessingProgressBar.setValue(33)
        self.alertfilechecker()
        self.totalprocessingProgressBar.setValue(66)
        ## Add Ambience Checks Here + Close
        print("Checks Passed")

    def recheckentrainment(self):
        if not self.main.entrainment.checkentrainment():
            QMessageBox.critical(None, "Missing Neccessary Files", "Necessary Sound Files Are Missing From "
                                                                  "The Program. Please Try Reinstalling The Program")
            quit()
            # self.startupchecksfaileddialog = QDialog(self.gui)
            # self.startupchecksfaileddialog.resize(444, 103)
            # self.label = QtGui.QLabel(self.startupchecksfaileddialog)
            # self.label.setGeometry(QtCore.QRect(30, 0, 371, 61))
            # self.label.setAlignment(QtCore.Qt.AlignCenter)
            # self.label.setWordWrap(True)
            # self.pushButton = QtGui.QPushButton(self.startupchecksfaileddialog)
            # self.pushButton.setGeometry(QtCore.QRect(350, 70, 75, 23))
            # self.label.setText("Missing Some Necessary Sound Files From The Program. Please Go To This Link To Download Them:  \nhttp://link.com/  \n(NOTE: If You Don\'t Do This The Program May Freeze Or Make Incomplete Or Silent Sessions)")
            # self.pushButton.setText("OK")
            # QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.startupchecksfaileddialog.accept)
            # self.startupchecksfaileddialog.exec_()
            # # Display A Dialog To A Link With The Entrainment Files Neccasry For Program (Maybe Google Drive?)


class Kujiin:
    def __init__(self):
        print("Real Database Loaded. Change It To Test The Program.")
        self.cutsinsession = list()
        self.pre = {"number": 0, "name": "Presession", "duration": 0, "ramp": 2}
        self.rin = {"number": 1, "name": "Rin", "duration": None}
        self.kyo = {"number": 2, "name": "Kyo", "duration": None}
        self.toh = {"number": 3, "name": "Toh", "duration": None}
        self.sha = {"number": 4, "name": "Sha", "duration": None}
        self.kai = {"number": 5, "name": "Kai", "duration": None}
        self.jin = {"number": 6, "name": "Jin", "duration": None}
        self.retsu = {"number": 7, "name": "Retsu", "duration": None}
        self.zai = {"number": 8, "name": "Zai", "duration": None}
        self.zen = {"number": 9, "name": "Zen", "duration": None}
        self.post = {"number": 10, "name": "Postsession", "duration": 0, "ramp": 2}
        self.alert = {"name": "Alert", "duration": None}
        self.deletetempfiles()
        self.cuts = [self.pre, self.rin, self.kyo, self.toh, self.sha, self.kai, self.jin, self.retsu, self.zai,
                     self.zen, self.post]
        self.cutinvocationduration = int()
        app = QSingleApplication(sys.argv)
        app.setApplicationName("Kuji-In")
        app.setQuitOnLastWindowClosed(True)
        screen_rect = app.desktop().screenGeometry()
        self.screenwidth, self.screenheight = screen_rect.width(), screen_rect.height()
        self.gui = Gui.KujiDesign(self)
        self.ambience = Ambience.SessionAmbience(self, self.gui)
        self.sessiondb = Database.SessionDatabase(self.gui)
        self.sessiondb.getgoalstatus()
        self.sessionplayer = Player.SessionPlayer(self, self.sessiondb)
        self.gui.setWindowTitle("Kuji-In")
        self.gui.move((self.screenwidth / 2) - (self.gui.frameSize().width() / 2),
                      (self.screenheight / 2) - (self.gui.frameSize().height() / 2))
        self.entrainment = Entrainment.Entrainment(self, self.gui)
        self.entrainmentplayer = None
        self.ambienceplayer = None
        self.sessioncreated = False
        self.createdsessionhasmabience = False
        self.ambienceenabled = False
        self.cutsinsession = list()
        # StartupChecks(self.gui, self)
        sessions = self.sessiondb.testifnosessions()
        if not sessions:
            self.welcomescreen()
        app.singleStart(self.gui)
        self.sessionreference = ReferenceFiles(self, self.gui)
        sys.exit(app.exec_())

    def welcomescreen(self):
        self.welcomedialog = QDialog(self.gui)
        self.welcomedialog.resize(561, 244)
        self.welcometextBrowser = QtGui.QTextBrowser(self.welcomedialog)
        self.welcometextBrowser.setGeometry(QtCore.QRect(10, 10, 541, 191))
        self.horizontalLayoutWidget = QtGui.QWidget(self.welcomedialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 210, 181, 31))
        self.welcomebuttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.welcomebuttonLayout.setMargin(0)
        self.welcometutorialsButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.welcomebuttonLayout.addWidget(self.welcometutorialsButton)
        self.welcomecloseButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.welcomebuttonLayout.addWidget(self.welcomecloseButton)
        self.welcomedialog.setWindowTitle("Welcome")
        welcomefile = open(WELCOMEMESSAGE).read()
        self.welcometextBrowser.setHtml(welcomefile)
        self.welcometutorialsButton.setText("Tutorials")
        self.welcomecloseButton.setText("Close")
        QtCore.QObject.connect(self.welcomecloseButton, QtCore.SIGNAL("clicked()"), self.welcomedialog.reject)
        QtCore.QObject.connect(self.welcometutorialsButton, QtCore.SIGNAL("clicked()"), self.welcomedialog.accept)
        ret = self.welcomedialog.exec_()
        if ret == QDialog.Accepted:
            self.gui.howtousethisprogram()

    def resetsession(self):
        self.cutsinsession = list()
        self.deletetempfiles()
        for i in self.cuts:
            i["duration"] = 0

    def createsession(self):
        self.creator = Creator.SessionCreator(self, self.gui, self.sessionplayer)
        self.creator.createsession()

    def ambiencecheckboxchecked(self):
        checkboxstate = self.gui.AmbienceOption.checkState()
        checked = 2
        unchecked = 0
        if not self.sessioncreated:
            if checkboxstate == checked:
                self.ambience.selectambiencetype()
        else:
            if checkboxstate == checked:
                if not self.createdsessionhasmabience:
                    quit_msg = "Session Does Not Contain Ambience. Would You Like To Recreate The Session With Ambience?"
                    reply = QtGui.QMessageBox.question(self.gui, 'Recreate Session',
                                                       quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QtGui.QMessageBox.Yes:
                        self.ambience.selectambiencetype()
                        if checkboxstate == checked:
                            self.createsession()
                    else:
                        self.gui.AmbienceOption.setChecked(False)
            elif checkboxstate == unchecked:
                if self.createdsessionhasmabience:
                    quit_msg = "Session Contains Ambience. Would You Like To Recreate The Session Without Ambience?"
                    reply = QtGui.QMessageBox.question(self.gui, 'Recreate Session',
                                     quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QtGui.QMessageBox.Yes:
                        self.ambience.selectambiencetype()
                        if checkboxstate == checked:
                            self.createsession()
                    else:
                        self.gui.AmbienceOption.setChecked(True)

    def referenceboxchecked(self): # TODO Disable Reference Files When Unchecked
        checkboxstate = self.gui.ReferenceDisplayOption.checkState()
        if checkboxstate == 2:
            a = self.sessionreference.selectreferencetype("This Will Automatically Display And Cycle "
                                                      "Reference Files Throughout Session Playback")
            self.gui.ReferenceDisplayOption.setChecked(a)
            self.sessionreference.automaticallyopen = a
        else:
            self.gui.ReferenceDisplayOption.setChecked(False)
            self.sessionreference.automaticallyopen = False
            self.gui.statusBar.showMessage("Reference Files Will No Longer Auto-Display During Session Playback", 5000)

    def playsession(self):
        self.sessioncreated = self.sessioncreated
        if self.sessioncreated:
            playback = self.sessionplayer.sessionplaybacktipsmethod()
            if playback:
                self.sessionplayer.playsession(self.cutsinsession, self.entrainmentplayer, self.ambienceplayer)
        else:
            QtGui.QMessageBox.information(None, "No Session Created",
                                           "You Must Create A Session In Order For Me To Play",
                                           QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                           QtGui.QMessageBox.NoButton)

    def exportsession(self):
        Exporter.ExportSession(self, self.gui, self.sessionplayer)

    def pausesession(self):
        self.sessionplayer.pausesession()

    def stopsession(self):
        self.sessionplayer.stopsession()

    @staticmethod
    def deletetempfiles():
        try:
            [os.remove(os.path.join(TEMPDIRECTORY, x)) for x in os.listdir(TEMPDIRECTORY) if not os.path.isdir(os.path.join(TEMPDIRECTORY, x))]
            [os.remove(os.path.join(TEMPDIRECTORY, 'Ambience', x)) for x in os.listdir(os.path.join(TEMPDIRECTORY, 'Ambience'))]
        except PermissionError: pass


if __name__ == '__main__':
    Kujiin()
