# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advance_amount_pay.ui'
#
# Created: Wed Dec 18 15:04:10 2013
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
        Dialog.resize(783, 512)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 751, 391))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.close = QtGui.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(680, 480, 75, 23))
        self.close.setStyleSheet(_fromUtf8("font: 63 12pt \"Segoe UI Semibold\";"))
        self.close.setObjectName(_fromUtf8("close"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 751, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(180, 24, 201, 16))
        self.label.setStyleSheet(_fromUtf8("font: 63 12pt \"Segoe UI Semibold\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.amount = QtGui.QLineEdit(self.groupBox)
        self.amount.setGeometry(QtCore.QRect(416, 24, 113, 20))
        self.amount.setStyleSheet(_fromUtf8("font: 63 12pt \"Segoe UI Semibold\";"))
        self.amount.setObjectName(_fromUtf8("amount"))
        self.add = QtGui.QPushButton(self.groupBox)
        self.add.setGeometry(QtCore.QRect(581, 22, 75, 23))
        self.add.setStyleSheet(_fromUtf8("font: 63 12pt \"Segoe UI Semibold\";"))
        self.add.setObjectName(_fromUtf8("add"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Advance Amount Pay", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Employee Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Employee ID", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "  Remaining Amount", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Paid Amount", None))
        self.close.setText(_translate("Dialog", "Close", None))
        self.groupBox.setTitle(_translate("Dialog", "Payment Information", None))
        self.label.setText(_translate("Dialog", "Enter Amount to be Paid :", None))
        self.add.setText(_translate("Dialog", "Add", None))

