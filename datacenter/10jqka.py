# 爱基金
# 获取基金数据
# https://fund.10jqka.com.cn/datacenter/sy/

import json

from pymysql import Connection

# import requests

# url = "http://fund.10jqka.com.cn/data/Net/info/all_F009_desc_0_0_1_9999_0_0_0_jsonp_g.html"

# response = requests.request("GET", url).text[2:-1]

# with open("D:/PyLearn/datacenter/10jqka.json", "w", encoding="utf8") as f:
#     f.write(response)
#     print("<-- 数据已写入到 10jqka.json -->")
#     print()

with open("D:/PyLearn/datacenter/10jqka.json", "r", encoding="utf8") as f:
    str = json.loads(f.read())

# for k in str['data']['data']:
#     print(str['data']['data'][k]['code'], "-->",
#           str['data']['data'][k]['name'])


def getconn():
    """
    实例化mysql数据库的对象
    """
    connn = Connection(
        host='localhost',  # ip地址
        port=3306,  # 端口，默认3306
        user='root',  # 账号
        password='123456'  # 密码
    )

    return connn


# 将数据写入到数据库中
conn = getconn()  # 实例化数据库对象
cursor = conn.cursor()  # 获取游标对象
count = 0  # 用于统计for循环影响了多少行数据

for line in str['data']['data']:
    sqlcarry = f"insert into pydb.sina(symbol, name, clrq, jjjl) values ('{str['data']['data'][line]['code']}', '{str['data']['data'][line]['name']}', '{str['data']['data'][line]['clrq']}', '')"
    try:
        # 执行sql语句
        cursor.execute(sqlcarry)
        # 提交到数据库执行
        conn.commit()
        count += cursor.rowcount
    except Exception as e:
        # 发生错误时回滚
        print(f"-> 执行语句：{repr(sqlcarry)}")
        print(f"-> 报错Error：{e}")
        print()
        conn.rollback()
        continue

# 执行sql语句，获取数据库中全部行数量
cursor.execute("select count(*) from pydb.sina")

print("-" * 100)
print(f"<-- 新增数据 {count} 条-->")
print(f"<-- 数据库中现有 {cursor.fetchall()[0][0]} 条数据 -->")

cursor.close()  # 关闭游标对象
conn.close()  # 关闭到数据库的链接
print("<-- 已关闭数据库链接 -->")
