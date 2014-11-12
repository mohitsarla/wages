##this code is used for attandance module and main window
from PyQt4 import QtCore, QtGui
import datetime
from wageshandler import WagesHandler
class AttendanceHandler(WagesHandler):

    #this function is used for defining requir header in table
    
    def initializeModule(self):
        self.phl = {}
        self.leaveDict = {}
        ## this is use for preDefine leaves
        self.query.exec_("""select UPPER(SUBSTRING(title,1,2)), UPPER(title) from leaves
                            where shift_id = '%s';"""%self.shift_id)
        while self.query.next():
            key = str(self.query.value(0).toString())
            value = str(self.query.value(1).toString())       
            self.leaveDict[key] = value 
        self.leave = [('', i) for i in self.leaveDict.values()]
        #############################################################  

        ## following are payment header ###########              
        self.payHeader = [('', 'Rate'), ('', 'Gross Pay'), ('', 'Over Time'), ('', 'Total')]
        ####################################

        ## Overtime rate#########
        self.overTimeRate = 2
        #########################
        
        self.query.exec_("""select title, date from public_holiday;""")
        while self.query.next():
            key = str(self.query.value(1).toString())
            value = str(self.query.value(0).toString())       
            self.phl[key] = value 

        
    ##Following function use for fetch position ID
    def position_id(self,var):
        self.query.exec_(""" select positions_id from positions where  title = '%s' """%(var))
        while self.query.next():
            self.position_id = self.query.value(0).toInt()[0]    ############## position id is here
        self.get_shift_id(str(self.ui.shift.currentText()))
        return  self.position_id
    ###############################################



    ##Following function use for fetch shift ID
    def get_shift_id(self,var):
        self.query.exec_(""" select regular_wages_setup_id from regular_wages_setup where  title = '%s' """%(var))
        while self.query.next():
            self.shift_id = self.query.value(0).toInt()[0] ################  shift_id is here
        ## adding employee correspod to shift
        self.query.exec_("""select first_name,last_name from employee_information
                           where regular_wages_setup_id = '%s' and positions_id_positions = '%s'
                         """%(self.shift_id,self.position_id))
        self.empList = []
        while self.query.next():
            self.empList.append(str(self.query.value(0).toString())+' ' +str(self.query.value(1).toString()))
        ###########################################  
        ## seting employee in table ####################
        self.ui.attandance_table.setRowCount(len(self.empList))
        for i,j in enumerate(self.empList):                
            item = QtGui.QTableWidgetItem('%s'%j)
            self.ui.attandance_table.setItem(i, 0, item)
        self.initializeModule() # M2     
        self.set_header()
        self.show_day()
        ##################################################    
    #############################################################################


        
    ##Following function use for fetch shift Name #########################
    def get_shift_name(self):
        try:
            shiftList= []
            self.query.exec_(""" select title from regular_wages_setup ;""")
            while self.query.next():
                shiftList.append(self.query.value(0).toString())
            self.ui.shift.addItems(shiftList)
        except Exception ,e :
            print e
    #################################################################        



    ##Following function use for fetch position name #########################
    def get_position_name(self):
        try:
            positionList = []
            self.query.exec_(""" select title from positions ;""")
            while self.query.next():
                positionList.append(self.query.value(0).toString())
            self.ui.position.addItems(positionList)
        except Exception ,e :
            print e
    #########################################################        

 


    ###################################################### 
    ## Following code use for setting of header of table
    ####################################################        
    def set_header(self, dayList = [] ):

        self.days = dayList[:]
        self.indexList = [] # index list is used for index of shift date
        
        dayList.insert(0, ('', 'Emp Name')) ##First Colomn of table is employee name
        dayList.append(('', 'Total Hour'))  ## next colomn after shift heafer is total hour
         
        if 'Attendance' in str(self.__class__):pass
        else:
            dayList += self.leave # next colomn are leaves
            dayList += self.payHeader # next colomn are user for payment header  
        self.dayList = dayList


        ###########################################################
        ## Setting of headers in table corredponding to date and holydaay
        ###########################################################
        for day in range(len(dayList)):

            ## setting of header in table
            self.attandance_table.setColumnCount(day + 1)

            item = QtGui.QTableWidgetItem()
            self.attandance_table.setHorizontalHeaderItem(day, item)
            
            item = self.attandance_table.horizontalHeaderItem(day)

            ## if field has da patter like (x, y) then it will date otherwise
            #it will normal header like ('', x)
            if dayList[day][0] == '':
                item.setText("%s %s"%dayList[day])
            else:
                self.indexList.append(day)
                item.setText("%s %s"%dayList[day])
                color = QtGui.QColor()

                ## if comming date is belong to the holiday table then header color will be in deffrant red color
                if self.phl.has_key(dayList[day][1]):
                    color.setRgb(237, 28, 36)
                    item.setTextColor(color)

                ## if date is today then it show in green color    
                if dayList[day][1] == self.today:
                    self.crt_colomn = day
                    color.setRgb(11, 163, 8)
                    item.setTextColor(color)
                    

        ##########################################################  
        ### setting total rows in table it will shows total present and total absent
        ### it always take place after list of employee        
        #####################################################
        temp = 0
        self.query.exec_("""select first_name,last_name from employee_information
                      where regular_wages_setup_id = '%s' and positions_id_positions = '%s'
                      """%(self.shift_id,self.position_id))
        while self.query.next():
            temp += 1
       
        totalCount =  temp + 2

        ## setting of font #################
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        #################################

        ## setting of total row acept employee data
        self.ui.attandance_table.setRowCount(totalCount)
        ################################################

        
        item = QtGui.QTableWidgetItem('Total Present')
        item.setFont(font)
        self.ui.attandance_table.setItem(totalCount-2, 0, item)

        
        item = QtGui.QTableWidgetItem('Total Absent')
        item.setFont(font)
        self.ui.attandance_table.setItem(totalCount-1, 0, item)
        
        #self.showTotals()
        
        self.query.exec_("""select  minimum_hour,  maximum_hour from regular_wages_setup
                           where regular_wages_setup_id = '%s'"""%self.shift_id)
        self.minHour, self.maxHour = '', ''
        while self.query.next():
            self.minHour = str(self.query.value(0).toString())
            self.maxHour = str(self.query.value(1).toString())

    
        self.fetchEmployeeRecord()

        ################################################################
        ################################################################
   
    ###################################################
    ##                 
    ###################################################    
    def fetchData(self, fields, table, field, value):
        fields = ", ".join(fields)
        sql = """select %s from %s where %s = '%s' """%(fields, table, field, value)
        self.query.exec_(sql)
        if self.query.first():
            return map(lambda x : str(self.query.value(x).toString()), range(2))
        else:
            return False    
        
    #################################################        


    #############################################################################
    ## Following Code is returns leave code and its id correspont to  leave
    #############################################################################    
    def leaveCodes(self):
        self.handler.leaveCode() 

        #return codeLeave            
    ##############################################################################

    
    def show_day(self):
        weekDay = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        weekF, weekL = self.fetchData(['week_start', 'week_end'], 'regular_wages_setup', 'regular_wages_setup_id', self.shift_id)
   

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

        ## Calling of setHeader according to shift  ##############
        self.set_header(weekDays)
        ###################################################



    def attandance(self):
    
        count = self.ui.attandance_table.rowCount()
        di = {}
        index = []
        leaveList = []
        codeLeave = self.leaveCode()

        self.fromDate = str(self.ui.date_from.date().toPyDate())
        self.toDate = str(self.ui.date_to.date().toPyDate())

        rows = self.ui.attandance_table.rowCount()

        for index, day in enumerate(self.days):
           index = index + 1 
           flage = True
           for rc in range(rows):
               
                #########################################
                ##Code for fetching employee Id
                emp_name = str(self.ui.attandance_table.item(rc, 0).text())
                self.query.exec_(""" select employee_information_id from employee_information where first_name = '%s' and
                                      last_name = '%s' """%(emp_name.split()[0],emp_name.split()[1]))    
                while self.query.next(): 
                    empID = self.query.value(0).toInt()[0]
                #########################################

                    
                workingHour = self.ui.attandance_table.item(rc, index)
                
                if workingHour:
                    if codeLeave.has_key(workingHour):
                        leave_id = codeLeave[workingHour][0]
                        workingHour = '0'
                    else:
                        leave_id = 2
                    workingHour = str(workingHour.text())

                    preSql  = """select attendance_id from attendance
                               where date = '%s' and employee_information_id = '%s';"""%(day[1], empID)
                    self.query.exec_(preSql)
                    atnId = 0
                    while self.query.next():
                            atnId = self.query.value(0).toInt()[0]
                    if atnId:
                        sql = """update attendance set working_hour = '%s', leaves_id = '%s'
                                where attendance_id = '%s'"""%(workingHour,leave_id, atnId)
                    else:    
                        sql = ("""insert into attendance (employee_information_id,date,regular_wages_setup_id,positions_id,
                                                        working_hour,leaves_id) values(%s,'%s',%s,%s,'%s',%s) 
                                                        """%(empID,day[1],self.shift_id,self.position_id,workingHour,leave_id))
                    self.query.exec_(sql)
   

        self.show_day()         
