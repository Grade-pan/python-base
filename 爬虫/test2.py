import requests
from lxml import etree

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-11-11&leftTicketDTO.from_station=CDW' \
      '&leftTicketDTO.to_station=FZS&purpose_codes=ADULT '
r = requests.get(url)
html = r.text
print(html)
r = etree.HTML(html)
print(r.text)
