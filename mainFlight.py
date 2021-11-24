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
    words = input("Please enter the words you would like to search: ")
    searchWordsInFlights = search.words_in_web_contents(jsonFlights, words)
    if len(searchWordsInFlights) == 0:
        print("The words you entered in the flight database do not exist.")
    else:
        print("Flight details that contains the words you searched for: ")
        for flight in searchWordsInFlights:
            print(flight)
    sleep(60)
