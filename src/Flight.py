class Flight:

    TOTAL_SEATS = 50
    ECONOMY_SEATS = 25
    BUSINESS_SEATS = 25

    def __init__(self, flight_code, departure, destination, schedule):
        self.__flight_code = flight_code
        self.__departure = departure
        self.__destination = destination
        self.__schedule = schedule
        self.__booking_list = []

    def get_flight_code(self):
        return self.__flight_code

    def get_departure(self):
        return self.__departure

    def get_destination(self):
        return self.__destination

    def get_schedule(self):
        return self.__schedule

    # ================= TOTAL AVAILABLE =================
    def get_available_seats(self):
        booked = sum(
            b.get_no_of_seats()
            for b in self.__booking_list
            if b.get_status() == "confirmed"
        )
        return self.TOTAL_SEATS - booked

    # ================= ECONOMY AVAILABLE =================
    def get_economy_seats(self):
        booked = sum(
            b.get_no_of_seats()
            for b in self.__booking_list
            if b.get_status() == "confirmed" and b.get_seat_class().lower() == "economy"
        )
        return self.ECONOMY_SEATS - booked

    # ================= BUSINESS AVAILABLE =================
    def get_business_seats(self):
        booked = sum(
            b.get_no_of_seats()
            for b in self.__booking_list
            if b.get_status() == "confirmed"
            and b.get_seat_class().lower() == "business"
        )
        return self.BUSINESS_SEATS - booked

    def add_booking(self, booking):
        self.__booking_list.append(booking)

    def __str__(self):
        return (
            "Flight Code: "
            + self.__flight_code
            + "\nDeparture: "
            + self.__departure
            + "\nDestination: "
            + self.__destination
            + "\n"
            + str(self.__schedule)
            + "\nTotal Available Seats: "
            + str(self.get_available_seats())
            + "\nEconomy Seats Left: "
            + str(self.get_economy_seats())
            + "\nBusiness Seats Left: "
            + str(self.get_business_seats())
        )
