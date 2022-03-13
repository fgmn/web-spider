
import requests
import urllib.request
import urllib.error
import socket
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait




# response = urllib.request.urlopen('https://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))


# try:
#     response=urllib.request.urlopen('https://httpbin.org/get',timeout=10)
#     print(response.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

#https://www.baidu.com/
# request = urllib.request.urlopen('https://httpbin.org/get')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# r=requests.get('https://httpbin.org/get')
# print(type(r.text))
# # print(r.cookies)
# # print(r.text)
# print(r.json)
# print(type(r.json()))

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                        'Chrome/88.0.4324.104 Safari/537.36',
# 'cookie': '_zap=80ec4a0d-361f-400c-944b-a3e62defb1d5; '
#           'd_c0="AMBUjZ7M1xGPTp4meYAfTAlLVSAAKEkcCjY=|1599319821";'
#           '_ga=GA1.2.1961794314.1599319824; '
#           'tst=r; z_c0=Mi4xcE40UUJ3QUFBQUFBd0ZTTm5zelhFUmNBQUFCaEFsVk5XQ3RmWUFDRDhuX3paSnQ2bVduZ0V1eklfX0EteER2VWRB|1601297752|29368a9e54186f85e4803c98fd34254a29ea6674;'
#           ' __utma=51854390.1961794314.1599319824.1606916146.1606916146.1; __utmz=51854390.1606916146.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/19613730/hot;'
#           ' __utmv=51854390.100--|2=registration_date=20171228=1^3=entry_date=20171228=1; q_c1=9c7b01f71f6d4f09b000d473535a85af|1610845953000|1599385348000; _xsrf=e85d76e6-5049-4790-9bea-7e50b904b02f; '
#           'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1611975174,1611994297,1612152191,1612171719; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1612171719; SESSIONID=EcRNv8jPAD2CICcrDyhJ1Tro60wM4DObB5nKqJFU94n;'
#           ' KLBRSID=d017ffedd50a8c265f0e648afe355952|1612171718|1612171716; JOID=V1wcCkpsPLrtwOYNLGAJb7FoJt8xKFLoq7LfanwpeYWugaFvU6b4pYHF6gAkz7RbhjtUlGKbJluiM_JSz7o3rxg=;'
#           ' osd=VV8TB0puP7XgwOQOI20JbbJnK98zK13lq7DcZXEpe4ahjKFtUKn1pYPG5Q0kzbdUiztWl22WJlmhPP9Szbk4ohg='
#            }
# r = requests.get('https://www.zhihu.com/', headers=headers)
# pattern = re.compile('<div itemProp="zhihu:question" itemType="http://schema.org/Question" itemscope=""><meta itemProp="url" content="https://www.zhihu.com/question/(.*)"/><meta itemProp="name" content="(.*?)"/>', re.S)
# title = re.findall(pattern, r.text)
# print(title)
# print(r.text)


# r = requests.get('https://github.com/favicon.ico')
# print(r.text)
# print(r.content)
# with open('favicon', 'wb') as f:
#     f.write(r.content)

# XPATH库的使用


# selenium自动化工具使用

b = webdriver.Chrome()
try:
    b.get('https://www.baidu.com/')
    input = b.find_element_by_id('kw')
    input.send_keys('刘浩存')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(b, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(b.current_url, '\n')
    print(b.get_cookies(),  '\n')
    print(b.page_source)
finally:
    # b.close()
    print(1)















































