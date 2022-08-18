import requests
import bs4 as BeautifulSoup
print('input website address here:')
url= input (" ")

page= requests.get(url)
soup= BeautifulSoup.BeautifulSoup(page.content,'html.parser')
print(soup.text)
