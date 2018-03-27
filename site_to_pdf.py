import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from fpdf import FPDF
from fpdf import HTMLMixin
import genshi
class create_pdf(object):
    def __init__(self, article_links, content_html, content_text):
        self.article_links=article_links
        self.content_html=content_html
        self.content_text=content_text

    def get_urls():
        page = urllib2.urlopen("http://www.paulgraham.com/articles.html")
        soup = BeautifulSoup(page,'html.parser')
        urls = soup.findAll('table', {'width': '435'})[1].findAll('a')
        articles = []
        for url in urls:
            if  "sep.yimg" not in url["href"]: 
                articles.append("http://www.paulgraham.com/" + url["href"]) 
        return articles

    def get_article(link):
        page = urllib2.urlopen(link)
        soup = BeautifulSoup(page,'html.parser')
        font = str(soup.findAll('table', {'width':'435'})[0].findAll('font')[0])
        if not 'Get funded by' in font and not 'Watch how this essay was' in font and not 'Like to build things?' in font and not len(font)<100:
            content = font
        else:
            content = ''
            for par in soup.findAll('table', {'width':'455'})[0].findAll('p'):
                content += str(par)
        return content

    def html_to_text(content):
        return genshi.core.Markup(content.replace("\n","<br />").split("<br /><br />"))

    def add_to_pdf(text_content):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_xy(0, 0)
        pdf.set_font('arial', 'B', 13.0)
        pdf.cell(60, 10, "", 0, 1, 'C')
        HTMLMixin.write_html(self = pdf,text = text_content, image_map = None)
        pdf.output('paul.pdf', 'F')


    article_links = get_urls()
    content_html = get_article(article_links[0])
    content_text = html_to_text(content_html)
    add_to_pdf(content_html)
    