"""
script kết nối với database tạo connection phục vụ các tác vụ của chương trình
...

Classes:
---------
none

import:
----------
pymysql
    phục vụ kết nối database thông qua pymysql
"""

import pymysql


def getConnection():
    """
    trả về connection để kết nối đến database

    Parameters
    ----------
    none

    Returns
    -------
    connection
        tiện ích phục vụ kết nối database
    """
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 port='',
                                 password='',
                                 db='qlsv',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


