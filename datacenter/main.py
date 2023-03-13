import os

from pyutils import pyutils

conn = pyutils.db()
tt0 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
print(f"<-- 数据库中现有 {tt0} 条数据 -->")
print("-" * 100)

print("开始执行sina.py")
os.system('python sina.py')

print("开始执行10jka.py")
os.system('python 10jqka.py')

print("开始执行eastmoney.py")
os.system('python eastmoney.py')

print("-" * 80)
tt3 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
print(f"<-- 数据库中现有 {tt3} 条数据 -->")
