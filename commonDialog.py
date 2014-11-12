import sys
from PyQt4 import QtCore, QtGui
from Ui.commonDialog import Ui_Dialog

class Popup(QtGui.QDialog):

    __doc__ = '''
              This is the main window of the software                      
              '''
        
    def __init__(self,query,var,parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        self.var = var
        QtCore.QObject.connect(self.ui.ok,QtCore.SIGNAL("clicked()"),self.get_title)

    def get_title(self):
        self.query.exec_(""" insert into title (title_name,title_type) values('%s','%s') ;"""%(str(self.ui.title.text()),self.var))
        print self.query.isActive()
        self.close()
        

        
       
