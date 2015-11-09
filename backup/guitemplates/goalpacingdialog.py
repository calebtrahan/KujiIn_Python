# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'goalpacingdialog.ui'
#
# Created: Tue Dec 23 17:47:59 2014
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

class Ui_goalpacingDialog(object):
    def setupUi(self, goalpacingDialog):
        goalpacingDialog.setObjectName(_fromUtf8("goalpacingDialog"))
        goalpacingDialog.resize(400, 258)
        self.goalpacingtopLabel = QtGui.QLabel(goalpacingDialog)
        self.goalpacingtopLabel.setGeometry(QtCore.QRect(10, 20, 371, 81))
        self.goalpacingtopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goalpacingtopLabel.setWordWrap(True)
        self.goalpacingtopLabel.setObjectName(_fromUtf8("goalpacingtopLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(goalpacingDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 110, 171, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.goalpacingValuesLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.goalpacingValuesLayout.setMargin(0)
        self.goalpacingValuesLayout.setObjectName(_fromUtf8("goalpacingValuesLayout"))
        self.goalpaincgValue = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.goalpaincgValue.setMaximum(7)
        self.goalpaincgValue.setObjectName(_fromUtf8("goalpaincgValue"))
        self.goalpacingValuesLayout.addWidget(self.goalpaincgValue)
        self.goalpacingdaysLabel = QtGui.QLabel(self.horizontalLayoutWidget)
        self.goalpacingdaysLabel.setObjectName(_fromUtf8("goalpacingdaysLabel"))
        self.goalpacingValuesLayout.addWidget(self.goalpacingdaysLabel)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(goalpacingDialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(200, 190, 188, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.goalpacingButtonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.goalpacingButtonLayout.setMargin(0)
        self.goalpacingButtonLayout.setObjectName(_fromUtf8("goalpacingButtonLayout"))
        self.goalpacingcalculateButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.goalpacingcalculateButton.setObjectName(_fromUtf8("goalpacingcalculateButton"))
        self.goalpacingButtonLayout.addWidget(self.goalpacingcalculateButton)
        self.goalpacingcancelButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.goalpacingcancelButton.setObjectName(_fromUtf8("goalpacingcancelButton"))
        self.goalpacingButtonLayout.addWidget(self.goalpacingcancelButton)

        self.retranslateUi(goalpacingDialog)
        QtCore.QMetaObject.connectSlotsByName(goalpacingDialog)

    def retranslateUi(self, goalpacingDialog):
        goalpacingDialog.setWindowTitle(_translate("goalpacingDialog", "Dialog", None))
        self.goalpacingtopLabel.setText(_translate("goalpacingDialog", "In Order To Calculate How Much You Need To Meditate To Reach Your Goals, I Need To Know How Many Days A Week You Will Be Meditating", None))
        self.goalpacingdaysLabel.setText(_translate("goalpacingDialog", "Days A Week", None))
        self.goalpacingcalculateButton.setText(_translate("goalpacingDialog", "CALCULATE", None))
        self.goalpacingcancelButton.setText(_translate("goalpacingDialog", "CANCEl", None))

