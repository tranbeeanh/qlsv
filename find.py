import getconnect
import show

connection = getconnect.getConnection()


def query():
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM SINHVIEN'
            cursor.execute(sql)
            rows = cursor.fetchall()
            return rows
    finally:
        connection.close()


def find(ten):
    a = query()
    for i in range(len(a)):
        if a[i]['NAME'] == ten:
            return True
    return False
