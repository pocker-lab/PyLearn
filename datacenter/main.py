import os
import sys

from pyutils import pyutils

sys.path.append("D:\PyLearn")

conn = pyutils.db()
tt0 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
print(f"--> 数据库中现有 {tt0} 条数据 -->")
print("-" * 80)

# print("开始执行 --> sina.py")
# os.system('python sina.py')

# print("开始执行 --> 10jka.py")
# os.system('python 10jqka.py')

# print("开始执行 --> eastmoney.py")
# os.system('python eastmoney.py')

print("开始执行 --> howbuy.py")
os.system("python howbuy.py")

print("-" * 80)
tt3 = conn.Query_Order("select count(*) from pydb.fund")[0][0]
print(f"--> 数据库中现有 {tt3} 条数据 -->")
