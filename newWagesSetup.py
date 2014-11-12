#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Mohit Sarla
# Create On : 21 Dec,2013

import sys
from PyQt4 import QtCore, QtGui
from Ui.regulerWagesSetuppopup import Ui_Dialog
from commonDialog import Popup


class WagesSetup(QtGui.QDialog):

    __doc__ = '''
              This is the main window of the software                      
              '''
        
    def __init__(self,query,parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query

        self.show_leave()
        self.show_holiday()
        self.show_tax()
        self.show_deduction()
        self.show_allowance()
        self.signal()

    def signal(self) :
        QtCore.QObject.connect(self.ui.addLeave,QtCore.SIGNAL("clicked()"),self.fun)
        QtCore.QObject.connect(self.ui.addTax,QtCore.SIGNAL("clicked()"),self.fun)
        QtCore.QObject.connect(self.ui.addHoliday,QtCore.SIGNAL("clicked()"),self.fun)
        QtCore.QObject.connect(self.ui.addDeduction,QtCore.SIGNAL("clicked()"),self.fun)
        QtCore.QObject.connect(self.ui.addAllowance,QtCore.SIGNAL("clicked()"),self.fun)
        QtCore.QObject.connect(self.ui.save,QtCore.SIGNAL("clicked()"),self.save)


    def show_leave(self):
        dataList = []
        self.query.exec_("""select title_name from title where title_type='Leave' ;""")
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))
        self.leave(dataList,self.ui.leaveTable)

    def show_holiday(self):
        dataList = []
        self.query.exec_("""select title_name from title where title_type='Holiday' ;""")
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))
        self.holiday(dataList,self.ui.holidayTable)

    def show_tax(self):
        dataList = []
        self.query.exec_("""select title_name from title where title_type='Tax' ;""")
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))
        self.tax(dataList,self.ui.taxTable)

    def show_deduction(self):
        dataList = []
        self.query.exec_("""select title_name from title where title_type='Deduction' ;""")
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))
        self.deduction(dataList,self.ui.deductionTable)

    def show_allowance(self):
        dataList = []
        self.query.exec_("""select title_name from title where title_type='Allowance' ;""")
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))
        self.allowance(dataList,self.ui.allowanceTable)        
    
    def fun(self):
        di = {'Leave' :self.ui.leaveTable,'Tax':self.ui.taxTable,'Holiday':self.ui.holidayTable,
              'Deduction' : self.ui.deductionTable,'Allowance':self.ui.allowanceTable}
        key = str(self.sender().objectName()).replace("add", '')
        obj = Popup(self.query,key)
        obj.exec_()
        di[key].setRowCount(0)
        self.show_table(key, di[key])

   
       
    def show_table(self,var,tableObj):        
        dataList = []
        self.query.exec_("""select title_name from title where title_type='%s' ;"""%(var))
        while self.query.next():
            dataList.append(str(self.query.value(0).toString()))

        if var == 'Leave' :
            self.leave(dataList,tableObj)
            
        if var == 'Tax' :
            self.tax(dataList,tableObj)

        if var ==  'Deduction' :
            self.deduction(dataList,tableObj)

        if var == 'Allowance' :
            self.allowance(dataList,tableObj)

        if var == 'Holiday' :
            self.holiday(dataList,tableObj)


    def leave(self,li,tableObj) :
        tableObj.setRowCount(len(li))    
        for i in range(len(li)) :
            comboBox = QtGui.QComboBox(tableObj)
            comboBox.addItems(['Standard', 'No Pay'])       

            checkBox = QtGui.QCheckBox(tableObj)
            
            item = QtGui.QTableWidgetItem(li[i])
            tableObj.setItem(i,0,item)
                          
            comboBox.setObjectName('comboBox_%s'%(i))
            tableObj.setCellWidget(i,1,comboBox)

            checkBox.setObjectName('checkBox_%s'%(i))
            tableObj.setCellWidget(i,3,checkBox)           
            tableObj.resizeColumnToContents(i)
            
    def tax(self,li,tableObj) :
        tableObj.setRowCount(len(li))    
        for i in range(len(li)) :
            comboBox = QtGui.QComboBox(tableObj)
            comboBox.addItems(['%', 'Fix'])       

            checkBox = QtGui.QCheckBox(tableObj)
            
            item = QtGui.QTableWidgetItem(li[i])
            tableObj.setItem(i,0,item)
                          
            comboBox.setObjectName('comboBox_%s'%(i))
            tableObj.setCellWidget(i,1,comboBox)

            checkBox.setObjectName('checkBox_%s'%(i))
            tableObj.setCellWidget(i,3,checkBox) 
            tableObj.resizeColumnToContents(i)
            
    def deduction(self,li,tableObj) :
        tableObj.setRowCount(len(li))    
        for i in range(len(li)) :
            comboBox = QtGui.QComboBox(tableObj)
            comboBox.addItems(['%', 'Fix'])       

            checkBox = QtGui.QCheckBox(tableObj)
            
            item = QtGui.QTableWidgetItem(li[i])
            tableObj.setItem(i,0,item)
                                                                    
            comboBox.setObjectName('comboBox_%s'%(i))
            tableObj.setCellWidget(i,1,comboBox)

            checkBox.setObjectName('checkBox_%s'%(i))
            tableObj.setCellWidget(i,3,checkBox) 
            tableObj.resizeColumnToContents(i)
            
    def allowance(self,li,tableObj) :
        tableObj.setRowCount(len(li))    
        for i in range(len(li)) :
            comboBox = QtGui.QComboBox(tableObj)
            comboBox.addItems(['%', 'Fix'])       

            checkBox = QtGui.QCheckBox(tableObj)
            
            item = QtGui.QTableWidgetItem(li[i])
            tableObj.setItem(i,0,item)
                          
            comboBox.setObjectName('comboBox_%s'%(i))
            tableObj.setCellWidget(i,1,comboBox)

            checkBox.setObjectName('checkBox_%s'%(i))
            tableObj.setCellWidget(i,3,checkBox) 
            tableObj.resizeColumnToContents(i)
            
    def holiday(self,li,tableObj) :
        tableObj.setRowCount(len(li))    
        for i in range(len(li)) :
            comboBox = QtGui.QComboBox(tableObj)
            comboBox.addItems(['Standard', 'No Pay'])       

            checkBox = QtGui.QCheckBox(tableObj)
            
            item = QtGui.QTableWidgetItem(li[i])
            tableObj.setItem(i,0,item)
                          
            comboBox.setObjectName('comboBox_%s'%(i))
            tableObj.setCellWidget(i,1,comboBox)

            checkBox.setObjectName('checkBox_%s'%(i))
            tableObj.setCellWidget(i,2,checkBox) 
            tableObj.resizeColumnToContents(i)

    def get_rows(self,key, tableObject) :
        resultList = []
	for row in range(tableObject.rowCount()):
	    temp = []
	    flageList = []
	    for column in range(4) :
                item = getattr(tableObject, 'item')(row, column)
                cellItem = getattr(tableObject, 'cellWidget')(row, column)
                ele = ''
                if item:
                    ele =  item.text()
                else:    
                    widget = {'QComboBox':'currentText','QCheckBox':'checkState'}
                    for i, j in widget.items():
                        if i in str(cellItem): 
                            ele =  getattr(cellItem, j)()
                            flageList.append(ele and True)       
                temp.append(str(ele))
            if False not in flageList:    
                resultList.append(temp)
               
        print "list is" ,resultList
        self.query.exec_("select regular_wages_setup_id from regular_wages_setup ;")
        while self.query.next():
            lastId = self.query.value(0).toInt()[0]        
        for i in resultList:                
            self.query.exec_(""" insert into %s(title,%s_type,value,applicable,regular_wages_id) values('%s','%s','%s','%s',%s)
                                 """%(key,key,i[0],i[1],i[2],i[3],lastId))

        if key == 'leaves' :
            for i in resultList:                
                self.query.exec_(""" insert into leaves(title,payment_type,total_leave,applicable,shift_id) values('%s','%s','%s','%s',%s)
                                 """%(i[0],i[1],i[2],i[3],lastId))
                print "for i n leaves",self.query.isActive()
            
        if key == 'holiday' :
            for i in resultList:
                self.query.exec_(""" insert into holiday(title,payment_type,applicable,regular_wages_id) values('%s','%s','%s',%s)
                                 """%(i[0],i[1],i[2],lastId))


    def save(self):

        maxHour = str(self.ui.maxHour.text())
        minHour = str(self.ui.minHour.text())
        weekStart = str(self.ui.weekStart.currentText())
        weekEnd = str(self.ui.weekEnd.currentText())
        double = str(self.ui.doubleTime.text())
        halfTime = str(self.ui.halfTime.text())
        title = str(self.ui.title.text())
        print title,type(minHour),maxHour,weekStart,weekEnd,type(double),halfTime 
        
        self.query.exec_(""" insert into regular_wages_setup (title,minimum_hour,maximum_hour,
                                                              week_start,week_end,double_time,time_and_half)
                                                              values ('%s','%s','%s','%s','%s','%s','%s') """%(title,minHour,maxHour,weekStart,weekEnd,double,halfTime))


        
        print "save clicked"
        di =  {'tax' : self.ui.taxTable,'deduction' : self.ui.deductionTable,'allowance':self.ui.allowanceTable,
               'leaves' : self.ui.leaveTable, 'holiday' : self.ui.holidayTable}
        for k,v in di.iteritems():
            self.get_rows(k,v)
           
