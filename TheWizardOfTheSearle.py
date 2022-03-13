# -*-codeing=utf-8-*-
# @time:2020/11/7 11:43
# @File:赛尔号精灵图鉴.py
# @software:PyCharm

import re
import urllib.request, urllib.error
import os
import time
from pyquery import PyQuery
import requests

url="http://news.4399.com/seer/jinglingdaquan/"
headers={
"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
}
html = ""
req = urllib.request.Request(url=url, headers=headers, method="GET")
response = urllib.request.urlopen(req)
# try:
html = response.read().decode('gb2312')
# except UnicodeDecodeError:
#     print("解码失败")

doc = PyQuery(html)
items = doc('script').items()
for each in items:
    if len(each.text()) > 100:
        ori_data = each.text()
# print(ori_data)
detail_url_storege = []
# 获取子链接
ori_data_url = re.findall(r'gonglue(.+?)htm', ori_data)
for detail_url in ori_data_url:
    detail_url = 'http:\/\/news.4399.com\/gonglue' + detail_url + 'htm'
    detail_url = detail_url.replace('\\', '')
    # 将构造好的URL存入列表
    detail_url_storege.append(detail_url)
# print(detail_url_storege)
# 获取图片和名字
for each_url in detail_url_storege:
    # time.sleep(1)
    each_html = requests.get(each_url).content.decode(encoding='gbk', errors='ignore')
    # pq解析
    each_doc = PyQuery(each_html)
    each_name = each_doc(".focusimg>img").attr('alt')
    each_name = each_name[3:]
    each_img = each_doc(".focusimg>img").attr('src')
    # 变量可以存储图片信息
    each_img_content = requests.get(each_img).content
    # print(each_name,each_img)
    # 新建该路径下的一个jpg文件
    # 将图片存在一个文件夹
    with open('F:\\赛尔号精灵图鉴4' + "\\" + each_name + '.jpg', "wb") as file:
          file.write(each_img_content)
print('六只精灵你能秒我')



























