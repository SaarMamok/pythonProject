from webScraper import WebScraper
import search

url = "https://www.bbc.com"
scraper = WebScraper()
articlesDictionary = scraper.scrapeArticle(url)


for i in range(5):
    words = input("Please enter the words you would like to search: ")
    articlesDictionarySearchResult = search.search_words(articlesDictionary, words)
    for a in articlesDictionarySearchResult:
        print(a)
