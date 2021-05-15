import getconnect
import pymysql


def averagePoint(t, l, h):
    return round((t + l + h) / 3, 2)


def rank(tb):
    if tb >= 8:
        return "Gioi"
    elif tb >= 7:
        return "Kha"
    elif tb >= 6:
        return "Trung binh"
    else:
        return "Yeu"

def addStudent():
    ten = input('Nhap ten sinh vien: ')
    toan = float(input("Nhập diem toan: "))
    ly = float(input("Nhập diem ly: "))
    hoa = float(input("Nhập diem hoa: "))
    diemtb = averagePoint(toan, ly, hoa)
    phanloai = rank(diemtb)

    connection = getconnect.getConnection()
    # xac nhan thay doi database
    connection.autocommit(True)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO SINHVIEN (NAME, DIEMTOAN, DIEMLY, DIEMHOA, DIEMTB, PHANLOAI) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"

            # Thực thi sql và truyền tham số
            cursor.execute(sql, (ten, toan, ly, hoa, diemtb, phanloai))

            print("Da them thong tin sinh vien", ten)
    finally:
        connection.close()
