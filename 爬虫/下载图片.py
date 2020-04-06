# coding: utf8
import requests


def download_img(img_url):
    print(img_url)
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 " \
                 "Safari/537.36 "
    headers = {"User-Agent": user_agent}
    r = requests.get(img_url, headers=headers, stream=True)
    print(r.status_code)  # 返回状态码
    if r.status_code == 200:
        open('D:\\imagss\\img.png', 'wb').write(r.content)  # 将内容写入图片
        print("done")
    del r


if __name__ == '__main__':
    # 下载要的图片
    img_url = "http://pic.netbian.com/uploads/allimg/190922/212043-1569158443de0c.jpg"
    api_token = "fklasjfljasdlkfjlasjflasjfljhasdljflsdjflkjsadljfljsda"
    download_img(img_url)
