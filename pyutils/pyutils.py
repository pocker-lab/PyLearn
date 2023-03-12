import time

from pymysql import Connection


def MergeList(*lists: list) -> list:
    """
    多个list列表合并
    """
    listdata = []
    for item in lists:
        listdata.extend(item)
    return listdata


class Timer:
    '''
    `start`方法来记录当前时间

    `end`方法来计算两者的时间差
    '''

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        elapsed = time.time() - self.start_time
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        print(f"\r运行时间: {hours:02d}:{minutes:02d}:{seconds:02d}")


class db(Connection):
    """
    这个类是一个数据库连接类，它继承了Connection类，你可以用这个类来创建一个数据库连接对象，并使用Connection类的方法来执行SQL语句
    """

    def __init__(self):
        super().__init__(
            host='localhost',  # ip地址
            port=3306,         # 端口，默认3306
            user='root',       # 账号
            password='123456'  # 密码
        )
        count = 0

    def data_ver(self):
        """
        查看数据库版本
        """
        cursor = self.cursor()
        # cursor.execute("select count(*) from pydb.fund")
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print("Database version : %s " % data)
        cursor.close()

    def Query_Order(self, queryorder: str) -> tuple:
        '''
        执行mysql查询语句，并返回结果，返回类型为`tuple`
        '''
        cursor = self.cursor()
        cursor.execute(queryorder)
        cursor.close()
        tt = cursor.fetchall()
        return tt

    def Insert_Order(self, insertorder: str, err=False):
        '''
        执行mysql插入语句，并返回影响行数和错误行数
        '''
        cursor = self.cursor()
        try:
            cursor.execute(insertorder)
            self.commit()
            print(f"\r已添加 {self.count} 条数据", end='')
            self.count += 1
        except Exception as e:
            if err:
                print(f"-> 执行语句：{insertorder}")
                print(f"-> 报错Error：{e}")
            self.rollback()
        return


if __name__ == "__main__":
    pass
