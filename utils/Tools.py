def _fromUtf8(s): return s


import math
from shutil import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
from pydub import AudioSegment

from main_const import *


class ProcessAudioFiles(QThread):
    def __init__(self, listofaudiofiles):
        QThread.__init__(self)
        self.listofaudiofiles = listofaudiofiles
        self.currentaudiopath = str()
        self.currentaudioname = str()
        self.currentaudiolengthformatted = str()

    def run(self):
        for x, i in enumerate(self.listofaudiofiles):
            length = getaudiofilelength(i)
            if length is not False:
                self.currentaudiopath = i
                self.currentaudioname = os.path.basename(i)
                self.currentaudiolengthformatted = formatmilliseconds(length)
                # Emit Signal Here


def getaudiofilelength(file):
        try:
            file = os.path.abspath(file)
            if str(file).endswith(".mp3"):
                temp = AudioSegment.from_mp3(file)
                return len(temp)
            elif str(file).endswith(".wav"):
                temp = AudioSegment.from_wav(file)
                return len(temp)
            elif str(file).endswith(".ogg"):
                temp = AudioSegment.from_ogg(file)
                return len(temp)
            else:
                return False
        except Exception:
            return False


def formatmilliseconds(milliseconds):
        seconds = milliseconds/1000
        minutes,seconds = divmod(seconds,60)
        hours,minutes = divmod(minutes,60)
        if hours:
            msg = "%s:%02d:%02d" % (hours, minutes, seconds)
            return msg
        else:
            msg = "%02d:%02d" % (minutes, seconds)
            return msg

