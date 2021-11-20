import urllib.request
from bs4 import BeautifulSoup

from article import Article




class WebScraper:
    def __init__(self, url):
        self.url = url

        self.source = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.source, 'html.parser')

    def scrapeTitle(self):
        titles = self.soup.findAll("h3", {"class": "media__title"})
        links = self.soup.findAll("a", {"class": "block-link__overlay-link"})
        # self.soup.findAll("li", {"class":"media-list__item"

        for i in range(len(titles)):
            titles[i] = titles[i].text
            if("https://www.bbc.com" in links[i].attrs['href']):
                links[i] = links[i].attrs['href']
            else:
                links[i] = url + links[i].attrs['href']

            if link in articlesDic:
                continue;
            else:
                articlesDic[link] = Article (titles[i], "a", "a", links[i], "a")

            articles.append(Article (titles[i], "a", "a", links[i], "a"))
        h= 0
        return articles

    def scrapeContent(self):
        content = self.soup.findAll("p")
        contentString = ""
        for c in content:
            contentString = contentString + " " + c.getText()
        return contentString



articles = []

url = "https://www.bbc.com"
scraper = WebScraper(url)
articles = scraper.scrapeTitle()
articlesDic = {}
s = articles

contents =[]
for a in articles:
    url = a.link
    print(WebScraper(url).scrapeContent())
    contents.append(WebScraper(url).scrapeContent())

h=0