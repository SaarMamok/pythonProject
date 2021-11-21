
class Flight:

    flightNumber = None
    planeTypes = None
    arrive = None
    departingTime = None
    landingTime = None

    def __init__(self, flightNumber, planeTypes, arrive, departingTime, landingTime):
        self.flightNumber = flightNumber
        self.planeTypes = planeTypes
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

    def set_planeTypes(self, planeTypes):
        self.planeTypes = planeTypes

    def set_arrive(self, arrive):
        self.arrive = arrive

    def set_departingTime(self, departingTime):
        self.departingTime = departingTime

    def set_landingTime(self, landingTime):
        self.landingTime = landingTime

