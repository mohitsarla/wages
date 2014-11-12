#!/usr/bin/env python
# -*- coding: utf-8 -*-

#####################################################################
#Develop By : Pankaj pathak
# Create On : 18 Dec,2013
# Modify On : 1>(18 Dec, 2013), 2> (19 Dec, 2013) 
######################################################################


##############################################################################################
## Following class is used for calculation of attandance which is depandas on     
## date and employee. It target ot only on perticuler day like which type of that.
##
## FORMULAS FOR CALCULATE TOTAL OVER IN SHIFT
## ----------------------------------------------------------------------------------   
## WH = working hour, MH = minimum shift hour, MX = maximum shift hour, OT = over time
## LC = leave code, HR = hourly rate, PT = paymentType on leave, TH = total hours    
## ----------------------------------------------------------------------------------
## case 1: Spacial pay days (Public Holiday or day which takes double pay)
##         if works : TH = (WH*PT) + MH
##         else     : TH = (MH)         
## case 2: Normal Pay leaves
##         if (no of leaves avilable) : TH = (MH)
##         elif (manager approve leavae) : TH = (MH)
##         else                       : TH = 0
## case 3: Over time
##         OT = WH - MH
##         TH = WH + (OT * PT)
##_______________________________________________________________________________________
##
## After calculate of all employees total working hour it will set data on table
## and calculate the salary of employee and show total type of leaves taken and
## working hours in a shift.
#############################################################################################    

## NOTE: (19-12-2013)
## 1) Employee salary type is static it should dynamic
## 2) Over time payment method shoult define


