# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attendance.ui'
#
# Created: Mon Dec 23 19:04:38 2013
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

class Ui_attendance(object):
    def setupUi(self, attendance):
        attendance.setObjectName(_fromUtf8("attendance"))
        attendance.resize(799, 604)
        self.gridLayout_2 = QtGui.QGridLayout(attendance)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(attendance)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Kalinga"))
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.close = QtGui.QPushButton(self.frame)
        self.close.setMaximumSize(QtCore.QSize(191, 28))
        self.close.setObjectName(_fromUtf8("close"))
        self.gridLayout.addWidget(self.close, 2, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(761, 53))
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
        self.position = QtGui.QComboBox(self.groupBox)
        self.position.setGeometry(QtCore.QRect(470, 20, 101, 22))
        self.position.setObjectName(_fromUtf8("position"))
        self.shift = QtGui.QComboBox(self.groupBox)
        self.shift.setGeometry(QtCore.QRect(630, 20, 111, 22))
        self.shift.setObjectName(_fromUtf8("shift"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(590, 20, 31, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(410, 20, 61, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        self.attandance_table = QtGui.QTableWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        font.setPointSize(7)
        self.attandance_table.setFont(font)
        self.attandance_table.setObjectName(_fromUtf8("attandance_table"))
        self.attandance_table.setColumnCount(1)
        self.attandance_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(_fromUtf8("header1"))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.attandance_table.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.attandance_table, 1, 0, 1, 3)
        self.save = QtGui.QPushButton(self.frame)
        self.save.setMaximumSize(QtCore.QSize(191, 28))
        self.save.setObjectName(_fromUtf8("save"))
        self.gridLayout.addWidget(self.save, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(attendance)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Yi Baiti"))
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 1, 1, 1)
        self.leaveShort = QtGui.QTreeWidget(attendance)
        self.leaveShort.setObjectName(_fromUtf8("leaveShort"))
        self.gridLayout_2.addWidget(self.leaveShort, 1, 0, 1, 1)

        self.retranslateUi(attendance)
        QtCore.QMetaObject.connectSlotsByName(attendance)

    def retranslateUi(self, attendance):
        attendance.setWindowTitle(_translate("attendance", "Dialog", None))
        self.close.setText(_translate("attendance", "Close", None))
        self.groupBox.setTitle(_translate("attendance", "Date Seach", None))
        self.label.setText(_translate("attendance", "From", None))
        self.label_2.setText(_translate("attendance", "To", None))
        self.search.setText(_translate("attendance", "Search", None))
        self.label_4.setText(_translate("attendance", "Shift", None))
        self.label_3.setText(_translate("attendance", "Position", None))
        self.save.setText(_translate("attendance", "Save", None))
        self.label_5.setText(_translate("attendance", "Attendance", None))
        self.leaveShort.headerItem().setText(0, _translate("attendance", "Code", None))
        self.leaveShort.headerItem().setText(1, _translate("attendance", "Leave", None))

