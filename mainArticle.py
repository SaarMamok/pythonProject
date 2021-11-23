from webScraper import WebScraper
import search

url = "https://www.bbc.com"
scraper = WebScraper()
articlesDictionary = scraper.scrapeArticles(url) # this line takes about 25 seconds because of the connection of all the article pages.

for i in range(5):
    articlesDictionarySearchResult = search.search_words_in_articles(articlesDictionary)
