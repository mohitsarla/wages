from PyQt4 import QtCore, QtGui
from Ui.publicHoliday import Ui_Dialog

class PublicHoliday(QtGui.QDialog):
    def __init__(self,query,parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.query = query
        QtCore.QObject.connect(self.ui.calendarWidget,QtCore.SIGNAL("clicked(QDate)"),self.get_date)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.add)

        self.show_table()

    def get_date(self,date):
        print "date is",date
        date = str(date.toPyDate())
        print date
        self.ui.date.setText(date)

    def add(self):
        if len(str(self.ui.name.text())) == 0:
            QtGui.QMessageBox.warning(self,'Warning','Please Give the Name Of Holiday !!!')

        else :            
            self.query.exec_(""" insert into public_holiday(title,date)values('%s','%s')"""%(self.ui.name.text(),self.ui.date.text()))
            self.ui.name.clear(),self.ui.date.clear()
            self.show_table()
       
    def show_table(self) :
        dataList = []
        self.query.exec_(""" select title,date from public_holiday; """)
        while self.query.next():
            dataList.append((self.query.value(0).toString(),self.query.value(1).toString()))
        self.ui.tableWidget.setRowCount(len(dataList))
        for i in range(len(dataList)):
            for j in range(len(dataList[i])):
                item = QtGui.QTableWidgetItem(str(dataList[i][j]))
	        self.ui.tableWidget.setItem(i,j,item)     
                self.ui.tableWidget.resizeColumnToContents(j)
        	   #self.ui.tableWidget.horizontalHeader().setResizeMode(j,QtGui.QHeaderView.Fixed)		    
    
