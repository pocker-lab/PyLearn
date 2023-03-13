# 好买基金网
# https://www.howbuy.com/fundtool/filter.htm


import requests
from bs4 import BeautifulSoup

from pyutils import pyutils

timer = pyutils.Timer()
timer.start()

def Get_Find_Howbuy(*types, page=1000, num=50):
    url = "https://www.howbuy.com/fund/ajax/fundtool/newfilter.htm"
    datalist = []
    count = 0
    for index in types:
        for page1 in range(1, page):
            data = {
            'fundTypeCode' : index , # 基金类型代码，1：股票型， 3：混合型， 9：QDII， 8：指数型， 5：债券型， 7：货币型， 53：理财型，
            'page': page1,          # 页数
            'perPage': num,      # 每页数据
            }

            html_doc = requests.post(url=url, data=data).text

            soup = BeautifulSoup(html_doc, 'lxml')
            find_tbody = soup.find('tbody')
            find_all_td = find_tbody.find_all('td', attrs={"width":"134", "class":"tdl n nname"})
            count += len(find_all_td)
            
            if len(find_all_td) == 0 :
                print()
                break

            for line in find_all_td:
                code = line.find('a').text[-7:-1]
                name = line.find('a').text[:-9]
                datalist.append([code, name])
            print(f'\r-->\t 共获取 {count} 条', end='')
    timer.end()
    return datalist

tt = ('1','3','9','8','5','7','53')

datalist = Get_Find_Howbuy(tt)

# 将数据写入到数据库中
conn = pyutils.db()  # 实例化数据库对象

for line in datalist:
    sqlcarry = f"insert into pydb.fund(symbol, name, clrq, jjjl) values ('{line[0]}', '{line[1]}', '', '')"
    conn.Insert_Order(sqlcarry)

conn.close()
