import insert
import show
import update
import delete


action = 0
while action >= 0:
    if action == 1:
        insert.addStudent()
    elif action == 2:
        show.showStudents()
    elif action == 3:
        update.update()
    elif action == 4:
        delete.delete()

    print('Chương trình quản lý sinh viên'.center(60,'-'))
    print("Nhập 1: Thêm sinh viên")
    print("Nhập 2: Xem danh sách sinh viên")
    print("Nhập 3: Cập nhật thông tin sinh viên")
    print("Nhập 4: Xóa thông tin sinh viên")
    print("Nhập 0: Thoát khỏi chương trình")
    print("-" * 60)
    action = int(input())
    if action == 0:
        break
