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
page= driver.get('https://housing.com/rent/search-P49rjj9lqcgscvm36')
while i<20:
   driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
   time.sleep(10)
   i=i+1
html=driver.page_source
soup= BeautifulSoup.BeautifulSoup(html,'html.parser')
lists = soup.find ('div',class_="results-wrapper css-19v6osn")
new=lists.findAll('article',class_="css-8jw9t9")
table=soup.find('table')
row_data=[]


with open('housee.csv','w', encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['Title','price','build area','furnishing','amenities','no of floors','lease type','images']
    thewriter.writerow(header)
    for list in new:
        title = list.find('div', class_="css-11nfaq3").text
        price= list.find('div', class_="css-1cxwewr").text
        buildarea=list.find('div', class_="css-14teu4h").text
        soup.find('table')
        image = list.find('div',class_="css-uwwqev")
        info = [title,price, buildarea,image ]
        thewriter.writerow(info)






