#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Developing By : Mohit Sarla
# Date : 2013-11-23
import testdb
import sys
import sqlite3
from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from Ui.employeeInformation import Ui_Dialog
from datetime import date,timedelta,datetime
import validation
from dbHandler import DB
import MySQLdb

class EmployeeInformation(QtGui.QDialog):
    def __init__(self,query,db,parent = None) :
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.db = db
        self.signal()
        self.get_position_name()
        
    def signal(self):
        QtCore.QObject.connect(self.ui.browse,QtCore.SIGNAL('clicked()'),self.browse)
        QtCore.QObject.connect(self.ui.save,QtCore.SIGNAL('clicked()'),self.create_employee)
        QtCore.QObject.connect(self.ui.wages_type,QtCore.SIGNAL('currentIndexChanged(QString)'),self.get_shift_name) 


    def get_shift_name(self,strg):
        self.ui.shift_type.clear()
        if self.ui.wages_type.currentText() == 'Regular':
            self.query.exec_(""" select title from regular_wages_setup ;""")
            while self.query.next():
                self.ui.shift_type.addItem(self.query.value(0).toString())
        if self.ui.wages_type.currentText() == 'Non-Regular':
            self.query.exec_(""" select title from non_regular_wages_setup ;""")
            while self.query.next():
                self.ui.shift_type.addItem(self.query.value(0).toString())  

    def get_position_name(self):
        try:
            self.query.exec_(""" select title from positions ;""")
            while self.query.next():
                self.ui.position.addItem(self.query.value(0).toString())
        except Exception ,e :
            print e
            
    def browse(self):
        self.ui.browse.hide()    
        self.filePath = QtGui.QFileDialog.getOpenFileName(
            self,
            "Select an image",
            ".",
            "Image Files(*.png *.gif *.jpg *jpeg *.bmp)"
        )
        if not self.filePath.isEmpty():
            self.insertImage(self.filePath)

    def insertImage(self, filePath):
        self.filename = filePath.split('/')[-1]
        self.ui.imagepath.setText(filePath)
        self.ui.label_19.setPixmap(QtGui.QPixmap(filePath))
                
        self.fi = open(str(filePath),'rb').read()



    def create_employee(self):
        strList = [('First Name' , self.ui.firstname),
                   ('Last Name' , self.ui.lastname),
                   ('Country',self.ui.country),
                   ('Nationality',self.ui.nationality)]
        ind = 0
        flag = True
        while ind != len(strList):
            if validation.check_string(strList[ind][1].text()):
                pass
            else:
                strList[ind][1].clear()
                QtGui.QMessageBox.warning(None, "Warning",'Invalid %s'%strList[ind][0])
                flag = False
                break
            ind += 1
            
            
        if self.ui.male.isChecked() :
            gender = 'male'
        if self.ui.female.isChecked() :
            gender = 'female'
        if self.ui.others.isChecked() :
            gender = 'other'            
        print gender

        #if validation.check_email(self.ui.email.text()):pass
        #else:flage = False    

        print str(self.ui.shift_type.currentText())
        if flag:
            try :
                self.query.exec_(""" select regular_wages_setup_id from regular_wages_setup where  title = '%s' """%(str(self.ui.shift_type.currentText())))
                if self.query.next():
                    shift_id = self.query.value(0).toInt()[0] ################  shift_id is here
                else :
                    shift_id = 0
                self.query.exec_(""" select non_regular_wages_setup_id from non_regular_wages_setup where  title = '%s' """%(str(self.ui.shift_type.currentText())))
                if self.query.next():
                    non_shift_id = self.query.value(0).toInt()[0] ################  shift_id is here
                else :
                    non_shift_id = 0
                
                self.query.exec_(""" select positions_id from positions where  title = '%s' """%(str(self.ui.position.currentText())))
                if self.query.next():
                    position_id = self.query.value(0).toInt()[0]    ############## position id is here
                else :
                    position_id = 0
                
            
                
                insert_path = open("Employee_Photo/"+str(self.filename),'wb')
                insert_path.write(self.fi)
                insert_path.close()            
                sql = (""" insert into employee_information(first_name ,last_name ,employee_id ,
                                                                 gender ,dob ,address ,city ,state ,country ,pin_no ,nationality ,
                                                                 mobile_no1 ,mobile_no2 ,landline_no ,fnpf,account_no ,rate,
                                                                 date_of_joining ,image_path,regular_wages_setup_id,
                                                                 non_regular_wages_setup_id,
                                                                 positions_id_positions,employee_type,payment_type)
                                                                 values
                                                                 ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                  '%s','%s','%s','%s','%s','%s','%s',%s,%s,%s,'%s','%s')"""%(self.ui.firstname.text(),
                                                                  self.ui.lastname.text(),self.ui.empid.text(),
                                                                  gender,str(self.ui.dob.date().toPyDate()),
                                                                  self.ui.address.toPlainText(),
                                                                  self.ui.city.text(),self.ui.state.text(),
                                                                  self.ui.country.text(),self.ui.pinno.text(),
                                                                  self.ui.nationality.text(),self.ui.mobileno.text(),
                                                                  self.ui.mobileno_2.text(),self.ui.landlineno.text(),
                                                                  self.ui.fpnf_no.text(),self.ui.accountno.text(),
                                                                  self.ui.rate.text(),str(self.ui.dateofjoining.date().toPyDate()),
                                                                  self.filename,shift_id,non_shift_id,position_id,
                                                                  self.ui.emp_type.currentText(),self.ui.payment_type.currentText())) ########## employee 
                                                                

                print sql
                #testdb.cursor.execute(sql)
                self.query.exec_(sql)
                print self.query.isActive()

                QtGui.QMessageBox.information(self,'Information','Employee Created Successfully !!!')
                self.close()
            except :
                QtGui.QMessageBox.warning(self,'Error','Please Upload Photo !!!')
