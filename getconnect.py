import pymysql


# Ham tra ve mot connection
def getConnection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 port='',
                                 password='',
                                 db='gsc_db',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


