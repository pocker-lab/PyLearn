import time

from pymysql import Connection


def RunTime():
    """
    显示运行时长
    """
    start = time.time()
    while True:
        time.sleep(1)
        elapsed = time.time() - start
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        print(f"\r运行时间: {hours:02d}:{minutes:02d}:{seconds:02d}", end="")


def GetConnMySql():
    """
    快速实例化mysql数据库的对象
    """
    conn = Connection(
        host='localhost',  # ip地址
        port=3306,  # 端口，默认3306
        user='root',  # 账号
        password='123456'  # 密码
    )

    return conn


if __name__ == "__main__":
    conn = GetConnMySql()
    conn.close()

    # RunTime()
