

import pymysql

# 连接mysql
db = pymysql.connect(host='localhost', user='root', password='520qiqi', port=3306)
# 获得mysql操作光标，利用光标执行mysql语句
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 获得第一条数据（即版本号）
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()

















