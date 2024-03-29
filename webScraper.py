import urllib.request
from bs4 import BeautifulSoup
from article import Article
from flight import Flight
import datetime


class WebScraper:
    articlesDictionary = {}
    lastFlightUpdate = datetime.datetime.now()
    dataListForFlights = []
    hashFlightData = None


    def connect(self, url):
        """
        Connect function to retrieve information from a website.
        :param url: a link to the same site from which we would like to extract the information.
        :return: an object that contains all the html content.
        """

        self.source = urllib.request.urlopen(url)
        self.soup = BeautifulSoup(self.source, 'html.parser')

        return self.soup


    def scrapeArticles(self, url):
        """
        A function that extracts the articles from a website and saves them in a dictionary.
        key: link (url)
        value: Article (object that contains a title, link, and content)
        :param url: Link to the main page.
        :return: a dictionary of articles that contains all the information of the articles (title, link, content).
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
        :param url: link of a specific article.
        :return: content of a specific article.
        """

        self.connect(url)
        content = self.soup.findAll("p")
        contentString = ""
        for c in content:
            contentString = contentString + " " + c.getText()

        return contentString


    def scrapeFlights(self, url):
        """
        A function that extracts information from the flight website and updates every minute in case there was a change.
        :param url: a link to the website of the flight table.
        :return: data list for flights containing flight information.
        """

        if self.lastFlightUpdate > datetime.datetime.now() - datetime.timedelta(minutes=1) and len(self.dataListForFlights) != 0:
            return self.dataListForFlights

        self.connect(url)

        # The flight table (html) is divided into even and odd rows.
        oddRowFromTable = self.soup.findAll("td", {"class": "smallrow1"})
        evenRowFromTable = self.soup.findAll("td", {"class": "smallrow2"})

        # Check if there was a change in the flight data
        currentFlightHash = hash(str(oddRowFromTable) + str(evenRowFromTable))
        if (currentFlightHash == self.hashFlightData ):
            print("Data didn't change")
            return self.dataListForFlights
        self.hashFlightData = currentFlightHash

        self.dataListForFlights = []
        maxLength = max(len(oddRowFromTable), len(evenRowFromTable))
        i = 0

        while i < maxLength:

            j = i
            # check that there is no deviation from the length of the list.
            if i < len(oddRowFromTable):
                flightNumberOddRow = oddRowFromTable[i].getText()
                i += 1
                planeTypeOddRow = oddRowFromTable[i].getText()
                i += 1
                arriveOddRow = oddRowFromTable[i].getText()
                i += 1
                departingTimeOddRow = oddRowFromTable[i].getText()
                i += 1
                landingTimeOddRow = oddRowFromTable[i].getText()

                flightOddRow = Flight(flightNumberOddRow, planeTypeOddRow, arriveOddRow, departingTimeOddRow,
                                      landingTimeOddRow)
                self.dataListForFlights.append(flightOddRow)

            # check that there is no deviation from the length of the list.
            if j < len(evenRowFromTable):
                flightNumberEvenRow = evenRowFromTable[j].getText()
                j += 1
                planeTypeEvenRow = evenRowFromTable[j].getText()
                j += 1
                arriveEvenRow = evenRowFromTable[j].getText()
                j += 1
                departingTimeEvenRow = evenRowFromTable[j].getText()
                j += 1
                landingTimeEvenRow = evenRowFromTable[j].getText()

                flightEvenRow = Flight(flightNumberEvenRow, planeTypeEvenRow, arriveEvenRow, departingTimeEvenRow,
                                       landingTimeEvenRow)
                self.dataListForFlights.append(flightEvenRow)

            i += 1

        self.lastFlightUpdate = datetime.datetime.now()
        return self.dataListForFlights

