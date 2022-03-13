

import requests
from lxml import etree
import random
import time
import pandas as pd

headers_cur ='''Cookie: ll="118220"; bid=uo6qbpntGdE; douban-fav-remind=1; _vwo_uuid_v2=D843314CE04CCBB03109064B0FCEE72BB|3541694b8165faa953fc78d1e228aad9; __gads=ID=669c5b056fcd0086-2254ffb9e5c400ad:T=1606387728:S=ALNI_MY-rt4SYXx7RqeHEwpIiQ4g7hbmig; push_doumail_num=0; push_noty_num=0; __utmv=30149280.22254; ap_v=0,6.0; __utmc=30149280; __utma=30149280.1926299260.1604057374.1630399842.1630403319.24; __utmz=30149280.1630403319.24.8.utmcsr=search.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/movie/subject_search; __utmt=1; __utmb=30149280.1.10.1630403319; dbcl2="222546299:81P3G5dLzPA"; ck=y3h0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'''

# 快速构造headers
def HTTD(headers):
    st1 = headers.split('\n')
    headers_dict = {}
    for text1 in st1:
        s1 = text1.replace(': ', '#$', 1)
        st2 = s1.split('#$')
        headers_dict[st2[0]] = st2[1]
    return headers_dict

headers = HTTD(headers_cur)

# 请求页面
def get_page(url):
    response = requests.get(url=url, headers=headers)
    html = response.text
    return html

# 获取翻页的link
def parse4link(html, base_url):
    link = None
    html_elem = etree.HTML(html)
    url = html_elem.xpath('//div[@id="paginator"]/a[@class="next"]/@href')
    if url:
        link = base_url + url[0]
    return link

# 解析页面
def parse4html(html):
    html = etree.HTML(html)
    contents = html.xpath('//div[@class="comment-item "]/div[2]/p/span/text()')
    return contents

# 打开文件
def openfile(fm, name):
    f_name = "C:/Users/DELL/Desktop/电影放映厅/源文本/" + str(name) + '.txt'
    fd = None
    if fm == 'txt':
        fd = open(f_name, 'w', encoding='utf-8')
    return fd

# 保存到文件
def save2file(fm, fd, data):
    global num
    if fm == 'txt':
        for item in data:
            # fd.write(str(num) + '\n')
            # num += 1
            fd.write(str(item) + '\n')

# 爬虫
def crawl(id, name):
    moveID = str(id)
    base_url = 'https://movie.douban.com/subject/' + moveID + '/comments'
    fm = 'txt'

    fd = openfile(fm, name)
    print('开始爬取')
    link = base_url
    while link:
        time.sleep(1)
        print('正在爬取' + str(link))
        html = get_page(link)
        link = parse4link(html, base_url)
        data = parse4html(html)
        save2file(fm, fd, data)
        time.sleep(random.random())
    fd.close()
    print('结束爬取')

def work():
    df = pd.read_excel("C:/Users/DELL/Desktop/电影放映厅/电影清单.xls", usecols=[0,1], names=None)
    df_li = df.values.tolist()
    print(df_li)

    for i in df_li:
        crawl(i[0], i[1])
work()
