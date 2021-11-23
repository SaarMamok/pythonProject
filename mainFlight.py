from time import sleep
from webScraper import WebScraper
import search


#url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
# a web page that requests "I am not a robot" (ReCaptcha)
# and therefore it is not possible in legal ways to extract information from the page.

url = "https://he.flightaware.com/live/airport/LLBG/arrivals"
scraper = WebScraper()

while True: # every one minute the json file is updated.
    jsonFlights = scraper.scrapeFlights(url)
    searchWordsInFlights = search.search_words_in_flights(jsonFlights)
    sleep(60)
