import os

from pyutils import pyutils

conn = pyutils.db()
tt0 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
print(f"<-- 数据库中现有 {tt0} 条数据 -->")

print("开始执行sina.py")
os.system('python datacenter/sina.py')

print("开始执行10jka.py")
os.system('python datacenter/10jqka.py')

print("-" * 100)
tt3 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
print(f"<-- 数据库中现有 {tt3} 条数据 -->")
