import MySQLdb
connection = MySQLdb.connect(user = 'root', passwd = '12345', host = 'localhost')
cursor = connection.cursor()
cursor.execute("use wages;")



