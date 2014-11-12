import MySQLdb,sqlite3
from PyQt4 import QtGui,QtCore
from Ui.db_conf import DataBaseConfigration

class DataBaseConfiguration(QtGui.QDialog):
    def __init__(self,parent = None):   ### var is the id from the takeAdvancePayment
        QtGui.QDialog.__init__(self,parent)
        self.ui = DataBaseConfigration()
        self.ui.setupUi(self)
        self.query = query

        QtCore.QObject.connect(self.ui.dbType, QtCore.SIGNAL("currentIndexChanged(QString)"), self.get_db)


    def get_db(self,db):
        if db == 'MySql':
            connection = MySQLdb.connect(host = str(self.ui.dbHost.text()),
                                         user = str(str.ui.dbUser.text()),
                                         passwd = str(self.ui.dbPassword.text()))
            cursor = connection.cursor()
        if db == 'SQLite' :
            connection = sqlite3.connect('wages.db')
            cursor = connection.cursor()

            
        
