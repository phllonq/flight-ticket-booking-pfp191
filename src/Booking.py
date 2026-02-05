class Booking:
    def __init__(self, name, seat_class, no_of_seats):
        self.__name = name
        self.__seat_class = seat_class
        self.__no_of_seats = no_of_seats
        self.__booking_id = ""
        self.__status = "confirmed"
        self.__check = False
    def get_check(self):
        return self.__check
    def set_check(self):
        if self.__check == False:
            self.__check = True
        else:
            self.__check = False
        return self.__check
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_seat_class(self):
        return self.__seat_class
    def set_seat_class(self, seat_class):
        self.__seat_class = seat_class
    def get_no_of_seats(self):
        return int(self.__no_of_seats)
    def set_no_of_seats(self, no_of_seats):
        self.__no_of_seats = no_of_seats
    def get_booking_id(self):
        return self.__booking_id
    def set_booking_id(self, booking_id):
        self.__booking_id = booking_id
    def get_status(self):
        return self.__status
    def cancel_booking(self):
        self.__status = "cancelled"
    def __str__(self):
        return ("Name: " + self.__name
        + "\nSeat Class: " + self.__seat_class
        + "\nNo. of Seats: "
        + str(self.__no_of_seats)
        + "\nBooking ID: " + self.__booking_id
        + "\nStatus: " + self.__status)