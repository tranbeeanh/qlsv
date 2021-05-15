import getconnect
import find

connection = getconnect.getConnection()
connection.autocommit(True)


def delete():
    ten = input('Nhap ten sinh vien muon xoa: ')
    a = find.find(ten)
    if a != False:
        try:
            with connection.cursor() as cursor:
                sql = 'Delete from SINHVIEN where NAME = %s'

                cursor.execute(sql, (ten))

                print('Da xoa thong tin sinh vien', ten)
        finally:
            connection.close()
    else:
        print('Khong ton tai sinh vien co ten', ten)
