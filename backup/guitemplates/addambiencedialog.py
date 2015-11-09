# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addambiencedialog.ui'
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

class Ui_addambienceDialog(object):
    def setupUi(self, addambienceDialog):
        addambienceDialog.setObjectName(_fromUtf8("addambienceDialog"))
        addambienceDialog.resize(657, 450)
        self.audioFilesTable = QtGui.QTableWidget(addambienceDialog)
        self.audioFilesTable.setGeometry(QtCore.QRect(10, 40, 631, 291))
        self.audioFilesTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.audioFilesTable.setAutoFillBackground(False)
        self.audioFilesTable.setObjectName(_fromUtf8("audioFilesTable"))
        self.audioFilesTable.setColumnCount(2)
        self.audioFilesTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.audioFilesTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.audioFilesTable.setHorizontalHeaderItem(1, item)
        self.addFilesToTableButton = QtGui.QPushButton(addambienceDialog)
        self.addFilesToTableButton.setGeometry(QtCore.QRect(10, 340, 91, 31))
        self.addFilesToTableButton.setObjectName(_fromUtf8("addFilesToTableButton"))
        self.previewButton = QtGui.QPushButton(addambienceDialog)
        self.previewButton.setGeometry(QtCore.QRect(560, 340, 84, 31))
        self.previewButton.setObjectName(_fromUtf8("previewButton"))
        self.topLabel = QtGui.QLabel(addambienceDialog)
        self.topLabel.setGeometry(QtCore.QRect(10, 10, 631, 20))
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.addToProgramButton = QtGui.QPushButton(addambienceDialog)
        self.addToProgramButton.setGeometry(QtCore.QRect(440, 410, 111, 31))
        self.addToProgramButton.setObjectName(_fromUtf8("addToProgramButton"))
        self.cancelButton = QtGui.QPushButton(addambienceDialog)
        self.cancelButton.setGeometry(QtCore.QRect(560, 410, 84, 31))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.editCurrentAmbienceButton = QtGui.QPushButton(addambienceDialog)
        self.editCurrentAmbienceButton.setGeometry(QtCore.QRect(10, 410, 141, 31))
        self.editCurrentAmbienceButton.setObjectName(_fromUtf8("editCurrentAmbienceButton"))
        self.previewSlider = QtGui.QSlider(addambienceDialog)
        self.previewSlider.setGeometry(QtCore.QRect(260, 380, 221, 20))
        self.previewSlider.setOrientation(QtCore.Qt.Horizontal)
        self.previewSlider.setObjectName(_fromUtf8("previewSlider"))
        self.previewFileNameLabel = QtGui.QLabel(addambienceDialog)
        self.previewFileNameLabel.setGeometry(QtCore.QRect(260, 350, 251, 20))
        self.previewFileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewFileNameLabel.setObjectName(_fromUtf8("previewFileNameLabel"))
        self.previewcurrentTimeLabel = QtGui.QLabel(addambienceDialog)
        self.previewcurrentTimeLabel.setGeometry(QtCore.QRect(200, 380, 51, 16))
        self.previewcurrentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.previewcurrentTimeLabel.setObjectName(_fromUtf8("previewcurrentTimeLabel"))
        self.previewtotalTimeLabel = QtGui.QLabel(addambienceDialog)
        self.previewtotalTimeLabel.setGeometry(QtCore.QRect(490, 380, 41, 16))
        self.previewtotalTimeLabel.setObjectName(_fromUtf8("previewtotalTimeLabel"))
        self.pushButton = QtGui.QPushButton(addambienceDialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 340, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.statusBar = QtGui.QLabel(addambienceDialog)
        self.statusBar.setGeometry(QtCore.QRect(160, 420, 271, 16))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.horizontalSlider = QtGui.QSlider(addambienceDialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(560, 380, 81, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

        self.retranslateUi(addambienceDialog)
        QtCore.QMetaObject.connectSlotsByName(addambienceDialog)

    def retranslateUi(self, addambienceDialog):
        addambienceDialog.setWindowTitle(_translate("addambienceDialog", "Dialog", None))
        item = self.audioFilesTable.horizontalHeaderItem(0)
        item.setText(_translate("addambienceDialog", "Name", None))
        item = self.audioFilesTable.horizontalHeaderItem(1)
        item.setText(_translate("addambienceDialog", "Length", None))
        self.addFilesToTableButton.setText(_translate("addambienceDialog", "Add File(s)", None))
        self.previewButton.setText(_translate("addambienceDialog", "Preview", None))
        self.topLabel.setText(_translate("addambienceDialog", "Add Ambience Files To The Kuji-In Program", None))
        self.addToProgramButton.setText(_translate("addambienceDialog", "Add To Program", None))
        self.cancelButton.setText(_translate("addambienceDialog", "Cancel", None))
        self.editCurrentAmbienceButton.setText(_translate("addambienceDialog", "Edit Current Ambience", None))
        self.previewFileNameLabel.setText(_translate("addambienceDialog", "Preview File Name", None))
        self.previewcurrentTimeLabel.setText(_translate("addambienceDialog", "00:00", None))
        self.previewtotalTimeLabel.setText(_translate("addambienceDialog", "99:99", None))
        self.pushButton.setText(_translate("addambienceDialog", "Remove File(s)", None))
        self.statusBar.setText(_translate("addambienceDialog", "Text", None))

