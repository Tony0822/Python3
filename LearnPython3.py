# !/usr/bin/env python3
# ---coding:UTF-8---

print ('hello world')

# 模块
# datetime
from datetime import datetime 
now = datetime.now() #获取当前的时间
print ("当前时间为：%s" % now)



'''
# 导入sqlite3驱动
import sqlite3

# 连接到sqlite3数据库
# 数据库文件是test.db
# 如果数据库不存在，会自动在当前目录创建
conn = sqlite3.connect('test.db')

# 创建一个cursor
cursor = conn.cursor()

# 执行一条sql语句，创建user表
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 插入一条记录
cursor.execute('insert into user (id name) values (\'1\', \'Michael\')')

print ('数据表的行数 %d' % cursor.rowcount)

# 关闭数据库
cursor.close()
#提交事务
cursor.commit()
# 关闭connection
conn.close()
'''