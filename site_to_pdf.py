import urllib2
from bs4 import BeautifulSoup

def get_urls():
    page = urllib2.urlopen("http://www.paulgraham.com/articles.html")
    soup = BeautifulSoup(page,'html.parser')
    urls = soup.findAll('table', {'width': '435'})[1].findAll('a')
    articles = []
    for url in urls:
        print(url)
        if  "http://" not in url["href"]: 
            articles.append("http://www.paulgraham.com/" + url["href"]) 
    return articles


article_links = get_urls()
for article_link in article_links:
    print(article_link)
