import bs4 as BeautifulSoup
import  requests
from csv import writer
url='https://housing.com/rent/search-P49rjj9lqcgscvm36'
page=requests.get(url)
soup= BeautifulSoup.BeautifulSoup(page.content,'html.parser')
lists = soup.find ('div',class_="results-wrapper css-19v6osn")
new=lists.findAll('article',class_="css-8jw9t9")
table=soup.find('table')
row_data=[]


with open('housee.csv','w', encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['Title','build area','furnishing','amenities','no of floors','lease type','images']
    thewriter.writerow(header)
    for list in new:
        title = list.find('div', class_="css-11nfaq3").text
        price= list.find('div', class_="css-1cxwewr").text
        buildarea=list.find('div', class_="css-14teu4h").text
        soup.find('table')


        image = list.find('div', class_="slider-inner css-7nnslv")

        print(title,price,buildarea,image,row_data)



