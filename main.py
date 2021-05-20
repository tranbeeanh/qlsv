"""
script dùng để chạy chương trình quản lý sinh viên
...
functions:
----------
    main()

Cần import:
    module student chứa class student đại diện mô hình một sinh viên
    class Control trong module control chưa các static method chạy các chức năng phù hơp
"""


import student
from control import Control


def main():
    """hàm chạy chương trình quản lý sinh viên

    thông qua vòng lặp while để tùy theo lựa chọn input của user để thực hiện các hàm tương ứng
    input 1: thêm sinh viên mới
        yêu cầu nhập id sinh viên cần thêm, chạy hàm find(id) để tìm kiếm theo id sinh viên,
            nếu id chưa tồn tại thì tạo instance s của student yêu cầu user nhập các argument tương ứng,
            chạy addStudent(s) với đầu vào một instance s để thêm sinh viên mới
            nếu id đã tồn tại, in thông báo, để user nhập input tiếp tục chương trình
    input 2: chạy hàm showAll() để hiện thông tin tất cả sinh viên
    input 3: cập nhật thông tin sinh viên
        yêu cầu nhập id sinh viên cần cập nhật, chạy hàm find(id) để tìm kiếm theo id sinh viên,
            nếu id chưa tồn tại, in thông báo, để user nhập input tiếp tục chương trình
            nếu id đã tồn tại, tạo instance s của student yêu cầu user nhập các argument tương ứng,
            chạy update(s) với đầu vào một instance s để cập nhật thông tin
    input 4: xóa thông tin sinh viên
        yêu cầu nhập id sinh viên cần xóa, chạy hàm find(id) để tìm kiếm theo id sinh viên,
            nếu id chưa tồn tại, in thông báo, để user nhập input tiếp tục chương trình
            nếu id đã tồn tại, chạy delete(s) với đầu vào là id đã nhập để cập xóa thông tin thông tin có id đó
    input 5: ghi danh sách thông tin sinh viên ra file json
        yêu cầu nhập tên file, chạy hàm ghiFileJson() để ghi ra file

    """

    action = 0
    while action >= 0:

        if action == 1:
            id = int(input('Nhập id của sinh viên: '))
            st = Control.findID(id)
            if st:
                print("ID sinh viên đã tồn tại")
            else:
                s = student.Student(id, input('Nhập tên của sinh viên: '), float(input("Nhập điểm toán: ")),
                                    float(input("Nhập điểm lý: ")), float(input("Nhập điểm hóa: ")))
                Control.addStudent(s)

        elif action == 2:
            a = Control.showAll()
            print('Tổng số sinh viên: ', len(a))
            for i in a:
                print(i)

        elif action == 3:
            id = int(input('Nhập id của sinh viên muốn cập nhật: '))
            st = Control.findID(id)
            if st:
                s = student.Student(id, input('Nhập tên của sinh viên: '), float(input("Nhập điểm toán: ")),
                                    float(input("Nhập điểm lý: ")), float(input("Nhập điểm hóa: ")))
                Control.update(s)
            else:
                print('Không tồn tại sinh viên cần cập nhật')

        elif action == 4:
            st = Control.findID(int(input('Nhập id của sinh viên muốn xóa: ')))
            Control.delete(st)

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

if __name__ == '__main__':
    main()
