import getconnect

def showStudents():
    connection = getconnect.getConnection()

    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM SINHVIEN'

            result_count = cursor.execute(sql)

            print('Tong so sinh vien: ' + str(result_count))

            rows = cursor.fetchall()
            for row in rows:
                print(row)
    finally:
        connection.close()


