#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Pankaj pathak
# Create On : 26 Nov,2013
# Modify On : 1>(17 Nov, 2013), 2>(18 Nov, 2013), 3> (19- Nov, 2013) 4> murge mohit and my code
# 

## NOTE: (19-12-2013)
## 1) Public holi should be depand on database entry.
## 2) Holidays have not define.
## 3) Auto today date.
## 4) Database Configuration should be change.


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
from attendanceHandler import AttendanceHandler


class MainWindow(AttendanceHandler, QtGui.QMainWindow): #M2 inharit attendanceHandler

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


         
        self.holiday = ['2013-12-18'] #M3 its depands on holiday list
        
        self.get_shift_id(str(self.ui.shift.currentText()))
        self.show_day()
        
        
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
         
from time import time, sleep
## M3 Add splash screen on startup
def main():
    app = QtGui.QApplication(sys.argv)
    start = time() 
    splash = QtGui.QSplashScreen(QtGui.QPixmap("splash.png"))
    splash.show()
    while time() - start < 1:
        sleep(1)

        app.processEvents()
    win = MainWindow()
    splash.finish(win)
    win.show()
    app.exec_()      

if __name__ == "__main__":
    main()

