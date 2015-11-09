# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designerstyled.ui'
#
# Created: Thu Dec  4 15:14:28 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1300, 771)
        MainWindow.setStyleSheet(_fromUtf8("background-color:#212526;\n"
""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1301, 731))
        self.frame.setStyleSheet(_fromUtf8("background-color:#212526;\n"
""))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 80, 691, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.DurationLabels_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.DurationLabels_2.setMargin(0)
        self.DurationLabels_2.setObjectName(_fromUtf8("DurationLabels_2"))
        self.preLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.preLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-right: 1px solid black;\n"
"border-left: 1px solid black;"))
        self.preLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.preLabel_2.setObjectName(_fromUtf8("preLabel_2"))
        self.DurationLabels_2.addWidget(self.preLabel_2)
        self.rinLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.rinLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.rinLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.rinLabel_2.setObjectName(_fromUtf8("rinLabel_2"))
        self.DurationLabels_2.addWidget(self.rinLabel_2)
        self.kyoLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.kyoLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.kyoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.kyoLabel_2.setObjectName(_fromUtf8("kyoLabel_2"))
        self.DurationLabels_2.addWidget(self.kyoLabel_2)
        self.tohLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.tohLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.tohLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tohLabel_2.setObjectName(_fromUtf8("tohLabel_2"))
        self.DurationLabels_2.addWidget(self.tohLabel_2)
        self.shaLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.shaLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.shaLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.shaLabel_2.setObjectName(_fromUtf8("shaLabel_2"))
        self.DurationLabels_2.addWidget(self.shaLabel_2)
        self.kaiLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.kaiLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.kaiLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.kaiLabel_2.setObjectName(_fromUtf8("kaiLabel_2"))
        self.DurationLabels_2.addWidget(self.kaiLabel_2)
        self.jinLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.jinLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.jinLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.jinLabel_2.setObjectName(_fromUtf8("jinLabel_2"))
        self.DurationLabels_2.addWidget(self.jinLabel_2)
        self.retsuLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.retsuLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.retsuLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.retsuLabel_2.setObjectName(_fromUtf8("retsuLabel_2"))
        self.DurationLabels_2.addWidget(self.retsuLabel_2)
        self.zaiLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.zaiLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.zaiLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.zaiLabel_2.setObjectName(_fromUtf8("zaiLabel_2"))
        self.DurationLabels_2.addWidget(self.zaiLabel_2)
        self.zenLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.zenLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-left: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.zenLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.zenLabel_2.setObjectName(_fromUtf8("zenLabel_2"))
        self.DurationLabels_2.addWidget(self.zenLabel_2)
        self.postLabel_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.postLabel_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-right: 1px solid black;\n"
