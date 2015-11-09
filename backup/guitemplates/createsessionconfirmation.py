# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createsessionconfirmation.ui'
#
# Created: Tue Jun 16 17:50:33 2015
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(395, 550)
        Dialog.setStyleSheet(_fromUtf8("background-color:#212526;"))
        self.sessionpartsListWidget = QtGui.QListWidget(Dialog)
        self.sessionpartsListWidget.setGeometry(QtCore.QRect(30, 80, 341, 281))
        self.sessionpartsListWidget.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(42, 52, 53);"))
        self.sessionpartsListWidget.setObjectName(_fromUtf8("sessionpartsListWidget"))
        self.topLabel = QtGui.QLabel(Dialog)
        self.topLabel.setGeometry(QtCore.QRect(20, 20, 361, 20))
        self.topLabel.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"font: 12pt \"Arial Black\";"))
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName(_fromUtf8("topLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 500, 231, 37))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.buttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.buttonLayout.setMargin(0)
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        self.createButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.createButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.buttonLayout.addWidget(self.createButton)
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setStyleSheet(_fromUtf8("color: #98A6A8;\n"
"background-color: rgb(53, 63, 68);"))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.buttonLayout.addWidget(self.cancelButton)
        self.toplabel2 = QtGui.QLabel(Dialog)
        self.toplabel2.setGeometry(QtCore.QRect(20, 50, 361, 20))
        self.toplabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabel2.setObjectName(_fromUtf8("toplabel2"))
        self.ambienceLabel = QtGui.QLabel(Dialog)
        self.ambienceLabel.setGeometry(QtCore.QRect(90, 400, 101, 20))
        self.ambienceLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ambienceLabel.setObjectName(_fromUtf8("ambienceLabel"))
        self.AmbienceStatus = QtGui.QLabel(Dialog)
        self.AmbienceStatus.setGeometry(QtCore.QRect(220, 400, 71, 19))
        self.AmbienceStatus.setObjectName(_fromUtf8("AmbienceStatus"))
        self.referencefilesLabel = QtGui.QLabel(Dialog)
        self.referencefilesLabel.setGeometry(QtCore.QRect(80, 430, 111, 20))
        self.referencefilesLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.referencefilesLabel.setObjectName(_fromUtf8("referencefilesLabel"))
        self.ReferenceFilesActual = QtGui.QLabel(Dialog)
        self.ReferenceFilesActual.setGeometry(QtCore.QRect(220, 430, 58, 19))
        self.ReferenceFilesActual.setObjectName(_fromUtf8("ReferenceFilesActual"))
        self.totalsessiontimeLabel = QtGui.QLabel(Dialog)
        self.totalsessiontimeLabel.setGeometry(QtCore.QRect(80, 460, 121, 19))
        self.totalsessiontimeLabel.setObjectName(_fromUtf8("totalsessiontimeLabel"))
        self.TotalSessionTimeActual = QtGui.QLabel(Dialog)
        self.TotalSessionTimeActual.setGeometry(QtCore.QRect(220, 460, 151, 20))
        self.TotalSessionTimeActual.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TotalSessionTimeActual.setObjectName(_fromUtf8("TotalSessionTimeActual"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.topLabel.setText(_translate("Dialog", "Create This Session?", None))
        self.createButton.setText(_translate("Dialog", "CREATE", None))
        self.cancelButton.setText(_translate("Dialog", "CANCEL", None))
        self.toplabel2.setText(_translate("Dialog", "Session Parts:", None))
        self.ambienceLabel.setText(_translate("Dialog", "Ambience:", None))
        self.AmbienceStatus.setText(_translate("Dialog", "Enabled", None))
        self.referencefilesLabel.setText(_translate("Dialog", "Reference Files:", None))
        self.ReferenceFilesActual.setText(_translate("Dialog", "Disabled", None))
        self.totalsessiontimeLabel.setText(_translate("Dialog", "Total Session Time:", None))
        self.TotalSessionTimeActual.setText(_translate("Dialog", "9 Hours And 99 Minutes", None))

