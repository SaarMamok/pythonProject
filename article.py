from webContent import WebContent

class Article(WebContent):
    title = None
    link = None
    content = None

    def __init__(self, title, link, content):
            self.title = title
            self.link = link
            self.content = content

    def get_title(self):
        return self.title

    def get_link(self):
        return self.link

    def get_content(self):
        return self.content

    def include(self, words):
        return words in " ".join([self.title, self.link, self.content])
