#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Developing By : Mohit Sarla
# Date : 2013-11-23

import sys
import sqlite3
from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from Ui.employerInformation import Ui_Dialog
from datetime import date,timedelta,datetime
import validation
from dbHandler import DB

class EmployerInformation(QtGui.QDialog):
    def __init__(self,query,db,parent = None) :
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.db = db
        self.signal()

    def signal(self):
        QtCore.QObject.connect(self.ui.browse,QtCore.SIGNAL('clicked()'),self.logo_employer)
        QtCore.QObject.connect(self.ui.browse_2,QtCore.SIGNAL('clicked()'),self.logo_company)
        QtCore.QObject.connect(self.ui.save,QtCore.SIGNAL('clicked()'),self.onclick_save)
        #QtCore.QObject.connect(self.ui.next,QtCore.SIGNAL('clicked()'),self.onclick_next)

    def logo_company(self):
        self.ui.browse_2.hide()    
        self.filePath = QtGui.QFileDialog.getOpenFileName(
            self,
            "Select an image",
            ".",
            "Image Files(*.png *.gif *.jpg *jpeg *.bmp)"
        )
        if not self.filePath.isEmpty():
            self.filename = self.filePath.split('/')[-1]
            self.ui.imagepath.setText(self.filePath)
            self.ui.label_23.setPixmap(QtGui.QPixmap(self.filePath))
            self.fi = open(str(self.filePath),'rb').read()
            
    def logo_employer(self):
        self.ui.browse.hide()    
        self.filePath_emp = QtGui.QFileDialog.getOpenFileName(
            self,
            "Select an image",
            ".",
            "Image Files(*.png *.gif *.jpg *jpeg *.bmp)"
        )
        if not self.filePath_emp.isEmpty():
            self.filename_emp = self.filePath_emp.split('/')[-1]
            self.ui.imagepath.setText(self.filePath_emp)
            self.ui.label_14.setPixmap(QtGui.QPixmap(self.filePath_emp))
            self.fi = open(str(self.filePath_emp),'rb').read()

                
        #self.fi = open(str(filePath),'rb').read()
        
    def onclick_save(self):
        '''
        strList = [('First Name' , self.ui.firstname),
                   ('Last Name' , self.ui.lastname),
                   ('Organization Name',self.ui.organizationName),
                   
                   ('Country',self.ui.country),
                   ('Nationality',self.ui.nationality)]
        ind = 0
        '''
        flag = True
        '''
        while ind != len(strList):
            if validation.check_string(strList[ind][1].text()):
                pass
            else:
                strList[ind][1].clear()
                QtGui.QMessageBox.warning(None, "Warning",'Invalid %s'%strList[ind][0])
                flag = False
                break
            ind += 1
            
        '''    
        if self.ui.male.isChecked() :
            gender = 'male'
        if self.ui.female.isChecked() :
            gender = 'female'
        if self.ui.others.isChecked() :
            gender = 'other'            
        print gender

        #if validation.check_email(self.ui.email.text()):pass
        #else:flage = False    


        if flag:
            insert_path = open("Employer_Photo/"+str(self.filename_emp),'wb')
            insert_path.write(self.fi_emp)
            insert_path.close() 
            self.query.exec_(""" insert into employer_information(first_name ,last_name, 
                                                        gender ,dob ,email,website,
                                                       address ,city ,state ,country ,pin_no ,nationality ,
                                                       mobile_no1 ,mobile_no2 ,landline_no ,account_no,image_path )
                                                        values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s',
                                                                  '%s','%s','%s','%s','%s','%s')"""%(self.ui.lastname.text(),
                                                                                                gender,str(self.ui.dob.date().toPyDate()),
                                                                                                self.ui.email.text(),self.ui.website.text(),
                                                                                                self.ui.address.text(),
                                                                                                self.ui.city.text(),self.ui.state.text(),
                                                                                                self.ui.country.text(),self.ui.pinno.text(),
                                                                                                self.ui.nationality.text(),self.ui.mobileno.text(),
                                                                                                self.ui.mobileno_2.text(),self.ui.landlineno.text(),
                                                                                                self.ui.accountno.text(),self.filename_emp))

            insert_path = open("Company_logo/"+str(self.filename),'wb')
            insert_path.write(self.fi)
            insert_path.close() 
            self.query.exec_("""
                             insert into company (company_name,company_category,address_line1,address_line2,city,state,country,
                                                  pin_no ,nationality ,mobile_no1 ,mobile_no2 ,landline_no ,website,email,image_path )
                                                  values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""
                                                  %(self.ui.companyName.text(),self.ui.tradeName.text(),self.ui.address1.toPlainText(),
                                                    self.ui.address2.toPlainText(),self.ui.city_2.text(),self.ui.state_2.text(),self.ui.country_2.text(),
                                                    self.ui.pinno_2.text(),self.ui.nationality_2.text(),self.ui.mobileno_4.text(),
                                                    self.ui.mobileno_3.text(),self.ui.landlineno_2.text(),
                                                    self.ui.website_2.text(),self.ui.email_2.text(),self.filename))

                               

            print self.query.isActive()
            QtGui.QMessageBox.information(self,'Information','Record Saved Successfully !!!')
            self.close()


