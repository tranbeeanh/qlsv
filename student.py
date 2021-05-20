"""
script mô tả model của sinh viên
...

Classes:
---------
Student
"""

from control import Control


class Student:
    """
    class đại diện cho một sinh viên
    ...

    Attributes
    ----------
    id : int
        id của sinh viên
    ten : str
        tên của sinh viên
    toan : float
        điểm toán của sinh viên
    ly : float
        điểm lý của sinh viên
    hoa: float
        điểm hóa của sinh viên

    Methods
    -------

    """
    def __init__(self, id, ten, toan, ly, hoa):
        """
        Hàm constructor

        Parameters
        ----------
        id : int
            id của sinh viên
        ten : str
            tên của sinh viên
        toan : float
            điểm toán của sinh viên
        ly : float
            điểm lý của sinh viên
        hoa: float
            điểm hóa của sinh viên

        Attributes
        ----------
        diemtb : float
            Điểm trung bình, tính thông qua hàm averagePoint()
        phanloai : str
            Phân loại thông qua điểm trung bình, tính thông qua hàm rank()
        """

        self.id = id
        self.ten = ten
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.diemtb = Control.averagePoint(toan, ly, hoa)
        self.phanloai = Control.rank(self.diemtb)
