from webScraper import WebScraper

url = "https://www.bbc.com"
scraper = WebScraper()
articlesDictionary = scraper.scrapeArticle(url)

k=0