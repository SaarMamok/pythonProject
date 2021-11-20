
class Flight:
    airlineCompany = None
    flightNumber = None
    arrive = None
    terminal = None
    scheduledTime = None
    updatedTime = None
    status = None

    def __init__(self, airlineCompany, flightNumber, arrive, terminal, scheduledTime, updatedTime, status):
        self.airlineCompany = airlineCompany
        self.flightNumber = flightNumber
        self.arrive = arrive
        self.terminal = terminal
        self.scheduledTime = scheduledTime
        self.updatedTime = updatedTime
        self.status = status

    def get_airlineCompany(self):
        return self.airlineCompany

    def get_flightNumber(self):
        return self.flightNumber

    def get_arrive(self):
        return self.arrive

    def get_terminal(self):
        return self.terminal

    def get_scheduledTime(self):
        return self.scheduledTime

    def get_updatedTime(self):
        return self.updatedTime

    def get_status(self):
        return self.status

    def set_airlineCompany(self, airlineCompany):
        self.airlineCompany = airlineCompany

    def set_flightNumber(self, flightNumber):
        self.flightNumber = flightNumber

    def set_arrive(self, arrive):
        self.arrive = arrive

    def set_terminal(self, terminal):
        self.terminal = terminal

    def set_scheduledTime(self, scheduledTime):
        self.scheduledTime = scheduledTime

    def set_updatedTime(self, updatedTime):
        self.updatedTime = updatedTime

    def set_status(self, status):
        self.status = status