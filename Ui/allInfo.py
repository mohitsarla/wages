# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allInfo.ui'
#
# Created: Mon Dec 23 16:12:46 2013
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
        Dialog.resize(874, 598)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 16))
        self.label.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.empId = QtGui.QLineEdit(Dialog)
        self.empId.setGeometry(QtCore.QRect(150, 50, 113, 20))
        self.empId.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.empId.setObjectName(_fromUtf8("empId"))
        self.name = QtGui.QLineEdit(Dialog)
        self.name.setEnabled(True)
        self.name.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.name.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.name.setObjectName(_fromUtf8("name"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_2.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.label_3.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 31, 16))
        self.label_4.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 101, 16))
        self.label_5.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.allowance = QtGui.QLineEdit(Dialog)
        self.allowance.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.allowance.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.allowance.setObjectName(_fromUtf8("allowance"))
        self.tax = QtGui.QLineEdit(Dialog)
        self.tax.setGeometry(QtCore.QRect(140, 150, 113, 20))
        self.tax.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.tax.setObjectName(_fromUtf8("tax"))
        self.deduction = QtGui.QLineEdit(Dialog)
        self.deduction.setGeometry(QtCore.QRect(140, 180, 113, 20))
        self.deduction.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.deduction.setObjectName(_fromUtf8("deduction"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Employee Record", None))
        self.label.setText(_translate("Dialog", "Employee Name", None))
        self.label_2.setText(_translate("Dialog", "Employee ID", None))
        self.label_3.setText(_translate("Dialog", "Total Allowance", None))
        self.label_4.setText(_translate("Dialog", "Tax", None))
        self.label_5.setText(_translate("Dialog", "Deduction", None))

