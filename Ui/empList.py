# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empList.ui'
#
# Created: Thu Dec 19 12:37:12 2013
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

class Ui_EmpList(object):
    def setupUi(self, EmpList):
        EmpList.setObjectName(_fromUtf8("EmpList"))
        EmpList.resize(575, 547)
        self.label = QtGui.QLabel(EmpList)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 21))
        self.label.setStyleSheet(_fromUtf8("font: 12pt \"Segoe UI Symbol\";\n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(EmpList)
        self.lineEdit.setGeometry(QtCore.QRect(110, 23, 151, 21))
        self.lineEdit.setStyleSheet(_fromUtf8("font: 12pt \"Segoe UI Symbol\";"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.treeWidget = QtGui.QTreeWidget(EmpList)
        self.treeWidget.setGeometry(QtCore.QRect(0, 70, 571, 471))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))

        self.retranslateUi(EmpList)
        QtCore.QMetaObject.connectSlotsByName(EmpList)

    def retranslateUi(self, EmpList):
        EmpList.setWindowTitle(_translate("EmpList", "Employee List", None))
        self.label.setText(_translate("EmpList", "Search", None))
        self.treeWidget.headerItem().setText(0, _translate("EmpList", "Employee Name", None))
        self.treeWidget.headerItem().setText(1, _translate("EmpList", "Employee ID", None))

