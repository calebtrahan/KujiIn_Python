# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'typeofambiencedialog.ui'
#
# Created: Wed Jun 17 19:28:13 2015
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

class Ui_typeofambienceDialog(object):
    def setupUi(self, typeofambienceDialog):
        typeofambienceDialog.setObjectName(_fromUtf8("typeofambienceDialog"))
        typeofambienceDialog.resize(423, 155)
        self.specifcdescription = QtGui.QLabel(typeofambienceDialog)
        self.specifcdescription.setGeometry(QtCore.QRect(30, 70, 161, 31))
        self.specifcdescription.setAlignment(QtCore.Qt.AlignCenter)
        self.specifcdescription.setWordWrap(True)
        self.specifcdescription.setObjectName(_fromUtf8("specifcdescription"))
        self.generaldescription = QtGui.QLabel(typeofambienceDialog)
        self.generaldescription.setGeometry(QtCore.QRect(220, 70, 191, 31))
        self.generaldescription.setAlignment(QtCore.Qt.AlignCenter)
        self.generaldescription.setWordWrap(True)
        self.generaldescription.setObjectName(_fromUtf8("generaldescription"))
        self.specifcButton = QtGui.QPushButton(typeofambienceDialog)
        self.specifcButton.setGeometry(QtCore.QRect(10, 40, 201, 23))
        self.specifcButton.setObjectName(_fromUtf8("specifcButton"))
        self.generalButton = QtGui.QPushButton(typeofambienceDialog)
        self.generalButton.setGeometry(QtCore.QRect(220, 40, 191, 23))
        self.generalButton.setObjectName(_fromUtf8("generalButton"))
        self.helpButton = QtGui.QPushButton(typeofambienceDialog)
        self.helpButton.setGeometry(QtCore.QRect(320, 120, 90, 23))
        self.helpButton.setObjectName(_fromUtf8("helpButton"))
        self.checkBox = QtGui.QCheckBox(typeofambienceDialog)
        self.checkBox.setGeometry(QtCore.QRect(20, 120, 181, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label = QtGui.QLabel(typeofambienceDialog)
        self.label.setGeometry(QtCore.QRect(17, 0, 391, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        typeofambienceDialog.setWindowTitle(_translate("typeofambienceDialog", "Dialog", None))
        self.specifcdescription.setText(_translate("typeofambienceDialog", "Randomized Ambience For Each Specifc Cut", None))
        self.generaldescription.setText(_translate("typeofambienceDialog", "General Ambience Played Through The Whole Session", None))
        self.specifcButton.setText(_translate("typeofambienceDialog", "Specific", None))
        self.generalButton.setText(_translate("typeofambienceDialog", "General", None))
        self.helpButton.setText(_translate("typeofambienceDialog", "Help", None))
        self.checkBox.setText(_translate("typeofambienceDialog", "Full Screen", None))
        self.label.setText(_translate("typeofambienceDialog", "Some Label Text", None))

