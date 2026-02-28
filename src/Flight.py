class Flight:
    def __init__(self, flight_code, departure, destination, schedule):
        self.__flight_code = flight_code
        self.__departure = departure
        self.__destination = destination
        self.__schedule = schedule
        self.__book_list = []
        self.__available_seats = 50
        self.__economy_seats = 25
        self.__business_seats = 25
    def get_economy_seats(self):
        return self.__economy_seats
    def get_business_seats(self):
        return self.__business_seats
    def get_flight_code(self):
        return self.__flight_code
    def get_departure(self):
        return self.__departure
    def get_destination(self):
        return self.__destination
    def get_schedule(self):
        return self.__schedule
    def get_available_seats(self):
        return self.__available_seats
    def add_book_list(self,ticket):
        self.__book_list.append(ticket)
    def calculate_available_seats(self):
        self.__available_seats = 50
        self.__economy_seats = 25
        self.__business_seats = 25
        for ticket in self.__book_list:
            if ticket.get_status() == "confirmed":
                self.__available_seats-= ticket.get_no_of_seats()
            if ticket.get_seat_class() == "economy" and ticket.get_status() == "confirmed":
                self.__economy_seats-= ticket.get_no_of_seats()
            elif ticket.get_seat_class() == "business" and ticket.get_status() == "confirmed":
                self.__business_seats-= ticket.get_no_of_seats()
        return self.__available_seats, self.__economy_seats, self.__business_seats
    def __str__(self):
        return ("Flight Code: " + self.__flight_code
        + "\nDeparture: " + self.__departure
        + "\nDestination: " + self.__destination
        + "\n"+str(self.__schedule)
        + "\nAvailable Seats: " + str(self.__available_seats)
        + "\nEconomy seats: " + str(self.get_economy_seats())
        + "\nBusiness seats: " + str(self.get_business_seats()))