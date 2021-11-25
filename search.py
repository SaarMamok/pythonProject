
def words_in_web_contents(webContents, words):
    """
    Search function in all site data if words are contained in them.
    :param webContents: web Contents.
    :param words: Search terms you want to search for.
    :return: All the content that the search terms contain.
    """

    webContentsResults = []
    for webContent in webContents:
        if webContent.include(words):
            webContentsResults.append(webContent)

    return webContentsResults
