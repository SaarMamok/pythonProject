from webScraper import WebScraper
import search

url = "https://www.bbc.com"
scraper = WebScraper()
articlesDictionary = scraper.scrapeArticles(url)

for i in range(5):
    words = input("Please enter the words you would like to search: ")
    articlesDictionarySearchResult = search.search_words_in_articles(articlesDictionary, words)
    if len(articlesDictionarySearchResult) == 0:
        print("The words you entered in the article database do not exist.")
    else:
        print("Links to sites where the words you entered appear: ")
        flagExisting = True
        for article in articlesDictionarySearchResult:
            print(article)
