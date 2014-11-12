from PyQt4 import QtCore, QtGui
from Ui.advance import Ui_Dialog
from payDialog import PayPopUp
from listOfEmployee import Short_EmployeeList
from statement import Statement
import datetime

class AdvancePayment(QtGui.QDialog):
    def __init__(self,query,db,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.i = 0
        QtCore.QObject.connect(self.ui.addNew, QtCore.SIGNAL("clicked()"), self.addData)
        QtCore.QObject.connect(self.ui.give, QtCore.SIGNAL("clicked()"), self.active)
        QtCore.QObject.connect(self.ui.search, QtCore.SIGNAL("clicked()"), self.popup)        
        self.ui.dateEdit.setDate(datetime.datetime.today())      
        self.showTable()
        self.hide()

    def popup(self):
        obj = Short_EmployeeList(self.query)
        obj.exec_()
        li = obj.get_list()
        self.ui.name.setText(li[0])
        self.ui.empId.setText(li[1])
        
    def hide(self):
        self.ui.empId.setEnabled(False)
        self.ui.dateEdit.setEnabled(False)
        self.ui.name.setEnabled(False)
        self.ui.amount.setEnabled(False)
        self.ui.addNew.setEnabled(False)
        self.ui.search.setEnabled(False)

    def active(self):
        self.ui.empId.setEnabled(True)
        self.ui.dateEdit.setEnabled(True)
        self.ui.name.setEnabled(True)
        self.ui.amount.setEnabled(True)  
        self.ui.addNew.setEnabled(True)
        self.ui.search.setEnabled(True)
        
    def showTable(self):
        dataList = []
        count = 0        
        query = '''
 
                select concat(employee_information.first_name, ' ', employee_information.last_name),
                     employee_information.employee_id,
                     advance_amount.date,
                     advance_amount.amount,
                     advance_amount.amount,
                     0,
                     advance_amount.advance_amount_id
                     from advance_amount
                     join employee_information
                     on advance_amount.employee_information_id = employee_information.employee_information_id
                     where advance_amount.advance_amount_id not in (
                               select advance_amount_id from pay_advance_amount group by advance_amount_id)
                 
               union all

               select concat(employee_information.first_name, ' ', employee_information.last_name) as empname,
                     employee_information.employee_id as empid,
                     advance_amount.date as date,
                     advance_amount.amount as advance,
                     advance_amount.amount - sum(pay_advance_amount.pay_amount) as remian,
                     sum(pay_advance_amount.pay_amount) as paid,
                     advance_amount.advance_amount_id as amnt_id
                     from advance_amount
                     join employee_information
                     on advance_amount.employee_information_id = employee_information.employee_information_id
                     join pay_advance_amount
                     on pay_advance_amount.advance_amount_id = advance_amount.advance_amount_id
                    group by advance_amount.advance_amount_id
                  ;
					
                '''
        self.query.exec_(query)
        while self.query.next():
            advanceId = str(self.query.value(6).toString())
            print "aaaaaa",advanceId
            remain = str(self.query.value(4).toString())
            
            self.ui.tableWidget.setRowCount(count + 1)
            for index in range(6):
                data = str(self.query.value(index).toString())
                item = QtGui.QTableWidgetItem(data)
	        self.ui.tableWidget.setItem(count, index, item)               

            edit = QtGui.QPushButton(self.ui.tableWidget)
            edit.setText('Edit')
            edit.setObjectName(str("edit_%s"%advanceId))
            self.ui.tableWidget.setCellWidget(count, 6, edit)
            QtCore.QObject.connect(edit, QtCore.SIGNAL("clicked()"), self.editData)

	    pay = QtGui.QPushButton(self.ui.tableWidget)
            pay.setText('Pay')
            pay.setObjectName(str("pay_%s_%s"%(advanceId, remain)))
            self.ui.tableWidget.setCellWidget(count, 7, pay)
            QtCore.QObject.connect(pay, QtCore.SIGNAL("clicked()"), self.pay_amount)

	    stmt = QtGui.QPushButton(self.ui.tableWidget)
            stmt.setText('Statement')
            stmt.setObjectName(str("stmt_%s"%advanceId))
            self.ui.tableWidget.setCellWidget(count, 8, stmt)
            QtCore.QObject.connect(stmt, QtCore.SIGNAL("clicked()"), self.statement)
                
            count += 1    



    def statement(self) :
        cId = str(self.sender().objectName()).split('_')[1]
        print "1212",cId
        obj = Statement(self.query,cId)
        obj.exec_()
        
    def pay_amount(self):
        cId,remain =  str(self.sender().objectName()).split('_')[1:]
        print "cid in pay",cId, remain
        obj = PayPopUp(self.query,cId,remain)
        obj.exec_()
        
        self.showTable()
                 
    def editData(self):
        self.ui.empId.setEnabled(True)
        self.ui.dateEdit.setEnabled(True)
        self.ui.name.setEnabled(True)
        self.ui.amount.setEnabled(True)
        self.ui.addNew.setEnabled(True)
        dataList = [] 
        cId =  self.sender().objectName().replace("edit_", "")
        query = '''  select concat(employee_information.first_name, ' ', employee_information.last_name),
                     employee_information.employee_id, date, amount,advance_amount_id from advance_amount join employee_information
                     on advance_amount.employee_information_id = employee_information.employee_information_id;'''
        self.query.exec_(query)
        while self.query.next():
            dataList.append((self.query.value(0).toString(),self.query.value(1).toString(),self.query.value(2).toString(),
                             self.query.value(3).toString(),self.query.value(4).toInt()[0]))
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
