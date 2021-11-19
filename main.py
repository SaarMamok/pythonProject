import urllib.request
from bs4 import BeautifulSoup

from article import Article

class WebScraper:
    def __init__(self, articles, url):
        self.url = url
        self.articles = articles

        self.source = urllib.request.urlopen(self.url)
        self.soup = BeautifulSoup(self.source, 'html.parser')

    def scrapeTitle(self):
        titles = self.soup.findAll("h3", {"class": "media__title"})
        summaries = self.soup.findAll("p", {"class": "media__summary"})

        for i in range(len(titles)):
            articles.append(Article (titles[i].text, summaries[i].text, "a", "a", "a"))





articles = []
url = "https://www.bbc.com/"
WebScraper(articles, url).scrapeTitle()
s =articles