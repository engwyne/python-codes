from selenium.webdriver.common.by import By
from selenium import webdriver
import bs4 as BeautifulSoup
import  requests
from csv import writer
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = "C:\\Users\\headybii\\Downloads\\Compressed\\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get('https://www.magicbricks.com/Real-estate-projects-Search/residential-new-project?&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=New-Delhi&mbTrackSrc=tabChange&page=1&category=B')
html=driver.page_source
time.sleep(5)
suu = BeautifulSoup.BeautifulSoup(html, "html.parser")

lists = suu.findAll ('div',class_="clearAll")
for list in lists:
    element = driver.find_element(By.ID, 'projectSearchResultWrapper').click()
    time.sleep(5)
    newhtml=driver.page_source
    time.sleep(5)
    soup= BeautifulSoup.BeautifulSoup ( newhtml,"html.parser")


    with open('housing.csv','w', encoding='utf8',newline='') as f:
        thewriter= writer(f)
        header=['Title','location','map Url','build area','furnishing','amenities','no of floors','lease type','images']
        thewriter.writerow(header)

        title = list.find('h1', class_="heading")
        location = list.find('div', class_="proj-info__data__block")
        price = list.find('div',class_="proDescColm2")
        bhk= list.find('div',class_="proDescColm1")
        buildarea = list.find('div',class_="mb-srp__card__summary__list--item")
        furnishing = list.find ('div', class_="mb-srp__card__summary--value")
        amenisties = list.find ('div',class_="mb-srp__card__summary__list--item")
        nooffloors = list.find ('div',data_summary_="mb-srp__card__summary--value")
        ageproperty =list.find ('div',class__="mb-srp__card__summary--label" ,data_summary_="transaction")
        leasetype =list.find ('div',data_summary_="mb-srp__card__summary--value")
        images =list.find ('img',class_ ="lazy")
        info=[ title,buildarea,furnishing,amenisties,nooffloors,leasetype,images ]
        print(title,location)
        thewriter.writerow(info)

driver.quit()


driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        newhtml = driver.page_source
        time.sleep(5)
        suop = BeautifulSoup.BeautifulSoup(html, "html.parser")

,class_="jsx-3970352998"