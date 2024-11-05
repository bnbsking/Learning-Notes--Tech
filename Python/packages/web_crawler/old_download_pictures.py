from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
#import requests
#import copy
#import pyautogui
import hashlib
import urllib


delaytime = 3;
count = 10;
driverpath = "C:/Users/bnbsk/Downloads/Desktop/geckodriver.exe";
driver = webdriver.Firefox(executable_path=driverpath);
driver.get('https://www.google.com/search?q=柯基&tbm=isch');

n = 0;
for i in range(count):
    if n < 4:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);");
        n = n + 1;
        time.sleep(delaytime);
    else : 
        try:
            driver.find_element_by_class_name("mye4qd").click();
            n = 0;
            time.sleep(delaytime);
        except:
            break


n = 0;
imgs = driver.find_elements_by_tag_name("img");
imglist = []
for img in imgs:
    imglist.append(img.get_attribute("src"))
hl = hashlib.md5();



for src in imglist:
    if src != None :
        print(src);
        driver.get(src);
        time.sleep(1);
        hl.update(src.encode(encoding='utf-8'));
        urllib.request.urlretrieve(src,"result\\" + hl.hexdigest() + ".png")
        n = n + 1;
print("總共 : " + str(n) + "張圖片");

driver.quit();
