import math

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
from pydub import AudioSegment

from main_const import *




class ExportSession():
    def __init__(self, main, gui, player):
        self.main = main
        self.gui = gui
        self.player = player
        self.exportsession()

    def exportsession(self):
        playing = (self.player.entrainmentObject.state() == Phonon.PlayingState)
        paused = (self.player.entrainmentObject.state() == Phonon.PausedState)
        if playing or paused:
            quit_msg = "Stop The Loaded Session To Export The Session?"
            reply = QtGui.QMessageBox.question(self, 'Confirmation To Stop Session For Export',
                             quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.player.entrainmentObject.stop()
                if self.gui.AmbienceOption.isChecked():
                    self.player.ambienceObject.stop()
                self.gui.statusBar.showMessage("Session Stopped For Export")
        elif not self.main.sessioncreated:
            QtGui.QMessageBox.information(None, "No Session Created",
                                           "A Session Must Be Created In Order To Export",
                                           QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                           QtGui.QMessageBox.NoButton)
        elif self.main.sessioncreated:
            self.finalentrainmentlist = self.main.entrainmentplayer.cutstoplay
            if self.gui.AmbienceOption.isChecked():
                self.finalambiencelist = self.main.ambienceplayer.finalambience
            else:
                self.finalambiencelist = None
            self.totalshittodo = (len(self.main.cutsinsession) + 1)
            self.exportfilename = QtGui.QFileDialog.getSaveFileName(self.gui, "Where Do You Want Me To Export This Session?",
                '', "Music Files (*.mp3);;All Files (*)")
            ExportSessionDialog(self.gui, self.main, self)


class ExportThread(QThread):
    def __init__(self, entrainmentfiles, ambiencefiles, cutsinsession, exportfile):
        QThread.__init__(self)
        self.entrainmentfiles = entrainmentfiles
        self.ambiencefiles = ambiencefiles
        self.exportfile = exportfile
        self.cutsinsession = cutsinsession
        self.finallist = list()
        self.settoexit = False

    def run(self):
        while True:
            totallength = int()
            if self.ambiencefiles is not None: # Ambience And Entrainment
                alertactual = AudioSegment.from_mp3(ALERTFILE)
                alertnotactual = AudioSegment.from_mp3(ALERTSILENCE)
                alertogg = alertactual.overlay(alertnotactual)
                for x, i in enumerate(self.entrainmentfiles):
                    self.emit(SIGNAL("asignal"), self.cutsinsession[x]["name"])
                    nextentrainment = AudioSegment.from_mp3(i)
                    nextambience = AudioSegment.from_mp3(self.ambiencefiles[x])
                    output = nextentrainment.overlay(nextambience)
                    tempoutputname = os.path.join(TEMPDIRECTORY, "Export", str(x) + ".mp3")
                    output.export(tempoutputname, format="mp3")
                    if x == 0:
                        finallist = output
                        finallist += alertogg
                        totallength += len(alertogg)
                    else:
                        finallist += output
                        if i != self.entrainmentfiles[-1]:
                            finallist += alertogg
                            totallength += len(alertogg)
                    totallength += len(output)
                self.emit(SIGNAL("asignal"), True)
                exportfilename = str(self.exportfile)
                finallist.export(exportfilename, format="mp3")
            else: # Entrainment Only
                alertactual = AudioSegment.from_mp3(ALERTFILE)
                alertnotactual = AudioSegment.from_mp3(ALERTSILENCE)
                alertogg = alertactual.overlay(alertnotactual)
                for x, i in enumerate(self.entrainmentfiles):
                    self.emit(SIGNAL("asignal"), self.cutsinsession[x]["name"])
                    if x == 0:
                        nextentrainment = AudioSegment.from_mp3(i)
                        nextentrainment += alertogg
                        #totallength += len(alertogg)
                    else:
                        nextentrainment += AudioSegment.from_mp3(i)
                        if i != self.entrainmentfiles[-1]:
                            nextentrainment += alertogg
                            #totallength += len(alertogg))
                    # self.emit(SIGNAL("asignal"))
                self.emit(SIGNAL("asignal"), True)
                totallength = len(nextentrainment)
                exportfilename = str(self.exportfile)
                nextentrainment.export(exportfilename, format="mp3")
            exportfiled = AudioSegment.from_mp3(exportfilename)
            exportfileminutes = math.trunc((len(exportfiled) / 1000) / 60)
            totallengthminutes = math.trunc((totallength / 1000) / 60)
            if exportfileminutes == totallengthminutes:
                self.emit(SIGNAL("asignal"), False)
                [os.remove(os.path.join(TEMPDIRECTORY, 'Export', x)) for x in os.listdir(os.path.join(TEMPDIRECTORY, 'Export'))]
                break
            else:
                print('The Exported File With Length %s Does Not Match The Totallength Variable With Length %s' %
                      (exportfileminutes, totallengthminutes))
                print("Trying Export Again...")
                continue


class ExportSessionDialog(QDialog):
    def __init__(self, maingui, mainprogram, exporter):
        QDialog.__init__(self, maingui)
        self.percentsessioncreated = int()
        self.totalshittodo = int()
        self.resize(391, 114)
        self.main = mainprogram
        self.main.sessioncreated = False
        self.gui = maingui
        self.progress = int()
        self.exporter = exporter
        self.exportsessionProgressBar = QtGui.QProgressBar(self)
        self.exportsessionProgressBar.setGeometry(QtCore.QRect(20, 40, 361, 23))
        self.exportsessionCancelButton = QtGui.QPushButton(self)
        self.exportsessionCancelButton.setGeometry(QtCore.QRect(300, 70, 84, 30))
        self.topLabel = QtGui.QLabel(self)
        self.topLabel.setGeometry(QtCore.QRect(20, 10, 351, 20))
        self.exportStatusUpdate = QtGui.QLabel(self)
        self.exportStatusUpdate.setGeometry(QtCore.QRect(20, 70, 271, 16))
        self.setWindowTitle("Exporting Session")
        self.topLabel.setText("(This May Take A While)")
        self.exportsessionCancelButton.setText("Cancel")
        self.exportsessionProgressBar.setValue(0)
        QtCore.QObject.connect(self.exportsessionCancelButton, QtCore.SIGNAL("clicked()"), self.cancelsessioncreation)
        QtCore.QObject.connect(self.exportsessionProgressBar, QtCore.SIGNAL("valueChanged(int)"), self.seeifexportdone)
        self.exec_()

    def cancelsessioncreation(self):
        self.close()

    def seeifexportdone(self):
        if self.exportsessionProgressBar.value() == 100:
            self.gui.statusBar.showMessage("Session Exported To: ( %s )" % self.exporter.exportfilename)
            self.accept()

    def callthreads(self):
        self.sessionexporter = ExportThread(self.exporter.finalentrainmentlist,
                                             self.exporter.finalambiencelist,
                                             self.main.cutsinsession,
                                             self.exporter.exportfilename)
        QObject.connect(self.sessionexporter,SIGNAL("asignal"),self.sessionexporterupdates,Qt.QueuedConnection)
        self.sessionexporter.start()
        self.gui.statusBar.showMessage("Exporting Session...")

    def sessionexporterupdates(self, cutname):
        percent = 100 / (self.exporter.totalshittodo + 1)
        self.progress += percent
        self.exportsessionProgressBar.setValue(int(self.progress))
        if isinstance(cutname, str):
            self.exportStatusUpdate.setText("Building %s..." % cutname)
        else:
            if cutname:
                self.exportStatusUpdate.setText("Building Final Session File...")
            else:
                pass
                # Reset To 0
                # Print To Label...An Error Occured, Retrying

    def showEvent(self, QShowEvent):
        self.callthreads()

    def closeEvent(self, QCloseEvent):
        self.sessionexporter.settoexit = True
        self.gui.statusBar.showMessage("Session Exporter Cancelled", 3000)
        self.accept()