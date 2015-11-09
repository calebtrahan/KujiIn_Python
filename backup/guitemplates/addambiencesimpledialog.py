# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addambiencesimpledialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.1
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
        Dialog.resize(586, 124)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 491, 51))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 80, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 80, 80, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Please Add At Least 3 Ambience Files (The More The Better) To The General Ambience Directory Located At:", None))
        self.pushButton.setText(_translate("Dialog", "TAKE ME THERE", None))
        self.pushButton_2.setText(_translate("Dialog", "BACK", None))

