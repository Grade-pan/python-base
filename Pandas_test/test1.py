import pandas as pd
import numpy as np

# s = pd.Series([1, 2, 3, np.nan], index=['A', 'B', 'C', 'D'])
# print(s)
# dates = pd.date_range('20191029', periods=5)
# print(dates)
# df = pd.DataFrame(np.random.rand(5, 5), columns=['a', 'b', 'c', 'd', 'e'])
# print(df)
# df1 = pd.DataFrame({
#     'A': 1,
#     'B': pd.date_range('20191029', periods=4),
#     'C': pd.Series(np.arange(4)),
#     'D': pd.Categorical(['test', 'train', 'test', 'train'])
# })
# print(df1)
# print(df1.dtypes)
# print(df1.index)
# print(df1.columns)
# print(df1.values)
# noteSeries = pd.Series(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
# index = [1, 2, 3, 4, 5, 6, 7]
# weekdaySeries = pd.Series(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
# index = [1, 2, 3, 4, 5, 6, 7]
# df2 = pd.DataFrame([noteSeries, weekdaySeries])
# print(df2)
# # df2["No."] = pd.Series([1, 2, 3, 4, 5, 6, 7])
# # print('df2:\n{}\n'.format(df2))
#
# df3 = pd.DataFrame({"note": ["C", "D", "E", "F", "G", "A", "B"],
#                     "weekday": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]})
# print("df3:\n{}\n".format(df3))
# del df3["note"]
# print('df3:\n{}\n'.format(df3))
# df1 = pd.DataFrame(np.arange(400).reshape(20, 20))
# df1.columns = ['column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7', 'column8', 'column9',
#                'column10', 'column10', 'column12', 'column13', 'column14', 'column15', 'column16', 'column17',
#                'column18',
#                'column19', 'column20']
# df1.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
# print(df1)
# print(df1.index)
# print(df1.columns)
# print(df1.iloc[[1], 0])
# print(df1.loc[['B'], 'column1'])
# df1 = pd.read_excel('D:\\China_weather\\db_weather.xlsx')
# print(df1)
# print(df1.iloc[[128], np.arange(9)])
# print(df1.describe())  # 数字总结
# print(df1.T)  # 数据翻转
# url = 'http://www.weather.com.cn/textFC/xn.shtml'
# dfs = pd.read_html(url)
# print(dfs)
from PIL._imaging import display

# print(7 in [1, 2, 3, 4, 5])
# print(set([1, 2, 3]) & set([2, 3, 4]))  # 交集
# print(set([1, 2, 3]) | set([2, 3, 4]))  # 并集
# number = pd.read_csv('H:\\pandas中文参考手册 (cookbook翻译版) 完整版PDF\\pandas-cookbook-code-notes_jb51\\t1.csv')
# # A = number['A']
# # print(A)
# # A = A.isnull().sum()
# # print(A)
# print(number.tail())
# print(number.columns)
# print(number.count())
# print(number.describe())
# print(number.isnull().any().any())
# print(number != np.nan)
# print(number.shape)
# print(number.T)
# print(number.info())
# print(number.describe(include=[np.number], percentiles=[.01, .05, .10, .25, .5, .75, .9, .95, .99]).T)
# A = number.memory_usage(deep=True)
# print(A)
# # 改变数据类型 由int64变为int8
# # 任何数值类型的列，只要有一个缺失值，就会成为浮点型；这列中的任何整数都会强 制成为浮点型
# number['A'] = number['A'].astype(np.int8)
# number['B'] = number['B'].astype(np.int8)
# number['C'] = number['C'].astype(np.int8)
# number['1'] = number['1'].astype(np.int8)
# A = number.memory_usage(deep=True)
# print(A)
# print(number.dtypes)
data_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"  # 填写url读取
df = pd.read_html(data_url)
print(df)
