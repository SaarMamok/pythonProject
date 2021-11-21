
class Flight:

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

    def get_flightNumber(self):
        return self.flightNumber

    def get_planeTypes(self):
        return self.planeTypes

    def get_arrive(self):
        return self.arrive

    def get_departingTime(self):
        return self.departingTime

    def get_landingTime(self):
        return self.landingTime

    def set_flightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def set_planeType(self, planeType):
        self.planeType = planeType

    def set_arrive(self, arrive):
        self.arrive = arrive

    def set_departingTime(self, departingTime):
        self.departingTime = departingTime

    def set_landingTime(self, landingTime):
        self.landingTime = landingTime

