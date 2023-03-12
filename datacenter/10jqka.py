# 爱基金
# 获取基金数据：代码，名称，成立日期
# https://fund.10jqka.com.cn/datacenter/sy/

import json

import requests

from pyutils import pyutils

timer = pyutils.Timer()
timer.start()


def Get_10jqka(*type: str):
    """
    根据输入的基金类型来获取不同类型的数据，
    `"all"`: 全部；
    `"gpx"`: 股票型；
    `"zqx"`: 债券型；
    `"hhx"`: 混合型;
    `"ETF"`: ETF;
    `"LOF"`: LOF;
    `"QDII"`: QDII;
    `"bbx"`: 保本型基金;
    `"zsx"`: 指数型基金;
    `"dxx"`: 打新基金;
    """

    response = {}
    for line in type:
        url = f"http://fund.10jqka.com.cn/data/Net/info/{line}_F009_desc_0_0_1_9999_0_0_0_jsonp_g.html"
        dict1 = json.loads(requests.request(
            "GET", url).text[2:-1])['data']['data']
        response.update(dict1)
        print(f"{line}：\t{len(dict1)}条")
    print(f"共获取到{len(response)}条")
    timer.end()
    return response


textdict = Get_10jqka("all", "gpx", "zqx", "hhx", "ETF",
                      "LOF", "QDII", "bbx", "zsx", "dxx")

# textdict = Get_10jqka("bbx")

with open("D:/PyLearn/datacenter/10jqka.json", "w") as f:
    # print("<-- 已将\'10jpka\'的基金数据写入到\'10jqka.json\'中")
    json.dump(textdict, f)

with open("D:/PyLearn/datacenter/10jqka.json", "r", encoding="utf8") as f:
    textdict = json.load(f)

# 将数据写入到数据库中
conn = pyutils.db()  # 实例化数据库对象
for line in textdict:
    sqlcarry = f"insert into pydb.fund(symbol, name, clrq, jjjl) values ('{textdict[line]['code']}', '{textdict[line]['name']}', '{textdict[line]['clrq']}', '')"
    conn.Insert_Order(sqlcarry)

# 执行sql语句，获取数据库中全部行数量
tt = conn.Query_Order("select count(*) from pydb.fund")[0][0]

print(f"<-- 数据库中现有 {tt} 条数据 -->")

conn.close()  # 关闭到数据库的链接
