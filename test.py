from pymysql import Connection


class db(Connection):

    def __init__(self):
        super().__init__(
            host='localhost',  # ip地址
            port=3306,         # 端口，默认3306
            user='root',       # 账号
            password='123456'  # 密码
        )

    def lli(self, *args):
        for line in args:
            print(line)


l1 = [1, 2, 3, 4, 5]
conn = db()
conn.lli(l1)
