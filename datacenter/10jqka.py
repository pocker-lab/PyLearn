# 爱基金
# 获取基金数据：代码，名称，成立日期
# https://fund.10jqka.com.cn/datacenter/sy/

import json

import requests

from pyutils import pyutils


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
        response.update(json.loads(requests.request(
            "GET", url).text[2:-1])['data']['data'])
    return response


textdict = Get_10jqka("all", "gpx", "zqx", "hhx", "ETF",
                      "LOF", "QDII", "bbx", "zsx", "dxx")

# textdict = Get_10jqka("bbx", "dxx")s

with open("D:/PyLearn/datacenter/10jqka.json", "w") as f:
    print("<-- 已将\'10jpka\'的基金数据写入到\'10jqka.json\'中")
    json.dump(textdict, f)

with open("D:/PyLearn/datacenter/10jqka.json", "r", encoding="utf8") as f:
    textdict = json.load(f)

# 将数据写入到数据库中
conn = pyutils.GetConnMySql()  # 实例化数据库对象
cursor = conn.cursor()  # 获取游标对象
count = 0  # 用于统计新增多少条数据
counterror = 0  # 用于统计新增失败多少条数据

for line in textdict:
    sqlcarry = f"insert into pydb.sina(symbol, name, clrq, jjjl) values ('{textdict[line]['code']}', '{textdict[line]['name']}', '{textdict[line]['clrq']}', '')"
    try:
        # 执行sql语句
        cursor.execute(sqlcarry)
        # 提交到数据库执行
        conn.commit()
        count += cursor.rowcount()
    except Exception as e:
        # 发生错误时回滚
        # print(f"-> 执行语句：{repr(sqlcarry)}")
        # print(f"-> 报错Error：{e}")
        # print()
        counterror += 1
        conn.rollback()
        continue

# 执行sql语句，获取数据库中全部行数量
cursor.execute("select count(*) from pydb.sina")

print("-" * 100)
print(f"<-- 从 \'10jpka\' 中获取到 {len(textdict)} 条数据-->")
print(f"<-- 新增数据 {count} 条-->")
print(f"<-- 新增失败 {counterror} 条-->")
print(f"<-- 数据库中现有 {cursor.fetchall()[0][0]} 条数据 -->")

cursor.close()  # 关闭游标对象
conn.close()  # 关闭到数据库的链接
print("<-- 已关闭数据库链接 -->")
