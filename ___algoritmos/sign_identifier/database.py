

import mysql.connector as mysql

instance_ = mysql.connect(host='localhost',
                          username='lucasf1',
                          password='mysqluser1',
                          database='lucasf1_bdd2')

command = instance_.cursor()
