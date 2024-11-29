import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airport',
         user='newuser',
         password='password',
         autocommit=True,
         collation = "utf8mb3_general_ci"
         )