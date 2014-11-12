#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Mohit Sarla
# Create On : 28 Nov,2013


import sys
from PyQt4 import QtGui, QtCore
from Ui.leave import Ui_Dialog

class LeaveConfiguration(QtGui.QDialog):
    def __init__(self,query,db, parent = None) :
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.query = query
        self.db =db



        
