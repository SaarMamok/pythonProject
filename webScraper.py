import urllib.request
from bs4 import BeautifulSoup
from article import Article
import json
from flight import Flight

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

        dataListForFlights = []
        maxLength = max(len(oddRowFromTable), len(evenRowFromTable))
        i=0
        while i < maxLength:
            j = i
            if i < len(oddRowFromTable):
                flightNumber = oddRowFromTable[i].getText()
                i += 1
                planeType = oddRowFromTable[i].getText()
                i += 1
                arrive = oddRowFromTable[i].getText()
                i += 1
                departingTime = oddRowFromTable[i].getText()
                i += 1
                landingTime = oddRowFromTable[i].getText()
                flight = Flight(flightNumber, planeType, arrive, departingTime, landingTime)
                dataListForFlights.append(flight)

            if j < len(evenRowFromTable):
                flightNumber = evenRowFromTable[j].getText()
                j += 1
                planeType = evenRowFromTable[j].getText()
                j += 1
                arrive = evenRowFromTable[j].getText()
                j += 1
                departingTime = evenRowFromTable[j].getText()
                j += 1
                landingTime = evenRowFromTable[j].getText()

                flight = Flight(flightNumber, planeType, arrive, departingTime, landingTime)

                dataListForFlights.append(flight)

            i += 1


        h =0
        return




"""
        flight1 = {
             'flightNumber':None,
             'planeTypes': None,
             'arrive': None,
             'departingTime': None,
             'landingTime': None
        }
        flight1['flightNumber'] = 44
"""
