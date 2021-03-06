#方便延时加载
import time
from selenium import webdriver
import numpy as np 
import ddddocr as docr
import urllib
import os
from os.path import join
#read files


import PIL 
from PIL import Image

import random



File_Path = 'D:/Auto_Temp'
acc_file = 'acc.txt'
pwd_file = 'pwd.txt'
Digit_Path = '/Digit_Temp'
Digit_Xpath = "//*[@id='fm1']/div[4]/img"
Digit_Filename = '/digit.png'

with open(join(File_Path,acc_file), 'r+', encoding='utf-8') as f_acc:
    acc_ar = f_acc.read().splitlines()


with open(join(File_Path,pwd_file), 'r+', encoding='utf-8') as f_pwd:
    pwd_ar = f_pwd.read().splitlines()


for i in range(len(acc_ar)):
    
    # 模拟浏览器打开网站
    driver = webdriver.Chrome()
    #options.add_argument('--log-level=3')
    driver.get('https://web-vpn.sues.edu.cn')
    # 将窗口最大化
    # driver.maximize_window()


    #browser.find_element_by_xpath('/html/body/div[1]/div/div[4]/span/a[1]').click()
    # 延时2秒，以便网页加载所有元素，避免之后找不到对应的元素
    time.sleep(2)
  
    accounts = acc_ar[i]
    pwd = pwd_ar[i]
    #  //*[@id="username"]
    #/html/body/div[2]/div[1]/div[2]/div/div[1]/div/div/form[1]/div[2]/input

    # acc and pwd (自己写)

    #accounts = ''
    #pwd = ''


    # Find UserName and pwd, login
    driver.find_element_by_xpath(
    "//*[@id='username']").send_keys(accounts)
    driver.find_element_by_xpath(
    "//*[@id='password']").send_keys(pwd)
    # 验证码
    ## locate Digit
    #img = driver.find_element_by_xpath(Digit_Xpath)
    #src = img.get_attribute('src')
    ## Download Digit image
    Digit_save_path = join(File_Path, Digit_Path)
    with open(join(Digit_save_path, Digit_Filename), 'wb+') as d:
        d.write(driver.find_element_by_xpath(Digit_Xpath).screenshot_as_png)
    
    #urllib.urlretrieve(src, Digit_Filename)
    ## ddddocr recognize numbers
    ocr = docr.DdddOcr()
    with open(join(Digit_save_path, Digit_Filename),'rb') as d:
        img_bytes = d.read()
    res = ocr.classification(img_bytes)



    driver.find_element_by_xpath("//*[@id='authcode']").send_keys(str(res))
    # 在输入用户名和密码之后,点击登陆按钮
    driver.find_element_by_xpath("//*[@id='passbutton']").click()
    time.sleep(2)
    # 点击健康填报信息
    # 需在最近访问中置顶
    driver.find_element_by_xpath("//*[@id='group-4']/div[2]/div/div[2]/p[2]").click()
    time.sleep(3)

    handles = driver.window_handles
    #获取当前页句柄
    print(handles)
    driver.switch_to.window(handles[1]) 

    # randomly choose a temperature

    a = random.uniform(35,37)
    temprature = round(a,1)

    print(temprature)

    driver.find_element_by_xpath("//*[@id='form']/div[18]/div[1]/div/div[2]/div/div/input").send_keys(str(temprature))
    #time.sleep(2)
    #//*[@id="form"]/div[18]/div[1]/div/div[2]/div/div/input
    driver.find_element_by_xpath('//*[@id="post"]').click()

    #time.sleep(10)

    # proceed 
    print("学号：{}\n体温填报成功".format(accounts))
    time.sleep(3)
    # 删除验证码图片
    os.remove(join(Digit_save_path, Digit_Filename))
    # quit browser
    driver.quit()


