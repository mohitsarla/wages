from PyQt4 import QtCore, QtGui
from Ui.statement import Ui_Dialog

class Statement(QtGui.QDialog):
    def __init__(self,query,getId,parent = None):   ### var is the id from the takeAdvancePayment
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.id = getId
        print "--------",self.id
        self.get_data()
        
    def get_data(self) :    
        self.query.exec_("""select date,pay_amount from pay_advance_amount where advance_amount_id= %s """%(int(self.id)))
        print self.query.isActive()
        while self.query.next():
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0,str(self.query.value(0).toString()))
            item.setText(1,str(self.query.value(1).toString()))
                         
