from control import Control


class Student:

    def __init__(self, id, ten, toan, ly, hoa):
        self.id = id
        self.ten = ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.diemtb = Control.averagePoint(toan, ly, hoa)
        self.phanloai = Control.rank(self.diemtb)
