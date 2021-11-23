import json


def search_words_in_articles(articlesDictionary):
    """
    A function that searches for words in all saved articles.
    articlesDictionary -- A dictionary that holds all the saved articles.
    return - articlesDictionary after filtering the search.
    """

    words = input("Please enter the words you would like to search: ")
    articlesDictionarySearchResult = {}
    words = words

    for article in articlesDictionary.values():
        title = article.get_title()
        link = article.get_link()
        content = article.get_content()
        if words in title or words in link or words in content:
            articlesDictionarySearchResult[article.get_link()] = article

    if len(articlesDictionarySearchResult) == 0:
        print("The words you entered in the article database do not exist.")
    else:
        print("Links to sites where the words you entered appear: ")
        for article in articlesDictionarySearchResult:
            print(article)

    return articlesDictionarySearchResult


def search_words_in_flights(jsonFile):
    """
    A search function for words contained in the flight database (json).
    A function that asks the user to enter the words he wants to search for
    jsonFile -- json of all flight data
    return - searchListForFlights after filtering the search.
    """

    searchListForFlights = []
    dataFlights = json.loads(jsonFile)
    words = input("Please enter the words you would like to search: ")
    for flight in dataFlights:
         if ((words in flight['flightNumber']) or
             (words in flight['planeType']) or
             (words in flight['arrive']) or
             (words in flight['departingTime']) or
             (words in flight['landingTime'])):
             searchListForFlights.append(flight)

    if len(searchListForFlights) == 0:
        print("The words you entered in the flight database do not exist.")
    else:
        print("Flight details that contains the words you searched for: ")
        for flight in searchListForFlights:
            print(flight)

    return searchListForFlights
