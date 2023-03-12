# 新浪
# 获取基金数据：代码，名称，成立日期，基金经理
# http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjgmall
import json

import requests

from pyutils import pyutils


def getsina():
    """
    获取新浪基金数据
    """
    url = "http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList['9o_rfPFvmkgcHnSk']/NetValueReturn_Service.NetValueReturnOpen?"

    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'vip.stock.finance.sina.com.cn',
        'Connection': 'keep-alive'
    }
    datalist = []
    for page in range(1, 1000):

        params = {
            "page": page,
            "num": "80",
            "sort": "zmjgm",
            "asc": "0",
            "ccode": "",
            "type2": "",
            "type3": ""
        }
        # 获取GET请求内容
        res = requests.request(
            "GET", url,
            headers=headers,
            data={},
            params=params
        ).text[91:-2]

        resdict = json.loads(res)

        if len(res) < 1:
            raise print("未获取到sina网页内容")
        elif resdict["data"] == None:
            break

        datalist.extend(resdict["data"])
        print(f"\r正在获取：{page}页，获取到数据：{len(datalist)}条", end="")

    return datalist


# 获取新浪数据
datalist = getsina()

# 写入到文件中
with open("D:/PyLearn/datacenter/sina.json", "w") as f:
    json.dump(datalist, f)

# 从文件中读取
with open("D:/PyLearn/datacenter/sina.json", "r") as f:
    datalist = json.load(f)

# 将数据写入到数据库中

conn = pyutils.GetConnMySql()  # 实例化数据库对象
cursor = conn.cursor()  # 获取游标对象
count = 0  # 用于统计for循环影响了多少行数据
for line in datalist:
    sqlcarry = f"insert into pydb.sina(symbol, name, clrq, jjjl) values ('{line['symbol']}', '{line['name']}', '{line['clrq']}', '{line['jjjl']}')"
    try:
        # 执行sql语句
        cursor.execute(sqlcarry)
        # 提交到数据库执行
        conn.commit()
        count += cursor.rowcount
    except Exception as e:
        # 发生错误时回滚
        # print(f"-> 执行语句：{repr(sqlcarry
        # print()
        conn.rollback()
        continue

# 执行sql语句，获取数据库中全部行数量
cursor.execute("select count(*) from pydb.sina")

print()
print("-" * 100)
print(f"<-- 获取的基金总数：{len(datalist)} -->")
print(f"<-- 新增数据 {count} 条-->")
print(f"<-- 数据库中现有 {cursor.fetchall()[0][0]} 条数据 -->")

cursor.close()  # 关闭游标对象
conn.close()  # 关闭到数据库的链接
print("<-- 已关闭数据库链接 -->")
