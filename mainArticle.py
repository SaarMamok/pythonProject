from webScraper import WebScraper
import search

url = "https://www.bbc.com"
scraper = WebScraper()
articlesDictionary = scraper.scrapeArticles(url) # this line takes about 25 seconds because of the connection of all the article pages.

for i in range(5):

    words = input("\nPlease enter the words you would like to search: ")
    articlesDictionarySearchResult = search.words_in_web_contents(articlesDictionary.values(), words)

    if len(articlesDictionarySearchResult) == 0:
        print("\nThe words you entered in the article database do not exist.")
    else:
        print("\nLinks to website where the words you entered appear: ")
        for article in articlesDictionarySearchResult:
            print(article.link)
