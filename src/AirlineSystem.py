import random
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
class Flight:
    def __init__(self, flight_code, departure, destination, schedule):
        self.__flight_code = flight_code
        self.__departure = departure
        self.__destination = destination
        self.__schedule = schedule
        self.__book_list = []
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
    def add_book_list(self,ticket):
        self.__book_list.append(ticket)
    def calculate_available_seats(self):
        for ticket in self.__book_list:
            if ticket.get_status() == "confirmed" and not ticket.get_check():
                self.__available_seats-= ticket.get_no_of_seats()
            elif ticket.get_status() == "cancelled" and ticket.get_check():
                self.__available_seats+= ticket.get_no_of_seats()
        return self.__available_seats
    def __str__(self):
        return ("Flight Code: " + self.__flight_code
        + "\nDeparture: " + self.__departure
        + "\nDestination: " + self.__destination
        + "\n"+str(self.__schedule)
        + "\nAvailable Seats: " + str(self.__available_seats))
class FlightSchedule:
    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time
    def get_date(self):
        return self.__date
    def get_start_time(self):
        return self.__start_time
    def get_end_time(self):
        return self.__end_time
    def __str__(self):
        return ("Date: " + self.__date+ "\nStart Time: " + self.__start_time + "\nEnd Time: " + self.__end_time)


class AirlineSystem:
    def __init__(self):
        self.__booking_list = []
        self.__flight_list = []
    def add_flight(self, flight_code, departure, destination, schedule):
        found = False
        for flight in self.__flight_list:
            if flight.get_flight_code() == flight_code:
                found = True
                print("FLight Already Exist!")
                break
        if not found:       
            self.__flight_list.append(Flight( flight_code, departure, destination, schedule))
            print("Add flight successfully!")
    def del_flight(self,flight_code):
        found = False
        for flight in self.__flight_list:
            if flight.get_flight_code() == flight_code:
                found = True
                self.__flight_list.remove(flight)
                print("Remove flight successfully!")
                break
        if not found:
            print("Flight not found!")
    def add_booking(self):
        choice = input("Enter Your flight code: ")
        found = False
        for flight in self.__flight_list:
            if flight.get_flight_code() == choice:
                found = True
                name = input("Enter your name: ")
                seat_class = input("Enter your seat class: ")
                no_of_seats = int(input("Enter number of seats you want to book: "))
                if no_of_seats <= flight.get_available_seats():
                    ticket = Booking(name,seat_class,no_of_seats)
                    ticket.set_booking_id(flight.get_flight_code()+str(ticket.get_no_of_seats())+str(random.randint(1,1000)))
                    self.__booking_list.append(ticket)
                    flight.add_book_list(ticket)
                    flight.calculate_available_seats()
                    ticket.set_check()
                    print("Book successfully! Check your booking id at 'View booking list'")
                else:
                    print("Flight code",flight.get_flight_code(),"only has",flight.get_available_seats(),"seat(s) left, Please try again!")
                break
        if not found:
            print("Flight not found!")
    def cancel_booking(self):
        code = input("Enter your booking id: ")
        found = False
        for ticket in self.__booking_list:
            if ticket.get_booking_id() == code:
                found = True
                ticket.cancel_booking()
                for flight in self.__flight_list:
                    flight.calculate_available_seats()
                ticket.set_check()
                print("Cancel successfully!")
                break
        if not found:
            print("booking id not found, Try again!")
    def view_bookings(self):
        if len(self.__booking_list) != 0:
            for ticket in self.__booking_list:
                print(ticket)
        else:
            print("You haven't book anything yet!")
    def view_flights(self):
        if len(self.__flight_list) != 0:
            for flight in self.__flight_list:
                print(flight)
                print()
            print("We have",len(self.__flight_list),"flights available at the moment!")
        else:
            print("No Flight at the moment")
    def run(self):
        print("WELCOME TO FLIGHT TICKET BOOKING MENU!")
        print(" 1.View flights information	        5.View booking list\n"
              " 2.Add new flight			6.Save\n"
              " 3.Delete flight			7.Load\n"
              " 4.Booking/Cancel booking		8.Exit\n"
              )
        while True:
            try:
                action = int(input())
                if action == 8:
                    print("THANK YOU FOR USING OUR PROGRAM! GOOD BYE")
                    break
                elif action == 1:
                    self.view_flights()
                elif action == 2:
                    flight_code = input("Enter flight code: ")
                    departure = input("Enter the departure location: ")
                    destination = input("Enter the destination: ")
                    date = input("Enter date of flight: ")
                    start_time = input("Enter start time: ")
                    end_time = input("Enter estimate end time: ")
                    self.add_flight(flight_code, departure, destination, FlightSchedule(date, start_time, end_time))
                elif action == 3:
                    flight_code = input("Enter your flight code: ")
                    self.del_flight(flight_code)
                elif action == 4:
                    choice = int(input("Press 1 to Booking or 2 to Cancel booking: "))
                    if choice == 1:
                        self.add_booking()
                    elif choice == 2:
                        self.cancel_booking()
                    else:
                        print("Action not available!")
                elif action == 5:
                    self.view_bookings()
                elif action == 6:
                    pass
                elif action == 7:
                    pass
                else:
                    print(" 1.View flights information	        5.View booking list\n"
              " 2.Add new flight			6.Save\n"
              " 3.Delete flight			7.Load\n"
              " 4.Booking/Cancel booking		8.Exit\n"
              )
            except:
                print("Error! Try again")
khoa = AirlineSystem()
khoa.run()