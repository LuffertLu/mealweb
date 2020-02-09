#! /usr/bin/python3

from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://bbs.51testing.com/forum.php")

# 设置浏览器宽800，高200
driver.set_window_size(800, 200)

# 等待3秒
sleep(3)

# 最大化窗口
driver.maximize_window()

# 等待3秒
sleep(3)

# 设置浏览器宽200，高100
driver.set_window_size(200, 100)

# 等待3秒
sleep(3)

# 定位“登录”按钮并获取登录按钮的type属性值
type = driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').get_attribute("type")

# 打印type属性值
print(type)

# 刷新页面
driver.refresh()

# 等待3秒
sleep(3)

# 定位“登录”按钮并进行点击操作
driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').click()

# 等待3秒
sleep(3)

# 后退到上一个页面
driver.back()

# 用id定位账号输入框并输入账号
driver.find_element_by_id("ls_username").send_keys("luffert")

# 用id定位密码输入框并输入密码
driver.find_element_by_id("ls_password").send_keys("51testing")

# 等待3秒
sleep(3)

# 定位“登录”按钮并进行点击操作
driver.find_element_by_xpath('//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button').click()

# 等待3秒
sleep(10)

# 定位“退出”按钮并获取登录按钮的文本
txt = driver.find_element_by_xpath('//*[@id="um"]/p[1]/a[6]').text
print(txt)

# 定位“退出”按钮并获取href属性值
txt = driver.find_element_by_xpath('//*[@id="um"]/p[1]/a[6]').get_attribute("href")
print(txt)

# 拉指定高度
js = 'document.documentElement.scrollTop=200;'
driver.execute_script(js)

# 等待3秒
sleep(3)

# 用目标元素做参考下拉页面
target_element = driver.find_element_by_id('ft')
js = 'arguments[0].scrollIntoView();'
driver.execute_script(js,target_element)

# 等待3秒
sleep(3)

#driver.quit()
# 定位“退出”按钮并点击
driver.find_element_by_xpath('//*[@id="um"]/p[1]/a[6]').click()

# 等待3秒
sleep(3)

# 转到页面alert形式的提醒框
#alert = driver.switch_to.alert

# 查看alert中的文字
#print(alert.text)

# 点击确定
#alert.accept()

# 点击取消（如果有）
#alert.dismiss()

# 退出浏览器
driver.quit()
