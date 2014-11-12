#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Develop By : Pankaj Pathak
# Written On : 26-11-2013

from PyQt4 import QtCore, QtGui
import re
def check_email(email):
    email = str(email)
    pattern = '[\.\w]{1,}[@]\w+[.]\w+'
    if re.match(pattern, email):
        return email
    else:
        
        return False


def check_mobile(mobile):
    p = re.compile('(^[+0-9]{1,3})*([0-9]{10,11}$)')
    if p.match(mobile)!= None :
        return mobile
    else:

        return False


def check_string(string):
     string = str(string)
     if not re.search('\d+', string) :
         return string
     else:
    
         return False


