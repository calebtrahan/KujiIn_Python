# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\cutselector.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_cutselectorDialog(object):
    def setupUi(self, cutselectorDialog):
        cutselectorDialog.setObjectName(_fromUtf8("cutselectorDialog"))
        cutselectorDialog.resize(627, 139)
        self.generalcheckbox = QtGui.QCheckBox(cutselectorDialog)
        self.generalcheckbox.setGeometry(QtCore.QRect(450, 70, 171, 20))
        self.generalcheckbox.setObjectName(_fromUtf8("generalcheckbox"))
        self.descriptionLabel = QtGui.QLabel(cutselectorDialog)
        self.descriptionLabel.setGeometry(QtCore.QRect(10, 0, 611, 31))
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.OKButton = QtGui.QPushButton(cutselectorDialog)
        self.OKButton.setGeometry(QtCore.QRect(450, 100, 84, 31))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.cancelButton = QtGui.QPushButton(cutselectorDialog)
        self.cancelButton.setGeometry(QtCore.QRect(540, 100, 84, 31))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayoutWidget = QtGui.QWidget(cutselectorDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 611, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.presession = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.presession.setObjectName(_fromUtf8("presession"))
        self.horizontalLayout.addWidget(self.presession)
        self.rin = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.rin.setObjectName(_fromUtf8("rin"))
        self.horizontalLayout.addWidget(self.rin)
        self.kyo = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.kyo.setObjectName(_fromUtf8("kyo"))
        self.horizontalLayout.addWidget(self.kyo)
        self.toh = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.toh.setObjectName(_fromUtf8("toh"))
        self.horizontalLayout.addWidget(self.toh)
        self.sha = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.sha.setObjectName(_fromUtf8("sha"))
        self.horizontalLayout.addWidget(self.sha)
        self.kai = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.kai.setObjectName(_fromUtf8("kai"))
        self.horizontalLayout.addWidget(self.kai)
        self.jin = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.jin.setObjectName(_fromUtf8("jin"))
        self.horizontalLayout.addWidget(self.jin)
        self.retsu = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.retsu.setObjectName(_fromUtf8("retsu"))
        self.horizontalLayout.addWidget(self.retsu)
        self.zai = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.zai.setObjectName(_fromUtf8("zai"))
        self.horizontalLayout.addWidget(self.zai)
        self.zen = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.zen.setObjectName(_fromUtf8("zen"))
        self.horizontalLayout.addWidget(self.zen)
        self.postsession = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.postsession.setObjectName(_fromUtf8("postsession"))
        self.horizontalLayout.addWidget(self.postsession)

        self.retranslateUi(cutselectorDialog)
        QtCore.QMetaObject.connectSlotsByName(cutselectorDialog)

    def retranslateUi(self, cutselectorDialog):
        cutselectorDialog.setWindowTitle(_translate("cutselectorDialog", "Dialog", None))
        self.generalcheckbox.setText(_translate("cutselectorDialog", "General (Unspecific Ambience)", None))
        self.descriptionLabel.setText(_translate("cutselectorDialog", "Please Select Which Cut(s) You Would Like To Add Ambience To:", None))
        self.OKButton.setText(_translate("cutselectorDialog", "OK", None))
        self.cancelButton.setText(_translate("cutselectorDialog", "Cancel", None))
        self.presession.setText(_translate("cutselectorDialog", "Pre-Session", None))
        self.rin.setText(_translate("cutselectorDialog", "Rin", None))
        self.kyo.setText(_translate("cutselectorDialog", "Kyo", None))
        self.toh.setText(_translate("cutselectorDialog", "Toh", None))
        self.sha.setText(_translate("cutselectorDialog", "Sha", None))
        self.kai.setText(_translate("cutselectorDialog", "Kai", None))
        self.jin.setText(_translate("cutselectorDialog", "Jin", None))
        self.retsu.setText(_translate("cutselectorDialog", "Retsu", None))
        self.zai.setText(_translate("cutselectorDialog", "Zai", None))
        self.zen.setText(_translate("cutselectorDialog", "Zen", None))
        self.postsession.setText(_translate("cutselectorDialog", "Post-Session", None))

