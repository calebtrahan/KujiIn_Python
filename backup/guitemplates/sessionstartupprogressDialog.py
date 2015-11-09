# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sessionstartupprogressDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(292, 65)
        self.currentlyprocessingLabel = QtGui.QLabel(Dialog)
        self.currentlyprocessingLabel.setGeometry(QtCore.QRect(0, 40, 291, 17))
        self.currentlyprocessingLabel.setObjectName(_fromUtf8("currentlyprocessingLabel"))
        self.totalprocessingProgressBar = QtGui.QProgressBar(Dialog)
        self.totalprocessingProgressBar.setGeometry(QtCore.QRect(0, 20, 291, 23))
        self.totalprocessingProgressBar.setProperty("value", 24)
        self.totalprocessingProgressBar.setObjectName(_fromUtf8("totalprocessingProgressBar"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.currentlyprocessingLabel.setText(_translate("Dialog", "Currently Checking %s. Please Wait", None))

