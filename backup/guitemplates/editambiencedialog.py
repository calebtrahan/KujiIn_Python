# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editambiencedialog.ui'
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

class Ui_editAmbienceDialog(object):
    def setupUi(self, editAmbienceDialog):
        editAmbienceDialog.setObjectName(_fromUtf8("editAmbienceDialog"))
        editAmbienceDialog.resize(664, 736)
        self.loadSelectedCutsAmbienceButton = QtGui.QPushButton(editAmbienceDialog)
        self.loadSelectedCutsAmbienceButton.setGeometry(QtCore.QRect(220, 40, 101, 31))
        self.loadSelectedCutsAmbienceButton.setObjectName(_fromUtf8("loadSelectedCutsAmbienceButton"))
        self.cutselectorComboBox = QtGui.QComboBox(editAmbienceDialog)
        self.cutselectorComboBox.setGeometry(QtCore.QRect(60, 40, 151, 29))
        self.cutselectorComboBox.setObjectName(_fromUtf8("cutselectorComboBox"))
        self.topLabel1 = QtGui.QLabel(editAmbienceDialog)
        self.topLabel1.setGeometry(QtCore.QRect(60, 10, 261, 20))
        self.topLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel1.setObjectName(_fromUtf8("topLabel1"))
        self.topLabel2 = QtGui.QLabel(editAmbienceDialog)
        self.topLabel2.setGeometry(QtCore.QRect(390, 10, 241, 16))
        self.topLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel2.setObjectName(_fromUtf8("topLabel2"))
        self.currentAmbienceLabel = QtGui.QLabel(editAmbienceDialog)
        self.currentAmbienceLabel.setGeometry(QtCore.QRect(384, 50, 251, 20))
        self.currentAmbienceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentAmbienceLabel.setObjectName(_fromUtf8("currentAmbienceLabel"))
        self.audioFilesTable = QtGui.QTableWidget(editAmbienceDialog)
        self.audioFilesTable.setGeometry(QtCore.QRect(20, 120, 621, 481))
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
        self.addAmbienceButton = QtGui.QPushButton(editAmbienceDialog)
        self.addAmbienceButton.setGeometry(QtCore.QRect(20, 610, 101, 31))
        self.addAmbienceButton.setObjectName(_fromUtf8("addAmbienceButton"))
        self.removeAmbienceButton = QtGui.QPushButton(editAmbienceDialog)
        self.removeAmbienceButton.setGeometry(QtCore.QRect(130, 610, 111, 31))
        self.removeAmbienceButton.setObjectName(_fromUtf8("removeAmbienceButton"))
        self.previewAmbienceButton = QtGui.QPushButton(editAmbienceDialog)
        self.previewAmbienceButton.setGeometry(QtCore.QRect(560, 610, 81, 31))
        self.previewAmbienceButton.setObjectName(_fromUtf8("previewAmbienceButton"))
        self.previewSlider = QtGui.QSlider(editAmbienceDialog)
        self.previewSlider.setGeometry(QtCore.QRect(240, 650, 251, 20))
        self.previewSlider.setOrientation(QtCore.Qt.Horizontal)
        self.previewSlider.setObjectName(_fromUtf8("previewSlider"))
        self.previewFileNameLabel = QtGui.QLabel(editAmbienceDialog)
        self.previewFileNameLabel.setGeometry(QtCore.QRect(250, 620, 231, 20))
        self.previewFileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.previewFileNameLabel.setObjectName(_fromUtf8("previewFileNameLabel"))
        self.previewcurrentTimeLabel = QtGui.QLabel(editAmbienceDialog)
        self.previewcurrentTimeLabel.setGeometry(QtCore.QRect(180, 650, 51, 16))
        self.previewcurrentTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.previewcurrentTimeLabel.setObjectName(_fromUtf8("previewcurrentTimeLabel"))
        self.previewtotalTimeLabel = QtGui.QLabel(editAmbienceDialog)
        self.previewtotalTimeLabel.setGeometry(QtCore.QRect(500, 650, 41, 16))
        self.previewtotalTimeLabel.setObjectName(_fromUtf8("previewtotalTimeLabel"))
        self.topLabel3 = QtGui.QLabel(editAmbienceDialog)
        self.topLabel3.setGeometry(QtCore.QRect(24, 90, 611, 20))
        self.topLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel3.setObjectName(_fromUtf8("topLabel3"))
        self.closeButton = QtGui.QPushButton(editAmbienceDialog)
        self.closeButton.setGeometry(QtCore.QRect(570, 700, 84, 31))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.statusBar = QtGui.QLabel(editAmbienceDialog)
        self.statusBar.setGeometry(QtCore.QRect(10, 710, 541, 16))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.horizontalSlider = QtGui.QSlider(editAmbienceDialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(570, 650, 61, 20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))

        self.retranslateUi(editAmbienceDialog)
        QtCore.QMetaObject.connectSlotsByName(editAmbienceDialog)

    def retranslateUi(self, editAmbienceDialog):
        editAmbienceDialog.setWindowTitle(_translate("editAmbienceDialog", "Dialog", None))
        self.loadSelectedCutsAmbienceButton.setText(_translate("editAmbienceDialog", "Load Ambience", None))
        self.topLabel1.setText(_translate("editAmbienceDialog", "Select Cut To Edit Ambience", None))
        self.topLabel2.setText(_translate("editAmbienceDialog", "Currently Editing:", None))
        self.currentAmbienceLabel.setText(_translate("editAmbienceDialog", "%s Ambience", None))
        item = self.audioFilesTable.horizontalHeaderItem(0)
        item.setText(_translate("editAmbienceDialog", "Name", None))
        item = self.audioFilesTable.horizontalHeaderItem(1)
        item.setText(_translate("editAmbienceDialog", "Length", None))
        self.addAmbienceButton.setText(_translate("editAmbienceDialog", "Add Ambience", None))
        self.removeAmbienceButton.setText(_translate("editAmbienceDialog", "Remove Selected", None))
        self.previewAmbienceButton.setText(_translate("editAmbienceDialog", "Preview", None))
        self.previewFileNameLabel.setText(_translate("editAmbienceDialog", "Preview File Name", None))
        self.previewcurrentTimeLabel.setText(_translate("editAmbienceDialog", "00:00", None))
        self.previewtotalTimeLabel.setText(_translate("editAmbienceDialog", "99:99", None))
        self.topLabel3.setText(_translate("editAmbienceDialog", "NOTE: These Changes Cannot Be Undone", None))
        self.closeButton.setText(_translate("editAmbienceDialog", "Close", None))
        self.statusBar.setText(_translate("editAmbienceDialog", "TextLabel", None))

