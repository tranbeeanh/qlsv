import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             port='',
                             password='')
try:
    with connection.cursor() as cursor:
        cursor.execute('CREATE DATABASE QLSV')

finally:
    connection.close()

print('Đã tạo database QLSV')