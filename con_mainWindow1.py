#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Mohit Sarla
# Create On : 26 Nov,2013

import testdb
import sys
from PyQt4 import QtCore, QtGui
from Ui.mainWindow import Ui_MainWindow
from dbHandler import DB
from con_employeeInformation import EmployeeInformation
from con_employerInformation import EmployerInformation
from con_leaveConf import LeaveConfiguration
from configuration import PostionConf
from configuration import DepartmentConf
from configuration import ShiftCreate
#from wages_setup import WagesSetup   #### for old wages setup
import datetime
from listOfEmployee import EmployeeList
from bankSheet import BankSheet
from takeAdvancePayment import AdvancePayment
#from payAdvancePayment import PayAdvanceAmount
from nonRegularEmployee import NonRegularEmployee
from publicHoliday import PublicHoliday

from newWagesSetup import WagesSetup
from listOfEmployee import AllInfo

class MainWindow(QtGui.QMainWindow):

    __doc__ = '''
              This is the main window of the software                      
              '''
    
    
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        conf = {'user':'root', 'password':'12345'}
        self.db = DB(conf)
        self.query = self.db.query

        self.signal()

        self.today = str(datetime.datetime.today()).split()[0]
        self.today = '2013-12-10'
        self.attandance_table = self.ui.attandance_table
        
        self.ui.date_from.setDate(datetime.datetime.today())
        self.ui.date_to.setDate(datetime.datetime.today())



        self.leave = [('', 'Total Hour'),('', 'Plb Holiday'), ('', 'Holiday'), ('', 'Sick Leave'),
                      ('', 'Yearly'), ('', 'Bereavement'), ('', 'Voting'),
                      ('', 'Rate'), ('', 'Gross Pay'), ('', 'total')]
        self.shift_id,self.position_id = '',''
      
        self.set_header()
        self.get_position_name()
        self.get_shift_name()
        
        
        self.phl = {'2013-12-13': 'Publc H1', '2013-12-17': 'Publc H2'}
        self.show_day()
        #self.attandance()
    def signal(self):
        QtCore.QObject.connect(self.ui.actionAdd_Employee,QtCore.SIGNAL("triggered()"),self.add_employee)
        QtCore.QObject.connect(self.ui.actionCompany_Setup,QtCore.SIGNAL("triggered()"),self.add_employer)
        QtCore.QObject.connect(self.ui.actionConfiguation,QtCore.SIGNAL("triggered()"),self.leave_configuration)
        QtCore.QObject.connect(self.ui.actionPostion_Configuration,QtCore.SIGNAL("triggered()"),self.add_position)
        QtCore.QObject.connect(self.ui.actionDepartment_Configuration,QtCore.SIGNAL("triggered()"),self.add_department)
        QtCore.QObject.connect(self.ui.actionShifting_Configuration,QtCore.SIGNAL("triggered()"),self.create_shift)
        QtCore.QObject.connect(self.ui.actionWages_Setup,QtCore.SIGNAL("triggered()"),self.wages_setup)
        QtCore.QObject.connect(self.ui.actionList_Of_Employee,QtCore.SIGNAL("triggered()"),self.list_of_emp)
        QtCore.QObject.connect(self.ui.actionBank_List,QtCore.SIGNAL("triggered()"),self.bank_list)
        QtCore.QObject.connect(self.ui.actionCreate_Public_Holiday,QtCore.SIGNAL("triggered()"),self.public_holiday)
        
        QtCore.QObject.connect(self.ui.actionAdvance_Payment,QtCore.SIGNAL("triggered()"),self.advance)
        QtCore.QObject.connect(self.ui.actionNon_Regular_Employee,QtCore.SIGNAL("triggered()"),self.non_regular_employee)
        QtCore.QObject.connect(self.ui.actionPay_Advance_Amount,QtCore.SIGNAL("triggered()"),self.pay_advance_amount)
        QtCore.QObject.connect(self.ui.search, QtCore.SIGNAL("clicked()"), self.show_day)
        QtCore.QObject.connect(self.ui.save, QtCore.SIGNAL("clicked()"), self.attandance)
        QtCore.QObject.connect(self.ui.shift,QtCore.SIGNAL("currentIndexChanged(QString)"),self.get_shift_id)
        QtCore.QObject.connect(self.ui.position,QtCore.SIGNAL("currentIndexChanged(QString)"),self.position_id)

        QtCore.QObject.connect(self.ui.actionEmployee_Details,QtCore.SIGNAL("triggered()"),self.emp_info)

    def emp_info(self):
        obj =  AllInfo(self.query,empId='')
        obj.exec_()

    def position_id(self,var):
        self.query.exec_(""" select positions_id from positions where  title = '%s' """%(var))
        while self.query.next():
            self.position_id = self.query.value(0).toInt()[0]    ############## position id is here
        return  self.position_id       

    def get_shift_id(self,var):
        self.query.exec_(""" select regular_wages_setup_id from regular_wages_setup where  title = '%s' """%(var))
        while self.query.next():
            self.shift_id = self.query.value(0).toInt()[0] ################  shift_id is here
        self.query.exec_("""select first_name,last_name from employee_information where regular_wages_setup_id = '%s' and positions_id_positions = '%s' """
                                                                                                          %(self.shift_id,self.position_id))

        empList = []
        while self.query.next():
            empList.append(str(self.query.value(0).toString())+' ' +str(self.query.value(1).toString()))

        self.ui.attandance_table.setRowCount(len(empList))
        for i,j in enumerate(empList):                
            item = QtGui.QTableWidgetItem('%s'%j)
            self.ui.attandance_table.setItem(i, 0, item)
        
        #self.query.exec_(""" select employee_information_id,regular_wages_setup_id,working_hour,positions_id,leaves_id
        #                    from attendance where date '%s' between '%s'; """%(self.ui.date_from.))
        while self.query.next():
            empID = self.query.value(0).toString()
            self.query.exec_(""" select  """)
 
        
    def add_employee(self):
        obj = EmployeeInformation(self.query,self.db)
        obj.exec_()

    def add_employer(self):
        obj = EmployerInformation(self.query,self.db)
        obj.exec_()

    def leave_configuration(self):
        obj = LeaveConfiguration(self.query,self.db)
        obj.exec_()

    def add_position(self):
        obj = PostionConf(self.query,self.db)
        obj.exec_()
        
    def add_department(self):
        obj = DepartmentConf(self.query,self.db)
        obj.exec_()

    def create_shift(self):
        obj = ShiftCreate(self.query,self.db)
        obj.exec_()
    
    def wages_setup(self):
        obj = WagesSetup(self.query)
        obj.exec_()

    def list_of_emp(self):
        obj = EmployeeList(self.query)
        obj.exec_()

    def bank_list(self):
        obj = BankSheet(self.query,self.db)
        obj.exec_()

    def non_regular_employee(self):
        obj = NonRegularEmployee(self.query,self.db)
        obj.exec_()
        
    def advance(self):
        obj = AdvancePayment(self.query,self.db)
        obj.exec_()

    def public_holiday(self):
        obj = PublicHoliday(self.query)
        obj.exec_()

    def pay_advance_amount(self):
        pass
        #obj = PayAdvanceAmount(self.query)
        #obj.exec_()
        
    def get_shift_name(self):
        try:
            shiftList= []
            self.query.exec_(""" select title from regular_wages_setup ;""")
            while self.query.next():
                shiftList.append(self.query.value(0).toString())
            self.ui.shift.addItems(shiftList)
        except Exception ,e :
            print e

    def get_position_name(self):
        try:
            positionList = []
            self.query.exec_(""" select title from positions ;""")
            while self.query.next():
                positionList.append(self.query.value(0).toString())
            self.ui.position.addItems(positionList)
        except Exception ,e :
            print e
            
         
         
    def set_header(self, dayList = [] ):
        self.days = dayList
        self.indexList = [] # index list is used for index ofshift date
        dayList.insert(0, ('', 'Emp Name'))
        dayList += self.leave
        self.dayList = dayList
        for day in range(len(dayList)):
            self.attandance_table.setColumnCount(day + 1)
            item = QtGui.QTableWidgetItem()
            self.attandance_table.setHorizontalHeaderItem(day, item)
            item = self.attandance_table.horizontalHeaderItem(day)
            if dayList[day][0] == '':
                item.setText("%s %s"%dayList[day])
            else:
                self.indexList.append(day)
                item.setText("%s %s"%dayList[day])
                color = QtGui.QColor()
                if self.phl.has_key(dayList[day][1]):
                    color.setRgb(237, 28, 36)
                    item.setTextColor(color)
                if dayList[day][1] == self.today:
                    self.crt_colomn = day
                    
                    color.setRgb(11, 163, 8)
                    item.setTextColor(color)
          

        for day in self.indexList:
            sql = """
                  select employee_information.first_name, employee_information.last_name, employee_information.rate,
                         leaves_id, working_hour from attendance join employee_information
                         on attendance.employee_information_id = employee_information.employee_information_id where date = '%s'
                  """%(self.dayList[day][1]) 
            self.query.exec_(sql)
            tempDict = {}
            while self.query.next(): 
                employee = "%s %s"%(str(self.query.value(0).toString()), str(self.query.value(1).toString()))     
                rate = str(self.query.value(2).toString())
                leave = str(self.query.value(3).toString())
                workingHour = str(self.query.value(4).toString())
                attand = workingHour
                if leave == '7':
                    pass
                else:
                    print self.leaveCode(), leave, 
                    attand = dict([(j, i) for i, j in self.leaveCode().items()])[leave]
                tempDict[employee] = attand
            print tempDict
            for ind in range(len(tempDict)):
                emp = self.ui.attandance_table.item(ind, 0).text()
                item = QtGui.QTableWidgetItem(tempDict[str(emp)])
                self.ui.attandance_table.setItem(ind, day, item)

    def leaveCode(self):
        di = {'YL' :'Yearly','BL' : 'Bereavement Leave','PH':'Public Holiday','VL':'Voting','SL':'Sick Sheet','H' : 'Holiday', 'UL' : 'Unautorized Leave'}
        di = dict([(j, i) for i, j in di.items()])
        self.query.exec_(""" select leaves_id,title from leaves ;""")
        temp = {}
        while self.query.next() :
                temp[str(self.query.value(1).toString())] = str(self.query.value(0).toString())   
        codeLeave = {}
        for i, j in temp.items():
                if di.has_key(i):
                    codeLeave[di[i]] = j
        return codeLeave            
    
    def show_day(self):
        week = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
        fromDate = self.ui.date_from.date().toPyDate()
        toDate = self.ui.date_to.date().toPyDate()
        day = (toDate - fromDate).days
        div1 =  fromDate.weekday()
        div2 =  toDate.weekday()
        count = div1
        weekDays = []
        for d in range(day):
            if count >= 7:
                count = 0
            weekDays.append((week[count], str(fromDate + datetime.timedelta(days = d))))
            count += 1
        weekDays.append((week[div2], str(toDate)))               
        self.set_header(weekDays)
        

    def attandance(self):
        count = self.ui.attandance_table.rowCount()
        
        di = {}
        index = []
        leaveList = []
        codeLeave = self.leaveCode()
        print codeLeave
        self.fromDate = str(self.ui.date_from.date().toPyDate())
        self.toDate = str(self.ui.date_to.date().toPyDate())
        sql = """
                delete from attendance where date between '%s' and '%s' and regular_wages_setup_id = '%s' and positions_id = '%s';
              """%(self.fromDate, self.toDate, self.shift_id, self.position_id)

        print sql  
        self.query.exec_(sql)
        print self.query.isActive()
        rows = self.ui.attandance_table.rowCount()
        print [self.days[i] for i in self.indexList]
        for index in self.indexList:
           flage = True 
           for rc in range(rows):
                ##Code for fetching employee Id
                emp_name = str(self.ui.attandance_table.item(rc, 0).text())
                self.query.exec_(""" select employee_information_id from employee_information where first_name = '%s' and
                                      last_name = '%s' """%(emp_name.split()[0],emp_name.split()[1]))    
                while self.query.next(): 
                    empID = self.query.value(0).toInt()[0]
                #########################################

                    
                workingHour = self.ui.attandance_table.item(rc, index)
                print rc, index
                if workingHour:
                    
                    if codeLeave.has_key(workingHour):
                        leave_id = codeLeave[workingHour]
                        workingHour = '0'
                    else:
                        leave_id = 1
                    workingHour = str(workingHour.text())
                    print empID, workingHour, leave_id , self.days[index][1] 
                    
                    sql = ("""insert into attendance (employee_information_id,date,regular_wages_setup_id,positions_id,
                                                        working_hour,leaves_id) values(%s,'%s',%s,%s,'%s',%s) 
                                                        """%(empID,self.days[index][1],self.shift_id,self.position_id,workingHour,leave_id))

                    print sql
                    #testdb.cursor.execute(sql)
                    #testdb.connection.commit()
                    self.query.exec_(sql)
                    print self.query.isActive()
                   
                 
                else:
                    flage = False
                    QtGui.QMessageBox.warning(self,'Empty Entry','%s entry at %s invelid'%(emp_name, self.days[index][1]))
                    break
           if flage:
               pass
           else:
               break

        self.show_day()                      
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())        
