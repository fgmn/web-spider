

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pyqueryl import PyQuery as pq
import pymongo


browser = webdriver.Chrome()
# 延时等待确保content完全加载
wait = WebDriverWait(browser, 10)
KEYWORD = 'ipad'


# 抓取商品列表页
def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            # wait.until()等到某个信息加载出来
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn,J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'm-itemlist .item .item')))
        # 解析商品列表
        get_products()
    except TimeoutException:
        index_page()


def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp_itemlist .item .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),

        }
        print(product)
        save_to_mongo(product)


# 将商品信息保存至MongoDB
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
# database[数据库名]

def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION.insert(result)]:
            print('存储到mongodb成功')
    except Exception:
        print('存储到mongodb失败')

MAX_PAGE = 100

def main():
    for i in range(1, MAX_PAGE + 1):
        index_page(i)

if __name__ == '__main__':
    main()

# 如何查看mongo里的信息
#








