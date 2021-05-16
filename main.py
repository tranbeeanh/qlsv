import json
import getconnect


class Student:

    ten = ''
    toan = float
    ly = float
    hoa = float
    diemtb = float
    phanloai = ''

    def averagePoint(self, t, l, h):
        return round((t + l + h) / 3, 2)

    def rank(self, tb):
        if tb >= 8:
            return "Gioi"
        elif tb >= 7:
            return "Kha"
        elif tb >= 6:
            return "Trung binh"
        else:
            return "Yeu"

    def addStudent(self):
        self.ten = input('Nhap ten sinh vien: ')
        self.toan = float(input("Nhập diem toan: "))
        self. ly = float(input("Nhập diem ly: "))
        self.hoa = float(input("Nhập diem hoa: "))
        self.diemtb = self.averagePoint(self.toan, self.ly, self.hoa)
        self. phanloai = self.rank(self.diemtb)

        connection = getconnect.getConnection()
        # xac nhan thay doi database
        connection.autocommit(True)

        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO SINHVIEN (NAME, DIEMTOAN, DIEMLY, DIEMHOA, DIEMTB, PHANLOAI) " \
                      "VALUES (%s, %s, %s, %s, %s, %s)"

                # Thực thi sql và truyền tham số
                cursor.execute(sql, (self.ten, self.toan, self.ly, self.hoa, self.diemtb, self.phanloai))

                print("Da them thong tin sinh vien", self.ten)
        finally:
            connection.close()

    def showStudents(self):
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

    def query(self):
        connection = getconnect.getConnection()
        try:
            with connection.cursor() as cursor:
                sql = 'SELECT * FROM SINHVIEN'
                cursor.execute(sql)
                rows = cursor.fetchall()
                return rows
        finally:
            connection.close()

    def find(self, id):
        a = self.query()
        for i in range(len(a)):
            if a[i]['ID'] == id:
                return True
        return False

    def update(self):
        id = int(input('Nhap id sinh vien muon cap nhat: '))
        a = self.find(id)
        if a != False:
            ten = input("Nhập tên sinh viên: ")
            toan = float(input("Nhập diem toan: "))
            ly = float(input("Nhập diem ly: "))
            hoa = float(input("Nhập diem hoa: "))
            diemtb = self.averagePoint(toan, ly, hoa)
            phanloai = self.rank(diemtb)

            connection = getconnect.getConnection()
            connection.autocommit(True)

            try:
                with connection.cursor() as cursor:
                    sql = 'UPDATE SINHVIEN SET NAME = %s, DIEMTOAN = %s, DIEMLY =%s, DIEMHOA =%s, DIEMTB = %s, PHANLOAI =%s WHERE ID = %s'
                    cursor.execute(sql, (ten, toan, ly, hoa, diemtb, phanloai, id))
                    print('Da cap nhat thong tin sinh vien', ten)
            finally:
                connection.close()
        else:
            print('Khong ton tai sinh vien can cap nhat.')

    def delete(self):
        id = int(input('Nhap id sinh vien muon xoa: '))
        a = self.find(id)
        connection = getconnect.getConnection()
        connection.autocommit(True)
        if a != False:
            try:
                with connection.cursor() as cursor:
                    sql = 'Delete from SINHVIEN where ID = %s'

                    cursor.execute(sql, (id))

                    print('Da xoa thong tin sinh vien', id)
            finally:
                connection.close()
        else:
            print('Khong ton tai sinh vien co id', id)

    def ghiFileJson(self):
        a = input('Nhap ten file: ')
        listStudents = self.query()
        with open(f'{a}.json', 'w') as wf:
            json.dump(listStudents, wf, ensure_ascii=False, indent=2)
        print(f'Da ghi du lieu vao file {a}.json')


if __name__ == '__main__':
    s = Student()
    action = 0
    while action >= 0:
        if action == 1:
            s.addStudent()
        elif action == 2:
            s.showStudents()
        elif action == 3:
            s.update()
        elif action == 4:
            s.delete()
        elif action == 5:
            s.ghiFileJson()

        print('Chương trình quản lý sinh viên'.center(60,'-'))
        print("Nhập 1: Thêm sinh viên")
        print("Nhập 2: Xem danh sách sinh viên")
        print("Nhập 3: Cập nhật thông tin sinh viên")
        print("Nhập 4: Xóa thông tin sinh viên")
        print("Nhập 5: Ghi thông tin sinh viên ra file")
        print("Nhập 0: Thoát khỏi chương trình")
        print("-" * 60)
        action = int(input())
        if action == 0:
            break
