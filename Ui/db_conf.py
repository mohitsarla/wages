# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'db_conf.ui'
#
# Created: Thu Dec 19 16:59:15 2013
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

class Ui_DataBaseConfigration(object):
    def setupUi(self, DataBaseConfigration):
        DataBaseConfigration.setObjectName(_fromUtf8("DataBaseConfigration"))
        DataBaseConfigration.resize(475, 300)
        DataBaseConfigration.setMinimumSize(QtCore.QSize(475, 300))
        DataBaseConfigration.setMaximumSize(QtCore.QSize(475, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        DataBaseConfigration.setFont(font)
        DataBaseConfigration.setMouseTracking(True)
        DataBaseConfigration.setAcceptDrops(False)
        self.dbhost = QtGui.QLabel(DataBaseConfigration)
        self.dbhost.setGeometry(QtCore.QRect(70, 110, 81, 20))
        self.dbhost.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbhost.setObjectName(_fromUtf8("dbhost"))
        self.dbHost = QtGui.QLineEdit(DataBaseConfigration)
        self.dbHost.setGeometry(QtCore.QRect(200, 110, 211, 20))
        self.dbHost.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbHost.setText(_fromUtf8(""))
        self.dbHost.setObjectName(_fromUtf8("dbHost"))
        self.dbusername = QtGui.QLabel(DataBaseConfigration)
        self.dbusername.setGeometry(QtCore.QRect(70, 150, 101, 20))
        self.dbusername.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbusername.setObjectName(_fromUtf8("dbusername"))
        self.dbUser = QtGui.QLineEdit(DataBaseConfigration)
        self.dbUser.setGeometry(QtCore.QRect(200, 150, 211, 20))
        self.dbUser.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbUser.setObjectName(_fromUtf8("dbUser"))
        self.dbuserpassword = QtGui.QLabel(DataBaseConfigration)
        self.dbuserpassword.setGeometry(QtCore.QRect(70, 190, 111, 20))
        self.dbuserpassword.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbuserpassword.setObjectName(_fromUtf8("dbuserpassword"))
        self.conf_dbPassword = QtGui.QLineEdit(DataBaseConfigration)
        self.conf_dbPassword.setGeometry(QtCore.QRect(200, 190, 211, 20))
        self.conf_dbPassword.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.conf_dbPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.conf_dbPassword.setObjectName(_fromUtf8("conf_dbPassword"))
        self.dbhost_2 = QtGui.QLabel(DataBaseConfigration)
        self.dbhost_2.setGeometry(QtCore.QRect(60, 10, 391, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dbhost_2.setFont(font)
        self.dbhost_2.setStyleSheet(_fromUtf8("font: 75 20pt \"Cambria\";"))
        self.dbhost_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dbhost_2.setObjectName(_fromUtf8("dbhost_2"))
        self.dbhost_3 = QtGui.QLabel(DataBaseConfigration)
        self.dbhost_3.setGeometry(QtCore.QRect(70, 70, 111, 20))
        self.dbhost_3.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbhost_3.setObjectName(_fromUtf8("dbhost_3"))
        self.dbType = QtGui.QComboBox(DataBaseConfigration)
        self.dbType.setGeometry(QtCore.QRect(200, 70, 71, 22))
        self.dbType.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.dbType.setObjectName(_fromUtf8("dbType"))
        self.dbType.addItem(_fromUtf8(""))
        self.dbType.addItem(_fromUtf8(""))
        self.dbType.addItem(_fromUtf8(""))
        self.ok = QtGui.QPushButton(DataBaseConfigration)
        self.ok.setGeometry(QtCore.QRect(150, 250, 75, 23))
        self.ok.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.ok.setObjectName(_fromUtf8("ok"))
        self.cancel = QtGui.QPushButton(DataBaseConfigration)
        self.cancel.setGeometry(QtCore.QRect(240, 250, 75, 23))
        self.cancel.setStyleSheet(_fromUtf8("font: 75 12pt \"Cambria\";"))
        self.cancel.setObjectName(_fromUtf8("cancel"))

        self.retranslateUi(DataBaseConfigration)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), DataBaseConfigration.reject)
        QtCore.QMetaObject.connectSlotsByName(DataBaseConfigration)

    def retranslateUi(self, DataBaseConfigration):
        DataBaseConfigration.setWindowTitle(_translate("DataBaseConfigration", "Database Configuration ", None))
        self.dbhost.setText(_translate("DataBaseConfigration", "Host Name", None))
        self.dbHost.setPlaceholderText(_translate("DataBaseConfigration", "Database Host name", None))
        self.dbusername.setText(_translate("DataBaseConfigration", "Database User", None))
        self.dbUser.setPlaceholderText(_translate("DataBaseConfigration", "Database Username", None))
        self.dbuserpassword.setText(_translate("DataBaseConfigration", "User Password", None))
        self.conf_dbPassword.setPlaceholderText(_translate("DataBaseConfigration", "Database User Password", None))
        self.dbhost_2.setText(_translate("DataBaseConfigration", "Database Connection", None))
        self.dbhost_3.setText(_translate("DataBaseConfigration", "Database Type", None))
        self.dbType.setItemText(0, _translate("DataBaseConfigration", "Select", None))
        self.dbType.setItemText(1, _translate("DataBaseConfigration", "MySql", None))
        self.dbType.setItemText(2, _translate("DataBaseConfigration", "SQLite", None))
        self.ok.setText(_translate("DataBaseConfigration", "Ok", None))
        self.cancel.setText(_translate("DataBaseConfigration", "Cancel", None))

