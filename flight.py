from webContent import WebContent
import json

class Flight(WebContent):

    flightNumber = None
    planeType = None
    arrive = None
    departingTime = None
    landingTime = None

    def __init__(self, flightNumber, planeType, arrive, departingTime, landingTime):
        self.flightNumber = flightNumber
        self.planeType = planeType
        self.arrive = arrive
        self.departingTime = departingTime
        self.landingTime = landingTime

    def include(self, words):
        """
        Turns a flight data containing words into one string.
        :param words: Words you would like to search for.
        :return: string that contains all the flight data.
        """

        return words in " ".join([self.flightNumber, self.planeType, self.arrive, self.departingTime, self.landingTime])

    def to_json(self):
        return json.dumps(self.__dict__)

