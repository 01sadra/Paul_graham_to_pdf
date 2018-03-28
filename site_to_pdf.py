import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from fpdf import FPDF
from fpdf import HTMLMixin
class create_pdf(object):

    # Getting the urls of articles in archive page and save them in an array
    def get_urls():
        page = urllib2.urlopen("http://www.paulgraham.com/articles.html")
        soup = BeautifulSoup(page,'html.parser')
        urls = soup.findAll('table', {'width': '435'})[1].findAll('a')
        articles = []
        for url in urls:
            if  "sep.yimg" not in url["href"]: 
                articles.append("http://www.paulgraham.com/" + url["href"]) 
        return articles

    # Getting the Article of given link
    def get_article(link):
        try:
            page = urllib2.urlopen(link)
            soup = BeautifulSoup(page,'html.parser')
            font = str(soup.findAll('table', {'width':'435'})[0].findAll('font')[0])
            if not 'Get funded by' in font and not 'Watch how this essay was' in font and not 'Like to build things?' in font and not len(font)<100:
                content = font
            else:
                content = ''
                for par in soup.findAll('table', {'width':'435'})[0].findAll('p'):
                    content += str(par)
            return content
        except IndexError as erorr:
            print(erorr)

    #Eliminate the tags from given String and write it to the file
    def add_to_pdf(text_content,pdf): 
        try:
            new_text = text_content \
            .replace("<br />","\n") \
            .replace("<br/>","\n") \
            .replace("<br/><br/>","\n") \
            .replace("<br /><br />","\n") \
            .replace("<font face=\"verdana\" size=\"2\">", " ") \
            .replace("</font>"," ") \
            .replace("<b>"," ") \
            .replace("<i>"," ") \
            .replace("<ol>"," ") \
        
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
            pdf.set_font('DejaVu', '', 14.0)
            pdf.write(10, new_text)
        except (UnicodeEncodeError , AttributeError) as erorr:
            print(erorr)


    pdf = FPDF()
    article_links = get_urls()
    for link in article_links:
        content_html = get_article(link)
        add_to_pdf(content_html,pdf)    
        print(link)

    pdf.output('paul_graham.pdf', 'F')
    print("done")