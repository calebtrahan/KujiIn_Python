# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goallistdialog.ui'
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

class Ui_goallistdialog(object):
    def setupUi(self, goallistdialog):
        goallistdialog.setObjectName(_fromUtf8("goallistdialog"))
        goallistdialog.resize(417, 353)
        self.goallabel = QtGui.QLabel(goallistdialog)
        self.goallabel.setGeometry(QtCore.QRect(40, 20, 341, 20))
        self.goallabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goallabel.setObjectName(_fromUtf8("goallabel"))
        self.goalsList = QtGui.QListView(goallistdialog)
        self.goalsList.setGeometry(QtCore.QRect(40, 50, 341, 251))
        self.goalsList.setObjectName(_fromUtf8("goalsList"))
        self.goalslistOKButton = QtGui.QPushButton(goallistdialog)
        self.goalslistOKButton.setGeometry(QtCore.QRect(320, 310, 84, 30))
        self.goalslistOKButton.setObjectName(_fromUtf8("goalslistOKButton"))

        self.retranslateUi(goallistdialog)
        QtCore.QMetaObject.connectSlotsByName(goallistdialog)

    def retranslateUi(self, goallistdialog):
        goallistdialog.setWindowTitle(_translate("goallistdialog", "Dialog", None))
        self.goallabel.setText(_translate("goallistdialog", "CURRENT GOALS:", None))
        self.goalslistOKButton.setText(_translate("goallistdialog", "OK", None))

