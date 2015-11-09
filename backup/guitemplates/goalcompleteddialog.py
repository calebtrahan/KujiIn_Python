# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goalcompleteddialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.2
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

class Ui_goalcompleteddialog(object):
    def setupUi(self, goalcompleteddialog):
        goalcompleteddialog.setObjectName(_fromUtf8("goalcompleteddialog"))
        goalcompleteddialog.resize(406, 235)
        goalcompleteddialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        goalcompleteddialog.setAutoFillBackground(False)
        goalcompleteddialog.setModal(False)
        self.goalcompletedtopLabel = QtGui.QLabel(goalcompleteddialog)
        self.goalcompletedtopLabel.setGeometry(QtCore.QRect(120, 10, 161, 20))
        self.goalcompletedtopLabel.setStyleSheet(_fromUtf8("font: 12pt \"Arial\";\n"
"color: rgb(152, 166, 168);"))
        self.goalcompletedtopLabel.setObjectName(_fromUtf8("goalcompletedtopLabel"))
        self.goalcompletedmiddleLabel = QtGui.QLabel(goalcompleteddialog)
        self.goalcompletedmiddleLabel.setGeometry(QtCore.QRect(30, 40, 341, 21))
        self.goalcompletedmiddleLabel.setObjectName(_fromUtf8("goalcompletedmiddleLabel"))
        self.goalcompletedValue = QtGui.QLabel(goalcompleteddialog)
        self.goalcompletedValue.setGeometry(QtCore.QRect(90, 70, 211, 51))
        self.goalcompletedValue.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"font: 75 18pt \"Arial\";\n"
"color: rgb(152, 166, 168);"))
        self.goalcompletedValue.setAlignment(QtCore.Qt.AlignCenter)
        self.goalcompletedValue.setObjectName(_fromUtf8("goalcompletedValue"))
        self.goalcompletedbottomLabel = QtGui.QLabel(goalcompleteddialog)
        self.goalcompletedbottomLabel.setGeometry(QtCore.QRect(10, 130, 391, 51))
        self.goalcompletedbottomLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalcompletedbottomLabel.setWordWrap(True)
        self.goalcompletedbottomLabel.setObjectName(_fromUtf8("goalcompletedbottomLabel"))
        self.goalcompletedButton = QtGui.QPushButton(goalcompleteddialog)
        self.goalcompletedButton.setGeometry(QtCore.QRect(310, 200, 84, 30))
        self.goalcompletedButton.setObjectName(_fromUtf8("goalcompletedButton"))

        self.retranslateUi(goalcompleteddialog)
        QtCore.QMetaObject.connectSlotsByName(goalcompleteddialog)

    def retranslateUi(self, goalcompleteddialog):
        goalcompleteddialog.setWindowTitle(_translate("goalcompleteddialog", "Dialog", None))
        self.goalcompletedtopLabel.setText(_translate("goalcompleteddialog", "GOAL COMPLETED!", None))
        self.goalcompletedmiddleLabel.setText(_translate("goalcompleteddialog", "It Wasn\'t Easy, But You Stuck With It And Achieved Your Goal Of:", None))
        self.goalcompletedValue.setText(_translate("goalcompleteddialog", "GOAL HERE", None))
        self.goalcompletedbottomLabel.setText(_translate("goalcompleteddialog", "Celebrate In Your Success, And Achieve The Next Goal You Have Set. Anything Is Possible!", None))
        self.goalcompletedButton.setText(_translate("goalcompleteddialog", "OK", None))

