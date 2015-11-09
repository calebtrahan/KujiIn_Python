# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'processingdialog.ui'
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

class Ui_processingDialog(object):
    def setupUi(self, processingDialog):
        processingDialog.setObjectName(_fromUtf8("processingDialog"))
        processingDialog.resize(374, 64)
        self.messageLabel = QtGui.QLabel(processingDialog)
        self.messageLabel.setGeometry(QtCore.QRect(24, 20, 331, 20))
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))

        self.retranslateUi(processingDialog)
        QtCore.QMetaObject.connectSlotsByName(processingDialog)

    def retranslateUi(self, processingDialog):
        processingDialog.setWindowTitle(_translate("processingDialog", "Dialog", None))
        self.messageLabel.setText(_translate("processingDialog", "TextLabel", None))

