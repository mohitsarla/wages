from PyQt4 import QtCore, QtGui
from Ui.listOfEmployee import Ui_Dialog
from Ui.empList import Ui_EmpList
from allInfo import EmployeeAllInformation
#from payAdvancePayment import PayAdvanceAmount

class EmployeeList(QtGui.QDialog):
    def __init__(self,query,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
       
        QtCore.QObject.connect(self.ui.comboBox,QtCore.SIGNAL("currentIndexChanged(QString)"),self.add)

        QtCore.QObject.connect(self.ui.comboBox_2,QtCore.SIGNAL("currentIndexChanged(QString)"),self.get_data)
        

    def add(self,strg) :
        self.ui.comboBox_2.show()
        self.ui.comboBox_2.clear()
        if strg == 'Payment Type Wise' :
            self.ui.comboBox_2.clear()
            li = ['Contract-Based','Salary-Based','Wages-Based'] 
            self.ui.comboBox_2.addItems(li)
        if strg == 'Shift Wise' :
            self.ui.comboBox_2.clear()
            self.titleList = []
            self.query.exec_(""" select title from regular_wages_setup ;""")
            while self.query.next():
                self.titleList.append(self.query.value(0).toString())
            self.query.exec_(""" select title from non_regular_wages_setup ;""")
            while self.query.next():
                self.titleList.append(self.query.value(0).toString())
            self.ui.comboBox_2.addItems(self.titleList)
                
    def get_data(self,strg) :
        dataList = []
        
        if  strg == 'Wages-Based' :
            
            self.query.exec_(""" select first_name,last_name,address,mobile_no1,account_no,rate,date_of_joining,employee_information_id
                                 from employee_information where payment_type='%s' """%('Wages'))

            while self.query.next():
                dataList.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString(),
                                 self.query.value(3).toString(),self.query.value(4).toString(),self.query.value(5).toString(),
                                 self.query.value(6).toString(),self.query.value(7).toInt()[0]))
            self.enter_data(dataList)
            
        if  strg == 'Salary-Based' :
            
            self.query.exec_(""" select first_name,last_name,address,mobile_no1,account_no,rate,date_of_joining,employee_information_id
                                 from employee_information where payment_type='%s' """%('Salary'))
            while self.query.next():
                dataList.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString(),
                                 self.query.value(3).toString(),self.query.value(4).toString(),self.query.value(5).toString(),
                                 self.query.value(6).toString(),self.query.value(7).toInt()[0]))

            self.enter_data(dataList) 
        if  strg == 'Contract-Based' :
            
            self.query.exec_(""" select first_name,last_name,address,mobile_no1,account_no,rate,date_of_joining,employee_information_id
                                 from employee_information where payment_type='%s' """%('Contract'))
            while self.query.next():
                dataList.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString(),
                                 self.query.value(3).toString(),self.query.value(4).toString(),self.query.value(5).toString(),
                                 self.query.value(6).toString(),self.query.value(7).toInt()[0]))
            self.enter_data(dataList)

        if self.titleList :
            ids = []
            for i in range(len(self.titleList)) :
                try :
                    self.query.exec_(""" select regular_wages_setup_id from regular_wages_setup where title='%s' ;"""%(self.titleList[i]))
                    while self.query.next():
                        ids.append(self.query.value(0).toInt()[0])
                    self.query.exec_(""" select non_regular_wages_setup_id from non_regular_wages_setup where title='%s' ;"""%(self.titleList[i]))
                    while self.query.next():
                        ids.append(self.query.value(0).toInt()[0])
                except Exception, e:
                    print e
            print "lis is",ids
            for i in range(len(ids)):
                try :
                    dataList = []
                    self.query.exec_(""" select first_name,last_name,address,mobile_no1,account_no,rate,date_of_joining,employee_information_id
                                 from employee_information where regular_wages_setup_id = %s """%(ids[i]))
                    while self.query.next():
                        dataList.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString(),
                                 self.query.value(3).toString(),self.query.value(4).toString(),self.query.value(5).toString(),
                                 self.query.value(6).toString(),self.query.value(7).toInt()[0]))
                        
                    self.query.exec_(""" select first_name,last_name,address,mobile_no1,account_no,rate,date_of_joining,employee_information_id
                                 from employee_information where non_regular_wages_setup_id = %s """%(ids[i]))
                    while self.query.next():
                        dataList.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString(),
                                 self.query.value(3).toString(),self.query.value(4).toString(),self.query.value(5).toString(),
                                 self.query.value(6).toString(),self.query.value(7).toInt()[0]))                    
                except Exception, e:
                    print e                    

                self.enter_data(dataList)
                
    def enter_data(self,li):
        #self.ui.tableWidget.clear()
        getList = li
        self.ui.tableWidget.setRowCount(len(li))
        for i in range(len(li)):
            for j in range(len(li[i][:-1])):
                item = QtGui.QTableWidgetItem(str(li[i][j]))
	        self.ui.tableWidget.setItem(i,j,item)  

