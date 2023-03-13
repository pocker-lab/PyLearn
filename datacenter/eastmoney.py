# 天天基金网
# https://fund.eastmoney.com/data/diyfundranking.html


import json
import time

import requests

from pyutils import pyutils

# 开放式基金排名
# 全部     12889      all
# 股票型   2398       gp
# 混合型   7256       hh
# 债券型   2995       zq
# 指数型   1833       zs
# QDII    240        qdii
# LOF     350        lof
# FOF     618        fof
# =12880+2398+7256+2995+1833+240+350+618
# 28570
timer = pyutils.timer()
timer.start()

def Get_Func_eastmoeny(*types: str, page=1000, num=50):
    '''
    获取天天基金网基金数据

    Returns:
        `*types`:要获取的基金类型
            `"all"`: 全部；
            `"gp"`: 股票型；
            `"hh"`: 混合型；
            `"zq"`: 债券型；
            `"zs"`: 指数型；
            `"qdii"`: QDII；
            `"lof"`: LOF；
            `"fof"`: FOF；
        `page`: 页数（默认1000）
        `num`: 数量（默认50）
    '''

    # 获取当前日期
    times = time.strftime("%Y-%m-%d", time.localtime())

    url = "https://fund.eastmoney.com/data/rankhandler.aspx?"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Referer': 'https://fund.eastmoney.com/data/fundranking.html',
        'Accept': '*/*',
        'Host': 'fund.eastmoney.com',
        'Connection': 'keep-alive',
        'Cookie': 'ASP.NET_SessionId=0pw2zdm1e2oiuh2m04im1rmw'
    }

    datalist = []
    for item in types:
        count = 0
        for index in range(1, page):
            params = {
                "op": "ph",
                "dt": "kf",
                "ft": item,
                "sc": "1nzf",
                "st": "desc",
                "sd": times,
                "ed": times,
                "pi": index,
                "pn": num,
                "dx": "1",
            }

            response = requests.request(
                "GET", url, headers=headers, params=params)

            text = response.text[15:-1].replace("datas", "\"datas\"").replace("allRecords", "\"allRecords\"").replace("pageIndex", "\"pageIndex\"").replace("pageNum", "\"pageNum\"").replace("allPages", "\"allPages\"").replace("allNum", "\"allNum\"").replace(
                "gpNum", "\"gpNum\"").replace("hhNum", "\"hhNum\"").replace("zqNum", "\"zqNum\"").replace("zsNum", "\"zsNum\"").replace("bbNum", "\"bbNum\"").replace("qdiiNum", "\"qdiiNum\"").replace("etfNum", "\"etfNum\"").replace("lofNum", "\"lofNum\"").replace("fofNum", "\"fofNum\"")

            dictdata = json.loads(text)['datas']

            for line in dictdata:
                datalist.append(
                    [line.split(',')[0], line.split(',')[1], line.split(',')[16]])

            count += len(dictdata)

            print(f"\r{item}\t-->\t第 {index} 页 \t--> \t{count} 条", end='')

            if len(dictdata) == 0:
                print()
                break

    print(f"<-- 共获取到 {len(datalist)} 条")
    timer.end()
    print()

    return datalist

datalist = Get_Func_eastmoeny(
    "all", "gp", "hh", "zq", "zs", "qdii", "lof", "fof")

# 将数据写入到数据库中
conn = pyutils.db()  # 实例化数据库对象

for line in datalist:
    sqlcarry = f"insert into pydb.fund(symbol, name, clrq, jjjl) values ('{line[0]}', '{line[1]}', '{line[2]}', '')"
    conn.Insert_Order(sqlcarry)

# 执行sql语句，获取数据库中全部行数量
# tt1 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
# print(f"<-- 数据库中现有 {tt1} 条数据 -->")

conn.close()  # 关闭到数据库的链接
