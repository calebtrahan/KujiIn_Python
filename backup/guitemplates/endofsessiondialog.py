# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'endofsessiondialog.ui'
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

class Ui_sessioncompletedDialog(object):
    def setupUi(self, sessioncompletedDialog):
        sessioncompletedDialog.setObjectName(_fromUtf8("sessioncompletedDialog"))
        sessioncompletedDialog.resize(391, 142)
        self.sessioncompletedtopLabel = QtGui.QLabel(sessioncompletedDialog)
        self.sessioncompletedtopLabel.setGeometry(QtCore.QRect(30, 10, 331, 20))
        self.sessioncompletedtopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sessioncompletedtopLabel.setObjectName(_fromUtf8("sessioncompletedtopLabel"))
        self.sessioncompletedTotalTimeCompletedLabel = QtGui.QLabel(sessioncompletedDialog)
        self.sessioncompletedTotalTimeCompletedLabel.setGeometry(QtCore.QRect(30, 40, 331, 20))
        self.sessioncompletedTotalTimeCompletedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sessioncompletedTotalTimeCompletedLabel.setObjectName(_fromUtf8("sessioncompletedTotalTimeCompletedLabel"))
        self.sessioncompletedexportQuestionLabel = QtGui.QLabel(sessioncompletedDialog)
        self.sessioncompletedexportQuestionLabel.setGeometry(QtCore.QRect(30, 70, 331, 20))
        self.sessioncompletedexportQuestionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sessioncompletedexportQuestionLabel.setObjectName(_fromUtf8("sessioncompletedexportQuestionLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(sessioncompletedDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 100, 168, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.sessioncompletebuttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.sessioncompletebuttonLayout.setMargin(0)
        self.sessioncompletebuttonLayout.setObjectName(_fromUtf8("sessioncompletebuttonLayout"))
        self.sessioncompleteExportYesButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.sessioncompleteExportYesButton.setObjectName(_fromUtf8("sessioncompleteExportYesButton"))
        self.sessioncompletebuttonLayout.addWidget(self.sessioncompleteExportYesButton)
        self.sessioncompleteExportNoButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.sessioncompleteExportNoButton.setObjectName(_fromUtf8("sessioncompleteExportNoButton"))
        self.sessioncompletebuttonLayout.addWidget(self.sessioncompleteExportNoButton)

        self.retranslateUi(sessioncompletedDialog)
        QtCore.QMetaObject.connectSlotsByName(sessioncompletedDialog)

    def retranslateUi(self, sessioncompletedDialog):
        sessioncompletedDialog.setWindowTitle(_translate("sessioncompletedDialog", "Dialog", None))
        self.sessioncompletedtopLabel.setText(_translate("sessioncompletedDialog", "Session Completed! Great Work!", None))
        self.sessioncompletedTotalTimeCompletedLabel.setText(_translate("sessioncompletedDialog", "You Have Now Completed x Hours And x Minutes ", None))
        self.sessioncompletedexportQuestionLabel.setText(_translate("sessioncompletedDialog", "Would You Like To Export This Session For Later Use?", None))
        self.sessioncompleteExportYesButton.setText(_translate("sessioncompletedDialog", "YES", None))
        self.sessioncompleteExportNoButton.setText(_translate("sessioncompletedDialog", "NO", None))

