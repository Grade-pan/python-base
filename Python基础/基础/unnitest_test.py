# 引入unittest模组
import unittest

import HTMLTestRunner
# 定义测试类，名字为DemoTests
# 该类必须继承unittest.TestCase基类
import pymysql
import requests
from lxml import etree
from selenium import webdriver
import time


class DemoTests(unittest.TestCase):

    # 使用'@'修饰符，注明该方法是类的方法
    # setUpClass方法是在执行测试之前需要先调用的方法
    # 是开始测试前的初始化工作
    @classmethod
    def setUpClass(cls):
        print("call setUpClass()")

    # 每一个测试开始前的预置条件
    def setUp(self):
        print("call setUp()")

    # 每一个测试结束以后的清理工作
    def tearDown(self):
        print("call tearDown()")

    # 测试一（务必以test开头）
    def test_01(self):
        print("call test_01()")
        pass

    # 测试三（务必以test开头）
    def test_02(self):
        print("call test_02()")
        pass

    # 测试三（务必以test开头）
    def test_03(self):
        print("call test_03()")
        pass

    def test_04(self):
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\18178\\AppData\\Roaming\\Python\\Python37\\site-packages\\geckodriver.exe")
        driver.get("http://m.news.cctv.com/2019/10/13/ARTIEfbmIpxtaqf7TUDrzRV5191013.shtml")
        time.sleep(3)
        for i in range(9, 20):
            selector = '.cnt_bd > p:nth-child(' + str(i) + ')'
            text = driver.find_elements_by_css_selector(selector)
        driver.quit()

    def test_05(self):
        conn = pymysql.connect(user='root', password="123456", database='python', host='127.0.0.1', port=3306,
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute('drop table if exists IP1')
        cursor.execute('create table IP1 (id int AUTO_INCREMENT PRIMARY KEY, ip varchar(200),port varchar(200),'
                       'address varchar(200),Character_net varchar(200),Time_now varchar(200))')
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/67.0.3396.99 Safari/537.36",
        }
        Sum = 1
        for i in range(1, 21):
            url = 'http://www.89ip.cn/index_' + str(i) + '.html'
            response = requests.get(url, headers=header)
            html = etree.HTML(response.text)
            for i in range(1, 16):
                xpath_l = '/html/body/div[4]/div[1]/div/div[1]/table/tbody/tr' + str([i]) + '/td'
                html_data = html.xpath(xpath_l)
                A_list = list()
                for i in html_data:
                    A_list.append(i.text)
                try:
                    cursor.execute(
                        'insert into IP1 (ip,port,address,Character_net,Time_now) values (%s, %s,%s,%s,%s)',
                        [A_list[0], A_list[1], A_list[2], A_list[3], A_list[-1]])
                    print('第%d条数据写入成功' % Sum)
                    Sum = Sum + 1
                    conn.commit()
                except:
                    print('数据获取完毕')
        cursor.close()
        conn.close()
    # tearDownClass方法是执行完所有测试后调用的方法
    # 是测试结束后的清除工作
    @classmethod
    def tearDownClass(cls):
        print("call tearDownClass()")


# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    # unittest.main(verbosity=1)
    suite = unittest.TestSuite()
    suite.addTest(DemoTests('test_01'))
    suite.addTest(DemoTests('test_02'))
    suite.addTest(DemoTests('test_03'))
    suite.addTest(DemoTests("test_04"))
    suite.addTest(DemoTests('test_05'))
    # 创建一个新的测试结果文件
    buf = open("D:\\result.html", "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=buf,
                                           title="411 Test Result",
                                           description="Test Case Run Result")
    # 运行测试，并且将结果生成为HTML
    runner.run(suite)

    # 关闭文件输出

    buf.close()
