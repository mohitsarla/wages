from PyQt4 import QtCore, QtGui
from Ui.nonRegularEmployee import Ui_Dialog
import testdb
class NonRegularEmployee(QtGui.QDialog):
    def __init__(self,query,db,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query

        self.add_shift()
        QtCore.QObject.connect(self.ui.comboBox,QtCore.SIGNAL('currentIndexChanged(QString)'),self.get_emp)
        QtCore.QObject.connect(self.ui.save,QtCore.SIGNAL("clicked()"),self.onclick_save)
       

    def add_shift(self):
        self.shiftList = []
        self.query.exec_(""" select title from non_regular_wages_setup ;""")
        while self.query.next():
            self.shiftList.append(self.query.value(0).toString())
        self.ui.comboBox.addItems(self.shiftList)

        dataList = []
        self.query.exec_(""" select employee_name,employee_id,salary,date,bonus,comissions,tips from non_regular_wages_employee_info ;""")
        while self.query.next():
            dataList.append((self.query.value(0).toString(),self.query.value(1).toString(),self.query.value(2).toString(),self.query.value(3).toString(),
                             self.query.value(4).toString(),self.query.value(5).toString(),self.query.value(6).toString()))
        self.ui.tableWidget_3.setRowCount(len(dataList))
        for i in range(len(dataList)):
            for j in range(len(dataList[i])):
                item = QtGui.QTableWidgetItem(str(dataList[i][j]))
	        self.ui.tableWidget_3.setItem(i,j,item) 
     
    def get_emp(self,var):
        print "vaar is",var
        dataList = []
        self.query.exec_(""" select non_regular_wages_setup_id from non_regular_wages_setup where  title = '%s' """%(var))
        while self.query.next():
            self.id = self.query.value(0).toInt()[0]
            print "====",self.id
            self.query.exec_(""" select first_name,last_name,employee_id,rate from employee_information where non_regular_wages_setup_id = %s  """%(self.id))
            while self.query.next():
                dataList.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString(),self.query.value(3).toString()))
  
        self.ui.tableWidget_3.setRowCount(len(dataList))
        for i in range(len(dataList)):
            for j in range(len(dataList[i])):
                item = QtGui.QTableWidgetItem(str(dataList[i][j]))
	        self.ui.tableWidget_3.setItem(i,j,item)   
                
    def onclick_save(self) :
        self.ui.save.setEnabled(False)
	li = []
	for row in range(self.ui.tableWidget_3.rowCount()):
	    rowdata = []
	    for column in range(self.ui.tableWidget_3.columnCount()):
		item = self.ui.tableWidget_3.item(row,column)
		rowdata.append(str(item.text()))
            li.append(tuple(rowdata))	    
	print "--------------",li
	for i in li:
            print "i is",i
            self.query.exec_(""" insert into non_regular_wages_employee_info (title,employee_name,employee_id,salary,date,bonus,comissions,tips)
                                  values('%s','%s','%s','%s','%s','%s','%s','%s')"""%(self.ui.comboBox.currentText(),i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
            print self.query.isActive()
        QtGui.QMessageBox.information(self,'Message','Record Inserted Successfully !!!') 
