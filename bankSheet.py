from PyQt4 import QtCore, QtGui
from Ui.bankSheet import Ui_Dialog
import datetime

class BankSheet(QtGui.QDialog):
    def __init__(self,query,db,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.ui.date_from.setDate(datetime.datetime.today())
        self.ui.date_to.setDate(datetime.datetime.today())
        self.get_data()

    def get_data(self):
        self.query.exec_(""" select first_name,last_name,account_no from employee_information ;""")
        while self.query.next():
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0, self.query.value(0).toString()+' '+self.query.value(1).toString())
            item.setText(1, '')
            item.setText(2, self.query.value(2).toString())
