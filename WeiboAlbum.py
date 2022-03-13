
import time
from selenium import webdriver
from pyquery import PyQuery as pq
import requests

# 基本用法不熟悉，许多时间花在测试代码的用法上


headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.104 Safari/537.36',
        'cookie':  'SINAGLOBAL=7466163151376.384.1608513472452; '
                    'SUB=_2A25y24hLDeRhGeFN4lQS8yzKwjqIHXVuJygDrDV8PUJbkNAfLUzBkW1NQ6Uo-Eqe8yaYSEJHYpvcm8Z-gbTR5OvI;'
                    'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFp_qA5PeUUajo65_1sPmuo5NHD95QNe0.ce0eESo.cWs4Dqcj3i--Xi-zRiKLhi--ciK.ci-z4i--fi-zpiKnfi--fi-20i-8FP0epehMX; '
                    'UOR=,,www.baidu.com; wvr=6; _s_tentry=-; Apache=3663562456469.9263.1615541209405;'
                    'ULV=1615541209471:12:6:4:3663562456469.9263.1615541209405:1615475780957; YF-V-WEIBO-G0=35846f552801987f8c1e8f7cec0e2230;'
                    'XSRF-TOKEN=F3bDfRr048ApGcU8pbSr8EcL; WBPSESS=d4xMu9nMFhY85YGY8BTO1qRx1TRD4EL58EQE0K7Awb9bnGFcEcZsoKOHWV4cOsiZfW9V-euHQupCuXSf-ZIizQ5MVKRYKAhbYJYSq3REZRDxZ0cyrpANaj9VIHdwAjVQ; wb_view_log_7396332696=1280*7201; webim_unReadCount=%7B%22time%22%3A1615549047065%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A40%2C%22msgbox%22%3A0%7D'

    }

url = 'https://weibo.com/p/1005053932588380/photos?type=photo#place'
url1 = 'https://weibo.com/p/1006051242213702/photos?from=page_100605&mod=TAB#place'
# response = requests.get(url, headers=headers)
# print(response.text)

browser = webdriver.Chrome()
# 只能加载部分相片
browser.get(url1)

time.sleep(10)


# doc = pq(response.text)
doc = pq(browser.page_source)
target = doc('.PCD_photo_album_v2')
# print(target)

# 调用items方法
items = target.find('.photo_pict').items()
# 返回一个生成器对象
# print(items)
# print(type(items))

count = 0
pic_urls = []
for item in items:
    # print(item)
    pic_url = item.attr('src')
    if len(pic_url) < 65:
        pic_url = 'https:' + pic_url
    pic_urls.append(pic_url)
    print(pic_url)
    count += 1
    if count > 20:
        break

i = 100
for p in pic_urls:
    pic = requests.get(p).content
    with open('C:\\Users\\DELL\\Desktop\\刘浩存\\' + str(i) + '.jpg', 'wb') as file:
        file.write(pic)
    i += 1
'''
'''

