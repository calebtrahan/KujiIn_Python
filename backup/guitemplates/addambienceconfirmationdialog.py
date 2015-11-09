# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addambienceconfirmationdialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.3
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(593, 398)
        Dialog.setStyleSheet(_fromUtf8("background-color:#212526;"))
        self.filesListView = QtGui.QListView(Dialog)
        self.filesListView.setGeometry(QtCore.QRect(20, 70, 261, 261))
        self.filesListView.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(42, 52, 53);"))
        self.filesListView.setObjectName(_fromUtf8("filesListView"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
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
        self.topLabel = QtGui.QLabel(Dialog)
        self.topLabel.setGeometry(QtCore.QRect(50, 10, 481, 20))
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.statusBar = QtGui.QLabel(Dialog)
        self.statusBar.setGeometry(QtCore.QRect(20, 360, 291, 16))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.filestopLabel = QtGui.QLabel(Dialog)
        self.filestopLabel.setGeometry(QtCore.QRect(24, 40, 261, 20))
        self.filestopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filestopLabel.setObjectName(_fromUtf8("filestopLabel"))
        self.cutsListView = QtGui.QListView(Dialog)
        self.cutsListView.setGeometry(QtCore.QRect(310, 70, 261, 261))
        self.cutsListView.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(42, 52, 53);"))
        self.cutsListView.setObjectName(_fromUtf8("cutsListView"))
        self.ambiencetopLabel = QtGui.QLabel(Dialog)
        self.ambiencetopLabel.setGeometry(QtCore.QRect(310, 40, 261, 20))
        self.ambiencetopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ambiencetopLabel.setObjectName(_fromUtf8("ambiencetopLabel"))
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.acceptButton.setText(_translate("Dialog", "Accept", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.topLabel.setText(_translate("Dialog", "NOTE: This Can\'t Be Undone", None))
        self.statusBar.setText(_translate("Dialog", "Processing (00/99). Please Wait...", None))
        self.filestopLabel.setText(_translate("Dialog", "Add These File(s)", None))
        self.ambiencetopLabel.setText(_translate("Dialog", "As Ambience To These Cut(s)", None))

