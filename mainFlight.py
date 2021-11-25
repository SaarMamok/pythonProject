import json
from webScraper import WebScraper
import search


#url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
# a web page that requests "I am not a robot" (ReCaptcha)
# and therefore it is not possible in legal ways to extract information from the page.

url = "https://he.flightaware.com/live/airport/LLBG/arrivals"
scraper = WebScraper()

while True:
    flightsData = scraper.scrapeFlights(url)

    dicFlights = [flight.__dict__ for flight in flightsData]

    jsonFlights = json.dumps({"results": dicFlights})

    print("\nAll flights data: ")
    print(dicFlights)

    words = input("\nPlease enter the words you would like to search: ")
    searchWordsInFlights = search.words_in_web_contents(flightsData, words)
    if len(searchWordsInFlights) == 0:
        print("\nThe words you entered in the flight database do not exist.")
    else:
        print("\nFlight details that contains the words you searched for: ")
        for flight in searchWordsInFlights:
            print(flight.__dict__)

