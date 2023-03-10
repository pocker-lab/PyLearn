import json

import requests
from pymysql import Connection


def getsina(page: int, num: int) -> str:
    """
    获取新浪基金数据
    `page`: 页数， `num`：每页数据量
    """
    url = 'http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList[''%279o_rfPFvmkgcHnSk%27' \
      ']/NetValueReturn_Service.NetValueReturnOpen?'

    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'vip.stock.finance.sina.com.cn',
        'Connection': 'keep-alive'
    }

    params = {
        "page": page,
        "num": num,
        "sort": "zmjgm",
        "asc": "0",
        "ccode": "",
        "type2": "",
        "type3": ""
    }

    res = requests.request("GET", url, headers=headers, data={}, params=params)
    return res.text


def listsum(*lists: list) -> list:
    """
    多个list列表合并
    """
    listdata = []
    for item in lists:
        listdata.extend(item)
    return listdata


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


# ----------->
# 获取数据并转换为dict
sinadict1 = json.loads(getsina(1, 2)[91:-2])
sinadict2 = json.loads(getsina(2, 2)[91:-2])

print(f"<-- sina基金总数：{sinadict1['total_num']} -->")

print("-" * 100)
# 合并基金数据
datalist = listsum(sinadict1['data'], sinadict1['data'])
print(f"<-- 获取的基金总数{len(datalist)} -->")

print("-" * 100)
# 将基金数据写入到json文件中
with open("D:/PyLearn/datacenter/sina.json", "w", encoding="utf8") as f:
    f.write(json.dumps(datalist, ensure_ascii=False))
    print("<-- 数据已写入 -->")
    print("-" * 100)

# 将数据写入到数据库中
conn = getconn()
cursor = conn.cursor()

for line in datalist:
    sqlcarry = f"insert into pydb.sina(symbol, name, clrq, jjjl) values ('{line['symbol']}', '{line['name']}', '{line['clrq']}', '{line['jjjl']}')"
    try:
        # 执行sql语句
        cursor.execute(sqlcarry)
        # 提交到数据库执行
        conn.commit()
    except Exception as e:
        # 发生错误时回滚
        print(f"-> 报错Error：{e}")
        print(f"-> 执行语句：{repr(sqlcarry)}")
        conn.rollback()
        continue

cursor.execute("select count(*) from pydb.sina")
print("数据库中现有{}".format(cursor.fetchall()[0][0]))

print("-" * 100)
conn.close()  # 关闭到数据库的链接
print("<-- 已关闭数据库链接 -->")
