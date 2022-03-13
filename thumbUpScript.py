

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains    # 动作链
from selenium.webdriver.common.by import By
import time

# 声明浏览器对象
driver = webdriver.Chrome()

# https://user.qzone.qq.com/2714578616
# https://i.qq.com/
# https://user.qzone.qq.com/2031564629/infocenter

driver.get('https://i.qq.com/')
# driver.set_window_size(1400, 800)

# 切换作用域
driver.switch_to.frame('login_frame')

# xpath选择器
driver.find_element(By.XPATH, '//*[@id="qlogin_list"]/a').click()

# element = driver.find_element_by_link_text('注册新账号')
# ActionChains(driver).move_to_element(element).perform()     # 鼠标悬停

i = 0
# target = driver.find_elements_by_css_selector('a.btn-fs-sure')
# error: 识别为list
# target.click()
time.sleep(5)

'''
target = driver.find_elements_by_xpath('//a[@class="btn-fs-sure"]')
target.click()
driver.execute_script("arguments[0].scrollIntoView();", target)  # 滚动到元素位可见，执行js脚本
driver.execute_script("arguments[0].click();", target)
'''

while True:
        # 延时等待确保页面完全加载
        time.sleep(1)

        # elements = driver.find_elements_by_css_selector('a.item qz_like_btn_v3[data-clicklog="like"]') # 无效
        # elements = driver.find_elements_by_css_selector('i.fui-icon.icon-op-praise')
        elements = driver.find_elements_by_xpath('//a[@class="item qz_like_btn_v3 "]/i')
        if i == 20:
           break
        for element in elements:
            driver.execute_script("arguments[0].scrollIntoView();", element)  # 滚动到元素位可见
            # print(str(i)+'/'+str(len(elements)) + '点赞：' + element.get_attribute('outerHTML'))

            # 异常处理
            '''
            try:
                driver.execute_script("arguments[0].click();", element)
            except selenium.common.exceptions.ElementClickInterceptedException:
                print('Message: element click intercepted')
            '''
            # element.click()
            driver.execute_script("arguments[0].click();", element)
            
            time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 滚动到底部
        i += 1

# driver.find_element_by_id('switcher_plogin').click()
# driver.find_elements_by_css_selector('pt.qlogin.imgMouseover(this);').click()

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")  # 滚动到底部
# btns = driver.find_elements_by_css_selector('a.item.qz_like_btn_v3[data-clicklog="like"]')
# for btn in btns:
#     btn.click()
#     time.sleep(1)

# 执行js脚本
# js = "var q=document.documentElement.scrollTop=10000"
# driver.execute_script(js)