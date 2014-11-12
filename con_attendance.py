#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Mohit Sarla
# Create On : 26 Nov,2013

import testdb
import sys
from PyQt4 import QtCore, QtGui
from Ui.attendance import Ui_attendance
from dbHandler import DB
import datetime
from attendanceHandler import AttendanceHandler
from wageshandler import WagesHandler
class Attendance(AttendanceHandler, QtGui.QDialog):

    __doc__ = '''
              This is the main window of the software                      
              '''
    
    def __init__(self,parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_attendance()
        self.ui.setupUi(self)
        conf = {'user':'root', 'password':'12345'}
        self.db = DB(conf)
        self.query = self.db.query
        self.signal()
        self.initializeModule()
        self.today = str(datetime.datetime.today()).split()[0]
        self.today = '2013-12-10'
        self.attandance_table = self.ui.attandance_table
        
        self.ui.date_from.setDate(datetime.datetime.today())
        self.ui.date_to.setDate(datetime.datetime.today())

        self.leave = [('', 'Total Hour')]
        self.shift_id,self.position_id = '',''
      
        
        self.get_position_name()
        self.get_shift_name()
        self.holiday = ['2013-12-18'] #M3 its depands on holiday list
        self.phl = {'2013-12-13': 'Publc H1', '2013-12-17': 'Publc H2'}
        self.show_day()
              
        
        
    def signal(self):
        QtCore.QObject.connect(self.ui.search, QtCore.SIGNAL("clicked()"), self.show_day)
        QtCore.QObject.connect(self.ui.save, QtCore.SIGNAL("clicked()"), self.attandance)
        QtCore.QObject.connect(self.ui.shift,QtCore.SIGNAL("currentIndexChanged(QString)"),self.get_shift_id)
        QtCore.QObject.connect(self.ui.position,QtCore.SIGNAL("currentIndexChanged(QString)"),self.position_id)



            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Attendance()
    myapp.showMaximized()
    myapp.show()
    sys.exit(app.exec_())        

