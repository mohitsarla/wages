# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commonDialog.ui'
#
# Created: Sat Dec 21 14:04:20 2013
#      by: PyQt4 UI code generator 4.10.2
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
        Dialog.resize(332, 117)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 61, 21))
        self.label.setStyleSheet(_fromUtf8("font: 63 12pt \"Segoe UI Semibold\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.title = QtGui.QLineEdit(Dialog)
        self.title.setGeometry(QtCore.QRect(140, 30, 131, 20))
        self.title.setObjectName(_fromUtf8("title"))
        self.ok = QtGui.QPushButton(Dialog)
        self.ok.setGeometry(QtCore.QRect(130, 80, 61, 23))
        self.ok.setObjectName(_fromUtf8("ok"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Title", None))
        self.ok.setText(_translate("Dialog", "Ok", None))

