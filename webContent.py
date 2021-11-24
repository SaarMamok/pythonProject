from abc import ABC, abstractmethod

class WebContent(ABC):

    @abstractmethod
    def include(self, words):
        pass
