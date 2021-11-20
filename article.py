
class Article:
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

    def set_title(self, title):
        self.title = title

    def set_link(self, link):
        self.link = link

    def set_content(self, content):
        self.content = content

