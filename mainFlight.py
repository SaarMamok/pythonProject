from webScraper import WebScraper
import search

#url = "http://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"
url = "https://he.flightaware.com/live/airport/LLBG/arrivals"
scraper = WebScraper()
flightsDictionary = scraper.scrapeFlights(url)
