# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advance.ui'
#
# Created: Thu Dec 19 18:31:35 2013
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
        Dialog.resize(848, 563)
        Dialog.setMinimumSize(QtCore.QSize(848, 563))
        Dialog.setMaximumSize(QtCore.QSize(848, 563))
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 831, 331))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(9)
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
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.close = QtGui.QPushButton(Dialog)
        self.close.setGeometry(QtCore.QRect(790, 520, 51, 31))
        self.close.setObjectName(_fromUtf8("close"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 520, 51, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(320, 20, 101, 16))
        self.label.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 81, 16))
        self.label_2.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(320, 80, 46, 13))
        self.label_3.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 110, 61, 16))
        self.label_4.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.name = QtGui.QLineEdit(Dialog)
        self.name.setEnabled(True)
        self.name.setGeometry(QtCore.QRect(440, 20, 113, 20))
        self.name.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.name.setObjectName(_fromUtf8("name"))
        self.empId = QtGui.QLineEdit(Dialog)
        self.empId.setGeometry(QtCore.QRect(440, 50, 113, 20))
        self.empId.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.empId.setObjectName(_fromUtf8("empId"))
        self.amount = QtGui.QLineEdit(Dialog)
        self.amount.setGeometry(QtCore.QRect(440, 110, 113, 20))
        self.amount.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.amount.setObjectName(_fromUtf8("amount"))
        self.dateEdit = QtGui.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(440, 80, 110, 22))
        self.dateEdit.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.addNew = QtGui.QPushButton(Dialog)
        self.addNew.setGeometry(QtCore.QRect(400, 140, 75, 23))
        self.addNew.setStyleSheet(_fromUtf8("font: 63 10pt \"Segoe UI Semibold\";"))
        self.addNew.setObjectName(_fromUtf8("addNew"))
        self.give = QtGui.QPushButton(Dialog)
        self.give.setGeometry(QtCore.QRect(10, 10, 191, 61))
        self.give.setObjectName(_fromUtf8("give"))
        self.search = QtGui.QPushButton(Dialog)
        self.search.setGeometry(QtCore.QRect(560, 20, 31, 23))
        self.search.setText(_fromUtf8(""))
        self.search.setObjectName(_fromUtf8("search"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Advance Payee", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Employee Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Emp ID", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Date", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Advance Amt.", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Remaining Amt.", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Paid Amt.", None))
        self.close.setText(_translate("Dialog", "Close", None))
        self.pushButton_2.setText(_translate("Dialog", "Print", None))
        self.label.setText(_translate("Dialog", "Employee Name", None))
        self.label_2.setText(_translate("Dialog", "Employee ID", None))
        self.label_3.setText(_translate("Dialog", "Date", None))
        self.label_4.setText(_translate("Dialog", "Amount", None))
        self.addNew.setText(_translate("Dialog", "Add", None))
        self.give.setText(_translate("Dialog", "Give Advance Payment", None))

