import urllib2
from bs4 import BeautifulSoup
articles = "http://www.paulgraham.com/articles.html"
page = urllib2.urlopen(articles)
soup = BeautifulSoup(page,'html.parser')
new_url=soup.find('a')
print(new_url)