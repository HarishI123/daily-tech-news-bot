import requests
from bs4 import BeautifulSoup
import lxml  #using lxml as parser

#generating the url, in this case it has software as default since it is tech news.
def generate_url(topic="/software",page=1):
    base_url = "https://www.techradar.com"
    return base_url+topic+"/page/"+str(page)

news_url = generate_url(page=1) # to store the url of the first page
# print(news_url)

#function to scarp the news
def scarp_page(url):
    try:
        soup = BeautifulSoup(requests.get(url).text,"lxml")
        resultList = soup.find("div",class_="listingResults").find_all("div",class_="listingResult")
        result = []
        for res in resultList:
            try:
                atag = res.find("a")
                result.append([atag["aria-label"],atag["href"]])
            except: pass
        return result
    except Exception as e: print(e)

#All news is sorta stored here.
news_obtained = scarp_page(news_url)
# print(news_obtained)



