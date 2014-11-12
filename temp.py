from PyQt4 import QtCore, QtGui
from Ui.advance import Ui_Dialog
import datetime

class AdvancePayment(QtGui.QDialog):
    def __init__(self,query,db,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.i = 0
        QtCore.QObject.connect(self.ui.addNew, QtCore.SIGNAL("clicked()"), self.addData)
        self.ui.tableWidget.setRowCount(1)
        self.ui.dateEdit.setDate(datetime.datetime.today())
        self.tableWidget = self.ui.tableWidget
        item = QtGui.QTableWidgetItem('sdfsdf')
	self.ui.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem(str('sdfsdfsdf'))
	self.ui.tableWidget.setItem(1,0,item) 	
        #self.showTable()

    def showTable(self):
        query = '''  select advance_amount_id, concat(employee_information.first_name, ' ', employee_information.last_name),
                     employee_information.employee_id, date, amount from advance_amount join employee_information
                     on advance_amount.employee_information_id = employee_information.employee_information_id;'''
        self.query.exec_(query)
        count = 0
        tempList = []
        while self.query.next():
            tl = [str(self.query.value(dt).toString()) for dt in range(0, 5)]
            tempList.append(tl)
        self.ui.tableWidget.setRowCount(len(tempList))
        for index1, data in enumerate(tempList):
            for index2, dt in enumerate(data):
               item = QtGui.QTableWidgetItem(dt)
	       self.ui.tableWidget.setItem(index1 + 1, index2, item)
	    '''   
	    edit = QtGui.QPushButton(self.ui.tableWidget)
            edit.setText('Edit')
            edit.setObjectName("edit_%s"%str(self.query.value(dt).toString()))
            self.ui.tableWidget.setCellWidget(count, 4, edit)
            QtCore.QObject.connect(edit, QtCore.SIGNAL("clicked()"), self.editData)
           '''         
    def editData(self):
        dataList = [] 
        cId =  self.sender().objectName().replace("edit_", "")
        print cId, "sdfsdfsdfd"
        query_1 = self.query
        query_2 = self.query
        query_1.exec_("select employee_information_id, date, amount from advance_amount ;")
        while query_1.next() :
            date,amt = query_1.value(1).toString(),query_2.value(2).toString()
            query_2.exec_("select first_name,last_name,employee_id from employee_information where employee_information_id=%s "%(query_1.value(0).toInt()[0]))
            while query_2.next():
                dataList.append((query_2.value(0).toString()+' '+query_2.value(1).toString(),query_2.value(2).toString(),date,amt))
        print "datalist-----in edit",dataList
        self.ui.empId.setText(str(dataList[0][1]))
        li= str(dataList[0][2]).split('-')
        print "-----",li
        a= datetime.datetime(year = int(li[0]),month = int(li[1]), day = int(li[2]))
        self.ui.dateEdit.setDate(a)
        self.ui.name.setText(dataList[0][0])
        self.ui.amount.setText(dataList[0][3])
        self.ui.addNew.setText('Update')
        self.id = cId
      
    def addData(self):        
        operation =  self.sender().text()
        self.query.exec_(""" select employee_information_id from employee_information where employee_id='%s' """%(self.ui.empId.text()))
        while self.query.next() :
            empId = self.query.value(0).toInt()[0]
        if operation == 'Add':
            self.query.exec_("""
                  insert into advance_amount(employee_information_id, date, amount)
                  values(%s, '%s', '%s');
                  """%(empId,str(self.ui.dateEdit.date().toPyDate()),
                        self.ui.amount.text())
                             )
                   
            print self.query.isActive()
            self.showTable()
            self.ui.empId.setText("")
            self.ui.dateEdit.setDate(datetime.datetime.today())
            self.ui.name.setText("")
            self.ui.amount.setText("")
        else:
            self.query.exec_(""" select advance_amount_id from advance_amount where employee_information_id=%s """%(empId))
            while self.query.next() :
                amtId = self.query.value(0).toInt()[0]
            print empId,int(amtId),self.ui.amount.text(),str(self.ui.dateEdit.date().toPyDate())
            self.query.exec_("""         
                  update advance_amount set
                      employee_information_id = %s,
                      date = '%s',
                      amount = '%s'
                      where advance_amount_id = %s
                  """%(int(empId),str(self.ui.dateEdit.date().toPyDate()),
                        self.ui.amount.text(),int(amtId))
                   )
            print "update",self.query.isActive()
            self.showTable()
            self.ui.empId.setText("")
            self.ui.dateEdit.setDate(datetime.datetime.today())
            self.ui.name.setText("")
            self.ui.amount.setText("")
            self.ui.addNew.setText('Add')
