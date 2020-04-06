# 导入MySQL驱动:
import pymysql

# 注意把password设为root口令，需要提前创建好数据库
conn = pymysql.connect(user='root', password="123456", database='python', host='127.0.0.1', port=3306,
                       charset='utf8')
buffered = True
cursor = conn.cursor()
Sum = 2
# 创建user表:
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('drop table if exists user')
cursor.execute('create table user (id int  AUTO_INCREMENT PRIMARY KEY,  name varchar(2000),link varchar(2000))')
with open('E:\\aaaa.text', 'r') as f:
    while Sum < 99:
        A_String = str(f.readline())
        print(A_String.split('     ')[0])
        print(A_String.split('     ')[-1])
        cursor.execute(
            'insert into user (name, link) values (%s, %s)', [A_String.split('     ')[0], A_String.split('     ')[-1]])
        # 提交事务:
        conn.commit()
        print('第%d行数据写入成功' % Sum)
        Sum = Sum + 1
        new_id = cursor.lastrowid
    f.close()
# 关闭Cursor和Connection:
cursor.close()
conn.close()
print('数据写入成功')
