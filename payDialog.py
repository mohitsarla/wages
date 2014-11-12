from PyQt4 import QtCore, QtGui
from Ui.payDialog import Ui_Dialog
import datetime

class PayPopUp(QtGui.QDialog):
    def __init__(self,query,var,amt,parent = None):   ### var is the id from the takeAdvancePayment
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.id = var
        self.ui.remaining_amount.setText(amt)
        QtCore.QObject.connect(self.ui.addNew, QtCore.SIGNAL("clicked()"), self.pay)
        self.ui.date.setDate(datetime.datetime.today())  

        print self.id
    def pay(self):
        
        self.query.exec_(""" insert into pay_advance_amount(date,pay_amount,advance_amount_id) values('%s','%s',%s) """
                                                           %(str(self.ui.date.date().toPyDate()), 
                                                             self.ui.amount.text(),
                                                             int(self.id)))

        self.ui.amount.clear(),self.ui.remaining_amount.clear()
        QtGui.QMessageBox.information(self,'Message','Pay Successfully !!!')
        self.close()
