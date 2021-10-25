#方便延时加载
import time
from selenium import webdriver
import numpy as np 
# 模拟浏览器打开网站
driver = webdriver.Chrome()
driver.get('https://web-vpn.sues.edu.cn')
# 将窗口最大化
driver.maximize_window()
  

#browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()
# 延时2秒，以便网页加载所有元素，避免之后找不到对应的元素
time.sleep(2)
  

#//*[@id="username"]
#/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/form[1]/div[2]/input

# acc and pwd (自己写)

accounts = ''
pwd = ''


# Find UserName and pwd, login
driver.find_element_by_xpath(
 "//*[@id='username']").send_keys(accounts)
driver.find_element_by_xpath(
 "//*[@id='password']").send_keys(pwd)
# 在输入用户名和密码之后,点击登陆按钮
driver.find_element_by_xpath("//*[@id='passbutton']").click()
time.sleep(2)
# 点击健康填报信息
# 需在最近访问中置顶
driver.find_element_by_xpath("//*[@id='group-4']/div[2]/div/div[2]/p[1]").click()
time.sleep(5)

handles = driver.window_handles
#获取当前页句柄
print(handles)
driver.switch_to.window(handles[1]) 

# randomly choose a temperature

temp_choice = ['35.5', '35.6', '35.7', '35.8', '35.9', '36.0', '36.1', '36.2', '36.3' ,'36.4', '36.5', '36.6','36.7']
temprature = np.random.choice(temp_choice,size=1,replace=False)

print(temprature)

driver.find_element_by_xpath("//*[@id='form']/div[18]/div[1]/div/div[2]/div/div/input").send_keys(str(temprature))
#time.sleep(2)
#//*[@id="form"]/div[18]/div[1]/div/div[2]/div/div/input
driver.find_element_by_xpath('//*[@id="post"]').click()

#time.sleep(10)

# proceed 
print("体温填报成功")
time.sleep(5)
# quit browser
driver.quit()
