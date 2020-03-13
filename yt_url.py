# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:23:29 2020

@author: User
"""

import requests
import time

from xlwt import Workbook 
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 

from bs4 import BeautifulSoup

r=requests.get("https://www.youtube.com/playlist?list=PLKWF_aeBV2BEQGXt9Bt_NH7MIGwacucQ9") #Insert the link of the youtube playlist whose videos you want to scrape
temp = "initial"
v_no = 0;
c_no = 0;

soup=BeautifulSoup(r.content,'html.parser')
with Chrome() as driver:
    for i in soup.find_all('a'):
        link = i.get('href')  
        yt_link = "https://www.youtube.com"+ link
        print(yt_link)
        if (link[1:6:] == "watch") and (link != temp) and (link[-2::] == "0s") :
            print(i.get('href'))
            wait = WebDriverWait(driver,50)
            driver.get(yt_link)
            time.sleep(1)
            v_no = v_no + 1;
        
            for item in range(15): # Increasing the highest range can get more content
                time.sleep(2)
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.PAGE_DOWN)
                
            for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#comment #content-text"))):
                    print(comment.text)
                    sheet1.write(c_no, 0, comment.text)
                    sheet1.write(c_no, 1, v_no)
                    c_no = c_no + 1;
                    print("**************************")
            
            wb.save('xlwt_example.xls')
            print("+++++++++++++++++++++++++++++++++++++++++++++")                
        temp = link
        print("===========================================================================")
    
print('Complete!')