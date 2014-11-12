#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Developed By : Pankaj Pathak
# Writtn on : 26-11-2013

# Last updated by : Mohit Sarla  on   7/12/13


from PyQt4.QtSql import *
import sys,os
from PyQt4 import QtCore, QtGui
import MySQLdb

class DB:
    
    __doc__ = '''
              This module is used for autoincrement id for table and
              for create object use conf = {user:root, password:12345}
                                     db =DB(conf)
                                     query = db.query (this is your query object)
              '''                       
              
    
    def __init__(self, conf):
        self.conf = conf
        connection = MySQLdb.connect(host = 'localhost', user = conf['user'], passwd = conf['password'])
        cursor = connection.cursor()
        try: 
            cursor.execute("use wages;")
            
        except Exception,e:            
            cursor.execute("create database wages;")
            print e


        try :
            cursor.execute("""
                           CREATE TABLE positions (
                           positions_id INTEGER AUTO_INCREMENT NOT NULL  ,
                           title VARCHAR(255) NOT NULL ,
                            PRIMARY KEY (positions_id)
                           );
                          """)
          
        except Exception,e:
            print e


        try :
            cursor.execute("""
                           create table department(department_id INTEGER AUTO_INCREMENT NOT NULL,
                                                department_name VARCHAR(255) NOT NULL,
                                                PRIMARY KEY (department_id)
                                                );
                          """)
        except Exception,e:
            print e

        try :
            cursor.execute("""
                           create table company(company_id INTEGER AUTO_INCREMENT NOT NULL,
                                                company_name VARCHAR(255) NOT NULL ,
                                                company_category VARCHAR(255) NOT NULL,
                                                address_line1 VARCHAR(255) NOT NULL,
                                                address_line2 VARCHAR(255) NOT NULL,
                                                city VARCHAR(255) NOT NULL,              
                                                state VARCHAR(255) NOT NULL,
                                                country VARCHAR(255) NOT NULL,
                                                pin_no VARCHAR(255) NOT NULL,
                                                nationality VARCHAR(255) NOT NULL,
                                                mobile_no1 integer NOT NULL,
                                                mobile_no2 integer NOT NULL,
                                                landline_no integer NOT NULL,
                                                website VARCHAR(255) NOT NULL,
                                                email VARCHAR(255) NOT NULL,
                                                image_path VARCHAR(255) NOT NULL,
                                                PRIMARY KEY (company_id));
                           """)
            
        except Exception,e:
            print e            
        try :
            cursor.execute("""
                create table employer_information(employer_information_id INTEGER AUTO_INCREMENT NOT NULL,
                                  first_name VARCHAR(255) NOT NULL,
                                  last_name VARCHAR(255) NOT NULL,
                                  gender VARCHAR(255) NOT NULL,
                                  dob VARCHAR(255) NOT NULL,
                                  address VARCHAR(255) NOT NULL,
                                  city VARCHAR(255) NOT NULL,              
                                  state VARCHAR(255) NOT NULL,
                                  country VARCHAR(255) NOT NULL,
                                  pin_no VARCHAR(255) NOT NULL,
                                  nationality VARCHAR(255) NOT NULL,
                                  mobile_no1 integer NOT NULL,
                                  mobile_no2 integer NOT NULL,
                                  landline_no integer NOT NULL,
                                  account_no INTEGER NOT NULL ,
                                  website VARCHAR(255) NOT NULL,
                                  email VARCHAR(255) NOT NULL,
                                  image_path VARCHAR(255),
                                  PRIMARY KEY (employer_information_id)
                        ) ;
                        """)
        except Exception,e:
            print e
        
        try :
            cursor.execute("""
                create table employee_information(
                                  employee_information_id INTEGER AUTO_INCREMENT NOT NULL,
                                  first_name VARCHAR(255) NOT NULL,
                                  last_name VARCHAR(255) NOT NULL,
                                  employee_id VARCHAR(255) NOT NULL,
                                  gender VARCHAR(255) NOT NULL,
                                  dob VARCHAR(255) NOT NULL,
                                  address VARCHAR(255) NOT NULL,
                                  city VARCHAR(255) NOT NULL,              
                                  state VARCHAR(255) NOT NULL,
                                  country VARCHAR(255) NOT NULL,
                                  pin_no VARCHAR(255) NOT NULL,
                                  nationality VARCHAR(255) NOT NULL,
                                  mobile_no1 integer NOT NULL,
                                  mobile_no2 integer NOT NULL,
                                  landline_no integer NOT NULL,
                                  fnpf VARCHAR(255) NOT NULL ,
                                  account_no INTEGER NOT NULL ,
                                  payment_type VARCHAR(255),
                                  rate VARCHAR(255) NOT NULL ,
                                  date_of_joining VARCHAR(255) NOT NULL,
                                  image_path VARCHAR(255) NOT NULL,
                                  regular_wages_setup_id INTEGER,
                                  non_regular_wages_setup_id INTEGER,
                                  employee_type VARCHAR(255),
                                  PRIMARY KEY (employee_information_id),                                  
                                  positions_id_positions INTEGER                                 
                                  
                        ) ;
                        """)
        except Exception,e:
            print e
        try :
            cursor.execute("""
                           CREATE TABLE payment_type (
                           payment_type_id INTEGER AUTO_INCREMENT NOT NULL  ,
                           title VARCHAR(255) NOT NULL ,
                           rate VARCHAR(255) NOT NULL ,
                           PRIMARY KEY (payment_type_id)
                            );
                           """)
        except Exception,e :
            print e


        try:
            cursor.execute("""
                             CREATE TABLE public_holiday (
                            public_holiday_leave_id INTEGER AUTO_INCREMENT NOT NULL  ,
                            title VARCHAR(255),
                            date VARCHAR(255),
                             PRIMARY KEY (public_holiday_leave_id)
                            );
                            """)
        except Exception,e :
            print e

        try :
            cursor.execute("""
                            CREATE TABLE regular_wages_setup (
                           regular_wages_setup_id INTEGER AUTO_INCREMENT NOT NULL  ,
                           title VARCHAR(255) NOT NULL,
                           minimum_hour VARCHAR(255) NOT NULL ,
                           maximum_hour VARCHAR(255) NOT NULL ,
                           week_start VARCHAR(255) NOT NULL ,
                           week_end VARCHAR(255) NOT NULL ,
                           double_time VARCHAR(255) NOT NULL ,
                           time_and_half VARCHAR(255) NOT NULL ,
                           public_holiday_leave_id_public_holiday INTEGER,
                           PRIMARY KEY (regular_wages_setup_id),
                           FOREIGN KEY (public_holiday_leave_id_public_holiday) REFERENCES public_holiday (public_holiday_leave_id)
                           );
          
                         """)
        except Exception,e :
            print e
        try :
            cursor.execute("""
                            CREATE TABLE leaves (
                            leaves_id INTEGER AUTO_INCREMENT NOT NULL,
                            title VARCHAR(255) NOT NULL,
                            payment_type VARCHAR(255) NOT NULL,
                            total_leave VARCHAR(255) NOT NULL,
                            applicable VARCHAR(255),
                            shift_id INTEGER,
                            PRIMARY KEY (leaves_id),
                            FOREIGN KEY (shift_id) REFERENCES regular_wages_setup(regular_wages_setup_id)
                            );
                        """)
        except Exception,e :
            print e

        try :
            cursor.execute("""
                            CREATE TABLE advance_amount
                            (advance_amount_id INTEGER AUTO_INCREMENT NOT NULL,
                            employee_information_id INTEGER,
                            date VARCHAR(255),
                            amount VARCHAR(255),
                            PRIMARY KEY (advance_amount_id),
                            FOREIGN KEY (employee_information_id) REFERENCES employee_information(employee_information_id)                          
                            );
                           """)
        except Exception,e :
            print e


        try :
            cursor.execute("""
                            CREATE TABLE non_regular_wages_employee_info
                            (
                             non_regular_wages_employee_info_id INTEGER AUTO_INCREMENT NOT NULL,
                             employee_name VARCHAR(255),
                             employee_id VARCHAR(255),
                             salary VARCHAR(255),
                             date VARCHAR(255),
                             title VARCHAR(255) ,
                             bonus VARCHAR(255),
                             comissions VARCHAR(255),
                             tips VARCHAR(255),
                             PRIMARY KEY (non_regular_wages_employee_info_id)
                            );
                            """)
            
        except Exception,e :
            print e            
            
        try :
            cursor.execute("""
                           CREATE TABLE non_regular_wages_setup (
                           non_regular_wages_setup_id INTEGER AUTO_INCREMENT NOT NULL  ,
                           title VARCHAR(255) NOT NULL ,
                           bonus VARCHAR(255) NOT NULL ,
                           comissions VARCHAR(255) NOT NULL ,
                           tips VARCHAR(255) NOT NULL ,
                           PRIMARY KEY (non_regular_wages_setup_id)
                          );
                          """)
        except Exception,e :
            print e
            

        try :
            cursor.execute(""" create table attendance(attendance_id INTEGER AUTO_INCREMENT NOT NULL,employee_information_id INTEGER, date VARCHAR(20),
                               regular_wages_setup_id INTEGER, positions_id INTEGER, working_hour VARCHAR(255), leaves_id INTEGER,
                               PRIMARY KEY (attendance_id),
                               FOREIGN KEY (employee_information_id) REFERENCES employee_information(employee_information_id),
                               
                               FOREIGN KEY (regular_wages_setup_id) REFERENCES regular_wages_setup(regular_wages_setup_id),
                               FOREIGN KEY (positions_id) REFERENCES positions (positions_id),
                               FOREIGN KEY (leaves_id) REFERENCES leaves (leaves_id));""")

        except Exception,e :
            print e   
            


        try :
            cursor.execute(""" create table pay_advance_amount(pay_advance_amount_id INTEGER AUTO_INCREMENT NOT NULL,
                                                              employee_information_id INTEGER ,
                                                              date VARCHAR(255),
                                                              pay_amount VARCHAR(255),
                                                              advance_amount_id INTEGER, 
                                                              PRIMARY KEY(pay_advance_amount_id),
                                                              FOREIGN KEY (advance_amount_id)
                                                              REFERENCES advance_amount(advance_amount_id));
                          """)     

        except Exception,e :
            print e  
            

        try :
            cursor.execute(""" create table tax (tax_id INTEGER AUTO_INCREMENT NOT NULL, title VARCHAR(255), tax_type VARCHAR(255), value VARCHAR(255),
                                                 applicable VARCHAR(255), regular_wages_id INTEGER, PRIMARY KEY(tax_id),
                                                 FOREIGN KEY (regular_wages_id)
                                                 REFERENCES regular_wages_setup(regular_wages_setup_id));
                          """)     
            

        except Exception,e :
            print e  

        try :
            cursor.execute(""" create table deduction (deduction_id INTEGER AUTO_INCREMENT NOT NULL, title VARCHAR(255), deduction_type VARCHAR(255), value VARCHAR(255),
                                                 applicable VARCHAR(255), regular_wages_id INTEGER, PRIMARY KEY(deduction_id),
                                                 FOREIGN KEY (regular_wages_id)
                                                 REFERENCES regular_wages_setup(regular_wages_setup_id));
                          """)     
            

        except Exception,e :
            print e  

        try :
            cursor.execute(""" create table allowance (allowance_id INTEGER AUTO_INCREMENT NOT NULL, title VARCHAR(255), allowance_type VARCHAR(255), value VARCHAR(255),
                                                 applicable VARCHAR(255), regular_wages_id INTEGER, PRIMARY KEY(allowance_id),
                                                 FOREIGN KEY (regular_wages_id)
                                                 REFERENCES regular_wages_setup(regular_wages_setup_id));
                          """)     
            

        except Exception,e :
            print e  


        try :
            cursor.execute("""
                           create table title(title_id INTEGER AUTO_INCREMENT NOT NULL,title_name VARCHAR(255),title_type VARCHAR(255),
                                                 PRIMARY KEY(title_id));
                             """)
            
        except Exception,e :
            print e

        try:
            cursor.execute("""
                           create table holiday(holiday_id INTEGER AUTO_INCREMENT NOT NULL,title VARCHAR(255),payment_type varchar(255),applicable VARCHAR(255),
                                                 regular_wages_id INTEGER, PRIMARY KEY(holiday_id),
                                                 FOREIGN KEY (regular_wages_id)
                                                 REFERENCES regular_wages_setup(regular_wages_setup_id));
                          """)                       

  
            cursor.execute("""ALTER TABLE employee_information ADD FOREIGN KEY (positions_id_positions) REFERENCES positions (positions_id); """)
            
            #cursor.execute("""ALTER TABLE employee_information ADD FOREIGN KEY (employee_type_id_employee_type) REFERENCES employee_type (employee_type_id); """)

            #cursor.execute(""" ALTER TABLE  employee_information ADD FOREIGN KEY (regular_wages_setup_id) REFERENCES regular_wages_setup (regular_wages_setup_id); """)

            #cursor.execute(""" ALTER TABLE  employee_information ADD FOREIGN KEY (non_regular_wages_setup_id) REFERENCES non_regular_wages_setup (non_regular_wages_setup_id); """)

        except Exception,e :
            print e   

        
         
        # calling of connect function
        self.connect()
        self.query = QSqlQuery()


    ###########################################################
    ## This function gives auto increament id form calculate ##
    ## last value in database table                          ##
    ## args : tablename, field, coursor of db, preFix of id. ##
    ###########################################################
    def autoIncreament(self, tablename, field):
        seperator = '_'
        preFix = 'sd'
        self.query.exec_("select %s from %s order by %s asc;"%(field, tablename,field))
        cidList = []
        while self.query.next():
            cidList = self.query.value(0).toString()
        if cidList:
            preId =  cidList and cidList
            pos =  preId.split(seperator)

            nowId = preFix+seperator + str((int(pos[-1]) + 1))
            return nowId
        else:
            return preFix+seperator + '1'
    ##########################################################   


    
    def connect(self):
        #this function is used fro connection of mysql using pyqt library
        self.db = QSqlDatabase.addDatabase("QMYSQL");
        self.db.setHostName('localhost')
        self.db.setPort(3306)
        self.db.setDatabaseName('wages')
        self.db.setUserName(self.conf['user'])
        self.db.setPassword(self.conf['password'])
        if not self.db.open():
	    QtGui.QMessageBox.warning(None, "Error",QtCore.QString("Cant Connect to database"))
            sys.exit(1)



