import student
from control import Control

if __name__ == '__main__':

    action = 0
    while action >= 0:
        if action == 1:
            s = student.Student(input('Nhap ten sinh vien: '), float(input("Nhập diem toan: ")),
                                float(input("Nhập diem ly: ")),
                                float(input("Nhập diem hoa: ")))
            Control.addStudent(s)
        elif action == 2:
            Control.showAll()
        elif action == 3:
            Control.update(int(input('Nhap id sinh vien muon cap nhat: ')))
        elif action == 4:
            Control.delete(int(input('Nhap id sinh vien muon xoa: ')))
        elif action == 5:
            Control.ghiFileJson(input('Nhap ten file: '))
        elif action == 6:
            Control.showID(int(input('Nhap id sinh vien: ')))
        elif action == 7:
            Control.showName(input('Nhap ten sinh vien: '))

        print('Chương trình quản lý sinh viên'.center(60, '-'))
        print("Nhập 1: Thêm sinh viên")
        print("Nhập 2: Xem danh sách sinh viên")
        print("Nhập 3: Cập nhật thông tin sinh viên")
        print("Nhập 4: Xóa thông tin sinh viên")
        print("Nhập 5: Ghi thông tin sinh viên ra file")
        print("Nhập 6: Tìm kiếm thông tin sinh viên theo id")
        print("Nhập 7: Tìm kiếm thông tin sinh viên theo tên")
        print("Nhập 0: Thoát khỏi chương trình")
        print("-" * 60)
        action = int(input())
        if action == 0:
            break
