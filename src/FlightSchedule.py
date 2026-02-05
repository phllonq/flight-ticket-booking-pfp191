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

        return (
            'Date: ' + self.__date + '\n'
            'Start Time: ' + self.__start_time + '\n'
            'End Time: ' + self.__end_time
        )
