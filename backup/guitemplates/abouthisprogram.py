# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutthisprogram.ui'
#
# Created: Wed Apr  1 19:54:19 2015
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

class Ui_aboutdialog(object):
    def setupUi(self, aboutdialog):
        aboutdialog.setObjectName(_fromUtf8("aboutdialog"))
        aboutdialog.resize(433, 259)
        self.aboutcloseButton = QtGui.QPushButton(aboutdialog)
        self.aboutcloseButton.setGeometry(QtCore.QRect(320, 220, 90, 23))
        self.aboutcloseButton.setObjectName(_fromUtf8("aboutcloseButton"))
        self.aboutlabel = QtGui.QLabel(aboutdialog)
        self.aboutlabel.setGeometry(QtCore.QRect(20, 20, 391, 21))
        self.aboutlabel.setStyleSheet(_fromUtf8("font: 14pt \"Arial Black\";"))
        self.aboutlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.aboutlabel.setObjectName(_fromUtf8("aboutlabel"))
        self.abouttext = QtGui.QTextBrowser(aboutdialog)
        self.abouttext.setGeometry(QtCore.QRect(20, 50, 391, 161))
        self.abouttext.setObjectName(_fromUtf8("abouttext"))
        self.aboutHowToUseButton = QtGui.QPushButton(aboutdialog)
        self.aboutHowToUseButton.setGeometry(QtCore.QRect(20, 220, 111, 23))
        self.aboutHowToUseButton.setObjectName(_fromUtf8("aboutHowToUseButton"))

        self.retranslateUi(aboutdialog)
        QtCore.QMetaObject.connectSlotsByName(aboutdialog)

    def retranslateUi(self, aboutdialog):
        aboutdialog.setWindowTitle(_translate("aboutdialog", "Dialog", None))
        self.aboutcloseButton.setText(_translate("aboutdialog", "Close", None))
        self.aboutlabel.setText(_translate("aboutdialog", "About This Program", None))
        self.abouttext.setHtml(_translate("aboutdialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">This program was developed to be an aid to the practitioners of the Kuji-In through the use of brainwave entrainment technology. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">Program Development By Caleb Trahan (c) 2015 All Rights Reserved</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">Programmed With </span><a href=\"https://www.python.org/\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt; text-decoration: underline; color:#f0651f;\">Python 3</span></a><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\"> And Designed With </span><a href=\"http://qt-project.org/\"><span style=\" font-family:\'Sans Serif\'; font-size:10pt; text-decoration: underline; color:#f0651f;\">Qt 4</span></a><span style=\" font-family:\'Sans Serif\'; font-size:10pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p></body></html>", None))
        self.aboutHowToUseButton.setText(_translate("aboutdialog", "Tutorials", None))

