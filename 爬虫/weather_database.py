import pymysql
import xlrd

list_path = ['D:/China_weather/db_weather.xlsx', 'D:/China_weather/gat_weather.xlsx',
             'D:/China_weather/hb_weather.xlsx',
             'D:/China_weather/hz_weather.xlsx', 'D:/China_weather/hn_weather.xlsx', 'D:/China_weather/hd_weather.xlsx',
             'D:/China_weather/xn_weather.xlsx', 'D:/China_weather/xb_weather.xlsx']
name_database = ['db_weather', 'gat_weather', 'hb_weather', 'hz_weather', 'hn_weather', 'hd_weather', 'xn_weather',
                 'xb_weather']
try:
    database = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='java')
    print('连接成功')
except:
    print('连接失败')
cursor = database.cursor()

for i in range(0, 7):
    try:
        path = list_path[i]
        db_database = xlrd.open_workbook(path)
        print("打开文件成功")
    except:
        print('打开文件失败')
    sheet = db_database.sheet_by_name('Sheet1')

    query = 'drop table if exists' + ' ' + name_database[i]
    cursor.execute(query)
    query = """create table""" + ' ' + name_database[i] + ' ' + """(id int  AUTO_INCREMENT PRIMARY KEY,province varchar(30),city varchar(30),week_date varchar(30),wind varchar(30),
        high_temperature varchar(30),weather_p varchar(30),wind_2 varchar(30),low_temperature varchar(30))"""
    cursor.execute(query)
    name_insert = name_database[i]

    for i in range(1, sheet.nrows - 1):
        province = sheet.cell(i, 1).value
        city = sheet.cell(i, 2).value
        week_date = sheet.cell(i, 3).value
        wind = sheet.cell(i, 4).value
        high_temperature = sheet.cell(i, 5).value
        weather_p = sheet.cell(i, 6).value
        wind_2 = sheet.cell(i, 7).value
        low_temperature = sheet.cell(i, 8).value
        query = """insert into """ + ' ' + name_insert + ' ' + """(province, city, week_date, wind, high_temperature, weather_p, wind_2, 
        low_temperature) values(%s,%s,%s,%s,%s,%s,%s,%s) """
        cursor.execute(query, (province, city, week_date, wind, high_temperature, weather_p, wind_2, low_temperature))
    database.commit()
    print(path, '写入数据库成功')
cursor.close()
database.close()
