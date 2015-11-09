# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcomescreen.ui'
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

class Ui_welcomedialog(object):
    def setupUi(self, welcomedialog):
        welcomedialog.setObjectName(_fromUtf8("welcomedialog"))
        welcomedialog.resize(561, 244)
        self.welcometextBrowser = QtGui.QTextBrowser(welcomedialog)
        self.welcometextBrowser.setGeometry(QtCore.QRect(10, 10, 541, 191))
        self.welcometextBrowser.setObjectName(_fromUtf8("welcometextBrowser"))
        self.horizontalLayoutWidget = QtGui.QWidget(welcomedialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 200, 181, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.welcomebuttonLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.welcomebuttonLayout.setMargin(0)
        self.welcomebuttonLayout.setObjectName(_fromUtf8("welcomebuttonLayout"))
        self.welcometutorialsButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.welcometutorialsButton.setObjectName(_fromUtf8("welcometutorialsButton"))
        self.welcomebuttonLayout.addWidget(self.welcometutorialsButton)
        self.welcomecloseButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.welcomecloseButton.setObjectName(_fromUtf8("welcomecloseButton"))
        self.welcomebuttonLayout.addWidget(self.welcomecloseButton)

        welcomedialog.setWindowTitle(_translate("welcomedialog", "Dialog", None))
        self.welcometextBrowser.setHtml(_translate("welcomedialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hello And Welcome To The Kuji-In Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I designed this program to be an aid to fellow practitioners of the Kuji-In through the use of brainwave entrainment technology.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I have packed many features into this program, such as random ambience generation during the session, a goal setting and achieving feature, a non-invasive way to display information during the session, and an export feature if you want to take your created sessions on the go and a few more.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">I have included short tutorials to get you up to speed on how to use the various features of this program. Click the &quot;Tutorials\' button below to read them, and get started.</p></body></html>", None))
        self.welcometutorialsButton.setText(_translate("welcomedialog", "Tutorials", None))
        self.welcomecloseButton.setText(_translate("welcomedialog", "Close", None))

