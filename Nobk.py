from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4 as BeautifulSoup
import  requests
from csv import writer
import time
i=0
PATH = "C:\\Users\\headybii\\Downloads\\Compressed\\chromedriver.exe"
driver= webdriver.Chrome(PATH)
page= driver.get('https://www.nobroker.in/property/rent/delhi/South%20Delhi?searchParam=W3sibGF0IjoyOC40ODE2NTUxLCJsb24iOjc3LjE4NzI4NTY5OTk5OTk5LCJwbGFjZUlkIjoiQ2hJSnFYN2phNzNoRERrUlJBOVQyTFhVQUpnIiwicGxhY2VOYW1lIjoiU291dGggRGVsaGkifV0=&radius=2.0&sharedAccomodation=0&city=delhi&locality=South%20Delhi')
while i<200:
   driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
   time.sleep(1)
   i=i+1

html=driver.page_source
soup= BeautifulSoup.BeautifulSoup(html,'html.parser')
lists = soup.findAll ('div',class_="bg-white rounded-2 bg-clip-padding overflow-hidden my-1.2p mx-0.5p tp:border-b-0 tp:shadow-cardShadow tp:mt-0.5p tp:mx-0 tp:mb:1p hover:cursor-pointer nb__2_XSE")
table=soup.find('table')
row_data=[]


with open('housNobb.csv','w', encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['Title','BHK','Price','Location','build area','furnishing','amenities','no of floors','lease type','images']
    thewriter.writerow(header)
    for list in lists:
        title = list.find('span', class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full").text
        location = list.find('div', class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0 po:max-w-95").text
        price = list.find('div',class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r-0").text
        bhk= list.find('div',class_="flex flex-1 pl-0.5p").text
        buildarea = list.find('div',class_="flex flex-col w-33pe items-center border-r border-r-solid border-card-overview-border-color tp:w-half po:w-full last:border-r-1").text
        furnishing = list.find ('div', class_="flex-1 border-r border-r-solid border-r-cardbordercolor flex").text
        amenisties = list.find ('div',class_="mb-srp__card__summary__list--item")
        nooffloors = list.find ('div',data_summary_="mb-srp__card__summary--value")
        ageproperty =list.find ('div',class__="mb-srp__card__summary--label" ,data_summary_="transaction")
        leasetype =list.find ('div',data_summary_="mb-srp__card__summary--value")
        images =list.find ('div',class_="absolute right-0 top-0 m-1p h-1.4p w-1.4p rounded-t-2")
        info=[ title,bhk,price,location,buildarea,furnishing,amenisties,nooffloors,leasetype,images]
        thewriter.writerow(info)