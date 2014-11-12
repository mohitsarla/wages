from PyQt4 import QtCore, QtGui
from newWagesSetup import WagesSetup


class Table(WagesSetup):
    def after_popup(self,var,TableObj)   :  
        obj = Popup(self.query,var)
        obj.exec_()
        TableObj.clear()
        self.show_table(var,TableObj)
        
    def show_table(self,var,tableObj):
        
        dataList = []
        self.query.exec_("""select title_name from title where title_type='%s' ;"""%(var))
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))
        tableObj.setRowCount(len(dataList))
        for i in range(len(dataList)):            
            item = QtGui.QTableWidgetItem(dataList[i])
	    tableObj.setItem(i,0,item)               
