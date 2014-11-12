# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'departmentConfiguration.ui'
#
# Created: Sat Nov 30 16:09:58 2013
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

class Ui_Department(object):
    def setupUi(self, Department):
        Department.setObjectName(_fromUtf8("Department"))
        Department.resize(394, 412)
        self.departmentName = QtGui.QLineEdit(Department)
        self.departmentName.setGeometry(QtCore.QRect(150, 20, 131, 20))
        self.departmentName.setObjectName(_fromUtf8("departmentName"))
        self.line = QtGui.QFrame(Department)
        self.line.setGeometry(QtCore.QRect(10, 360, 371, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(Department)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.treeWidget = QtGui.QTreeWidget(Department)
        self.treeWidget.setGeometry(QtCore.QRect(10, 80, 371, 261))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.add = QtGui.QPushButton(Department)
        self.add.setGeometry(QtCore.QRect(300, 20, 81, 23))
        self.add.setObjectName(_fromUtf8("add"))
        self.close = QtGui.QPushButton(Department)
        self.close.setGeometry(QtCore.QRect(310, 380, 75, 23))
        self.close.setObjectName(_fromUtf8("close"))
        self.line_2 = QtGui.QFrame(Department)
        self.line_2.setGeometry(QtCore.QRect(0, 50, 381, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))

        self.retranslateUi(Department)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Department.reject)
        QtCore.QMetaObject.connectSlotsByName(Department)

    def retranslateUi(self, Department):
        Department.setWindowTitle(_translate("Department", "Department", None))
        self.label_2.setText(_translate("Department", "Department Name", None))
        self.treeWidget.headerItem().setText(0, _translate("Department", "Department Name", None))
        self.add.setText(_translate("Department", "Add", None))
        self.close.setText(_translate("Department", "Close", None))

