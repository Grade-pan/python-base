from datetime import datetime, timedelta

now = datetime.now()
# datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
print(now)  # 本地时间
dt = now.timestamp()
print(dt)
print(datetime.fromtimestamp(dt))  # 本地时间
print(datetime.utcfromtimestamp(dt))  # UTC时间
print(now.strftime('%a, %b %d %H:%M:%S'))  # 日期转换为字符串
str1 = '2019-9-20 18:19:59'
print(datetime.strptime(str1, '%Y-%m-%d %H:%M:%S'))  # 字符串转换为日期
print(now + timedelta(hours=5))  # 日期变化
print(now - timedelta(days=500000))  # 日期变化
