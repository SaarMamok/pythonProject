import json

def words_in_web_contents(webContents, words):
    webContentsResults = []
    for webContent in webContents:
        if webContent.include(words):
            webContentsResults.append(webContent)

    return webContentsResults


def search_words_in_articles(articlesDictionary, words):
    """
    A function that searches for words in all saved articles.
    :param articlesDictionary: A dictionary that holds all the saved articles.
    :return: articlesDictionary after filtering the search.
    """

    articlesDictionarySearchResult = {}

    for article in articlesDictionary.values():
        title = article.get_title()
        link = article.get_link()
        content = article.get_content()
        if words in title or words in link or words in content:
            articlesDictionarySearchResult[article.get_link()] = article

    return articlesDictionarySearchResult


def search_words_in_flights(jsonFile, words):
    """
    A search function for words contained in the flight database (json).
    A function that asks the user to enter the words he wants to search for
    :param jsonFile: json of all flight data
    :return: searchListForFlights after filtering the search.
    """

    searchListForFlights = []
    dataFlights = json.loads(jsonFile)
    for flight in dataFlights:
         if ((words in flight['flightNumber']) or
             (words in flight['planeType']) or
             (words in flight['arrive']) or
             (words in flight['departingTime']) or
             (words in flight['landingTime'])):
             searchListForFlights.append(flight)

    return searchListForFlights
