import urllib.request
from bs4 import BeautifulSoup
from article import Article
import json

class WebScraper:

    articlesDictionary = {}
    jsonFlight = json

    def connect(self, url):
        """
        Connect function to retrieve information from a website.
        url -- A link to the same site from which we would like to extract the information.
        """

        self.source = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.source, 'html.parser')

        return self.soup


    def scrapeArticles(self, url):
        """
        A function that extracts the articles from a website and saves them in a dictionary.
        key: link (url)
        value: Article (object that contains a title, link, and content)
        url -- Link to the main page.
        """

        self.connect(url)
        titles = self.soup.findAll("h3", {"class": "media__title"})
        links = self.soup.findAll("a", {"class": "block-link__overlay-link"})

        for i in range(len(titles)):
            title = titles[i].text
            title = title.strip()
            link = links[i].attrs['href']
            if ("https://www.bbc.com" in links[i].attrs['href'] or "https://www.bbc.co" in links[i].attrs['href']):
                link = links[i].attrs['href']
            else:
                link = url + link

            if link in self.articlesDictionary:
                continue;
            else:
                scraperToArticleContent = WebScraper().scrapeArticleContent(link)
                self.articlesDictionary[link] = Article(title, link, scraperToArticleContent)

        return self.articlesDictionary


    def scrapeArticleContent(self, url):
        """
        A function that extracts the content of a specific article.
        url -- Link of a specific article.
        """

        self.connect(url)
        content = self.soup.findAll("p")
        contentString = ""
        for c in content:
            contentString = contentString + " " + c.getText()

        return contentString

    def scrapeFlights(self, url):

        self.connect(url)
        oddRowFromTable = self.soup.findAll("td", {"class": "smallrow1"})
        evenRowFromTable = self.soup.findAll("td", {"class": "smallrow2"})

        dataArrayForFlights = []
        flightsNumber =[]
        planeTypes = []
        arrives = []
        departingTimes = []
        landingTimes = []

        maxLength = max(len(oddRowFromTable), len(evenRowFromTable))
        for i in range(0, maxLength, 5):
            if i < len(oddRowFromTable):
                dataArrayForFlights.append(oddRowFromTable[i].getText())
            if i < len(evenRowFromTable):
                dataArrayForFlights.append(evenRowFromTable[i].getText())


        h =0
        return





