from abc import ABC, abstractmethod

class WebContent(ABC):
    """
    Abstract class
    """

    @abstractmethod
    def include(self, words):
        pass
