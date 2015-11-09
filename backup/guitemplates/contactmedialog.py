
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

class Ui_contactmedialog(object):
    def setupUi(self, contactmedialog):
        contactmedialog.setObjectName(_fromUtf8("contactmedialog"))
        contactmedialog.resize(387, 206)
        self.contactmetextBrowser = QtGui.QTextBrowser(contactmedialog)
        self.contactmetextBrowser.setGeometry(QtCore.QRect(10, 10, 371, 161))
        self.contactmetextBrowser.setObjectName(_fromUtf8("contactmetextBrowser"))
        self.contactmeOKButton = QtGui.QPushButton(contactmedialog)
        self.contactmeOKButton.setGeometry(QtCore.QRect(300, 180, 80, 23))
        self.contactmeOKButton.setObjectName(_fromUtf8("contactmeOKButton"))

        self.retranslateUi(contactmedialog)
        QtCore.QMetaObject.connectSlotsByName(contactmedialog)

    def retranslateUi(self, contactmedialog):
        contactmedialog.setWindowTitle(_translate("contactmedialog", "Dialog", None))
        self.contactmetextBrowser.setHtml(_translate("contactmedialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:9pt;\">This program has been a project for me for a couple of years now, and it\'s grown from a basic terminal application to a full-fledged program (now over 4,000 lines of code). Seeing as I\'m the sole developer, chances are, I may have made a few mistakes, and sometimes programs don\'t work as expected. If this happens, please attach your log.txt file (in the program\'s directory) and shoot me an email at calebtrahan@gmail.com. I\'ll do my best to get back to you, and resolve the problem ASAP.</span></p></body></html>", None))
        self.contactmeOKButton.setText(_translate("contactmedialog", "Close", None))

