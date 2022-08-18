import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import re
import  time
import  requests
name=   input('My name?:   ')
myemail= input('What email to use:  ' )
try:
    phonenumber=input('phone number: ')
except:
    pass
message=input('What is todays message?:  ')

url= input('please input your search website:  ')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(url)
time.sleep(3)
html=driver.page_source
time.sleep(3)
soup = BeautifulSoup.BeautifulSoup(html, "html.parser")
lists = soup.findAll ('div',class_="jsx-372421607 cardWrapper")

for list in lists:
    newlink=list.findAll ('div',class_="jsx-372421607")
    for news in newlink:
        link= driver.find_element_by_xpath ('.//*[@id="agent_list_wrapper"]/div[2]/ul/div[1]/div/div/div[7]/button')
        link.click()
        time.sleep(3)
        infoname=driver.find_element_by_id("name" )
        infoname.click()
        infoname.send_keys(name)

        infomail = driver.find_element_by_id("email")
        infomail.click()
        infomail.send_keys(myemail)

        infonumber = driver.find_element_by_id("phone")
        infonumber.click()
        infonumber.send_keys(phonenumber)

        infomessage = driver.find_element_by_id("comment")
        infomessage.click()
        infomessage.send_keys(message)

        time.sleep(10)

        try:
            capture=driver.find('div',class_="recaptcha-checkbox-checkmark")
            capture.click()
            time.sleep(5)
        except:
            pass

        send=driver.find_element_by_id('ask-a-question-submit')
        send.click()
        time.sleep(10)
        exitsend=driver.find_element_by_xpath('.//*[@id="modalaskRealtor"]/div/div/div[1]/button')
        exitsend.click()











