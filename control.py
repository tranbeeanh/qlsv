import json

import getconnect


class Control:
    @staticmethod
    def averagePoint(toan, ly, hoa):
        return round((toan + ly + hoa) / 3, 2)

    @staticmethod
    def rank(tb):
        if tb >= 8:
            return "Gioi"
        elif tb >= 7:
            return "Kha"
        elif tb >= 6:
            return "Trung binh"
        else:
            return "Yeu"

    @staticmethod
    def addStudent(s):
        ten = s.ten
        toan = s.toan
        ly = s.ly
        hoa = s.hoa
        diemtb = Control.averagePoint(toan, ly, hoa)
        phanloai = Control.rank(diemtb)

        connection = getconnect.getConnection()
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

    @staticmethod
    def showAll():
        connection = getconnect.getConnection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM SINHVIEN'
                cursor.execute(sql)
                students = cursor.fetchall()
                return students
        finally:
            connection.close()

    @staticmethod
    def findID(id):
        connection = getconnect.getConnection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM SINHVIEN WHERE ID = %s'
                cursor.execute(sql, (id))
                student = cursor.fetchall()
                return student
        finally:
            connection.close()

    @staticmethod
    def update(id):
        a = Control.findID(id)
        if a:
            ten = input("Nhập tên sinh viên: ")
            toan = float(input("Nhập diem toan: "))
            ly = float(input("Nhập diem ly: "))
            hoa = float(input("Nhập diem hoa: "))
            diemtb = Control.averagePoint(toan, ly, hoa)
            phanloai = Control.rank(diemtb)

            connection = getconnect.getConnection()
            connection.autocommit(True)

            try:
                with connection.cursor() as cursor:
                    sql = 'UPDATE SINHVIEN SET NAME = %s, DIEMTOAN = %s, DIEMLY =%s, DIEMHOA =%s, DIEMTB = %s, ' \
                          'PHANLOAI =%s WHERE ID = %s '
                    cursor.execute(sql, (ten, toan, ly, hoa, diemtb, phanloai, id))
                    print('Da cap nhat thong tin sinh vien', ten)
            finally:
                connection.close()
        else:
            print('Khong ton tai sinh vien can cap nhat.')

    @staticmethod
    def delete(id):
        a = Control.findID(id)
        if a:
            connection = getconnect.getConnection()
            connection.autocommit(True)
            try:
                with connection.cursor() as cursor:
                    sql = 'Delete from SINHVIEN where ID = %s'

                    cursor.execute(sql, (id))

                    print('Đã xóa thông tin sinh viên có id', id)
            finally:
                connection.close()
        else:
            print('Khong ton tai sinh vien co id', id)

    @staticmethod
    def ghiFileJson(name):
        listStudents = Control.showAll()
        with open(f'{name}.json', 'w') as wf:
            json.dump(listStudents, wf, ensure_ascii=False, indent=2)
        print(f'Da ghi du lieu vao file {name}.json')