##
## BASE CLASS OF ATTENDANCE HANDLER CLASS
##
from PyQt4 import QtCore, QtGui
from dbHandler import DB
class WagesHandler:
    #<<<<<<<<<<<<<<<<------------------   M1
    def __init__(self, query):        
        self.query = query
    
   
    ###################################################################################### 
    ## Following Code is returns leave code, correspont to  leave id and its payment type
    ######################################################################################    
    def leaveCode(self):
        payTypeDict = {'Standard':1, 'No pay': 0, 'Double':2, 'Time & half':1.5}
        leaveCodes = dict([(j, i) for i, j in self.leaveDict.items()])
        self.codeLeave = {}
        self.query.exec_("""select leaves_id, title, payment_type, total_leave  from leaves where shift_id = '%s';"""%self.shift_id)       
        while self.query.next():
            key = str(self.query.value(1).toString())
            value = [str(self.query.value(0).toString()),
                     payTypeDict[str(self.query.value(2).toString())],
                     str(self.query.value(3).toString()) == 'Undifine' and False or str(self.query.value(3).toString()), 
                     ]
            if leaveCodes.has_key(key) : self.codeLeave.update({ leaveCodes[key] : value })
        return self.codeLeave
    ###______________________________________________________________________######
    ###############################################################################


    ########################################################################
    ## fetching of employee, shift and attendance information correspond to attendance table
    #########################################################################################
    def fetchEmployeeRecord(self):
        print "fetch all data"
        filterList = lambda lists : map(lambda x:x[1], lists)
        attendanceDict, employeeIdDict = {}, {}
        self.headers = filterList(self.dayList)
        dateList = filterList(self.days)
        dateIndex = range(1, (len(dateList) + 1))
        for day in dateIndex:
            ##############################################################
            sql = """
                  select employee_information.first_name, employee_information.last_name, employee_information.rate, 
                         leaves_id, working_hour, attendance.employee_information_id  from attendance join employee_information
                         on attendance.employee_information_id = employee_information.employee_information_id where date = '%s'
                  """%(dateList[day - 1])
            self.query.exec_(sql)
            ##################################################################
            tempList = []
            while self.query.next():
                print "this query is working"
                employee = "%s %s"%(str(self.query.value(0).toString()), str(self.query.value(1).toString()))
                rate = str(self.query.value(2).toString())
                leave = str(self.query.value(3).toString())
                workingHour = str(self.query.value(4).toString())
                attand = workingHour
                ## cheking of woking object it is leave or working
                if leave == '2':
                    ## if leave id is 2 thets mean no leave taken it is working hour
                    pass
                else:
                    ## swaping of leave code for fetching leave id
                    attand = dict([(j, i) for i, j in self.leaveCode().items()])[leave]
                    
                ## setting of attendance correspond to employee ### 
                employeeIdDict[employee] =  [str(self.query.value(5).toString()), rate] 

                if attendanceDict.has_key(employee):
                    attendanceDict[employee].append(attand)
                else:
                    attendanceDict[employee] = [attand]
        ##############################################################################
        if attendanceDict:            
            self.setAttendanceData(attendanceDict, employeeIdDict)
        ###############################################################################

        #---------------->>>>>>>>>>>>>>>>>>>> M1


    #<<<<<<<<<<<<<<<---------------------M2
    ##
    ##--------------------------------------------------------------------------     
    ## Following function is use for calculate over time hour
    ## overtime = (working hour) - (minimus shift hour)
    ##---------------------------------------------------------------------------      
    def overTime(self, workingHour):
        if workingHour > int(self.minHour):
            overHour = workingHour - int(self.minHour)
            return overHour
        else:
            return 0
    
    ##--------------------------------------------------------------------------     
    ## Following function is works on (FORMULAS FOR CALCULATE TOTAL OVER IN SHIFT)
    ## which are show in above of class
    ##---------------------------------------------------------------------------           
    def totalHours(self, leave, working, leaveDict, method):   
        if leave:
            payType = self.leaveCode()[leave][1]
            try:
                # CASE 1 if statement
                total = (int(working) * payType)
                if method == 'Salary':
                    total += int(self.minHour)
                else:
                    pass
                return total    
            except:
                # CASE 1 else statement
                return int(self.minHour)
        else:
            
            try:
                # CASE 3
                return int(working) + (self.overTime(int(working)) * self.overTimeRate)
            except:
                # CASE 2 
                if self.leaveCode().has_key(working) :
                    payType = self.leaveCode()[working][1]
                    # CASE 2 if statement 
                    if int(self.leaveCode()[working][2]) <= int(leaveDict[working]):
                        payType = 0
                    return int(self.minHour)*payType
                else:
                    # CASE 2 elif statement
                    lrt = ''
                    if working == 'MA':
                        lrt = int(self.minHour)
                    else:
                        lrt = 0
                    return lrt
                         
    ##--------------------------------------------------------------------------     
    ## Following function is use for holiday working or not
    ## and call toalHours function with following argument
    ## (leave type,  working hour, leaves payment type, wages type)
    ## and returns total working hours accorging to leave and working
    ##---------------------------------------------------------------------------        
    def checkHolidayPay(self, working, date, rate, leaveDict, method):
        flage = True
        if date in self.holiday:
            leaveType = 'H'        
        if date in self.phl.keys():
            leaveType = 'PH'
        if date not in self.holiday+self.phl.keys():
            leaveType = False
           
        return self.totalHours(leaveType, working, leaveDict, method)
    #############################################################################

    ##--------------------------------------------------------------------------     
    ## Following function is use for cheking employee total working on shift
    ## and call checkHolydayPay function with following argument
    ## (working,  date, rate, leave codes and rate, method of pay)
    ## and returns total working hours and leaves accorging date
    ##---------------------------------------------------------------------------  
    def checkEmployeeData(self, emp, attendance):
        ##### Payment type define ##########
        paymentType = 'Salary'
        attendanceDict = {}
        headerDict = {}
        ##################################
        sql = """
                select count(working_hour), working_hour from attendance
                    where employee_information_id  = '%s' group by working_hour
                  """%(emp[0])
        self.query.exec_(sql)
        leavesDict = {}
        while self.query.next(): 
            totalLeave = str(self.query.value(0).toString())
            leaveType = str(self.query.value(1).toString())
            if self.leaveDict.has_key(leaveType):
                leavesDict[leaveType] = totalLeave
        leaveCount = 0
        hourCount = 0
        totalHours = 0
        overTime = 0
        plbHour = 0
        holHour = 0
        for index, attend in enumerate(attendance):
            try:
                if self.headers[index + 1] not in self.holiday+self.phl.keys():
                      overTime += self.overTime(int(attend))
            except:
                pass
            leaveRate = self.checkHolidayPay(attend, self.headers[index+1], emp[1], leavesDict, paymentType)
            totalHours += leaveRate
            attendanceDict[self.headers[index + 1]] = [leaveRate, attend]
            if self.leaveDict.has_key(attend):
                leaveHead = self.leaveDict[attend] 
                if headerDict.has_key(leaveHead):
                    leaveCount += 1
                else:
                    leaveCount = 1
                if leaveHead in self.headers:    
                    headerDict[leaveHead] = leaveCount
                headerDict[self.headers[index+1]] = attend

            else:
                headerDict[self.headers[index+1]] = attend
                if self.headers[index + 1] in self.holiday:
                    holHour += leaveRate                    
                if self.headers[index + 1] in self.phl.keys():
                    plbHour += leaveRate

                
                hourCount += int(attend)
        headerDict['Total Hour'] = hourCount
        headerDict['Holiday'] = holHour
        headerDict['Public Holiday'] = plbHour
        for header in self.headers:
            if headerDict.has_key(header):
                pass
            else:
                headerDict[header] = '0'
        payHeader = ['Rate', 'Gross Pay', 'Over Time', 'Total']
        if 'Attendance' in str(self.__class__):pass
        else:
            headerDict['Rate'] =  emp[1]
            headerDict['Gross Pay'] =  int(emp[1]) * totalHours
            headerDict['Over Time'] = overTime
            headerDict['Total'] = (int(emp[1]) * totalHours) + (overTime * int(emp[1]))
        
        return headerDict, attendanceDict
    ################################################################################            
            
    ##--------------------------------------------------------------------------     
    ## Following function is use for cheking employee total working on shift
    ## and call checkEmloyeeData function with following argument
    ## (employee id, attandance of shift)
    ## This function set data of perticuler employee on table and calculate salary
    ## of perticuler employee.
    ##---------------------------------------------------------------------------  
    def setAttendanceData(self, allAttendance, employeeIdDict):
        employeeDict = {}
        for emp, attendance in allAttendance.items():
            employeeDict[emp] = self.checkEmployeeData(employeeIdDict[emp], attendance)
            
        rows = self.ui.attandance_table.rowCount()
        rw = rows - 2
        print employeeDict.keys()
        ## setting data in table correspond to employee #########
        for row in range(rw):
            emp = self.ui.attandance_table.item(row, 0).text()
            for col, headers in enumerate(self.headers[1:]):
                
                value = employeeDict[str(emp)][0][headers] 
                item = QtGui.QTableWidgetItem(str(value))
                self.ui.attandance_table.setItem(row, col+1, item)
        #######################################################
    
    #--------------------------->>>>>>>>>>>>>>> M2

