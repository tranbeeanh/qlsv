import student
from control import Control

if __name__ == '__main__':

    action = 0
    while action >= 0:
        if action == 1:
            s = student.Student(int(input('Nhập id của sinh viên: ')), input('Nhập tên của sinh viên: '), float(input("Nhập điểm toán: ")),
                                float(input("Nhập điểm lý: ")), float(input("Nhập điểm hóa: ")))
            Control.addStudent(s)
        elif action == 2:
            a = Control.showAll()
            print('Tổng số sinh viên: ', len(a))
            for i in a:
                print(i)
        elif action == 3:
            Control.update(int(input('Nhập id của sinh viên muốn cập nhật: ')))
        elif action == 4:
            Control.delete(int(input('Nhập id của sinh viên muốn xóa: ')))
        elif action == 5:
            Control.ghiFileJson(input('Nhập tên file: '))

        print('Chương trình quản lý sinh viên'.center(60, '-'))
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
