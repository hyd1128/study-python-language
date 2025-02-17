#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2024/9/6 9:14
# @Author : limber
# @desc :

# python内置标准库
import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')

# 创建一个Cursor
cursor = conn.cursor()

# 执行一条sql语句，创建user表
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# 继续执行一条SQL语句，插入一条记录:

sql = f"select * from user"
result = cursor.execute(sql)
print(str(result))

for i in result:
    print(i)
# 通过rowcount获得插入的行数
print(cursor.rowcount)

# 提交事务
conn.commit()
# 关闭cursor
cursor.close()
# 关闭connection
conn.close()
