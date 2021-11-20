

def search_words(articlesDictionary, words):
    articlesDictionarySearchResult = {}
    # words = input("Please Input Search words: ")
    words = words
    for article in articlesDictionary.values():
        title = article.get_title()
        link = article.get_link()
        content = article.get_content()
        if words in title or words in link or words in content:
            articlesDictionarySearchResult[article.get_link()] = article

    return articlesDictionarySearchResult
