import json
import random
from Booking import Booking
from Flight import Flight
from FlightSchedule import FlightSchedule


class AirlineSystem:

    def __init__(self):
        self.__booking_list = []
        self.__flight_list = []

    # ================= LOAD DATA =================
    def load_data(self):
        try:
            with open("airline_data.json", "r") as f:
                data = json.load(f)

            self.__flight_list = []

            for f_data in data.get("flights", []):
                schedule = FlightSchedule(
                    f_data["date"],
                    f_data["start_time"],
                    f_data["end_time"],
                )

                flight = Flight(
                    f_data["flight_code"],
                    f_data["departure"],
                    f_data["destination"],
                    schedule,
                )

                self.__flight_list.append(flight)

            print("Load data successfully!")

        except FileNotFoundError:
            print("Data file not found.")
        except json.JSONDecodeError:
            print("Invalid data format.")

    # ================= SAVE DATA =================
    def save_data(self):
        data = {"flights": []}

        for flight in self.__flight_list:
            schedule = flight.get_schedule()

            data["flights"].append(
                {
                    "flight_code": flight.get_flight_code(),
                    "departure": flight.get_departure(),
                    "destination": flight.get_destination(),
                    "date": schedule.get_date(),
                    "start_time": schedule.get_start_time(),
                    "end_time": schedule.get_end_time(),
                }
            )

        with open("airline_data.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Save data successfully!")

    # ================= FLIGHT =================
    def add_flight(self, flight_code, departure, destination, schedule):
        for flight in self.__flight_list:
            if flight.get_flight_code() == flight_code:
                print("Flight already exists!")
                return

        new_flight = Flight(flight_code, departure, destination, schedule)
        self.__flight_list.append(new_flight)
        print("Add flight successfully!")

    def del_flight(self, flight_code):
        for flight in self.__flight_list:
            if flight.get_flight_code() == flight_code:
                self.__flight_list.remove(flight)
                print("Remove flight successfully!")
                return

        print("Flight not found!")

    # ================= BOOKING =================
    def add_booking(self):
        code = input("Enter your flight code: ")

        for flight in self.__flight_list:
            if flight.get_flight_code() == code:

                name = input("Enter your name: ")
                seat_class = input("Enter your seat class: ")
                no_of_seats = int(input("Enter number of seats: "))

                if no_of_seats <= flight.get_available_seats():

                    ticket = Booking(name, seat_class, no_of_seats)

                    booking_id = code + str(random.randint(1000, 9999))
                    ticket.set_booking_id(booking_id)

                    self.__booking_list.append(ticket)

                    flight.add_booking(ticket)

                    print("Book successfully!")
                    print("Your booking ID:", booking_id)

                else:
                    print(
                        "Only",
                        flight.get_available_seats(),
                        "seat(s) left!",
                    )
                return

        print("Flight not found!")

    def cancel_booking(self):
        booking_id = input("Enter your booking ID: ")

        for ticket in self.__booking_list:
            if ticket.get_booking_id() == booking_id:
                ticket.cancel_booking()
                print("Cancel successfully!")
                return

        print("Booking ID not found!")

    # ================= VIEW =================
    def view_flights(self):
        if not self.__flight_list:
            print("No flights available.")
            return

        for flight in self.__flight_list:
            print(flight)
            print()

        print("Total flights:", len(self.__flight_list))

    def view_bookings(self):
        if not self.__booking_list:
            print("No bookings yet.")
            return

        for ticket in self.__booking_list:
            print(ticket)
            print()

    # ================= MENU =================
    def run(self):
        print("WELCOME TO FLIGHT TICKET BOOKING MENU!")

        while True:
            print(
                "\n1. View flights"
                "\n2. Add new flight"
                "\n3. Delete flight"
                "\n4. Booking / Cancel"
                "\n5. View bookings"
                "\n6. Save"
                "\n7. Load"
                "\n8. Exit"
            )

            try:
                action = int(input("Choose: "))

                if action == 1:
                    self.view_flights()

                elif action == 2:
                    flight_code = input("Enter flight code: ")
                    departure = input("Enter departure: ")
                    destination = input("Enter destination: ")
                    date = input("Enter date (YYYY-MM-DD): ")
                    start = input("Enter start time: ")
                    end = input("Enter end time: ")

                    schedule = FlightSchedule(date, start, end)
                    self.add_flight(flight_code, departure, destination, schedule)

                elif action == 3:
                    code = input("Enter flight code: ")
                    self.del_flight(code)

                elif action == 4:
                    choice = int(input("1.Book  2.Cancel: "))
                    if choice == 1:
                        self.add_booking()
                    elif choice == 2:
                        self.cancel_booking()

                elif action == 5:
                    self.view_bookings()

                elif action == 6:
                    self.save_data()

                elif action == 7:
                    self.load_data()

                elif action == 8:
                    print("GOOD BYE")
                    break

                else:
                    print("Invalid choice!")

            except Exception as e:
                print("Error:", e)
