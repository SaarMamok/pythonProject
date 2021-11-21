

def search_words_in_articles(articlesDictionary, words):
    """
    A function that searches for words in all saved articles.
    articlesDictionary - A dictionary that holds all the saved articles.
    words - words we would like to look for in articles.
    """

    articlesDictionarySearchResult = {}
    words = words
    for article in articlesDictionary.values():
        title = article.get_title()
        link = article.get_link()
        content = article.get_content()
        if words in title or words in link or words in content:
            articlesDictionarySearchResult[article.get_link()] = article

    return articlesDictionarySearchResult
