import urllib.request
from bs4 import BeautifulSoup
from article import Article
import json


class WebScraper:

    articlesDictionary = {}
    jsonFlights = None

    def connect(self, url):
        """
        Connect function to retrieve information from a website.
        url -- a link to the same site from which we would like to extract the information.
        returns - an object that contains all the html content.
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
        returns - a dictionary of articles that contains all the information of the articles (title, link, content).
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
        url -- link of a specific article.
        return - content of a specific article.
        """

        self.connect(url)
        content = self.soup.findAll("p")
        contentString = ""
        for c in content:
            contentString = contentString + " " + c.getText()

        return contentString


    def scrapeFlights(self, url):
        """
        A function that extracts flight information.
        url -- a link to the website of the flight table.
        return - jsonFlights containing flight information.
        """
        self.connect(url)

        # The flight table (html) is divided into even and odd rows.
        oddRowFromTable = self.soup.findAll("td", {"class": "smallrow1"})
        evenRowFromTable = self.soup.findAll("td", {"class": "smallrow2"})

        dataListForFlights = []
        maxLength = max(len(oddRowFromTable), len(evenRowFromTable))
        i=0

        while i < maxLength:
            j = i
            if i < len(oddRowFromTable): # check that there is no deviation from the length of the list.
                flightOddRow = {
                    'flightNumber': None,
                    'planeType': None,
                    'arrive': None,
                    'departingTime': None,
                    'landingTime': None
                }
                flightOddRow['flightNumber'] = oddRowFromTable[i].getText()
                i += 1
                flightOddRow['planeType'] = oddRowFromTable[i].getText()
                i += 1
                flightOddRow['arrive'] = oddRowFromTable[i].getText()
                i += 1
                flightOddRow['departingTime'] = oddRowFromTable[i].getText()
                i += 1
                flightOddRow['landingTime'] = oddRowFromTable[i].getText()

                dataListForFlights.append(flightOddRow)

            if j < len(evenRowFromTable): # check that there is no deviation from the length of the list.
                flightEvenRow = {
                    'flightNumber': None,
                    'planeType': None,
                    'arrive': None,
                    'departingTime': None,
                    'landingTime': None
                }
                flightEvenRow['flightNumber'] = evenRowFromTable[j].getText()
                j += 1
                flightEvenRow['planeType'] = evenRowFromTable[j].getText()
                j += 1
                flightEvenRow['arrive'] = evenRowFromTable[j].getText()
                j += 1
                flightEvenRow['departingTime'] = evenRowFromTable[j].getText()
                j += 1
                flightEvenRow['landingTime'] = evenRowFromTable[j].getText()

                dataListForFlights.append(flightEvenRow)

            i += 1

        self.jsonFlights = json.dumps(dataListForFlights) # write to json
        return self.jsonFlights

