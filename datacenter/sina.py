# 新浪
# 获取基金数据：代码，名称，成立日期，基金经理
# http://vip.stock.finance.sina.com.cn/fund_center/index.html#jjgmall
import json

import requests

from pyutils import pyutils

timer = pyutils.Timer()
timer.start()


def getsina(num=1000):
    '''
    获取新浪基金数据
    '''
    url = "http://vip.stock.finance.sina.com.cn/fund_center/data/jsonp.php/IO.XSRV2.CallbackList['9o_rfPFvmkgcHnSk']/NetValueReturn_Service.NetValueReturnOpen?"

    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'vip.stock.finance.sina.com.cn',
        'Connection': 'keep-alive'
    }
    datalist = []
    for page in range(1, num):

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
    print()
    timer.end()
    print()

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
conn = pyutils.db()  # 实例化数据库对象
for line in datalist:
    sqlcarry = f"insert into pydb.fund(symbol, name, clrq, jjjl) values ('{line['symbol']}', '{line['name']}', '{line['clrq']}', '{line['jjjl']}')"
    conn.Insert_Order(sqlcarry)

# tt = conn.Query_Order("select count(*) from pydb.fund")[0][0]

# print(f"<-- 数据库中现有 {tt} 条数据 -->")

conn.close()  # 关闭到数据库的链接
