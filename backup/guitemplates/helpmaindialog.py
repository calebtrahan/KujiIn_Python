# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpmaindialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(343, 396)
        self.helptopLabel = QtGui.QLabel(Dialog)
        self.helptopLabel.setGeometry(QtCore.QRect(40, 0, 271, 31))
        self.helptopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.helptopLabel.setObjectName(_fromUtf8("helptopLabel"))
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 29, 271, 331))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.helpbuttonsLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.helpbuttonsLayout.setMargin(0)
        self.helpbuttonsLayout.setObjectName(_fromUtf8("helpbuttonsLayout"))
        self.helpcreatingsessionsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpcreatingsessionsButton.setObjectName(_fromUtf8("helpcreatingsessionsButton"))
        self.helpbuttonsLayout.addWidget(self.helpcreatingsessionsButton)
        self.helpaddingambienceButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpaddingambienceButton.setObjectName(_fromUtf8("helpaddingambienceButton"))
        self.helpbuttonsLayout.addWidget(self.helpaddingambienceButton)
        self.helpreferencefilesButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpreferencefilesButton.setObjectName(_fromUtf8("helpreferencefilesButton"))
        self.helpbuttonsLayout.addWidget(self.helpreferencefilesButton)
        self.helpplayingsessionsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpplayingsessionsButton.setObjectName(_fromUtf8("helpplayingsessionsButton"))
        self.helpbuttonsLayout.addWidget(self.helpplayingsessionsButton)
        self.helpexportingsessionsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpexportingsessionsButton.setObjectName(_fromUtf8("helpexportingsessionsButton"))
        self.helpbuttonsLayout.addWidget(self.helpexportingsessionsButton)
        self.helpgoalsButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpgoalsButton.setObjectName(_fromUtf8("helpgoalsButton"))
        self.helpbuttonsLayout.addWidget(self.helpgoalsButton)
        self.helpContactingMeButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.helpContactingMeButton.setObjectName(_fromUtf8("helpContactingMeButton"))
        self.helpbuttonsLayout.addWidget(self.helpContactingMeButton)
        self.helpcloseButton = QtGui.QPushButton(Dialog)
        self.helpcloseButton.setGeometry(QtCore.QRect(250, 360, 84, 30))
        self.helpcloseButton.setObjectName(_fromUtf8("helpcloseButton"))
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.helptopLabel.setText(_translate("Dialog", "TUTORIALS", None))
        self.helpcreatingsessionsButton.setText(_translate("Dialog", "Creating Sessions", None))
        self.helpaddingambienceButton.setText(_translate("Dialog", "Adding Ambience", None))
        self.helpreferencefilesButton.setText(_translate("Dialog", "Reference Files", None))
        self.helpplayingsessionsButton.setText(_translate("Dialog", "Playing Sessions", None))
        self.helpexportingsessionsButton.setText(_translate("Dialog", "Exporting Sessions", None))
        self.helpgoalsButton.setText(_translate("Dialog", "Goals", None))
        self.helpContactingMeButton.setText(_translate("Dialog", "Contacting Me", None))
        self.helpcloseButton.setText(_translate("Dialog", "CLOSE", None))

