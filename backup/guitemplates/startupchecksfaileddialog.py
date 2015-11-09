# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startupchecksfaileddialog.ui'
#
# Created: Wed Feb  4 15:56:48 2015
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


        Dialog.resize(444, 103)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 0, 371, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 70, 75, 23))
        self.label.setText(_translate("Dialog", "Missing Some Necessary Sound Files From The Program. Please Go To This Link To Download Them:  http://link.com/  (NOTE: If You Don\'t Do This The Program May Freeze Or Make Incomplete Or Silent Sessions)", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))

