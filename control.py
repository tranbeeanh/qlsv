"""
script gồm các class Control chứa các static method thực hiện các chức năng của chương trình
...

Classes:
---------
Control

import:
----------
json
    phục vụ ghi file json
getconnet: module
    phục vụ kết nối với databse
student: module
    phục vụ tạo các instance từ class Student
"""


import json
import getconnect
import student


class Control:
    """
    class gồm các static method sử dụng để thực hiện các chức năng của chương trình

    ...

    Attributes
    ----------


    Methods
    -------
    averagePoint(toan, ly, hoa):
        Tính điểm trung bình 3 môn
    rank(tb):
        Xác định phân loại thông qua điểm trung bình
    addStudent(s):
        thêm thông tin sinh viên vào sql
    showAll():
        in ra danh sách các sinh viên trong sql
    findID(id):
        trả về instance một sinh viên thông qua nhập id để làm tham số các method khác
    update(st):
        cập nhật thông tin một sinh viên
    delete(st):
        xóa thông tin một sinh viên
    ghiFileJson(name):
        ghi danh sách thông tin sinh viên trong sql ra file json
    """

    @staticmethod
    def averagePoint(toan, ly, hoa):
        """
        trả về điểm trung bình làm tròn đến chữ số thập phân thứ 2

        Parameters
        ----------
        toan : float
        ly : float
        hoa : float

        Returns
        -------
        diemtb: float
            trung bình của toan, ly, hoa
        """
        return round((toan + ly + hoa) / 3, 2)

    @staticmethod
    def rank(tb):
        """
        return phân loại sinh viên thông qua điểm trung bình

        Parameters
        ----------
        tb: float
            điểm trung bình, tính qua hàm averagePoint(toan, ly, hoa)

        Returns
        -------
        phanloai: str

        """
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
        """
        kết nối database sql
        ghi thông tin sinh viên mới vào sql, in thông báo thêm thành công

        Parameters
        ----------
        s: dict
            một instance của class Student

        Returns
        -------
        none
        print đã thêm thông tin thành công

        """
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
        """
        kết nối database sql
        truy vấn danh sách tất cả các instance trong databse

        Parameters
        ----------
        none

        Returns
        -------
        students: list
            danh sách các dict là instance của class Student đã được ghi vào database

        """
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
        """
        kết nối database sql
        truy vấn instance của class Student có id giống như parameters

        Parameters
        ----------
        id: int
            id của sinh viên cần tìm

        Returns
        -------
        st: dict nếu trong database tồn tại instance có id giống parameter
            instance của class Student đã được ghi vào database có id trùng khớp với parameter
        False nết trong database không tồn tại instance có id giống parameter
        """
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
    def update(st):
        """
        kết nối database sql
        update thông tin instance trùng khớp parameter

        Parameters
        ----------
        st: dict
            instance của class Student

        Returns
        -------
        none
        print cập nhật thành công

        """
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


    @staticmethod
    def delete(st):
        """
        kết nối database sql
        xóa thông tin instance trùng khớp parameter

        Parameters
        ----------
        st: dict
            instance của class Student

        Returns
        -------
        none
        print xóa thành công

        """
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
        """
        tạo listStudents là list chứa các instance sinh viên trong database (dict) qua hàm showAll()
        ghi listStudents ra file json có tên là parameter

        Parameters
        ----------
        name: str
            tên file ghi thông tin sinh viên trong database

        Returns
        -------
        none
        print ghi file thành công

        """
        listStudents = Control.showAll()
        with open(f'{name}.json', 'w') as wf:
            json.dump(listStudents, wf, ensure_ascii=False, indent=2)
        print(f'Đã ghi thông tin sinh viên vào file {name}.json')
