#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Mohit Sarla
# Create On : 6 Dec,2013

import sys
from PyQt4 import QtCore, QtGui
from Ui.wages_setup import Ui_Dialog

class WagesSetup(QtGui.QDialog):

    __doc__ = '''
              This is the main window of the software                      
              '''
        
    def __init__(self,query,db,parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.db = db
        self.leave = self.ui.leave
        self.signal()
        self.leaveTable()
        self.leave.setColumnWidth(2,40)
        self.leave.setColumnWidth(1,90)
        self.buffer = []
        self.showTable()

        self.get_regular_wages_data()
        self.get_non_regular_wages_data()

    def signal(self):
        QtCore.QObject.connect(self.ui.add,QtCore.SIGNAL("clicked()"),self.onclick_add)
        QtCore.QObject.connect(self.ui.add_2,QtCore.SIGNAL("clicked()"),self.onclick_add_2)

    def onclick_add(self):
        leaveDict = {}
        rows = self.leave.rowCount()
        for rc in range(rows):
            leaveType = self.leave.item(rc, 0).text()
            payType = self.leave.cellWidget(rc, 1).currentText()
            total = self.leave.item(rc, 2)
            leaveDict[str(leaveType)]  = (str(payType), total and str(total.text()) or  '')
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

        for i in leaveDict:
            payment_type = leaveDict[i][0]
            total_leave = leaveDict[i][1]

            self.query.exec_(""" select regular_wages_setup_id from regular_wages_setup; """)
            while self.query.next():
                regular_wages_setup_id = self.query.value(0).toInt()[0]
            self.query.exec_(""" insert into leaves (title,payment_type,total_leave,shift_id) values ('%s','%s','%s','%s')"""%(i,payment_type,total_leave,regular_wages_setup_id))
        #insert data in database
        self.buffer.append([title, maxHour, minHour, weekStart, weekEnd,
                            double, halfTime,  leaveDict])
        self.showTable()
        self.get_regular_wages_data()
        
        self.ui.maxHour.clear(),self.ui.minHour.clear(),self.ui.doubleTime.clear(),self.ui.halfTime.clear(),self.ui.title.clear()
        
    def onclick_add_2(self):        
        self.query.exec_(""" insert into non_regular_wages_setup (title,bonus,comissions,tips) values ('%s','%s','%s','%s') """%(str(self.ui.lineEdit_3.text()),str(self.ui.bonus.text()),
                                                                                                                      str(self.ui.commision.text()),
                                                                                                                      str(self.ui.tips.text())))

        
	self.get_non_regular_wages_data()        
        self.ui.bonus.clear(),self.ui.commision.clear(),self.ui.tips.clear(),self.ui.lineEdit_3.clear(),self.ui.lineEdit_3.clear()   
    def get_non_regular_wages_data(self):
        dataList = []
        self.query.exec_(""" select title,bonus,comissions,tips from non_regular_wages_setup ;""")
        while self.query.next():
            dataList.append((self.query.value(0).toString(),self.query.value(1).toString(),self.query.value(2).toString(),self.query.value(3).toString()))
        self.ui.tableWidget_3.setRowCount(len(dataList))
        for i in range(len(dataList)):
            for j in range(len(dataList[i])):
                item = QtGui.QTableWidgetItem(str(dataList[i][j]))
	        self.ui.tableWidget_3.setItem(i,j,item)               


    def showTable(self):
        #function for show data in tables
        rows = len(self.buffer)
        for i in range(rows):
            self.ui.shiftTable.setRowCount(i+1)
            for ind, item in enumerate(self.buffer[i][:-1]):
                item = QtGui.QTableWidgetItem(item)
                self.ui.shiftTable.setItem(i, ind, item)        

        
    def leaveTable(self):
        # from leaves
        leaves = ['Public Holiday', 'Holiday', 'Sick Sheet',
                  'Yearly', 'Bereavement', 'Voting']
        for i in range(len(leaves)):
            self.leave.setRowCount(i+1)
            
            item = QtGui.QTableWidgetItem(leaves[i])
            self.leave.setItem(i, 0, item)
            
            btn = QtGui.QComboBox(self.leave)
            btn.addItems(['Standard', 'Double', 'Time & half'])
            btn.setObjectName('btn_%s'%(i))
            self.leave.setCellWidget(i,1,btn)            

             
    def get_regular_wages_data(self):
        dataList = []
        self.query.exec_(""" select title,maximum_hour,minimum_hour,week_start,week_end,double_time,
                             time_and_half from regular_wages_setup ;""")
        while self.query.next():
            dataList.append((self.query.value(0).toString(),self.query.value(1).toString(),self.query.value(2).toString(),
                             self.query.value(3).toString(),self.query.value(4).toString(),self.query.value(5).toString(),
                             self.query.value(6).toString()))
            
        self.ui.shiftTable.setRowCount(len(dataList))
        for i in range(len(dataList)):
            print "----",dataList[i]
	    for j in range(len(dataList[i])):
                print dataList[i][j]
	        item = QtGui.QTableWidgetItem(str(dataList[i][j]))
	        print "item is",item
		self.ui.shiftTable.setItem(i,j,item)            
            