class Short_EmployeeList(QtGui.QDialog):
    def __init__(self,query,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_EmpList()
        self.ui.setupUi(self)
        self.query = query

        QtCore.QObject.connect(self.ui.lineEdit,QtCore.SIGNAL("textChanged(QString)"),self.filter_data)
        QtCore.QObject.connect(self.ui.treeWidget,QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"),self.send_id)
	     
        
        self.showdata()


    def send_id(self,item,text) :
        name = item.text(0)
        empid = item.text(1)
        self.li = [name,empid]
        self.close()


    def get_list(self):
        return self.li
    
    def filter_data(self,var):
        li = []
        self.query.exec_(""" select first_name, last_name,employee_id from employee_information
                             where first_name LIKE '%s%%' or employee_id LIKE '%s%%' """%(var,var)) 
        while self.query.next():
            self.ui.treeWidget.clear()
            li.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString()))
        for i in li:
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0,i[0])
            item.setText(1,i[1])
            
    def showdata(self):
        li =[]
        self.query.exec_(""" select concat(first_name,' ',last_name),employee_id from employee_information ; """)
        while self.query.next():
            li.append((self.query.value(0).toString(),self.query.value(1).toString()))
        for i in li:
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0,i[0])
            item.setText(1,i[1])

class AllInfo(QtGui.QDialog):
    def __init__(self,query,empId,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_EmpList()
        self.ui.setupUi(self)
        self.query = query

        QtCore.QObject.connect(self.ui.lineEdit,QtCore.SIGNAL("textChanged(QString)"),self.filter_data)
        QtCore.QObject.connect(self.ui.treeWidget,QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem*,int)"),self.send_id)
	     
        
        self.showdata()


    def send_id(self,item,text) :
        name = item.text(0)
        empid = item.text(1)
        self.li = [name,empid]
        self.query.exec_(""" select employee_information_id from employee_information where employee_id='%s' """%(empid))
        while self.query.next():
            empId = self.query.value(0).toString()
        
        obj = EmployeeAllInformation(self.query,empId)
        obj.exec_()
        


    def get_list(self):
        return self.li
    
    def filter_data(self,var):
        li = []
        self.query.exec_(""" select first_name, last_name,employee_id from employee_information
                             where first_name LIKE '%s%%' or employee_id LIKE '%s%%' """%(var,var)) 
        while self.query.next():
            self.ui.treeWidget.clear()
            li.append((self.query.value(0).toString()+' '+self.query.value(1).toString(),self.query.value(2).toString()))
        for i in li:
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0,i[0])
            item.setText(1,i[1])
            
    def showdata(self):
        li =[]
        self.query.exec_(""" select concat(first_name,' ',last_name),employee_id from employee_information ; """)
        while self.query.next():
            li.append((self.query.value(0).toString(),self.query.value(1).toString()))
        for i in li:
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0,i[0])
            item.setText(1,i[1])


    
    
