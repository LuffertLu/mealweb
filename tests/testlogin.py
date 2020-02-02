#模拟登陆实战
# _*_ coding: utf-8 _*_

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def login(account, password):
    # 因为亚马逊的登录页面需要在主页中获取
    login_url = get_login_url()
    options = webdriver.ChromeOptions()  # 开启chrome设置
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)  # 设置无图模式
    # options.add_argument("--headless")    # 设置无头浏览器
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_options=options)  # 实例化driver
    wait = WebDriverWait(driver, 10)  # 智能等待
    driver.get(login_url)
    account_input = wait.until(EC.presence_of_element_located((By.ID, 'ap_email')))
    password_input = wait.until(EC.presence_of_element_located((By.ID, 'ap_password')))
    submit = wait.until(EC.element_to_be_clickable((By.ID, 'signInSubmit')))
    account_input.send_keys(account)
    password_input.send_keys(password)
    submit.click()
    # 等待五秒。浏览器关闭
    time.sleep(5)
    driver.close()

# 获取登录地址
def get_login_url():
    headers = {
        "Host": 'www.amazon.cn',
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
    }
    # 使用requests发送get请求，获取页面的源代码
    r = requests.get('https://www.amazon.cn',headers=headers).text
    # 使用bs4解析页面代码
    soup = BeautifulSoup(r, 'lxml')
    # css选择器获取元素
    url_params = soup.select('#nav-link-yourAccount')[0]['href']
    login_url = 'https://www.amazon.cn' + url_params
    print(login_url)
    return login_url

if __name__ == '__main__':
    login(你的账号, 你的密码)

