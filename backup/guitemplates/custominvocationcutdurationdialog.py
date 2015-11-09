# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'custominvocationcutdurationdialog.ui'
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

class Ui_custominvocationcutdurationdialog(object):
    def setupUi(self, custominvocationcutdurationdialog):
        custominvocationcutdurationdialog.setObjectName(_fromUtf8("custominvocationcutdurationdialog"))
        custominvocationcutdurationdialog.resize(400, 213)
        self.custominvocationtopLabel = QtGui.QLabel(custominvocationcutdurationdialog)
        self.custominvocationtopLabel.setGeometry(QtCore.QRect(90, 10, 221, 16))
        self.custominvocationtopLabel.setObjectName(_fromUtf8("custominvocationtopLabel"))
        self.custominvocationcutsLabel = QtGui.QLabel(custominvocationcutdurationdialog)
        self.custominvocationcutsLabel.setGeometry(QtCore.QRect(11, 30, 381, 20))
        self.custominvocationcutsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.custominvocationcutsLabel.setObjectName(_fromUtf8("custominvocationcutsLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(custominvocationcutdurationdialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 60, 160, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.custominvocationLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.custominvocationLayout.setMargin(0)
        self.custominvocationLayout.setObjectName(_fromUtf8("custominvocationLayout"))
        self.custominvocationValue = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.custominvocationValue.setObjectName(_fromUtf8("custominvocationValue"))
        self.custominvocationLayout.addWidget(self.custominvocationValue)
        self.custominvocationminLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.custominvocationminLabel.setObjectName(_fromUtf8("custominvocationminLabel"))
        self.custominvocationLayout.addWidget(self.custominvocationminLabel)
        self.custominvocationaddButton = QtGui.QPushButton(custominvocationcutdurationdialog)
        self.custominvocationaddButton.setGeometry(QtCore.QRect(160, 170, 131, 30))
        self.custominvocationaddButton.setObjectName(_fromUtf8("custominvocationaddButton"))
        self.custominvocationcancelButton = QtGui.QPushButton(custominvocationcutdurationdialog)
        self.custominvocationcancelButton.setGeometry(QtCore.QRect(300, 170, 84, 30))
        self.custominvocationcancelButton.setObjectName(_fromUtf8("custominvocationcancelButton"))

        self.retranslateUi(custominvocationcutdurationdialog)
        QtCore.QMetaObject.connectSlotsByName(custominvocationcutdurationdialog)

    def retranslateUi(self, custominvocationcutdurationdialog):
        custominvocationcutdurationdialog.setWindowTitle(_translate("custominvocationcutdurationdialog", "Dialog", None))
        self.custominvocationtopLabel.setText(_translate("custominvocationcutdurationdialog", "How Long Would You Like To Invoke:", None))
        self.custominvocationcutsLabel.setText(_translate("custominvocationcutdurationdialog", "Cuts Here", None))
        self.custominvocationminLabel.setText(_translate("custominvocationcutdurationdialog", "min", None))
        self.custominvocationaddButton.setText(_translate("custominvocationcutdurationdialog", "ADD TO SESSION", None))
        self.custominvocationcancelButton.setText(_translate("custominvocationcutdurationdialog", "CANCEL", None))

