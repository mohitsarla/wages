# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bankSheet.ui'
#
# Created: Sun Dec 15 19:41:17 2013
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
        Dialog.resize(592, 554)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(10, 70, 571, 431))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 510, 51, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 510, 51, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 581, 53))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setChecked(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.date_from = QtGui.QDateEdit(self.groupBox)
        self.date_from.setGeometry(QtCore.QRect(50, 20, 91, 22))
        self.date_from.setCalendarPopup(True)
        self.date_from.setObjectName(_fromUtf8("date_from"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 21, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.date_to = QtGui.QDateEdit(self.groupBox)
        self.date_to.setGeometry(QtCore.QRect(180, 20, 91, 22))
        self.date_to.setAutoFillBackground(False)
        self.date_to.setCalendarPopup(True)
        self.date_to.setObjectName(_fromUtf8("date_to"))
        self.search = QtGui.QPushButton(self.groupBox)
        self.search.setGeometry(QtCore.QRect(280, 20, 76, 24))
        self.search.setObjectName(_fromUtf8("search"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "Employee Name", None))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Gross Pay", None))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Account No", None))
        self.pushButton.setText(_translate("Dialog", "Close", None))
        self.pushButton_2.setText(_translate("Dialog", "Print", None))
        self.groupBox.setTitle(_translate("Dialog", "Date Seach", None))
        self.label.setText(_translate("Dialog", "From", None))
        self.label_2.setText(_translate("Dialog", "To", None))
        self.search.setText(_translate("Dialog", "Search", None))

