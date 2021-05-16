import pymysql


# Ham tra ve mot connection
def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 port='',
                                 password='',
                                 db='qlsv',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


