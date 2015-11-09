# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setgoaldialog.ui'
#
# Created: Tue Dec 23 18:15:13 2014
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

class Ui_setgoalsdialog(object):
    def setupUi(self, setgoalsdialog):
        setgoalsdialog.setObjectName(_fromUtf8("setgoalsdialog"))
        setgoalsdialog.resize(434, 241)
        self.setgoaldialogtopLabel = QtGui.QLabel(setgoalsdialog)
        self.setgoaldialogtopLabel.setGeometry(QtCore.QRect(40, 30, 381, 16))
        self.setgoaldialogtopLabel.setObjectName(_fromUtf8("setgoaldialogtopLabel"))
        self.setgoaldialoggoalLabel = QtGui.QLabel(setgoalsdialog)
        self.setgoaldialoggoalLabel.setGeometry(QtCore.QRect(130, 70, 59, 15))
        self.setgoaldialoggoalLabel.setObjectName(_fromUtf8("setgoaldialoggoalLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(setgoalsdialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(100, 90, 177, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.setgoalsdialoggoallayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.setgoalsdialoggoallayout.setMargin(0)
        self.setgoalsdialoggoallayout.setObjectName(_fromUtf8("setgoalsdialoggoallayout"))
        self.setgoaldialogvalue = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.setgoaldialogvalue.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.setgoaldialogvalue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.setgoaldialogvalue.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.setgoaldialogvalue.setObjectName(_fromUtf8("setgoaldialogvalue"))
        self.setgoalsdialoggoallayout.addWidget(self.setgoaldialogvalue)
        self.setgoaldialoghrslabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.setgoaldialoghrslabel.setObjectName(_fromUtf8("setgoaldialoghrslabel"))
        self.setgoalsdialoggoallayout.addWidget(self.setgoaldialoghrslabel)
        self.setgoaldialogDueDate = QtGui.QDateEdit(setgoalsdialog)
        self.setgoaldialogDueDate.setGeometry(QtCore.QRect(220, 100, 110, 22))
        self.setgoaldialogDueDate.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.setgoaldialogDueDate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.setgoaldialogDueDate.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.setgoaldialogDueDate.setDisplayFormat(_fromUtf8(""))
        self.setgoaldialogDueDate.setObjectName(_fromUtf8("setgoaldialogDueDate"))
        self.setgoalduedateLabel = QtGui.QLabel(setgoalsdialog)
        self.setgoalduedateLabel.setGeometry(QtCore.QRect(240, 70, 61, 20))
        self.setgoalduedateLabel.setObjectName(_fromUtf8("setgoalduedateLabel"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(setgoalsdialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 180, 334, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.setdialogbuttonslayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.setdialogbuttonslayout.setMargin(0)
        self.setdialogbuttonslayout.setObjectName(_fromUtf8("setdialogbuttonslayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.setdialogbuttonslayout.addWidget(self.pushButton)
        self.setgoaldialogAcceptButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.setgoaldialogAcceptButton.setObjectName(_fromUtf8("setgoaldialogAcceptButton"))
        self.setdialogbuttonslayout.addWidget(self.setgoaldialogAcceptButton)
        self.setgoaldialogCancelButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.setgoaldialogCancelButton.setObjectName(_fromUtf8("setgoaldialogCancelButton"))
        self.setdialogbuttonslayout.addWidget(self.setgoaldialogCancelButton)

        self.retranslateUi(setgoalsdialog)
        QtCore.QMetaObject.connectSlotsByName(setgoalsdialog)

    def retranslateUi(self, setgoalsdialog):
        setgoalsdialog.setWindowTitle(_translate("setgoalsdialog", "Dialog", None))
        self.setgoaldialogtopLabel.setText(_translate("setgoalsdialog", "You Are Currently At num Hours. Please Set A New Goal:", None))
        self.setgoaldialoggoalLabel.setText(_translate("setgoalsdialog", "GOAL", None))
        self.setgoaldialoghrslabel.setText(_translate("setgoalsdialog", "hrs", None))
        self.setgoalduedateLabel.setText(_translate("setgoalsdialog", "Due Date", None))
        self.pushButton.setText(_translate("setgoalsdialog", "VIEW CURRENT GOALS", None))
        self.setgoaldialogAcceptButton.setText(_translate("setgoalsdialog", "ACCEPT", None))
        self.setgoaldialogCancelButton.setText(_translate("setgoalsdialog", "CANCEL", None))

