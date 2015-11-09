# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changealertfile.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(458, 184)
        self.changealertfileAlertFileValue = QtGui.QLabel(Dialog)
        self.changealertfileAlertFileValue.setGeometry(QtCore.QRect(10, 70, 441, 21))
        self.changealertfileAlertFileValue.setAlignment(QtCore.Qt.AlignCenter)
        self.changealertfileAlertFileValue.setObjectName(_fromUtf8("changealertfileAlertFileValue"))
        self.changealertfileTopLabel = QtGui.QLabel(Dialog)
        self.changealertfileTopLabel.setGeometry(QtCore.QRect(10, 10, 441, 41))
        self.changealertfileTopLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changealertfileTopLabel.setWordWrap(True)
        self.changealertfileTopLabel.setObjectName(_fromUtf8("changealertfileTopLabel"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 140, 341, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.changealertfileButtonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.changealertfileButtonLayout.setMargin(0)
        self.changealertfileButtonLayout.setObjectName(_fromUtf8("changealertfileButtonLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.changealertfileButtonLayout.addWidget(self.pushButton)
        self.changealertfileSelectButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.changealertfileSelectButton.setObjectName(_fromUtf8("changealertfileSelectButton"))
        self.changealertfileButtonLayout.addWidget(self.changealertfileSelectButton)
        self.changealertfileCloseButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.changealertfileCloseButton.setObjectName(_fromUtf8("changealertfileCloseButton"))
        self.changealertfileButtonLayout.addWidget(self.changealertfileCloseButton)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 100, 441, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.changealertfileAlertFileValue.setText(_translate("Dialog", "New Alert File:", None))
        self.changealertfileTopLabel.setText(_translate("Dialog", "This function will change your alert file (played in between each cut practiced to let you know to change to the next one)", None))
        self.pushButton.setText(_translate("Dialog", "Change", None))
        self.changealertfileSelectButton.setText(_translate("Dialog", "Select A New Alert File", None))
        self.changealertfileCloseButton.setText(_translate("Dialog", "Close", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">New Alert File: /path/to/file.mp3 (x Seconds)</p></body></html>", None))

