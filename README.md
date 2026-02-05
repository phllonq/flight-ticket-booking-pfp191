Flight Ticket Booking Management System

Course: PFP191 

Class: AI2003

Lecturer: Trần Công Mua

Group: 6

1. Project Overview

This project implements a Flight Ticket Booking Management System using Python.
The system is a console-based application that allows administrators to manage flights and schedules, and allows users to search flights, book tickets, and cancel bookings.

The project focuses on applying fundamental programming concepts, including:

Object-Oriented Programming (OOP)

Basic data structures

File input/output with JSON

Exception handling

Menu-driven program control

2. Team Members & Responsibilities
Trần Phi Long - SE201868 (60%)

Design overall system architecture

Implement Flight and FlightSchedule classes

Implement flight and schedule management functions

Design data structures and JSON file format

Handle file input/output operations

Write Requirement Analysis & OOP Design sections

Nguyễn Ngọc Đăng Khoa - SE210374 (40%)

Implement Booking class and seat management logic

Implement booking, cancellation, and seat update functions

Design and implement console-based menu system

Perform system testing and validation

Write Algorithm Design, Testing, and Experimental Results sections

3. System Features
Flight Management

Add new flights

Update flight information

Delete flights (if not associated with any schedule)

Flight Schedule Management

Add flight schedules

Update flight schedules

Search schedules by flight code

Ticket Booking Management

Book tickets with seat availability checking

Cancel bookings and restore seats

View booking details

Seat Management

Check available seats

Update seats after booking

Restore seats after cancellation

File Management

Save system data to JSON file

Load system data when the program starts

Handle file errors and invalid formats

4. Project Structure
flight-ticket-booking-pfp191/
│
├── README.md
├── airline_data.json
└── src/
    ├── __init__.py
    ├── Flight.py
    ├── FlightSchedule.py
    ├── Booking.py
    ├── AirlineSystem.py
    └── Main.py

File Description

Flight.py: Defines the Flight class

FlightSchedule.py: Manages flight schedules and seat availability

Booking.py: Represents booking information

AirlineSystem.py: Core system logic and data management

Main.py: Console-based menu and program entry point

airline_data.json: Stores persistent system data

5. Technologies Used

Python 3.x

JSON for data storage

Git & GitHub for version control

6. How to Run the Program

Clone the repository:

git clone https://github.com/phllonq/flight-ticket-booking-pfp191.git


Navigate to the project directory:

cd flight-ticket-booking-pfp191


Run the program:

python src/Main.py

7. Testing

The system has been tested with the following scenarios:

Adding valid flights and schedules

Preventing duplicate flight codes

Booking tickets with sufficient and insufficient seats

Canceling bookings and restoring seats

Handling file not found and invalid file formats

8. Notes

This project is developed for academic purposes only.

The system uses a console-based interface and does not include a GUI.

Data persistence is handled via a JSON file.