class ChangeAlertFile(QDialog):
    def __init__(self, gui, msg=None):
        QDialog.__init__(self, gui)
        self.currentalertfile = ALERTFILE
        self.currentsilence = ALERTSILENCE
        self.newalertfile = str()
        self.newalertsilence = str()
        self.newalertfilename = str()
        self.gui = gui
        # GUI Bindings
        self.resize(458, 184)
        self.changealertfileAlertFileValue = QtGui.QLabel(self)
        self.changealertfileAlertFileValue.setGeometry(QtCore.QRect(10, 70, 441, 21))
        self.changealertfileAlertFileValue.setAlignment(QtCore.Qt.AlignCenter)
        self.changealertfileAlertFileValue.setObjectName(_fromUtf8("changealertfileAlertFileValue"))
        self.changealertfileTopLabel = QtGui.QLabel(self)
        self.changealertfileTopLabel.setGeometry(QtCore.QRect(10, 10, 441, 41))
        self.changealertfileTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changealertfileTopLabel.setWordWrap(True)
        self.changealertfileTopLabel.setObjectName(_fromUtf8("changealertfileTopLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 140, 341, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.changealertfileButtonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.changealertfileButtonLayout.setMargin(0)
        self.changealertfileButtonLayout.setObjectName(_fromUtf8("changealertfileButtonLayout"))
        self.changealertfileChangeButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.changealertfileChangeButton.setObjectName(_fromUtf8("pushButton"))
        self.changealertfileButtonLayout.addWidget(self.changealertfileChangeButton)
        self.changealertfileSelectButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.changealertfileSelectButton.setObjectName(_fromUtf8("changealertfileSelectButton"))
        self.changealertfileButtonLayout.addWidget(self.changealertfileSelectButton)
        self.changealertfileCloseButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.changealertfileCloseButton.setObjectName(_fromUtf8("changealertfileCloseButton"))
        self.changealertfileButtonLayout.addWidget(self.changealertfileCloseButton)
        self.textBrowser = QtGui.QTextBrowser(self)
        if msg is None:
            self.setWindowTitle("Change Alert File")
        else:
            self.setWindowTitle(msg)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 441, 28))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.changealertfileAlertFileValue.setText("New Alert File:")
        self.changealertfileTopLabel.setText("This function will change your alert file (played in between each cut "
                                             "practiced to let you know to change to the next one)")
        self.changealertfileChangeButton.setText("Accept")
        self.changealertfileSelectButton.setText("Open File")
        self.changealertfileCloseButton.setText("Close")
        self.textBrowser.setText("Please Select...")
        QtCore.QObject.connect(self.changealertfileSelectButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.changealertfile)
        QtCore.QObject.connect(self.changealertfileCloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reject)
        QtCore.QObject.connect(self.changealertfileChangeButton, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.commitchanges)
        self.exec_()

    def changealertfile(self):
        """Method To Change Alert File -> Format: New Alert File: /path/to/file.mp3 (x Seconds)"""
        #  Select File Dialog
        self.newalertfilename = QtGui.QFileDialog.getOpenFileName(self, "Select A New File To Use As An Alert File",
                                                                  '', "Music Files (*.mp3);;All Files (*)")
        if self.newalertfilename:
            try:
                self.newalertfile = AudioSegment.from_mp3(self.newalertfilename)
                self.changealertfileChangeButton.setText("Opening...")
                if len(self.newalertfile) > 10000:
                    msg = "The File You Have Selected Is %s Seconds. I Recommend You Keep The Alert File Less Than 10 Seconds. Really Use This File?" % \
                          str(math.floor(len(self.newalertfile) / 1000))
                    reply = QtGui.QMessageBox.question(self, 'Confirmation To Use A Long Alert File',
                                                       msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                    if reply == QtGui.QMessageBox.No:
                        self.newalertfile = str()
                        self.changealertfileChangeButton.setText("Accept")
                        return False
                if len(self.newalertfile) == 0:
                    QMessageBox.information(None, "Alert File Invalid", "This File Has A 0 Length, Please Try Another",
                                            QMessageBox.Ok | QMessageBox.Default,
                                            QMessageBox.NoButton)
                    self.newalertfile = str()
                    self.changealertfileChangeButton.setText("Accept")
                    return False
                self.changealertfileChangeButton.setText("Accept")
                newalertfiletext = "%s (%s Seconds)" % (
                self.newalertfilename, math.floor(len(self.newalertfile) / 1000))
                self.textBrowser.setText(newalertfiletext)
            except:
                QMessageBox.information(None, "Error Opening File",
                                        "I Couldn't Open That File, Is It A Valid .mp3 File?",
                                        QMessageBox.Ok | QMessageBox.Default,
                                        QMessageBox.NoButton)

    def commitchanges(self):
        if isinstance(self.newalertfile, str):
            QMessageBox.information(None, "No Alert File Selected", "Select A New Alert File First",
                                    QMessageBox.Ok | QMessageBox.Default,
                                    QMessageBox.NoButton)
        else:
            msg = "Are You Sure You Want To Use '%s' As The New Alert File? (This Will Erase Whatever Alert File You Had" \
                  " Before)" % self.newalertfilename
            reply = QtGui.QMessageBox.question(self, 'Confirmation To Change Alert File',
                                               msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                #  Move Old Alert File And Alert Silence To Temp (In Case The Export Doesn't Work)
                os.rename(ALERTFILE, os.path.join(TEMPDIRECTORY, "Alert.mp3"))
                os.rename(ALERTSILENCE, os.path.join(TEMPDIRECTORY, "AlertSilence.mp3"))
                #  Write New Alert File And Alert Silence
                try:
                    self.newalertsilence = AudioSegment.silent(len(self.newalertfile))
                    self.newalertsilence.export(ALERTSILENCE, format="mp3")
                    self.newalertfile.export(ALERTFILE, format="mp3")
                    alerttest = AudioSegment.from_mp3(ALERTFILE)
                    alertsilencetest = AudioSegment.from_mp3(ALERTSILENCE)
                    if os.path.exists(ALERTSILENCE) and os.path.exists(ALERTFILE):
                        print("Alert File: %s; Alert Silence: %s" % (len(alerttest), len(alertsilencetest)))
                        if len(alertsilencetest) > 0:
                            os.remove(os.path.join(TEMPDIRECTORY, "Alert.mp3"))
                            os.remove(os.path.join(TEMPDIRECTORY, "AlertSilence.mp3"))
                            self.gui.statusBar.showMessage("Alert File Changed Successfully", 5000)
                            self.accept()
                        else:
                            raise Exception
                    else:
                        raise Exception
                        # Test Files To Make Sure They Are Appropriate Length
                except:
                    # Delete Fucked Up Audio
                    if os.path.exists(ALERTFILE):
                        os.remove(ALERTFILE)
                    if os.path.exists(ALERTSILENCE):
                        os.remove(ALERTSILENCE)
                    os.rename(os.path.join(TEMPDIRECTORY, "Alert.mp3"), ALERTFILE)
                    os.rename(os.path.join(TEMPDIRECTORY, "AlertSilence.mp3"), ALERTSILENCE)
                    QMessageBox.critical(None, "Error", "Changing The Alert File Failed. Is The File You Selected"
                                                        "A Valid .mp3 File?",
                                         QMessageBox.Ok | QMessageBox.Default,
                                         QMessageBox.NoButton)

# TODO Make Processing Audio File(s) A QThread So It Doesn't Hang The Gui
# TODO Make An Option To Pass An Individual Ambience

class AddAmbienceFiles(QDialog):
    def __init__(self, parent, cutname=None):
        QDialog.__init__(self, parent)
        self.resize(734, 478)
        self.optionalcutname = cutname
        self.audioFilesTable = QtGui.QTableWidget(self)
        self.audioFilesTable.setGeometry(QtCore.QRect(50, 70, 631, 291))
        self.audioFilesTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.audioFilesTable.setAutoFillBackground(False)
        self.audioFilesTable.setObjectName(_fromUtf8("audioFilesTable"))
        self.audioFilesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.audioFilesTable.setColumnCount(2)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.audioFilesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.audioFilesTable.setHorizontalHeaderItem(1, item)
        header = self.audioFilesTable.horizontalHeader()
        header.setResizeMode(QHeaderView.Stretch)
        self.addFilesToTableButton = QtGui.QPushButton(self)
        self.addFilesToTableButton.setGeometry(QtCore.QRect(50, 370, 91, 31))
        self.addFilesToTableButton.setObjectName(_fromUtf8("addFilesToTableButton"))
        self.previewButton = QtGui.QPushButton(self)
        self.previewButton.setGeometry(QtCore.QRect(600, 370, 84, 31))
        self.previewButton.setObjectName(_fromUtf8("previewButton"))
        self.topLabel = QtGui.QLabel(self)
        self.topLabel.setGeometry(QtCore.QRect(50, 30, 631, 20))
        self.topLabel.setStyleSheet("font: 12pt Arial Black")
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.addToProgramButton = QtGui.QPushButton(self)
        self.addToProgramButton.setGeometry(QtCore.QRect(520, 440, 111, 31))
        self.addToProgramButton.setObjectName(_fromUtf8("addToProgramButton"))
        self.cancelButton = QtGui.QPushButton(self)
        self.cancelButton.setGeometry(QtCore.QRect(640, 440, 84, 31))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.editCurrentAmbienceButton = QtGui.QPushButton(self)
        self.editCurrentAmbienceButton.setGeometry(QtCore.QRect(10, 440, 141, 31))
        self.editCurrentAmbienceButton.setObjectName(_fromUtf8("editCurrentAmbienceButton"))
        self.previewFileNameLabel = QtGui.QLabel(self)
        self.previewFileNameLabel.setGeometry(QtCore.QRect(300, 380, 251, 20))
        self.previewFileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewFileNameLabel.setObjectName(_fromUtf8("previewFileNameLabel"))
        self.previewcurrentTimeLabel = QtGui.QLabel(self)
        self.previewcurrentTimeLabel.setGeometry(QtCore.QRect(240, 410, 51, 16))
        self.previewcurrentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.previewcurrentTimeLabel.setObjectName(_fromUtf8("previewcurrentTimeLabel"))
        self.previewtotalTimeLabel = QtGui.QLabel(self)
        self.previewtotalTimeLabel.setGeometry(QtCore.QRect(530, 410, 41, 16))
        self.previewtotalTimeLabel.setObjectName(_fromUtf8("previewtotalTimeLabel"))
        self.removefromTableButton = QtGui.QPushButton(self)
        self.removefromTableButton.setGeometry(QtCore.QRect(150, 370, 101, 31))
        self.removefromTableButton.setObjectName(_fromUtf8("pushButton"))
        self.statusBar = QtGui.QLabel(self)
        self.statusBar.setGeometry(QtCore.QRect(170, 450, 331, 16))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBar.setText("Click 'Add File(s)' To Choose Files To Add")
        self.setWindowTitle("Add Ambience To Program")
        item = self.audioFilesTable.horizontalHeaderItem(0)
        item.setText("Name")
        item = self.audioFilesTable.horizontalHeaderItem(1)
        item.setText("Length")
        self.addFilesToTableButton.setText("Open File(s)")
        self.removefromTableButton.setText("Remove File(s)")
        self.previewButton.setText("Preview")
        self.topLabel.setText("Add Ambience Files To The Kuji-In Program")
        self.addToProgramButton.setText("Add To Program")
        self.cancelButton.setText("Cancel")
        self.editCurrentAmbienceButton.setText("Edit Existing Ambience")
        self.previewFileNameLabel.setText("No File Selected")
        self.previewcurrentTimeLabel.setText("--:--")
        self.previewtotalTimeLabel.setText("--:--")
        # PHONON ------
        self.previewOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.previewplayer = Phonon.MediaObject(self)
        self.previewplayer.setTickInterval(1000)
        self.previewplayer.tick.connect(self.playertick)
        Phonon.createPath(self.previewplayer, self.previewOutput)
        self.seekslider = Phonon.SeekSlider(self.previewplayer, self)
        self.seekslider.setGeometry(QtCore.QRect(300, 410, 221, 20))
        self.seekslider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider = Phonon.VolumeSlider(self.previewOutput, self)
        self.volumeSlider.setGeometry(QtCore.QRect(570, 410, 114, 20))
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        # -------------
        QtCore.QObject.connect(self.addToProgramButton, QtCore.SIGNAL("clicked()"), self.addtoprogram)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.reject)
        QtCore.QObject.connect(self.editCurrentAmbienceButton, QtCore.SIGNAL("clicked()"), self.editcurrentambience)
        QtCore.QObject.connect(self.addFilesToTableButton, QtCore.SIGNAL("clicked()"), self.addtotable)
        QtCore.QObject.connect(self.removefromTableButton, QtCore.SIGNAL("clicked()"), self.removefromtable)
        QtCore.QObject.connect(self.previewButton, QtCore.SIGNAL("clicked()"), self.preview)
        QtCore.QObject.connect(self.audioFilesTable, QtCore.SIGNAL("currentItemChanged(QTableWidgetItem*,QTableWidgetItem*)"), self.loadselectedfileforpreview)
        ###
        self.mytableitems = list()
        self.mytablefiles = list()
        self.mytablelengths = list()
        self.index = int()
        self.tableselected = False
        ##
        self.exec_()

    def playertick(self, ticktime):
        """Method To Display Preview Time On Preview Widget"""
        displaytime = QtCore.QTime(0, (ticktime / 60000) % 60, (ticktime / 1000) % 60)
        self.previewcurrentTimeLabel.setText(str(displaytime.toString('mm:ss')))

    def addtoprogram(self):
        """Method To Find Out Which Cuts To Add Ambience In Table To, And Then Copy Those Audio Files There"""
        if len(self.mytableitems) != 0:
            if self.optionalcutname is not None:
                namelist = list()
                namelist.append(self.optionalcutname)
                AddAmbienceConfirmationDialog(self.mytableitems, self.mytableitems, namelist)
            else:
                self.cutstoaddto = ChooseWhichAmbienceDialog(self)
                if self.cutstoaddto.checkednames:
                    AddAmbienceConfirmationDialog(self.mytableitems, self.mytablefiles, self.cutstoaddto.checkednames)
        else:
            QtGui.QMessageBox.information(self, "No Files To Add To Program",
                                           "You Need To Add At Least One Audio File Before I Can Add It The Program",
                                           QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                           QtGui.QMessageBox.NoButton)

    def editcurrentambience(self):
        """Method That Calls EditAmbienceFiles() Below"""
        EditAmbienceFiles(self)

    def addtotable(self):
        """Method To Open A File Chooser (with multi-select) and test if multiple audio files while adding to table"""
        addtotablefilechooser = QFileDialog.getOpenFileNames(self, "Choose Music File(s) To Open", "",
                                                                      "Music Files(*.mp3 *.wav *.ogg);;All Files(*)")
        notworkingfiles = list()
        for x, i in enumerate(addtotablefilechooser):
            self.statusBar.setText("Processing Files (%s/%s). Please Wait..." % (x + 1, len(addtotablefilechooser)))
            QApplication.processEvents()
            length = getaudiofilelength(i)
            if length is not False:
                tablesize = self.audioFilesTable.rowCount()
                self.mytablefiles.append(i)
                self.mytableitems.append(os.path.basename(i))
                self.audioFilesTable.setRowCount(tablesize + 1)
                self.audioFilesTable.setItem(tablesize, 0, QTableWidgetItem(os.path.basename(i)))
                self.mytablelengths.append(formatmilliseconds(length))
                item = QTableWidgetItem(formatmilliseconds(length))
                item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                self.audioFilesTable.setItem(tablesize, 1, item)
            else:
                notworkingfiles.append(i)
        self.statusBar.setText("")

    def removefromtable(self):
        """Method To Remove Selected Ambience File From Table"""
        # TODO Indexes Are Fucked Up, Fix Them Here
        if self.tableselected:
            self.audioFilesTable.removeRow(self.index)
            self.mytablefiles.pop(self.index)
            self.mytablelengths.pop(self.index)
            self.mytableitems.pop(self.index)
            [print("%s: %s" % (i, x)) for i, x in enumerate(self.mytableitems)]
            [print("%s: %s" % (i, x)) for i, x in enumerate(self.mytablelengths)]
            [print("%s: %s" % (i, x)) for i, x in enumerate(self.mytablefiles)]
        else:
            self.statusBar.setText("Select Something To Remove From Table")

    def loadselectedfileforpreview(self, newItem, oldItem):
        """Method To Be Called When A Row Is Selected In The Table, And Passed Into Phonon For Instant Playback"""
        self.tableselected = True
        self.index = self.mytableitems.index(newItem.text())
        print("Current Index Should Be %s" % self.index)
        self.previewplayer.setCurrentSource(Phonon.MediaSource(os.path.abspath(self.mytablefiles[self.index])))
        self.previewFileNameLabel.setText(self.mytableitems[self.index])
        self.previewtotalTimeLabel.setText(self.mytablelengths[self.index])

    def preview(self):
        """Method To Preview Selected Audio File In Table"""
        playing = (self.previewplayer.state() == Phonon.PlayingState)
        if playing:
            self.previewplayer.stop()
            self.previewButton.setText("Preview")
        else:
            self.previewplayer.play()
            self.previewButton.setText("Stop")


class EditAmbienceFiles(QDialog):
    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.resize(664, 736)
        self.loadSelectedCutsAmbienceButton = QtGui.QPushButton(self)
        self.loadSelectedCutsAmbienceButton.setGeometry(QtCore.QRect(220, 40, 101, 31))
        self.loadSelectedCutsAmbienceButton.setObjectName(_fromUtf8("loadSelectedCutsAmbienceButton"))
        self.cutselectorComboBox = QtGui.QComboBox(self)
        self.cutselectorComboBox.setGeometry(QtCore.QRect(60, 40, 151, 29))
        self.cutselectorComboBox.setObjectName(_fromUtf8("cutselectorComboBox"))
        self.topLabel1 = QtGui.QLabel(self)
        self.topLabel1.setGeometry(QtCore.QRect(60, 10, 261, 20))
        self.topLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel1.setObjectName(_fromUtf8("topLabel1"))
        self.topLabel2 = QtGui.QLabel(self)
        self.topLabel2.setGeometry(QtCore.QRect(390, 10, 241, 16))
        self.topLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel2.setObjectName(_fromUtf8("topLabel2"))
        self.currentAmbienceLabel = QtGui.QLabel(self)
        self.currentAmbienceLabel.setGeometry(QtCore.QRect(384, 50, 251, 20))
        self.currentAmbienceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentAmbienceLabel.setObjectName(_fromUtf8("currentAmbienceLabel"))
        self.audioFilesTable = QtGui.QTableWidget(self)
        self.audioFilesTable.setGeometry(QtCore.QRect(20, 120, 621, 481))
        self.audioFilesTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.audioFilesTable.setAutoFillBackground(False)
        self.audioFilesTable.setObjectName(_fromUtf8("audioFilesTable"))
        self.audioFilesTable.setColumnCount(2)
        self.audioFilesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        header = self.audioFilesTable.horizontalHeader()
        header.setResizeMode(QHeaderView.Stretch)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.audioFilesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.audioFilesTable.setHorizontalHeaderItem(1, item)
        self.addAmbienceButton = QtGui.QPushButton(self)
        self.addAmbienceButton.setGeometry(QtCore.QRect(20, 610, 101, 31))
        self.addAmbienceButton.setObjectName(_fromUtf8("addAmbienceButton"))
        self.removeAmbienceButton = QtGui.QPushButton(self)
        self.removeAmbienceButton.setGeometry(QtCore.QRect(130, 610, 111, 31))
        self.removeAmbienceButton.setObjectName(_fromUtf8("removeAmbienceButton"))
        self.previewAmbienceButton = QtGui.QPushButton(self)
        self.previewAmbienceButton.setGeometry(QtCore.QRect(560, 610, 81, 31))
        self.previewAmbienceButton.setObjectName(_fromUtf8("previewAmbienceButton"))
        self.previewFileNameLabel = QtGui.QLabel(self)
        self.previewFileNameLabel.setGeometry(QtCore.QRect(250, 620, 231, 20))
        self.previewFileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewFileNameLabel.setObjectName(_fromUtf8("previewFileNameLabel"))
        self.previewcurrentTimeLabel = QtGui.QLabel(self)
        self.previewcurrentTimeLabel.setGeometry(QtCore.QRect(180, 650, 51, 16))
        self.previewcurrentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.previewcurrentTimeLabel.setObjectName(_fromUtf8("previewcurrentTimeLabel"))
        self.previewtotalTimeLabel = QtGui.QLabel(self)
        self.previewtotalTimeLabel.setGeometry(QtCore.QRect(500, 650, 41, 16))
        self.previewtotalTimeLabel.setObjectName(_fromUtf8("previewtotalTimeLabel"))
        self.topLabel3 = QtGui.QLabel(self)
        self.topLabel3.setGeometry(QtCore.QRect(24, 90, 611, 20))
        self.topLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel3.setObjectName(_fromUtf8("topLabel3"))
        self.closeButton = QtGui.QPushButton(self)
        self.closeButton.setGeometry(QtCore.QRect(570, 700, 84, 31))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.statusBar = QtGui.QLabel(self)
        self.statusBar.setGeometry(QtCore.QRect(10, 710, 541, 16))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.setWindowTitle("Edit Ambience")
        self.loadSelectedCutsAmbienceButton.setText("Load Ambience")
        self.topLabel1.setText("Select Cut To Edit Ambience")
        self.topLabel2.setText("Currently Editing:")
        self.currentAmbienceLabel.setText("Select A Cut's Ambience To Edit")
        item = self.audioFilesTable.horizontalHeaderItem(0)
        item.setText("Name")
        item = self.audioFilesTable.horizontalHeaderItem(1)
        item.setText("Length")
        self.addAmbienceButton.setText("Add Ambience")
        self.removeAmbienceButton.setText("Remove Selected")
        self.previewAmbienceButton.setText("Preview")
        self.previewFileNameLabel.setText("No File Selected")
        self.previewcurrentTimeLabel.setText("--:--")
        self.previewtotalTimeLabel.setText("--:--")
        self.topLabel3.setText("NOTE: These Changes Cannot Be Undone")
        self.closeButton.setText("Close")
        # PHONON
        self.previewOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.previewplayer = Phonon.MediaObject(self)
        self.previewplayer.setTickInterval(1000)
        self.previewplayer.tick.connect(self.playertick)
        Phonon.createPath(self.previewplayer, self.previewOutput)
        self.seekslider = Phonon.SeekSlider(self.previewplayer, self)
        self.seekslider.setGeometry(QtCore.QRect(240, 650, 251, 20))
        self.seekslider.setOrientation(QtCore.Qt.Horizontal)
        self.seekslider.setObjectName(_fromUtf8("previewSlider"))
        self.volumeSlider = Phonon.VolumeSlider(self.previewOutput, self)
        self.volumeSlider.setGeometry(QtCore.QRect(530, 650, 113, 20))
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        # -----------------
        self.cutlist = [
            "Presession", "Rin", "Kyo", "Toh", "Sha", "Kai", "Jin", "Retsu",
            "Zai", "Zen", "Postsession", "General"
        ]
        self.filenames = list()
        self.filepaths = list()
        self.filelengths = list()
        # -----------------
        self.cutselectorComboBox.addItems(self.cutlist)
        # Populate cutselectorComboBox here
        QtCore.QObject.connect(self.loadSelectedCutsAmbienceButton, QtCore.SIGNAL("clicked()"), self.loadcutsambience)
        QtCore.QObject.connect(self.addAmbienceButton, QtCore.SIGNAL("clicked()"), self.addambience)
        QtCore.QObject.connect(self.audioFilesTable, QtCore.SIGNAL("currentItemChanged(QTableWidgetItem*,QTableWidgetItem*)"), self.loadselectedfileforpreview)
        QtCore.QObject.connect(self.previewAmbienceButton, QtCore.SIGNAL("clicked()"), self.previewambience)
        QtCore.QObject.connect(self.removeAmbienceButton, QtCore.SIGNAL("clicked()"), self.removeambience)
        # QtCore.QObject.connect(self.previewButton, QtCore.SIGNAL("clicked()"), self.preview)
        self.exec_()

    def loadselectedfileforpreview(self, newItem, oldItem):
        """Method To Be Called When A Row Is Selected In The Table, And Passed Into Phonon For Instant Playback"""
        if newItem is not None:
            self.tableselected = True
            try:
                self.index = self.filenames.index(newItem.text())
            except ValueError:
                self.index = self.filelengths.index(newItem.text())
            self.previewcurrentTimeLabel.setText("00:00")
            self.previewplayer.setCurrentSource(Phonon.MediaSource(os.path.abspath(self.filepaths[self.index])))
            self.previewFileNameLabel.setText(self.filenames[self.index])
            self.previewtotalTimeLabel.setText(self.filelengths[self.index])

    def playertick(self, ticktime):
        """Method To Display Preview Time On Preview Widget"""
        displaytime = QtCore.QTime(0, (ticktime / 60000) % 60, (ticktime / 1000) % 60)
        self.previewcurrentTimeLabel.setText(str(displaytime.toString('mm:ss')))

    def loadcutsambience(self):
        """Method To Get A Cut From cutselectorComboBox, And Retrieve And Populate The Table With Ambience From That
        Folder"""
        self.filenames.clear()
        self.filepaths.clear()
        self.filelengths.clear()
        self.audioFilesTable.clearContents()
        self.audioFilesTable.setRowCount(0)
        name = self.cutselectorComboBox.currentText()
        if name in self.cutlist:
            self.currentAmbienceLabel.setText("%s" % name)
            notworkingfiles = list()
            listoffiles = os.listdir(os.path.join(AMBIENCEDIRECTORY, name))
            if len(listoffiles) > 0:
                for x, i in enumerate(listoffiles):
                    i = os.path.join(AMBIENCEDIRECTORY, name, i)
                    self.statusBar.setText("Processing Files (%s/%s). Please Wait..." % (x + 1, len(listoffiles)))
                    QApplication.processEvents()
                    length = getaudiofilelength(i)
                    if length is not False:
                        tablesize = self.audioFilesTable.rowCount()
                        self.filepaths.append(i)
                        self.filenames.append(os.path.basename(i))
                        self.audioFilesTable.setRowCount(tablesize + 1)
                        self.audioFilesTable.setItem(tablesize, 0, QTableWidgetItem(os.path.basename(i)))
                        self.filelengths.append(formatmilliseconds(length))
                        item = QTableWidgetItem(formatmilliseconds(length))
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
                        self.audioFilesTable.setItem(tablesize, 1, item)
                    else:
                        print("%s Didn't Work" % i)
                        notworkingfiles.append(i)
            else:
                quit_msg = "No Ambience Files Found! Add Ambience To %s" % name
                reply = QtGui.QMessageBox.question(self.gui, 'Add Ambience?',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    self.addambience()
                else:
                    return
            self.statusBar.setText("")
        else:
            self.statusBar.setText("Not A Valid Option. Check Your Selection At The Top Left")

    def addambience(self):
        """Method To Call The Add Ambience Dialog Written Above"""
        AddAmbienceFiles(self)
        self.loadcutsambience()

    def removeambience(self):
        """Method To Get The Index And Remove The Ambience From The Table, And Delete It From Disk! Make Sure There
        Is A Confirmation Dialog Before You Delete From Disk"""
        index = self.filenames.index(self.previewFileNameLabel.text())
        name = self.filenames[index]
        msg = "Really Delete '%s'?(This Cannot Be Undone)" % name
        reply = QtGui.QMessageBox.question(self, 'Really Delete This File?',
                                     msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QMessageBox.Yes:
            path = self.filepaths[index]
            os.remove(path)
            a = self.filenames.pop(index)
            b = self.filepaths.pop(index)
            c = self.filelengths.pop(index)
            print("Removed From Lists %s|%s|%s" % (a, b, c))
            self.audioFilesTable.removeRow(index)
            if not os.path.exists(path):
                self.statusBar.setText("%s Successfully Deleted" % name)
            else:
                self.statusBar.setText("An Error Occured Trying To Delete %s" % name)

    def previewambience(self):
        """Method To Preview The Selected Ambience In Table"""
        playing = (self.previewplayer.state() == Phonon.PlayingState)
        if playing:
            self.previewplayer.stop()
            self.previewAmbienceButton.setText("Preview")
        else:
            self.previewplayer.play()
            self.previewAmbienceButton.setText("Stop")

class ChooseWhichAmbienceDialog(QDialog):
    def __init__(self, parent, msg="Select Cut(s)"):
        QDialog.__init__(self, parent)
        self.resize(627, 139)
        self.generalcheckbox = QtGui.QCheckBox(self)
        self.generalcheckbox.setGeometry(QtCore.QRect(450, 70, 171, 20))
        self.generalcheckbox.setObjectName(_fromUtf8("generalcheckbox"))
        self.descriptionLabel = QtGui.QLabel(self)
        self.descriptionLabel.setGeometry(QtCore.QRect(10, 0, 611, 31))
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.OKButton = QtGui.QPushButton(self)
        self.OKButton.setGeometry(QtCore.QRect(450, 100, 84, 31))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.cancelButton = QtGui.QPushButton(self)
        self.cancelButton.setGeometry(QtCore.QRect(540, 100, 84, 31))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 611, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.presession = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.presession.setObjectName(_fromUtf8("presession"))
        self.horizontalLayout.addWidget(self.presession)
        self.rin = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.rin.setObjectName(_fromUtf8("rin"))
        self.horizontalLayout.addWidget(self.rin)
        self.kyo = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.kyo.setObjectName(_fromUtf8("kyo"))
        self.horizontalLayout.addWidget(self.kyo)
        self.toh = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.toh.setObjectName(_fromUtf8("toh"))
        self.horizontalLayout.addWidget(self.toh)
        self.sha = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.sha.setObjectName(_fromUtf8("sha"))
        self.horizontalLayout.addWidget(self.sha)
        self.kai = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.kai.setObjectName(_fromUtf8("kai"))
        self.horizontalLayout.addWidget(self.kai)
        self.jin = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.jin.setObjectName(_fromUtf8("jin"))
        self.horizontalLayout.addWidget(self.jin)
        self.retsu = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.retsu.setObjectName(_fromUtf8("retsu"))
        self.horizontalLayout.addWidget(self.retsu)
        self.zai = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.zai.setObjectName(_fromUtf8("zai"))
        self.horizontalLayout.addWidget(self.zai)
        self.zen = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.zen.setObjectName(_fromUtf8("zen"))
        self.horizontalLayout.addWidget(self.zen)
        self.postsession = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.postsession.setObjectName(_fromUtf8("postsession"))
        self.horizontalLayout.addWidget(self.postsession)
        ########
        self.setWindowTitle(msg)
        self.generalcheckbox.setText("General (Unspecific Ambience)")
        self.presession.setText("Pre-session")
        self.rin.setText("Rin")
        self.kyo.setText("Kyo")
        self.toh.setText("Toh")
        self.sha.setText("Sha")
        self.kai.setText("Kai")
        self.jin.setText("Jin")
        self.retsu.setText("Retsu")
        self.zai.setText("Zai")
        self.zen.setText("Zen")
        self.postsession.setText("Post-Session")
        self.descriptionLabel.setText("Please Select Which Cut(s) You Would Like To Add Ambience To:")
        self.OKButton.setText("OK")
        self.cancelButton.setText("Cancel")
        self.checkboxes = [
            self.presession,
            self.rin,
            self.kyo,
            self.toh,
            self.sha,
            self.kai,
            self.jin,
            self.retsu,
            self.zai,
            self.zen,
            self.postsession,
            self.generalcheckbox
        ]
        self.names = [
            "Presession",
            "Rin",
            "Kyo",
            "Toh",
            "Sha",
            "Kai",
            "Jin",
            "Retsu",
            "Zai",
            "Zen",
            "Postsession",
            "General"
        ]
        self.checkednames = list()
        QtCore.QObject.connect(self.OKButton, QtCore.SIGNAL("clicked()"), self.accept)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.reject)
        ret = self.exec_()
        if ret == QDialog.Accepted:
            for x, i in enumerate(self.checkboxes):
                if i.isChecked():
                    self.checkednames.append(self.names[x])

class ModifyReferenceFiles(QDialog):
    def __init__(self):
        QDialog.__init__(self)


class AddAmbienceConfirmationDialog(QDialog):
    def __init__(self, filenames, filepaths, cutnames):
        QDialog.__init__(self)
        self.filenames = filenames
        self.filepaths = filepaths
        self.cutnames = cutnames
        self.resize(593, 398)
        self.setStyleSheet(_fromUtf8("background-color:#212526;"))
        self.filesListView = QtGui.QListWidget(self)
        self.filesListView.setGeometry(QtCore.QRect(20, 70, 261, 261))
        self.filesListView.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(42, 52, 53);"))
        self.filesListView.setObjectName(_fromUtf8("filesListView"))
        self.horizontalLayoutWidget = QtGui.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(340, 350, 231, 33))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.buttonsLayou = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonsLayou.setMargin(0)
        self.buttonsLayou.setObjectName(_fromUtf8("buttonsLayou"))
        self.acceptButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.acceptButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.buttonsLayou.addWidget(self.acceptButton)
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.buttonsLayou.addWidget(self.cancelButton)
        self.topLabel = QtGui.QLabel(self)
        self.topLabel.setGeometry(QtCore.QRect(50, 10, 481, 20))
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.statusBar = QtGui.QLabel(self)
        self.statusBar.setGeometry(QtCore.QRect(20, 360, 291, 16))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.filestopLabel = QtGui.QLabel(self)
        self.filestopLabel.setGeometry(QtCore.QRect(24, 40, 261, 20))
        self.filestopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filestopLabel.setObjectName(_fromUtf8("filestopLabel"))
        self.cutsListView = QtGui.QListWidget(self)
        self.cutsListView.setGeometry(QtCore.QRect(310, 70, 261, 261))
        self.cutsListView.setStyleSheet(_fromUtf8("color: #98A6A8; background-color: rgb(42, 52, 53);"))
        self.cutsListView.setObjectName(_fromUtf8("cutsListView"))
        self.ambiencetopLabel = QtGui.QLabel(self)
        self.ambiencetopLabel.setGeometry(QtCore.QRect(310, 40, 261, 20))
        self.ambiencetopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ambiencetopLabel.setObjectName(_fromUtf8("ambiencetopLabel"))
        self.setWindowTitle("Confirmation")
        self.acceptButton.setText("Accept")
        self.cancelButton.setText("Cancel")
        self.topLabel.setText("NOTE: This Can\'t Be Undone")
        self.statusBar.setText("")
        self.filestopLabel.setText("Add These File(s)")
        self.ambiencetopLabel.setText("As Ambience To These Cut(s)")
        for i in self.filenames:
            msg = str(i)
            item = QListWidgetItem(msg)
            self.filesListView.addItem(item)
        for x in self.cutnames:
            msg = str(x)
            item = QListWidgetItem(msg)
            self.cutsListView.addItem(item)
        QtCore.QObject.connect(self.acceptButton, QtCore.SIGNAL("clicked()"), self.addfiles)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL("clicked()"), self.cancel)
        self.exec_()

    def cancel(self):
        """Method To Close Out Dialog And Return To Cut Selection Dialog"""
        self.reject()

    def addfiles(self):
        """Method To Add Ambience Files To Each Cut Folder Corresponding To cutnames"""
        for x, i in enumerate(self.cutnames):
            count = 1
            for h, g in enumerate(self.filepaths):
                newdirectory = os.path.abspath(os.path.join(AMBIENCEDIRECTORY, i, self.filenames[h]))
                olddirectory = g
                copy2(olddirectory, newdirectory)
                self.statusBar.setText("Processing (%s/%s). Please Wait..." % (count, int(self.cutnames * self.filepaths)))
                count += 1
        self.accept()


    def checkreferencefile(self, referencevariation, file):
        if isinstance(referencevariation, str):
            filedirectory = referencevariation
            filesexist = int()
            for i in os.listdir(filedirectory):
                filetocheck = os.path.join(filedirectory, i)
                fileisgood = self.checkifreferencefilegood(filetocheck)
                if fileisgood:
                    filesexist += 1
                else:
                    print("This Isn't Good: " + filetocheck)
            if filesexist == len(os.listdir(filedirectory)): ## All Files Have At Least 3 Lines With Working Characters
                return True
            elif filesexist > 0: ## Some Files Have At Least 3 Lines With Working Characters
                quit_msg = "Some Reference Files Have ContentF And Some Don't. Do You Want Me To Add The Reference" \
                           " Files That Have Content (The Ones That Don't Will Be Displayed Blank)?"
                reply = QtGui.QMessageBox.question(self.gui, 'Add Partial Reference Files To Session',
                                                   quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.Yes:
                    return True
                else:
                    return False
            else: ## No Files Have 3 Lines With Working Characters
                return False