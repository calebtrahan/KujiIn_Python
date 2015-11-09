# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'referencefileeditor.ui'
#
# Created: Thu Jun 18 18:10:18 2015
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

class Ui_referenceeditorDialog(object):
    def setupUi(self, referenceeditorDialog):
        referenceeditorDialog.setObjectName(_fromUtf8("referenceeditorDialog"))
        referenceeditorDialog.resize(958, 751)
        self.referencetextEditor = QtGui.QTextEdit(referenceeditorDialog)
        self.referencetextEditor.setGeometry(QtCore.QRect(40, 180, 891, 511))
        self.referencetextEditor.setObjectName(_fromUtf8("referencetextEditor"))
        self.acceptButton = QtGui.QPushButton(referenceeditorDialog)
        self.acceptButton.setGeometry(QtCore.QRect(760, 710, 85, 32))
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.cancelButton = QtGui.QPushButton(referenceeditorDialog)
        self.cancelButton.setGeometry(QtCore.QRect(860, 710, 85, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.LoadReferenceFileFrame = QtGui.QFrame(referenceeditorDialog)
        self.LoadReferenceFileFrame.setGeometry(QtCore.QRect(130, 20, 341, 141))
        self.LoadReferenceFileFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.LoadReferenceFileFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.LoadReferenceFileFrame.setObjectName(_fromUtf8("LoadReferenceFileFrame"))
        self.loadReferenceFileButton = QtGui.QPushButton(self.LoadReferenceFileFrame)
        self.loadReferenceFileButton.setGeometry(QtCore.QRect(240, 60, 85, 32))
        self.loadReferenceFileButton.setObjectName(_fromUtf8("loadReferenceFileButton"))
        self.LoadReferenceFileLabel_1 = QtGui.QLabel(self.LoadReferenceFileFrame)
        self.LoadReferenceFileLabel_1.setGeometry(QtCore.QRect(10, 40, 71, 31))
        self.LoadReferenceFileLabel_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LoadReferenceFileLabel_1.setObjectName(_fromUtf8("LoadReferenceFileLabel_1"))
        self.referenceFileSelectComboBox = QtGui.QComboBox(self.LoadReferenceFileFrame)
        self.referenceFileSelectComboBox.setGeometry(QtCore.QRect(90, 40, 131, 30))
        self.referenceFileSelectComboBox.setObjectName(_fromUtf8("referenceFileSelectComboBox"))
        self.versionSelectComboBox = QtGui.QComboBox(self.LoadReferenceFileFrame)
        self.versionSelectComboBox.setGeometry(QtCore.QRect(90, 90, 131, 30))
        self.versionSelectComboBox.setObjectName(_fromUtf8("versionSelectComboBox"))
        self.versionselectLabel = QtGui.QLabel(self.LoadReferenceFileFrame)
        self.versionselectLabel.setGeometry(QtCore.QRect(10, 90, 71, 31))
        self.versionselectLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.versionselectLabel.setObjectName(_fromUtf8("versionselectLabel"))
        self.LoadReferenceFileTopLabel = QtGui.QLabel(self.LoadReferenceFileFrame)
        self.LoadReferenceFileTopLabel.setGeometry(QtCore.QRect(10, 10, 311, 20))
        self.LoadReferenceFileTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoadReferenceFileTopLabel.setObjectName(_fromUtf8("LoadReferenceFileTopLabel"))
        self.CurrentlyEditingFrame = QtGui.QFrame(referenceeditorDialog)
        self.CurrentlyEditingFrame.setGeometry(QtCore.QRect(540, 20, 331, 141))
        self.CurrentlyEditingFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.CurrentlyEditingFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.CurrentlyEditingFrame.setObjectName(_fromUtf8("CurrentlyEditingFrame"))
        self.CurrentlyEditingTopLabel = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.CurrentlyEditingTopLabel.setGeometry(QtCore.QRect(10, 20, 311, 20))
        self.CurrentlyEditingTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentlyEditingTopLabel.setObjectName(_fromUtf8("CurrentlyEditingTopLabel"))
        self.CutNameActual = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.CutNameActual.setGeometry(QtCore.QRect(170, 60, 141, 20))
        self.CutNameActual.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.CutNameActual.setObjectName(_fromUtf8("CutNameActual"))
        self.Label_CutName = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.Label_CutName.setGeometry(QtCore.QRect(50, 60, 111, 21))
        self.Label_CutName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_CutName.setObjectName(_fromUtf8("Label_CutName"))
        self.Label_Variation = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.Label_Variation.setGeometry(QtCore.QRect(40, 100, 121, 21))
        self.Label_Variation.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Variation.setObjectName(_fromUtf8("Label_Variation"))
        self.VariationNameActual = QtGui.QLabel(self.CurrentlyEditingFrame)
        self.VariationNameActual.setGeometry(QtCore.QRect(170, 100, 141, 21))
        self.VariationNameActual.setObjectName(_fromUtf8("VariationNameActual"))

        self.retranslateUi(referenceeditorDialog)
        QtCore.QMetaObject.connectSlotsByName(referenceeditorDialog)

    def retranslateUi(self, referenceeditorDialog):
        referenceeditorDialog.setWindowTitle(_translate("referenceeditorDialog", "Dialog", None))
        self.acceptButton.setText(_translate("referenceeditorDialog", "Accept", None))
        self.cancelButton.setText(_translate("referenceeditorDialog", "Cancel", None))
        self.loadReferenceFileButton.setText(_translate("referenceeditorDialog", "Load", None))
        self.LoadReferenceFileLabel_1.setText(_translate("referenceeditorDialog", "Cut Name:", None))
        self.versionselectLabel.setText(_translate("referenceeditorDialog", "Variation:", None))
        self.LoadReferenceFileTopLabel.setText(_translate("referenceeditorDialog", "Load Reference File:", None))
        self.CurrentlyEditingTopLabel.setText(_translate("referenceeditorDialog", "Currently Editing:", None))
        self.CutNameActual.setText(_translate("referenceeditorDialog", "%s Name", None))
        self.Label_CutName.setText(_translate("referenceeditorDialog", "Cut Name:", None))
        self.Label_Variation.setText(_translate("referenceeditorDialog", "Variation:", None))
        self.VariationNameActual.setText(_translate("referenceeditorDialog", "%s Variation", None))

