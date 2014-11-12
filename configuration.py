#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Developing By : Mohit Sarla
# Date : 2013-11-30

import sys
from PyQt4 import QtCore,QtGui
from Ui.positionConfiguration import Ui_Position
from Ui.departmentConfiguration import Ui_Department
from Ui.shiftConfiguration import Ui_ShiftConfiguration
from datetime import date,timedelta,datetime
import validation
from dbHandler import DB


class PostionConf(QtGui.QDialog):
    def __init__(self,query,db,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui  = Ui_Position()
        self.ui.setupUi(self)
        self.query = query
        self.db = db
        self.signal()
        self.fetch_dept()

    def signal(self):
        QtCore.QObject.connect(self.ui.add,QtCore.SIGNAL("clicked()"),self.onclick_add)

    def onclick_add(self):
        
        if len(str(self.ui.positionName.text())) == 0 :
            QtGui.QMessageBox.warning(self,'Warning','Please Add Position !!!')

        else : 
            self.query.exec_("""insert into positions (title) values ('%s')"""%(self.ui.positionName.text()))
            
            self.fetch_dept()        
            QtGui.QMessageBox.information(self,'Information','Position Saved !!!')
        self.ui.positionName.clear()    

            
        
    def fetch_dept(self):
        self.ui.treeWidget.clear()
        self.query.exec_(""" select title from positions ;""")
        dept = []                     
        while self.query.next():
            dept.append(self.query.value(0).toString())
        for i in range(len(dept)):
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0, dept[i])


class DepartmentConf(QtGui.QDialog):
    def __init__(self,query,db,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui  = Ui_Department()
        self.ui.setupUi(self)
        self.query = query
        self.db = db
        self.signal()
        self.fetch_dept()

    def signal(self):
        QtCore.QObject.connect(self.ui.add,QtCore.SIGNAL("clicked()"),self.onclick_add)
        

    def onclick_add(self):
        self.ui.departmentName.clear()
        if len(str(self.ui.departmentName.text())) == 0:
            QtGui.QMessageBox.warning(self,'Warning','Please Add Department!!!')
        else :    
            self.query.exec_("""insert into department (department_name) values ('%s')"""%(self.ui.departmentName.text()))

            self.ui.treeWidget.clear() 
            self.fetch_dept()
            QtGui.QMessageBox.information(self,'Information','Department Saved !!!')

    def fetch_dept(self):
        self.query.exec_(""" select department_name from department ;""")
        dept = []                     
        while self.query.next():
            dept.append(self.query.value(0).toString())
        for i in range(len(dept)):
            item = QtGui.QTreeWidgetItem(self.ui.treeWidget)
            item.setText(0, dept[i])
        

class ShiftCreate(QtGui.QDialog):
    def __init__(self,query,db,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.ui  = Ui_ShiftConfiguration()
        self.ui.setupUi(self)
    
        
