# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creatingsessiondialog.ui'
#
# Created: Wed Jun 17 18:46:15 2015
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

class Ui_exportsessiondialog(object):
    def setupUi(self, exportsessiondialog):
        exportsessiondialog.setObjectName(_fromUtf8("exportsessiondialog"))
        exportsessiondialog.resize(391, 114)
        self.exportsessionProgressBar = QtGui.QProgressBar(exportsessiondialog)
        self.exportsessionProgressBar.setGeometry(QtCore.QRect(20, 40, 361, 23))
        self.exportsessionProgressBar.setProperty("value", 24)
        self.exportsessionProgressBar.setObjectName(_fromUtf8("exportsessionProgressBar"))
        self.exportsessionCancelButton = QtGui.QPushButton(exportsessiondialog)
        self.exportsessionCancelButton.setGeometry(QtCore.QRect(300, 70, 84, 30))
        self.exportsessionCancelButton.setObjectName(_fromUtf8("exportsessionCancelButton"))
        self.exportsessiontopLabel = QtGui.QLabel(exportsessiondialog)
        self.exportsessiontopLabel.setGeometry(QtCore.QRect(20, 10, 351, 20))
        self.exportsessiontopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exportsessiontopLabel.setObjectName(_fromUtf8("exportsessiontopLabel"))
        self.exportingProgressLabel = QtGui.QLabel(exportsessiondialog)
        self.exportingProgressLabel.setGeometry(QtCore.QRect(20, 80, 271, 16))
        self.exportingProgressLabel.setObjectName(_fromUtf8("exportingProgressLabel"))

        self.retranslateUi(exportsessiondialog)
        QtCore.QMetaObject.connectSlotsByName(exportsessiondialog)

    def retranslateUi(self, exportsessiondialog):
        exportsessiondialog.setWindowTitle(_translate("exportsessiondialog", "Dialog", None))
        self.exportsessionCancelButton.setText(_translate("exportsessiondialog", "Cancel", None))
        self.exportsessiontopLabel.setText(_translate("exportsessiondialog", "(This May Will Take A While)", None))
        self.exportingProgressLabel.setText(_translate("exportsessiondialog", "Exporting %s", None))

