import json

import getconnect
import student


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
        a = Control.findID(s.id)
        if a:
            print("ID sinh viên đã tồn tại")
        else:
            connection = getconnect.getConnection()
            connection.autocommit(True)
            try:
                with connection.cursor() as cursor:
                    sql = "INSERT INTO SINHVIEN (ID, NAME, DIEMTOAN, DIEMLY, DIEMHOA, DIEMTB, PHANLOAI) " \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    cursor.execute(sql, (s.id, s.ten, s.toan, s.ly, s.hoa, s.diemtb, s.phanloai))
                    print("Đã thêm thông tin sinh viên", s.ten)
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
                a = cursor.fetchone()
                if a:
                    st = student.Student(a['ID'], a['NAME'], a['DIEMTOAN'], a['DIEMLY'], a['DIEMHOA'])
                    return st
                else:
                    return False
        finally:
            connection.close()

    @staticmethod
    def update(id):
        st = Control.findID(id)
        if st:
            st.ten = input("Nhập tên sinh viên: ")
            st.toan = float(input("Nhập điểm toán: "))
            st.ly = float(input("Nhập điểm lý: "))
            st.hoa = float(input("Nhập điểm hóa: "))
            st.diemtb = Control.averagePoint(st.toan, st.ly, st.hoa)
            st.phanloai = Control.rank(st.diemtb)

            connection = getconnect.getConnection()
            connection.autocommit(True)

            try:
                with connection.cursor() as cursor:
                    sql = 'UPDATE SINHVIEN SET NAME = %s, DIEMTOAN = %s, DIEMLY =%s, DIEMHOA =%s, DIEMTB = %s, ' \
                          'PHANLOAI =%s WHERE ID = %s '
                    cursor.execute(sql, (st.ten, st.toan, st.ly, st.hoa, st.diemtb, st.phanloai, st.id))
                    print('Đã cập nhật thông tin của sinh viên', st.ten)
            finally:
                connection.close()
        else:
            print('Không tồn tại sinh viên cần cập nhật')

    @staticmethod
    def delete(id):
        st = Control.findID(id)
        if st:
            connection = getconnect.getConnection()
            connection.autocommit(True)
            try:
                with connection.cursor() as cursor:
                    sql = 'Delete from SINHVIEN where ID = %s'
                    cursor.execute(sql, (st.id))
                    print('Đã xóa thông tin sinh viên có id', st.id)
            finally:
                connection.close()
        else:
            print('Không tồn tại sinh viên có id', id)

    @staticmethod
    def ghiFileJson(name):
        listStudents = Control.showAll()
        with open(f'{name}.json', 'w') as wf:
            json.dump(listStudents, wf, ensure_ascii=False, indent=2)
        print(f'Đã ghi thông tin sinh viên vào file {name}.json')
