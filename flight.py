from webContent import WebContent

class Flight(WebContent):
    flightNumber = None
    planeType = None
    arrive = None
    departingTime = None
    landingTime = None

    def include(self, words):
        return words in " ".join([self.flightNumber, self.planeType, self.arrive, self.departingTime, self.landingTime])