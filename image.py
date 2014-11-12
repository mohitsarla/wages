
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtSql import *


class MyWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        #self.id_no = id_no
        self.pushButtonImage = QtGui.QPushButton(self)
        self.pushButtonImage.setText("Insert Image!")
        self.pushButtonImage.clicked.connect(self.on_pushButtonImage_clicked)

        self.textEditImage = QtGui.QTextEdit(self)
        self.textEditImage.setPlainText("Insert an image here:")
        
        self.save = QtGui.QPushButton(self)
        self.save.setText("Save")
        self.save.clicked.connect(self.on_save_clicked)

        self.layoutVertical = QtGui.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonImage)
        self.layoutVertical.addWidget(self.save)
        self.layoutVertical.addWidget(self.textEditImage)


    def on_pushButtonImage_clicked(self):
        filePath = QtGui.QFileDialog.getOpenFileName(
            self,
            "Select an image",
            ".",
            "Image Files(*.png *.gif *.jpg *jpeg *.bmp)"
        )

        if not filePath.isEmpty():
            self.insertImage(filePath)

    def insertImage(self, filePath):
        self.filename = filePath.split('/')[-1]
        fi = open(str(filePath),'rb').read()
        self.imageUri = QtCore.QUrl(QtCore.QString("file://{0}".format(filePath)))
        image    = QtGui.QImage(QtGui.QImageReader(filePath).read())
        insert_path = open("Scan_Documents/"+str(self.filename),'wb')
        insert_path.write(fi)
        insert_path.close()
        self.textEditImage.document().addResource(
            QtGui.QTextDocument.ImageResource,
            self.imageUri,
            QtCore.QVariant(image)
        )

        imageFormat = QtGui.QTextImageFormat()
        imageFormat.setWidth(image.width())
        imageFormat.setHeight(image.height())
        self.imageUri.toString()
        imageFormat.setName(self.imageUri.toString())

        textCursor = self.textEditImage.textCursor()
        textCursor.movePosition(
            QtGui.QTextCursor.End,
            QtGui.QTextCursor.MoveAnchor
        )
        textCursor.insertImage(imageFormat)

        # This will hide the cursor
        blankCursor = QtGui.QCursor(QtCore.Qt.BlankCursor)
        self.textEditImage.setCursor(blankCursor)
    
    def on_save_clicked(self):
        pass
    '''
        try :
            query = QSqlQuery()
            query.exec_(""" insert into image(image_name,id_no) values ('%s','%s')"""%(self.filename,self.id_no))
            print "saved clicked",query.isActive()
            self.close()
        except:
            pass
    '''
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.exec_()

    sys.exit(app.exec_())

