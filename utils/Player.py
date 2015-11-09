def _fromUtf8(s): return s


import math

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

from main_const import *


class SessionPlayer(object):
    def __init__(self, mainprogram, sessiondb):
        self.main = mainprogram
        self.gui = self.main.gui
        self.sessiondb = sessiondb
        self.entrainmentOutput = Phonon.AudioOutput(Phonon.MusicCategory, self.gui)
        self.ambienceOutput = Phonon.AudioOutput(Phonon.MusicCategory, self.gui)
        self.entrainmentObject = Phonon.MediaObject(self.gui)
        self.ambienceObject = Phonon.MediaObject(self.gui)
        self.gui.AmbienceVolumeSlider.setAudioOutput(self.ambienceOutput)
        self.gui.EntrainmentVolumeSlider.setAudioOutput(self.entrainmentOutput)
        self.entrainmentObject.setTickInterval(1000)
        self.entrainmentObject.currentSourceChanged.connect(self.sourceChanged)
        self.entrainmentObject.finished.connect(self.setnextfile)
        self.entrainmentObject.tick.connect(self.tick)
        self.sessiongenerator = None
        self.cutplayingname = None
        self.totalsessiondurationformatted = str()
        self.totalsessionseconds = int()
        Phonon.createPath(self.entrainmentObject, self.entrainmentOutput)
        Phonon.createPath(self.ambienceObject, self.ambienceOutput)

    def checktime(self, ticktime):
        listtocheck = self.cutplayingduration.split(":")
        currentminutes = math.floor((ticktime / 1000) / 60)
        currenthours = math.floor(((ticktime / 1000) / 60) / 60)
        if currenthours >= int(listtocheck[0]) and currentminutes >= int(listtocheck[1]):
            return True
        else:
            return False

    def tick(self, ticktime):
        if isinstance(self.cutplayingname, str):
            if self.cutplayingname != "Alert":
                if ticktime != 0:
                    displaytime = QtCore.QTime(0, (ticktime / 60000) % 60, (ticktime / 1000) % 60)
                    done = self.checktime(ticktime)
                    if not done: # NOT DONE
                        self.gui.statusBar.showMessage("")
                        self.totalsessionseconds += 1
                        currenttotaltime = self.secondstohoursminutesandseconds(self.totalsessionseconds)
                        self.gui.CutPlayingName.setText(self.cutplayingname)
                        self.gui.CutPlayingProgressActual.setText("%s > %s" %
                                                                  (str(displaytime.toString('hh:mm:ss')),
                                                                   self.cutplayingduration))
                        self.gui.thiscutprogressDescriptionLabel.setText("%s Progress:" % self.cutplayingname)
                        self.gui.TotalSessionPlayingProgressActual.setText("%s > %s" %
                                                                           (currenttotaltime,
                                                                            self.totalsessiondurationformatted))
                        self.gui.statusBar.showMessage("Session Is Playing. Now Playing %s..." % self.cutplayingname)
                    else: # DONE
                        testlist = self.cutplayingduration.split(":")
                        hours = math.floor(((ticktime / 1000) / 60) / 60)
                        minutes = math.floor((ticktime / 1000) / 60)
                        if not hours > int(testlist[0]) and not minutes > int(testlist[1]):
                            self.totalsessionseconds += 1
                        msg = self.cutplayingname + " Completed!"
                        self.gui.CutPlayingName.setText(msg)
                        self.gui.CutPlayingProgressActual.setText(msg)
                        # self.gui.statusBar.showMessage(msg)
            else:
                nextcutname = self.cutsinsession[self.index + 1]["name"]
                msg = "Get Ready For %s" % nextcutname
                currenttotaltime = self.secondstohoursminutesandseconds(self.totalsessionseconds)
                # %s Completed!
                self.gui.thiscutprogressDescriptionLabel.setText("Progress:")
                self.gui.CutPlayingProgressActual.setText(msg)
                self.gui.TotalSessionPlayingProgressActual.setText("(%s) -> (%s)" % (currenttotaltime, self.totalsessiondurationformatted))
                self.gui.statusBar.showMessage(msg)
                self.gui.CutPlayingName.setText(msg)
                self.gui.statusBar.showMessage("Session Is Playing. Get Ready To Work On %s" % nextcutname)

    def playsession(self, cutsinsession, entrainmentplayer, ambienceplayer=None):
        """ Session Player """
        self.sessiongenerator = self.sessioncutgenerator()
        self.cutsinsession = cutsinsession
        playing = (self.entrainmentObject.state() == Phonon.PlayingState)
        paused = (self.entrainmentObject.state() == Phonon.PausedState)
        if playing:
            self.gui.statusBar.showMessage("Already Playing Session", 3000)
        elif paused:
            self.entrainmentObject.play()
            if self.gui.AmbienceOption.isChecked():
                self.ambienceObject.play()
        else:
            self.calculatetotalsessiontime()
            self.gui.statusBar.showMessage("Preparing Session For Playback...")
            if self.main.sessioncreated is True:
                self.gui.statusBar.showMessage("Preparing Session For Playback...")
                self.finalentrainmentlist = entrainmentplayer.cutstoplay
                if self.gui.AmbienceOption.isChecked():
                    self.finalambiencelist = ambienceplayer.finalambience
                self.sessiondb.createnewsession()
                mylist = list()
                for w, p in enumerate(self.cutsinsession):
                    mylist.append(p)
                    if w != (len(self.cutsinsession) - 1):
                        mylist.append(self.main.alert)
                self.cutsinsession = mylist
                self.gui.statusBar.showMessage("Preparing Session To Be Played..")
                newentrainmentlist = list()
                for x, i in enumerate(self.finalentrainmentlist):
                    newentrainmentlist.append(i)
                    if i != self.finalentrainmentlist[-1]:
                        newentrainmentlist.append(ALERTFILE)
                self.entrainmentlisttoplay = newentrainmentlist
                if self.gui.AmbienceOption.isChecked():
                    newambiencelist = list()
                    for x, i in enumerate(self.finalambiencelist):
                        newambiencelist.append(i)
                        if i != self.finalambiencelist[-1]:
                            newambiencelist.append(ALERTSILENCE)
                    self.ambiencelisttoplay = newambiencelist
                else:
                    self.ambiencelisttoplay = None
                self.entrainmentObject.setCurrentSource(Phonon.MediaSource(self.entrainmentlisttoplay[0]))
                self.gui.statusBar.showMessage("Starting Session Playback...")
                if self.ambiencelisttoplay:
                    self.ambienceObject.setCurrentSource(Phonon.MediaSource(self.ambiencelisttoplay[0]))
                    self.sessionambiencegenerator = self.ambiencesoundgenerator()
                    self.ambienceObject.play()
                self.sessionentrainmentgenerator = self.entrainmentsoundgenerator()
                self.entrainmentObject.play()
                self.gui.OpenThisCutsReferenceFilesButton.setText("%s's Reference File" % self.cutplayingname)
                QtCore.QObject.connect(self.gui.OpenThisCutsReferenceFilesButton, QtCore.SIGNAL("clicked()"),
                                           self.displayreferencefile)
            else:
                self.gui.statusBar.showMessage("No Session Created")

    def displayreferencefile(self):
        if isinstance(self.cutplayingname, str):
            self.main.sessionreference.openreferencefile(self.cutplayingname)

    def pausesession(self):
        playing = (self.entrainmentObject.state() == Phonon.PlayingState)
        paused = (self.entrainmentObject.state() == Phonon.PausedState)
        if playing:
            self.entrainmentObject.pause()
            if self.gui.AmbienceOption.isChecked():
                self.ambienceObject.pause()
                self.gui.statusBar.showMessage("Session Paused")
        elif paused:
            self.gui.statusBar.showMessage("Session Already Paused", 3000)
        else:
            QtGui.QMessageBox.information(None, "No Session Playing",
                                           "A Session Must Be Playing In Order To Pause",
                                           QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                           QtGui.QMessageBox.NoButton)

    def stopsession(self):
        playing = (self.entrainmentObject.state() == Phonon.PlayingState)
        paused = (self.entrainmentObject.state() == Phonon.PausedState)
        if playing or paused:
            msg = "Really Stop Session? If You Stop, This Session Cannot Be Resumed, Only Restarted"
            reply = QtGui.QMessageBox.question(self.gui, 'Stop Session?',
                                                       msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                self.entrainmentObject.stop()
                if self.gui.AmbienceOption.isChecked():
                    self.ambienceObject.stop()
                    self.gui.statusBar.showMessage("Session Stopped")
            # TODO Reset The Player GUI Here
        else:
            QtGui.QMessageBox.information(None, "No Session Playing",
                                           "A Session Must Be Playing Or Paused In Order To Stop",
                                           QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                                           QtGui.QMessageBox.NoButton)

    def ambiencesoundgenerator(self):
        """Generator To Yield Ambience Sound Files Individually"""
        for e, x in enumerate(self.ambiencelisttoplay):
            if e > 0:
                yield Phonon.MediaSource(x)

    def entrainmentsoundgenerator(self):
        """Generator To Yield Entrainment Sound Files Individually"""
        for s, f in enumerate(self.entrainmentlisttoplay):
            if s > 0:
                yield Phonon.MediaSource(f)

    @staticmethod
    def secondstohoursminutesandseconds(totalseconds):
        hours = 0
        minutes = 0
        if totalseconds >= 3600:
            hours = int(totalseconds / 3600)
            totalseconds -= 3600 * hours
        if totalseconds >= 60:
            minutes = int(totalseconds / 60)
            totalseconds -= minutes * 60
        formattedstring = "%02d:%02d:%02d" % (hours, minutes, totalseconds)
        return formattedstring

    def setnextfile(self):
        """Method To Set Phonon Source To The Next File(s) In The Session"""
        try:
            self.entrainmentObject.setCurrentSource(next(self.sessionentrainmentgenerator))
            if self.ambiencelisttoplay:
                self.ambienceObject.setCurrentSource(next(self.sessionambiencegenerator))
                self.ambienceObject.play()
            self.entrainmentObject.play()
        except StopIteration:
            self.entrainmentObject.clear()
            if self.ambiencelisttoplay:
                self.ambienceObject.clear()
            self.endofsession()

    def calculatetotalsessiontime(self):
        fileduration = 0
        for x, i in enumerate(self.cutsinsession):
            if i["name"] != "Alert":
                if i["name"] in ["Presession", "Postsession"]:
                    fileduration += int(i["ramp"])
                fileduration += int(i["duration"])
        hours = int(fileduration / 60)
        minutes = fileduration % 60
        self.totalsessiondurationformatted = "%02d:%02d:00" % (hours, minutes)

    @staticmethod
    def calculatesessiontime(cut):
        if cut["name"] != "Alert":
            fileduration = int()
            hours = 0
            if cut["name"] in ["Presession", "Postsession"]:
                    fileduration += int(cut["ramp"])
            fileduration += int(cut["duration"])
            if fileduration >= 60:
                hours = int(fileduration / 60)
                fileduration -= hours * 60
            formattedduration = "%02d:%02d:00" % (hours, fileduration)
            return formattedduration

    def endofsession(self):
        """Method To End Session"""
        if self.gui.ReferenceDisplayOption.isChecked():
            self.cutdialog.close()
        self.sessiondb.checkifcompleted()
        self.gui.setgoalstatus()
        self.gui.statusBar.showMessage("Session Finished Playing")
        self.sessioncompletedDialog = QDialog(self.gui)
        self.sessioncompletedDialog.resize(391, 142)
        self.sessioncompletedtopLabel = QtGui.QLabel(self.sessioncompletedDialog)
        self.sessioncompletedtopLabel.setGeometry(QtCore.QRect(30, 10, 331, 20))
        self.sessioncompletedtopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sessioncompletedTotalTimeCompletedLabel = QtGui.QLabel(self.sessioncompletedDialog)
        self.sessioncompletedTotalTimeCompletedLabel.setGeometry(QtCore.QRect(30, 40, 331, 20))
        self.sessioncompletedTotalTimeCompletedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sessioncompletedexportQuestionLabel = QtGui.QLabel(self.sessioncompletedDialog)
        self.sessioncompletedexportQuestionLabel.setGeometry(QtCore.QRect(30, 70, 331, 20))
        self.sessioncompletedexportQuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayoutWidget = QtGui.QWidget(self.sessioncompletedDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 100, 168, 41))
        self.sessioncompletebuttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.sessioncompletebuttonLayout.setMargin(0)
        self.sessioncompleteExportYesButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.sessioncompletebuttonLayout.addWidget(self.sessioncompleteExportYesButton)
        self.sessioncompleteExportNoButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.sessioncompletebuttonLayout.addWidget(self.sessioncompleteExportNoButton)
        self.sessioncompletedDialog.setWindowTitle("Session Complete")
        self.sessioncompletedtopLabel.setText("Your Session Has Been Successfully Completed! Great Work!")
        hours, mins = self.main.sessiondb.calculatetotalhoursandminutes()
        self.sessioncompletedTotalTimeCompletedLabel.setText("You Have Now Completed %d Hours And %d Minutes " % (hours, mins))
        self.sessioncompletedexportQuestionLabel.setText("Would You Like To Keep (Export) This Session For Later Use? ")
        self.sessioncompleteExportYesButton.setText("YES")
        self.sessioncompleteExportNoButton.setText("NO")
        QtCore.QObject.connect(self.sessioncompleteExportYesButton, QtCore.SIGNAL("clicked()"), self.sessioncompletedDialog.accept)
        QtCore.QObject.connect(self.sessioncompleteExportNoButton, QtCore.SIGNAL("clicked()"), self.sessioncompletedDialog.reject)
        ret = self.sessioncompletedDialog.exec_()
        if ret == QDialog.Accepted:
            self.main.exportsession()
        else:
            return True

    def sessionplaybacktipsmethod(self):
        self.sessionplaybacktips = QDialog(self.gui)
        self.sessionplaybacktips.resize(585, 420)
        self.textBrowser = QtGui.QTextBrowser(self.sessionplaybacktips)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 561, 341))
        self.pushButton = QtGui.QPushButton(self.sessionplaybacktips)
        self.pushButton.setGeometry(QtCore.QRect(450, 390, 121, 23))
        self.label = QtGui.QLabel(self.sessionplaybacktips)
        self.label.setGeometry(QtCore.QRect(22, 10, 501, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.sessionplaybacktips.setWindowTitle("Session Playback Tips")
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Use Headphones! The Higher The Quality Of The Audio Source, The More Effective The Brainwave Entrainment Will Be. If You Have Them, Use Noise Isolating Or Noise Cancelling Headphones, For Better Isolation From The World For The Length Of The Session</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Remove Any And All Distractions For Your Selected Session Length. (I Ask My Roomates To Please Not Disturb Me For My Session Length)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Play Session In A Darker Room (I Find Light Changes Or Alot Of Light Distracting To Me Especially In Long And Very Long Sessions)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If Displaying Reference Files:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - Set The Screen Level As Dim As You Can Comfortably See In A Dark Room</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - Set The Screen To Not Turn Off</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - Set Computer Sleep To \'Never\' So The Computer Won\'t Go To Sleep During The Session Interrupting You</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If Not Displaying Reference Files:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - Set The Screen To Turn Off After 1-2 Minutes (The Program Will Still Run In The Background)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   - Set Computer Sleep To \'Never\' So The Computer Won\'t Go To Sleep During The Session Interrupting You</p></body></html>")
        self.pushButton.setText("Begin Session")
        self.label.setText("TIPS FOR SESSION PLAYBACK")
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.sessionplaybacktips.accept)
        ret = self.sessionplaybacktips.exec_()
        if ret == QDialog.Accepted:
            return True
        else:
            self.gui.statusBar.showMessage("Session Playback Cancelled")
            return False

    def sessioncutgenerator(self):
        for x, i in enumerate(self.cutsinsession):
            yield i, x

    def sourceChanged(self):
        try:
            self.cutplaying, self.index = next(self.sessiongenerator)
            self.cutplayingname = self.cutplaying["name"]
            self.cutplayingduration = self.calculatesessiontime(self.cutplaying)
            if self.main.sessionreference.automaticallyopen:
                if self.cutplayingname != "Alert":
                    if self.main.sessionreference.variation is not None:
                        self.main.sessionreference.openreferencefile(self.cutplayingname)
                else:
                    self.sessiondb.update(self.cutsinsession[self.index - 1])
                    self.main.sessionreference.closereferencefile()
            else:
                self.main.sessionreference.closereferencefile()
                if self.cutplayingname == "Alert":
                    self.sessiondb.update(self.cutsinsession[self.index - 1])
        except StopIteration:
            pass