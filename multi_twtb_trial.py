#方便延时加载
import time
from selenium import webdriver
import numpy as np 
import ddddocr as docr
import urllib
import os
from os.path import join
#read files
import urllib.request
import cv2 #进行模板匹配
#from PIL import Images
import PIL 
from PIL import Image

import random
#import beam

from selenium.webdriver.common.action_chains import ActionChains  #包含滑块操作

File_Path = 'D:/Auto_Temp/'
acc_file = 'acc.txt'
pwd_file = 'pwd.txt'
Digit_Path = '/Digit_Temp'
Digit_Xpath = "//*[@id='fm1']/div[4]/img"
Digit_Filename = '/digit.png'
knob_Filename = '/knob.png'
slider_Filename = '/slider.png'
trial_Filename = '/trial.png'
import io
Digit_save_path = join(File_Path, Digit_Path)
def cal_offset(x1, y1, x2, y2, x3, y3):
    ans = 0
    if x1 == x2:
        ans = abs(y1 - y2)
    elif x1 == x3:
        ans = abs(y1 - y3)
    else:
        ans = abs(y2 - y3)
    return ans

def convert(img, target_type_min, target_type_max, target_type):
    imin = img.min()
    imax = img.max()

    a = (target_type_max - target_type_min) / (imax - imin)
    b = target_type_max - a * imax
    new_img = (a * img + b).astype(target_type)
    return new_img

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
    # 获取当前页句柄
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
    # 处理滑动验证码
    # offset = 0 ## offset指拖动距离，需要传参
    # 滑块Xpath：//*[@id='layui-layer100001']/div/div/div/div[2]/div[2]/div[2]
    knob_xpath = "//*[@id='layui-layer100001']/div/div/div/div[2]/div[2]/div[2]"
    knob_image_xpath = "//*[@id='layui-layer100001']/div/div"
    small_slider_xpath = "//*[@id='layui-layer100001']/div/div/div/div[1]/img[2]"
    knob_image_class = "ap-slider-bg"

    '''
    browser.save_screenshot('screenshot.png')
    img = browser.find_element_by_xpath('//*[@id="cryptogram"]')
    loc = img.location

    image = cv2.LoadImage('screenshot.png', True)
    out = cv2.CreateImage((150,60), image.depth, 3)
    cv2.SetImageROI(image, (loc['x'],loc['y'],150,60))
    cv2.Resize(image, out)
    cv2.SaveImage('out.jpg', out)
    '''

    # get the image source
    #img = driver.find_element_by_class_name('ap-slider-bg')
    #src = img.get_attribute('src')
    #print("src: {}\n".format(src))
    # download the image
    #filepath = join(Digit_save_path, knob_Filename)
    #urllib.request.urlretrieve(src, filepath)
    with open(join(Digit_save_path, knob_Filename), 'wb+') as d: # 保存验证码图片
        d.write(driver.find_element_by_xpath(knob_image_xpath).screenshot_as_png)


    #img = Image.open(io.BytesIO(file.read()))
    with open(join(Digit_save_path, knob_Filename), 'rb') as file, Image.open(io.BytesIO(file.read())) as t:
        target_img = t
    target_img = np.asarray(PIL.Image.open(join(Digit_save_path, knob_Filename)))
    
    with open(join(Digit_save_path, slider_Filename), 'wb+') as d: # 保存小滑块图片，以进行模板匹配
        d.write(driver.find_element_by_xpath(small_slider_xpath).screenshot_as_png)

    template_img = np.asarray(PIL.Image.open(join(Digit_save_path, trial_Filename)))
    #with open(join(Digit_save_path, slider_Filename), 'rb') as file, Image.open(io.BytesIO(file.read())) as t:
    #    template_img = t


    '''
    result = cv2.matchTemplate(img, template, cv2.TM_SQDIFF)

    # the get the best match fast use this:
    (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
    (x,y) = minloc

    # get all the matches:
    result2 = np.reshape(result, result.shape[0]*result.shape[1])
    sort = np.argsort(result2)
    (y1, x1) = np.unravel_index(sort[0], result.shape) # best match
    (y2, x2) = np.unravel_index(sort[1], result.shape) # second best match
    ## https://stackoverflow.com/questions/14727255/opencv-python-matchtemplate-function-with-multiple-matches/14729254
    '''
    # 将图片转为numpy array格式
    print(type(target_img), type(template_img))
    target_img = PIL.Image.fromarray(np.uint8(target_img))
    template_img = PIL.Image.fromarray(np.uint8(template_img))
    target_img = np.array(target_img)
    template_img = np.array(template_img)
    #print(target_img.dtype)
    #target_img = convert(target_img, 0, 255, np.uint8)
    #template_img = convert(template_img, 0, 255, np.uint8)
    #info = np.iinfo(target_img.dtype) # Get the information of the incoming image type
    #data = data.astype(np.float64) / info.max # normalize the data to 0 - 1
    #target_img = target_img.astype(np.float64) / info.max
    #target_img = 255 * target_img
    #template_img = template_img.astype(np.float64) / info.max
    #template_img = 255 * template_img
    print(type(target_img), type(template_img))

    # 还要转化色彩空间
    target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
    template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
    print(type(target_img), type(template_img))
    template_match_result = cv2.matchTemplate(target_img, template_img, cv2.TM_SQDIFF)

    result_t = np.reshape(template_match_result, template_match_result.shape[0]*template_match_result.shape[1])
    sort = np.argsort(result_t)
    (y1, x1) = np.unravel_index(sort[0], result_t.shape) # best match
    (y2, x2) = np.unravel_index(sort[1], result_t.shape) # second best match
    (y3, x3) = np.unravel_index(sort[2], result_t.shape) # third best match

    offset = cal_offset(x1, y1, x2, y2, x3, y3)


    
    knob = driver.find_element_by_xpath(knob_xpath)
    Actionchains(driver).drag_and_drop_by_offset(knob, offset, 0).perform()

    # proceed 
    print("学号：{}\n体温填报成功".format(accounts))
    time.sleep(3)
    # 删除验证码图片
    os.remove(join(Digit_save_path, Digit_Filename))
    os.remove(join(Digit_save_path, knob_Filename))
    os.remove(join(Digit_save_path, slider_Filename))
    print("cache images cleaned!")
    time.sleep(2)
    # quit browser
    driver.quit()


