import sys
import urllib.request
from bs4 import BeautifulSoup
from article import Article
import multiprocessing as mp


class WebScraper:

    articlesDictionary = {}

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
            title = title.strip()
            link = links[i].attrs['href']
            if ("https://www.bbc.com" in links[i].attrs['href']):
                link = links[i].attrs['href']
            else:
                link = url + link

            if link in self.articlesDictionary:
                continue;
            else:
                scraperToArticleContent = WebScraper().scrapeContent(link)
                self.articlesDictionary[link] = Article(title, link, scraperToArticleContent)

        return self.articlesDictionary


    def scrapeContent(self, url):
        self.connect(url)
        content = self.soup.findAll("p")
        contentString = ""
        for c in content:
            contentString = contentString + " " + c.getText()

        return contentString


