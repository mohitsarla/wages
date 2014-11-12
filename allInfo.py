from PyQt4 import QtGui,QtCore
from Ui.allInfo import Ui_Dialog


class EmployeeAllInformation(QtGui.QDialog):
    def __init__(self,query,empId,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.id = empId

        self.fun()

    def fun(self):
        print "111"
           
