"""
script tạo database thông qua thư viện pymysql
...

Classes:
---------
none

import:
----------
pymysql
    phục vụ kết nối tạo database thông qua pymysql
"""

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