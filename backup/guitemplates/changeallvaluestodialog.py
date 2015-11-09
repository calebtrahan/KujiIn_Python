# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changeallvaluestodialog.ui'
#
# Created: Tue Jun 16 18:03:44 2015
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

class Ui_changevaluedialog(object):
    def setupUi(self, changevaluedialog):
        changevaluedialog.setObjectName(_fromUtf8("changevaluedialog"))
        changevaluedialog.resize(395, 208)
        changevaluedialog.setMinimumSize(QtCore.QSize(0, 208))
        changevaluedialog.setStyleSheet(_fromUtf8("background-color:#212526;"))
        self.changeValueTopLabel = QtGui.QLabel(changevaluedialog)
        self.changeValueTopLabel.setGeometry(QtCore.QRect(70, 30, 131, 20))
        self.changeValueTopLabel.setStyleSheet(_fromUtf8(""))
        self.changeValueTopLabel.setObjectName(_fromUtf8("changeValueTopLabel"))
        self.horizontalLayoutWidget_2 = QtGui.QWidget(changevaluedialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 337, 51))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.changeValueLayout2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.changeValueLayout2.setMargin(0)
        self.changeValueLayout2.setObjectName(_fromUtf8("changeValueLayout2"))
        self.changeValuecheckbox = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.changeValuecheckbox.setStyleSheet(_fromUtf8("color: #98A6A8;"))
        self.changeValuecheckbox.setObjectName(_fromUtf8("changeValuecheckbox"))
        self.changeValueLayout2.addWidget(self.changeValuecheckbox)
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.changeValueLayout2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.changeValueLayout2.addWidget(self.pushButton_2)
        self.changeValuespinbox = QtGui.QSpinBox(changevaluedialog)
        self.changeValuespinbox.setGeometry(QtCore.QRect(210, 30, 51, 20))
        self.changeValuespinbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.changeValuespinbox.setStyleSheet(_fromUtf8("color: #FFFFFF;\n"
"selection-color: rgb(255, 255, 255);"))
        self.changeValuespinbox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.changeValuespinbox.setObjectName(_fromUtf8("changeValuespinbox"))
        self.changeValueminuteslabel = QtGui.QLabel(changevaluedialog)
        self.changeValueminuteslabel.setGeometry(QtCore.QRect(270, 20, 91, 39))
        self.changeValueminuteslabel.setStyleSheet(_fromUtf8("color: #98A6A8;"))
        self.changeValueminuteslabel.setObjectName(_fromUtf8("changeValueminuteslabel"))
        self.retranslateUi(changevaluedialog)
        QtCore.QMetaObject.connectSlotsByName(changevaluedialog)

    def retranslateUi(self, changevaluedialog):
        changevaluedialog.setWindowTitle(_translate("changevaluedialog", "Dialog", None))
        self.changeValueTopLabel.setText(_translate("changevaluedialog", "Change All Values To:", None))
        self.changeValuecheckbox.setText(_translate("changevaluedialog", "Include Pre And Post", None))
        self.pushButton.setText(_translate("changevaluedialog", "OK", None))
        self.pushButton_2.setText(_translate("changevaluedialog", "Cancel", None))
        self.changeValueminuteslabel.setText(_translate("changevaluedialog", "mins", None))

