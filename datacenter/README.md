# datacenter

> 数据库结构：`symbol`：基金代码，`name`：基金名称，`clrq`：成立日期，`jjjl`：基金经理

1. 数据库基金代码判重，借用数据库的唯一键来判重，通过捕获错误来防止程序意外结束（数据来源：新浪，爱基金，天天基金网，备选晨星网）
2. 通过数据库中的基金代码到（天天基金网，晨星网）获取基金其他数据，并添加到数据库中。

## 20230312 TODO

~~[x]sina代码重构，通过for循环来获取基金数据，避免一次获取大量数据，for循环结束条件为获取的内容中data对应的是否为空值。~~  
~~[x]10jqka代码重构，新建一个main.py主程序文件来调用其他py文件函数。~~  
~~[x]sql语句常用命令封装为`class`类对象，来调用成员方法，避免多次复写重复代码~~  

## 20230313 TODO

~~[x] 获取天天基金网基金数据 <http://fund.eastmoney.com/data/>~~  
~~[x] 获取好买基金数据 <https://www.howbuy.com/fundtool/filter.htm>~~  
[] 通过天天基金网获取基金的名称，成立日期，基金经理，基金公司  

雪球：<https://xueqiu.com/hq>

[Robots.txt测试](http://www.wetools.com/robots-tester)

## 20230314 TODO

换Golang重构代码使用