"border-left: 1px solid black;"))
        self.postLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.postLabel_2.setObjectName(_fromUtf8("postLabel_2"))
        self.DurationLabels_2.addWidget(self.postLabel_2)
        self.sessionslidersLayout = QtGui.QWidget(self.frame)
        self.sessionslidersLayout.setGeometry(QtCore.QRect(10, 130, 751, 451))
        self.sessionslidersLayout.setObjectName(_fromUtf8("sessionslidersLayout"))
        self.DurationSliders_2 = QtGui.QHBoxLayout(self.sessionslidersLayout)
        self.DurationSliders_2.setContentsMargins(-1, -1, 0, -1)
        self.DurationSliders_2.setObjectName(_fromUtf8("DurationSliders_2"))
        self.preSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.preSlider_2.setStyleSheet(_fromUtf8(""))
        self.preSlider_2.setMaximum(90)
        self.preSlider_2.setSingleStep(5)
        self.preSlider_2.setPageStep(5)
        self.preSlider_2.setTracking(False)
        self.preSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.preSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.preSlider_2.setObjectName(_fromUtf8("preSlider_2"))
        self.DurationSliders_2.addWidget(self.preSlider_2)
        self.rinSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.rinSlider_2.setMaximum(90)
        self.rinSlider_2.setSingleStep(5)
        self.rinSlider_2.setPageStep(5)
        self.rinSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.rinSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.rinSlider_2.setObjectName(_fromUtf8("rinSlider_2"))
        self.DurationSliders_2.addWidget(self.rinSlider_2)
        self.kyoSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.kyoSlider_2.setMaximum(90)
        self.kyoSlider_2.setSingleStep(5)
        self.kyoSlider_2.setPageStep(5)
        self.kyoSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.kyoSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.kyoSlider_2.setObjectName(_fromUtf8("kyoSlider_2"))
        self.DurationSliders_2.addWidget(self.kyoSlider_2)
        self.tohSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.tohSlider_2.setMaximum(90)
        self.tohSlider_2.setSingleStep(5)
        self.tohSlider_2.setPageStep(5)
        self.tohSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.tohSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.tohSlider_2.setObjectName(_fromUtf8("tohSlider_2"))
        self.DurationSliders_2.addWidget(self.tohSlider_2)
        self.shaSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.shaSlider_2.setMaximum(90)
        self.shaSlider_2.setSingleStep(5)
        self.shaSlider_2.setPageStep(5)
        self.shaSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.shaSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.shaSlider_2.setObjectName(_fromUtf8("shaSlider_2"))
        self.DurationSliders_2.addWidget(self.shaSlider_2)
        self.kaiSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.kaiSlider_2.setMaximum(90)
        self.kaiSlider_2.setSingleStep(5)
        self.kaiSlider_2.setPageStep(5)
        self.kaiSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.kaiSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.kaiSlider_2.setObjectName(_fromUtf8("kaiSlider_2"))
        self.DurationSliders_2.addWidget(self.kaiSlider_2)
        self.jinSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.jinSlider_2.setMaximum(90)
        self.jinSlider_2.setSingleStep(5)
        self.jinSlider_2.setPageStep(5)
        self.jinSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.jinSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.jinSlider_2.setObjectName(_fromUtf8("jinSlider_2"))
        self.DurationSliders_2.addWidget(self.jinSlider_2)
        self.retsuSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.retsuSlider_2.setMaximum(90)
        self.retsuSlider_2.setSingleStep(5)
        self.retsuSlider_2.setPageStep(5)
        self.retsuSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.retsuSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.retsuSlider_2.setObjectName(_fromUtf8("retsuSlider_2"))
        self.DurationSliders_2.addWidget(self.retsuSlider_2)
        self.zaiSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.zaiSlider_2.setMaximum(90)
        self.zaiSlider_2.setSingleStep(5)
        self.zaiSlider_2.setPageStep(5)
        self.zaiSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.zaiSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.zaiSlider_2.setObjectName(_fromUtf8("zaiSlider_2"))
        self.DurationSliders_2.addWidget(self.zaiSlider_2)
        self.zenSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.zenSlider_2.setMaximum(90)
        self.zenSlider_2.setSingleStep(5)
        self.zenSlider_2.setPageStep(5)
        self.zenSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.zenSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.zenSlider_2.setObjectName(_fromUtf8("zenSlider_2"))
        self.DurationSliders_2.addWidget(self.zenSlider_2)
        self.postSlider_2 = QtGui.QSlider(self.sessionslidersLayout)
        self.postSlider_2.setMaximum(90)
        self.postSlider_2.setSingleStep(5)
        self.postSlider_2.setPageStep(5)
        self.postSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.postSlider_2.setTickPosition(QtGui.QSlider.NoTicks)
        self.postSlider_2.setObjectName(_fromUtf8("postSlider_2"))
        self.DurationSliders_2.addWidget(self.postSlider_2)
        self.toptotalsLabel = QtGui.QLabel(self.frame)
        self.toptotalsLabel.setGeometry(QtCore.QRect(280, 40, 221, 21))
        self.toptotalsLabel.setStyleSheet(_fromUtf8("font: 87 14pt \"Arial Black\";\n"
"color: #98A6A8;"))
        self.toptotalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.toptotalsLabel.setObjectName(_fromUtf8("toptotalsLabel"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 590, 701, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.CutDurationDisplays_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.CutDurationDisplays_2.setMargin(0)
        self.CutDurationDisplays_2.setObjectName(_fromUtf8("CutDurationDisplays_2"))
        self.preDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.preDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.preDisplay_2.setSmallDecimalPoint(False)
        self.preDisplay_2.setNumDigits(2)
        self.preDisplay_2.setObjectName(_fromUtf8("preDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.preDisplay_2)
        self.rinDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.rinDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.rinDisplay_2.setNumDigits(2)
        self.rinDisplay_2.setObjectName(_fromUtf8("rinDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.rinDisplay_2)
        self.kyoDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.kyoDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.kyoDisplay_2.setNumDigits(2)
        self.kyoDisplay_2.setObjectName(_fromUtf8("kyoDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.kyoDisplay_2)
        self.tohDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.tohDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.tohDisplay_2.setNumDigits(2)
        self.tohDisplay_2.setObjectName(_fromUtf8("tohDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.tohDisplay_2)
        self.shaDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.shaDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.shaDisplay_2.setNumDigits(2)
        self.shaDisplay_2.setObjectName(_fromUtf8("shaDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.shaDisplay_2)
        self.kaiDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.kaiDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.kaiDisplay_2.setNumDigits(2)
        self.kaiDisplay_2.setObjectName(_fromUtf8("kaiDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.kaiDisplay_2)
        self.jinDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.jinDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.jinDisplay_2.setNumDigits(2)
        self.jinDisplay_2.setObjectName(_fromUtf8("jinDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.jinDisplay_2)
        self.retsuDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.retsuDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.retsuDisplay_2.setNumDigits(2)
        self.retsuDisplay_2.setObjectName(_fromUtf8("retsuDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.retsuDisplay_2)
        self.zaiDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.zaiDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.zaiDisplay_2.setNumDigits(2)
        self.zaiDisplay_2.setObjectName(_fromUtf8("zaiDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.zaiDisplay_2)
        self.zenDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.zenDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.zenDisplay_2.setNumDigits(2)
        self.zenDisplay_2.setObjectName(_fromUtf8("zenDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.zenDisplay_2)
        self.postDisplay_2 = QtGui.QLCDNumber(self.horizontalLayoutWidget_2)
        self.postDisplay_2.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);"))
        self.postDisplay_2.setNumDigits(2)
        self.postDisplay_2.setObjectName(_fromUtf8("postDisplay_2"))
        self.CutDurationDisplays_2.addWidget(self.postDisplay_2)
        self.verticalLayoutWidget = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(790, 80, 91, 561))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.totalprogressLabels = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.totalprogressLabels.setMargin(0)
        self.totalprogressLabels.setObjectName(_fromUtf8("totalprogressLabels"))
        self.rintotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.rintotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.rintotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rintotalLabel.setObjectName(_fromUtf8("rintotalLabel"))
        self.totalprogressLabels.addWidget(self.rintotalLabel)
        self.kyototalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.kyototalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kyototalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kyototalLabel.setObjectName(_fromUtf8("kyototalLabel"))
        self.totalprogressLabels.addWidget(self.kyototalLabel)
        self.tohtotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.tohtotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.tohtotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tohtotalLabel.setObjectName(_fromUtf8("tohtotalLabel"))
        self.totalprogressLabels.addWidget(self.tohtotalLabel)
        self.shatotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.shatotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.shatotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.shatotalLabel.setObjectName(_fromUtf8("shatotalLabel"))
        self.totalprogressLabels.addWidget(self.shatotalLabel)
        self.kaitotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.kaitotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kaitotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.kaitotalLabel.setObjectName(_fromUtf8("kaitotalLabel"))
        self.totalprogressLabels.addWidget(self.kaitotalLabel)
        self.jintotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.jintotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.jintotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.jintotalLabel.setObjectName(_fromUtf8("jintotalLabel"))
        self.totalprogressLabels.addWidget(self.jintotalLabel)
        self.retsutotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.retsutotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.retsutotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.retsutotalLabel.setObjectName(_fromUtf8("retsutotalLabel"))
        self.totalprogressLabels.addWidget(self.retsutotalLabel)
        self.zaitotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.zaitotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zaitotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zaitotalLabel.setObjectName(_fromUtf8("zaitotalLabel"))
        self.totalprogressLabels.addWidget(self.zaitotalLabel)
        self.zentotalLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.zentotalLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-left: 1px solid black;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zentotalLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.zentotalLabel.setObjectName(_fromUtf8("zentotalLabel"))
        self.totalprogressLabels.addWidget(self.zentotalLabel)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(880, 80, 66, 561))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.totaldaysLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.totaldaysLayout.setMargin(0)
        self.totaldaysLayout.setObjectName(_fromUtf8("totaldaysLayout"))
        self.rintotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.rintotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.rintotaldaysDisplay.setObjectName(_fromUtf8("rintotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.rintotaldaysDisplay)
        self.kyototaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.kyototaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kyototaldaysDisplay.setObjectName(_fromUtf8("kyototaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.kyototaldaysDisplay)
        self.tohtotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.tohtotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.tohtotaldaysDisplay.setObjectName(_fromUtf8("tohtotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.tohtotaldaysDisplay)
        self.shatotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.shatotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.shatotaldaysDisplay.setObjectName(_fromUtf8("shatotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.shatotaldaysDisplay)
        self.kaitotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.kaitotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kaitotaldaysDisplay.setObjectName(_fromUtf8("kaitotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.kaitotaldaysDisplay)
        self.jintotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.jintotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.jintotaldaysDisplay.setObjectName(_fromUtf8("jintotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.jintotaldaysDisplay)
        self.retsutotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.retsutotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.retsutotaldaysDisplay.setObjectName(_fromUtf8("retsutotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.retsutotaldaysDisplay)
        self.zaitotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.zaitotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zaitotaldaysDisplay.setObjectName(_fromUtf8("zaitotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.zaitotaldaysDisplay)
        self.zentotaldaysDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_2)
        self.zentotaldaysDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zentotaldaysDisplay.setObjectName(_fromUtf8("zentotaldaysDisplay"))
        self.totaldaysLayout.addWidget(self.zentotaldaysDisplay)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(950, 80, 55, 561))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.totaldaysLabels = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.totaldaysLabels.setMargin(0)
        self.totaldaysLabels.setObjectName(_fromUtf8("totaldaysLabels"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.totaldaysLabels.addWidget(self.label_6)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.totaldaysLabels.addWidget(self.label_5)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.totaldaysLabels.addWidget(self.label_4)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.totaldaysLabels.addWidget(self.label_7)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_9.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.totaldaysLabels.addWidget(self.label_9)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_8.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.totaldaysLabels.addWidget(self.label_8)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.totaldaysLabels.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.totaldaysLabels.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.totaldaysLabels.addWidget(self.label)
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(1010, 80, 66, 561))
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.totalhoursLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.totalhoursLayout.setMargin(0)
        self.totalhoursLayout.setObjectName(_fromUtf8("totalhoursLayout"))
        self.rintotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.rintotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.rintotalhoursDisplay.setObjectName(_fromUtf8("rintotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.rintotalhoursDisplay)
        self.kyototalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.kyototalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kyototalhoursDisplay.setObjectName(_fromUtf8("kyototalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.kyototalhoursDisplay)
        self.tohtotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.tohtotalhoursDisplay.setObjectName(_fromUtf8("tohtotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.tohtotalhoursDisplay)
        self.shatotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.shatotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.shatotalhoursDisplay.setObjectName(_fromUtf8("shatotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.shatotalhoursDisplay)
        self.kaitotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.kaitotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kaitotalhoursDisplay.setObjectName(_fromUtf8("kaitotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.kaitotalhoursDisplay)
        self.jintotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.jintotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.jintotalhoursDisplay.setObjectName(_fromUtf8("jintotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.jintotalhoursDisplay)
        self.retsutotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.retsutotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.retsutotalhoursDisplay.setObjectName(_fromUtf8("retsutotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.retsutotalhoursDisplay)
        self.zaitotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.zaitotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zaitotalhoursDisplay.setObjectName(_fromUtf8("zaitotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.zaitotalhoursDisplay)
        self.zentotalhoursDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_4)
        self.zentotalhoursDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zentotalhoursDisplay.setObjectName(_fromUtf8("zentotalhoursDisplay"))
        self.totalhoursLayout.addWidget(self.zentotalhoursDisplay)
        self.verticalLayoutWidget_5 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(1080, 80, 55, 561))
        self.verticalLayoutWidget_5.setObjectName(_fromUtf8("verticalLayoutWidget_5"))
        self.totalhoursLabels = QtGui.QVBoxLayout(self.verticalLayoutWidget_5)
        self.totalhoursLabels.setMargin(0)
        self.totalhoursLabels.setObjectName(_fromUtf8("totalhoursLabels"))
        self.label_11 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_11.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.totalhoursLabels.addWidget(self.label_11)
        self.label_14 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_14.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.totalhoursLabels.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_15.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.totalhoursLabels.addWidget(self.label_15)
        self.label_18 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_18.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.totalhoursLabels.addWidget(self.label_18)
        self.label_17 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_17.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.totalhoursLabels.addWidget(self.label_17)
        self.label_16 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_16.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.totalhoursLabels.addWidget(self.label_16)
        self.label_13 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_13.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.totalhoursLabels.addWidget(self.label_13)
        self.label_12 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_12.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.totalhoursLabels.addWidget(self.label_12)
        self.label_10 = QtGui.QLabel(self.verticalLayoutWidget_5)
        self.label_10.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.totalhoursLabels.addWidget(self.label_10)
        self.verticalLayoutWidget_6 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(1140, 80, 66, 561))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.totalminutesLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_6)
        self.totalminutesLayout.setMargin(0)
        self.totalminutesLayout.setObjectName(_fromUtf8("totalminutesLayout"))
        self.rintotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.rintotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.rintotalminutesDisplay.setObjectName(_fromUtf8("rintotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.rintotalminutesDisplay)
        self.kyototalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.kyototalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kyototalminutesDisplay.setObjectName(_fromUtf8("kyototalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.kyototalminutesDisplay)
        self.tohtotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.tohtotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.tohtotalminutesDisplay.setObjectName(_fromUtf8("tohtotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.tohtotalminutesDisplay)
        self.shatotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.shatotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.shatotalminutesDisplay.setObjectName(_fromUtf8("shatotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.shatotalminutesDisplay)
        self.kaitotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.kaitotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.kaitotalminutesDisplay.setObjectName(_fromUtf8("kaitotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.kaitotalminutesDisplay)
        self.jintotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.jintotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.jintotalminutesDisplay.setObjectName(_fromUtf8("jintotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.jintotalminutesDisplay)
        self.retsutotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.retsutotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.retsutotalminutesDisplay.setObjectName(_fromUtf8("retsutotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.retsutotalminutesDisplay)
        self.zaitotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.zaitotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zaitotalminutesDisplay.setObjectName(_fromUtf8("zaitotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.zaitotalminutesDisplay)
        self.zentotalminutesDisplay = QtGui.QLCDNumber(self.verticalLayoutWidget_6)
        self.zentotalminutesDisplay.setStyleSheet(_fromUtf8("color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;"))
        self.zentotalminutesDisplay.setObjectName(_fromUtf8("zentotalminutesDisplay"))
        self.totalminutesLayout.addWidget(self.zentotalminutesDisplay)
        self.verticalLayoutWidget_7 = QtGui.QWidget(self.frame)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(1210, 80, 71, 561))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.totaldaysLayout_6 = QtGui.QVBoxLayout(self.verticalLayoutWidget_7)
        self.totaldaysLayout_6.setMargin(0)
        self.totaldaysLayout_6.setObjectName(_fromUtf8("totaldaysLayout_6"))
        self.label_19 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_19.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.totaldaysLayout_6.addWidget(self.label_19)
        self.label_23 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_23.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.totaldaysLayout_6.addWidget(self.label_23)
        self.label_22 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_22.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.totaldaysLayout_6.addWidget(self.label_22)
        self.label_21 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_21.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.totaldaysLayout_6.addWidget(self.label_21)
        self.label_25 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_25.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.totaldaysLayout_6.addWidget(self.label_25)
        self.label_20 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_20.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.totaldaysLayout_6.addWidget(self.label_20)
        self.label_26 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_26.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.totaldaysLayout_6.addWidget(self.label_26)
        self.label_24 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_24.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.totaldaysLayout_6.addWidget(self.label_24)
        self.label_27 = QtGui.QLabel(self.verticalLayoutWidget_7)
        self.label_27.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;\n"
"border-right: 1px solid black;"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.totaldaysLayout_6.addWidget(self.label_27)
        self.horizontalLayoutWidget_6 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(790, 19, 491, 61))
        self.horizontalLayoutWidget_6.setObjectName(_fromUtf8("horizontalLayoutWidget_6"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.topsessionLabel = QtGui.QLabel(self.horizontalLayoutWidget_6)
        self.topsessionLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"font: 12pt \"Arial Black\";"))
        self.topsessionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topsessionLabel.setObjectName(_fromUtf8("topsessionLabel"))
        self.horizontalLayout.addWidget(self.topsessionLabel)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_3.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 660, 291, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.AmbienceOption = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.AmbienceOption.setStyleSheet(_fromUtf8("color: rgb(155, 170, 172);\n"
"selection-background-color: rgb(200, 62, 67);\n"
""))
        self.AmbienceOption.setObjectName(_fromUtf8("AmbienceOption"))
        self.horizontalLayout_2.addWidget(self.AmbienceOption)
        self.ReferebceDisplayOption = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.ReferebceDisplayOption.setStyleSheet(_fromUtf8("color: rgb(155, 170, 172);\n"
"selection-background-color: rgb(53, 62, 67);"))
        self.ReferebceDisplayOption.setObjectName(_fromUtf8("ReferebceDisplayOption"))
        self.horizontalLayout_2.addWidget(self.ReferebceDisplayOption)
        self.gridLayoutWidget = QtGui.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(870, 650, 351, 61))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.actionsbuttonsLayout = QtGui.QHBoxLayout()
        self.actionsbuttonsLayout.setObjectName(_fromUtf8("actionsbuttonsLayout"))
        self.CreateButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.CreateButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.CreateButton.setObjectName(_fromUtf8("CreateButton"))
        self.actionsbuttonsLayout.addWidget(self.CreateButton)
        self.exportButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.exportButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.actionsbuttonsLayout.addWidget(self.exportButton)
        self.gridLayout.addLayout(self.actionsbuttonsLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.PlayButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.PlayButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.PlayButton.setObjectName(_fromUtf8("PlayButton"))
        self.horizontalLayout_3.addWidget(self.PlayButton)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setStyleSheet(_fromUtf8("color: #98A6A8;"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menuBar.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.menuBar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.menuBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuBar.setStyleSheet(_fromUtf8("background-color:#212526;\n"
"color: :#212526;\n"
""))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setStyleSheet(_fromUtf8("background-color:#212526; color: #98A6A8;"))
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setStyleSheet(_fromUtf8("background-color:#212526; color: #98A6A8;"))
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setStyleSheet(_fromUtf8("background-color:#212526; color: #98A6A8;"))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_Session = QtGui.QAction(MainWindow)
        self.actionOpen_Session.setObjectName(_fromUtf8("actionOpen_Session"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionCheck_Integrity = QtGui.QAction(MainWindow)
        self.actionCheck_Integrity.setObjectName(_fromUtf8("actionCheck_Integrity"))
        self.actionAbout_This_Program = QtGui.QAction(MainWindow)
        self.actionAbout_This_Program.setObjectName(_fromUtf8("actionAbout_This_Program"))
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.menuFile.addAction(self.actionOpen_Session)
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionCheck_Integrity)
        self.menuHelp.addAction(self.actionAbout_This_Program)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.PlayButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.statusBar.clearMessage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.preLabel_2.setText(_translate("MainWindow", "PRE", None))
        self.rinLabel_2.setText(_translate("MainWindow", "RIN", None))
        self.kyoLabel_2.setText(_translate("MainWindow", "KYO", None))
        self.tohLabel_2.setText(_translate("MainWindow", "TOH", None))
        self.shaLabel_2.setText(_translate("MainWindow", "SHA", None))
        self.kaiLabel_2.setText(_translate("MainWindow", "KAI", None))
        self.jinLabel_2.setText(_translate("MainWindow", "JIN", None))
        self.retsuLabel_2.setText(_translate("MainWindow", "RETSU", None))
        self.zaiLabel_2.setText(_translate("MainWindow", "ZAI", None))
        self.zenLabel_2.setText(_translate("MainWindow", "ZEN", None))
        self.postLabel_2.setText(_translate("MainWindow", "POST", None))
        self.toptotalsLabel.setText(_translate("MainWindow", "Create Session", None))
        self.rintotalLabel.setText(_translate("MainWindow", "RIN", None))
        self.kyototalLabel.setText(_translate("MainWindow", "KYO", None))
        self.tohtotalLabel.setText(_translate("MainWindow", "TOH", None))
        self.shatotalLabel.setText(_translate("MainWindow", "SHA", None))
        self.kaitotalLabel.setText(_translate("MainWindow", "KAI", None))
        self.jintotalLabel.setText(_translate("MainWindow", "JIN", None))
        self.retsutotalLabel.setText(_translate("MainWindow", "RETSU", None))
        self.zaitotalLabel.setText(_translate("MainWindow", "ZAI", None))
        self.zentotalLabel.setText(_translate("MainWindow", "ZEN", None))
        self.label_6.setText(_translate("MainWindow", "Days", None))
        self.label_5.setText(_translate("MainWindow", "Days", None))
        self.label_4.setText(_translate("MainWindow", "Days", None))
        self.label_7.setText(_translate("MainWindow", "Days", None))
        self.label_9.setText(_translate("MainWindow", "Days", None))
        self.label_8.setText(_translate("MainWindow", "Days", None))
        self.label_3.setText(_translate("MainWindow", "Days", None))
        self.label_2.setText(_translate("MainWindow", "Days", None))
        self.label.setText(_translate("MainWindow", "Days", None))
        self.tohtotalhoursDisplay.setStyleSheet(_translate("MainWindow", "color: rgb(187, 204, 207);\n"
"border-top: 1px solid black;\n"
"border-bottom: 1px solid black;", None))
        self.label_11.setText(_translate("MainWindow", "Hours", None))
        self.label_14.setText(_translate("MainWindow", "Hours", None))
        self.label_15.setText(_translate("MainWindow", "Hours", None))
        self.label_18.setText(_translate("MainWindow", "Hours", None))
        self.label_17.setText(_translate("MainWindow", "Hours", None))
        self.label_16.setText(_translate("MainWindow", "Hours", None))
        self.label_13.setText(_translate("MainWindow", "Hours", None))
        self.label_12.setText(_translate("MainWindow", "Hours", None))
        self.label_10.setText(_translate("MainWindow", "Hours", None))
        self.label_19.setText(_translate("MainWindow", "Minutes", None))
        self.label_23.setText(_translate("MainWindow", "Minutes", None))
        self.label_22.setText(_translate("MainWindow", "Minutes", None))
        self.label_21.setText(_translate("MainWindow", "Minutes", None))
        self.label_25.setText(_translate("MainWindow", "Minutes", None))
        self.label_20.setText(_translate("MainWindow", "Minutes", None))
        self.label_26.setText(_translate("MainWindow", "Minutes", None))
        self.label_24.setText(_translate("MainWindow", "Minutes", None))
        self.label_27.setText(_translate("MainWindow", "Minutes", None))
        self.topsessionLabel.setText(_translate("MainWindow", "Total Progress", None))
        self.pushButton.setText(_translate("MainWindow", "View List Of Sessions", None))
        self.pushButton_3.setText(_translate("MainWindow", "View Premature Endings", None))
        self.AmbienceOption.setText(_translate("MainWindow", "AMBIENCE", None))
        self.ReferebceDisplayOption.setText(_translate("MainWindow", "REFERENCE FILES", None))
        self.CreateButton.setText(_translate("MainWindow", "CREATE", None))
        self.exportButton.setText(_translate("MainWindow", "EXPORT", None))
        self.PlayButton.setText(_translate("MainWindow", "PLAY", None))
        self.pushButton_2.setText(_translate("MainWindow", "PAUSE", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_Session.setText(_translate("MainWindow", "Open Session", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionCheck_Integrity.setText(_translate("MainWindow", "Check Integrity", None))
        self.actionAbout_This_Program.setText(_translate("MainWindow", "About This Program", None))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt", None))

