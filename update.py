import find
import getconnect
from insert import averagePoint, rank


def update():
    ten = input('Nhap ten sinh vien muon cap nhat: ')
    a = find.find(ten)
    if a != False:
        toan = float(input("Nhập diem toan: "))
        ly = float(input("Nhập diem ly: "))
        hoa = float(input("Nhập diem hoa: "))
        diemtb = averagePoint(toan, ly, hoa)
        phanloai = rank(diemtb)

        connection = getconnect.getConnection()
        connection.autocommit(True)

        try:
            with connection.cursor() as cursor:
                sql = 'UPDATE SINHVIEN SET DIEMTOAN = %s, DIEMLY =%s, DIEMHOA =%s, DIEMTB = %s, PHANLOAI =%s WHERE NAME = %s'
                cursor.execute(sql, (toan, ly, hoa, diemtb, phanloai, ten))
                print('Da cap nhat thong tin sinh vien', ten)
        finally:
            connection.close()
    else:
        print('Khong ton tai sinh vien can cap nhat.')
