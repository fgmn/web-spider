

import requests
from lxml import etree
import csv
import random
import time
import re
import json

global num
num = 0

def get_page(url):
    headers = {
    'Cookie': 'll="118220"; bid=uo6qbpntGdE; douban-fav-remind=1; _vwo_uuid_v2=D843314CE04CCBB03109064B0FCEE72BB|3541694b8165faa953fc78d1e228aad9; dbcl2="222546299:WVqp0AeMZi4"; __gads=ID=669c5b056fcd0086-2254ffb9e5c400ad:T=1606387728:S=ALNI_MY-rt4SYXx7RqeHEwpIiQ4g7hbmig; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22254; ct=y; ck=nhuh; ap_v=0,6.0; __utmc=30149280; __utma=30149280.1926299260.1604057374.1628153545.1628155644.14; __utmb=30149280.0.10.1628155644; __utmz=30149280.1628155644.14.5.utmcsr=cnblogs.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html = response.text
    # print(html)
    return html

# 获取翻页的link
def parse4link(html, base_url):
    link = None
    html_elem = etree.HTML(html)
    url = html_elem.xpath('//div[@class="paginator"]/span[@class="next"]/a/@href')
    # print(url)
    if url:
        link = base_url + url[0]
    # print(link)
    return link

def parse4html(html):
    html = etree.HTML(html)
    review_id = html.xpath('//div[@class="main review-item"]/@id')
    print(review_id)
    return review_id

def get_rev(id):
    for one in id:
        rev_link = 'https://movie.douban.com/j/review/' + str(one) + '/full'
        print(rev_link)
        html = get_page(rev_link)
        print(html)

def openfile(fm):
    fd = None
    if fm == 'txt':
        fd = open('花束般的爱恋.txt', 'w', encoding='utf-8')
    return fd

def save2file(fm, fd, data):
    global num
    if fm == 'txt':
        for item in data:
            fd.write(str(num) + '\n')
            num += 1
            fd.write(str(item) + '\n')

# 爬虫
def crawl():
    moveID = '33407124'     # 电影id
    base_url = 'https://movie.douban.com/subject/' + moveID + '/reviews'
    fm = 'txt'

    fd = openfile(fm)
    print('开始爬取')
    link = base_url
    while link:
        print('正在爬取' + str(link) + '……')
        html = get_page(link)
        link = parse4link(html, base_url)
        rev_id = parse4html(html)
        html_full = get_rev(rev_id)
        save2file(fm, fd, data)
        time.sleep(random.random())
    fd.close()
    print('结束爬取')

crawl()

# 影评的页面格式不同，调整一下 xpath

# https://movie.douban.com/j/review/13783507/full
# https://movie.douban.com/j/review/13753111/full
# 获取影评的编号

# 获取完整版影评，下一步：页面解析