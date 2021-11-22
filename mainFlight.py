from webScraper import WebScraper
import json
import search


#url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
url = "https://he.flightaware.com/live/airport/LLBG/arrivals"
scraper = WebScraper()
jsonFlights = scraper.scrapeFlights(url)


for i in range(5):
    words = input("Please enter the words you would like to search: ")
    searchWordsInFlights = search.search_words_in_flights(jsonFlights, words)
    if len(searchWordsInFlights) == 0:
        print("The words you entered in the flight database do not exist.")
    else:
        print("Flight details that contains the words you searched for: ")
        flagExisting = True
        for flight in searchWordsInFlights:
            print(flight)


h=0