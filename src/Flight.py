class Flight:

    def __init__(self, flight_code, departure, destination, schedule):
        self.__flight_code = flight_code
        self.__departure = departure
        self.__destination = destination
        self.__schedule = schedule
        self.__booking_list = []
        self.__available_seats = 50

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

    def add_booking(self, booking):
        self.__booking_list.append(booking)

    def update_available_seats(self):
        self.__available_seats = 50
        for booking in self.__booking_list:
            if booking.get_status() == 'confirmed':
                self.__available_seats -= booking.get_no_of_seats()

    def __str__(self):
        return (
            'Flight Code: ' + self.__flight_code + '\n'
            + 'Departure: ' + self.__departure + '\n'
            + 'Destination: ' + self.__destination + '\n'
            + str(self.__schedule) + '\n'
            + 'Available Seats: ' + str(self.__available_seats)
        )
