import urllib.request
from bs4 import BeautifulSoup

from article import Article

class WebScraper:

    def connect(self, url):
        self.source = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.source, 'html.parser')
        return self.soup


    def scrapeArticle(self, url):
        self.connect(url)
        titles = self.soup.findAll("h3", {"class": "media__title"})
        links = self.soup.findAll("a", {"class": "block-link__overlay-link"})

        for i in range(len(titles)):
            title = titles[i].text
            link = links[i].attrs['href']
            if ("https://www.bbc.com" in links[i].attrs['href']):
                link = links[i].attrs['href']
            else:
                link = url + link

            if link in articlesDictionary:
                continue;
            else:
                scraperToArticleContent = WebScraper().scrapeContent(link)
                articlesDictionary[link] = Article(title, link, scraperToArticleContent)

        return articlesDictionary


    def scrapeContent(self, url):
        self.connect(url)
        content = self.soup.findAll("p")
        contentString = ""
        for c in content:
            contentString = contentString + " " + c.getText()
        return contentString



articlesDictionary = {}


url = "https://www.bbc.com"
scraper = WebScraper()
articlesDictionary = scraper.scrapeArticle(url)


h=0