import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             port='',
                             password='',
                             db='qlsv',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    try:
        sql = '''
            CREATE TABLE SINHVIEN (
                ID INT(11) NOT NULL AUTO_INCREMENT,
                NAME VARCHAR(255) NOT NULL,
                DIEMTOAN FLOAT NOT NULL,
                DIEMLY FLOAT NOT NULL,
                DIEMHOA FLOAT NOT NULL,
                DIEMTB FLOAT,
                PHANLOAI VARCHAR(50),
                PRIMARY KEY(ID))
        '''
        cursor.execute(sql)
    finally:
        connection.close()

print("Đã tạo bảng lưu trữ thông tin sinh viên")