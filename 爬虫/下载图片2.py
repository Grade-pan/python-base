import urllib.request


def download_img(img_url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/51.0.2704.103 " \
                 "Safari/537.36 "
    headers = {"User-Agent": user_agent}
    request = urllib.request.Request(img_url, headers=headers)
    print('下载链接：%s' % img_url)
    try:
        response = urllib.request.urlopen(request)
        img_name = "img1.png"
        filename = "D:\\imagss\\"+img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read())  # 将内容写入图片
            return filename
    except:
        return "failed"


if __name__ == '__main__':
    # 下载要的图片
    img_url = "http://pic.netbian.com/uploads/allimg/190922/212043-1569158443de0c.jpg"
    download_img(img_url)
print('下载成功')
