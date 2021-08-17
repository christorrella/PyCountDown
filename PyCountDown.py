from datetime import datetime as dt
from os import system, name
import time
from dateutil.relativedelta import relativedelta

"""Strings that are used throughout the program, they live here for less messiness """

str_user_prompt = "Enter the date and time to count down until as 'mm/dd/yyyy hh:mm [AM/PM]':\n"
str_accepted_datetime_format = "%m/%d/%Y %I:%M %p"
str_formatting_error = "Format didn't match 'mm/dd/yyyy hh:mm [AM or PM]', try again"
str_countdown_msg = "Time remaining: "

class PyCountDown:

    def clear(self):
        """Useful for cleaning the screen up, found online"""

        if name == 'nt':
            system('cls')
        else:
            system('clear')

    def yes_or_no(self, question):
        """Asking for verification from user"""

        while True:
            reply = str(input(question+' (y/n): ')).lower().strip()
            if reply[0] == 'y':
                return True
            if reply[0] == 'n':
                return False

    def ask_user_for_time(self):
        """Ask user for the time they wish to count down until, return valid datetime object"""

        print(f"The current time is {dt.now()}")
        user_input = input(str_user_prompt)

        try:
            formatted = dt.strptime(user_input, str_accepted_datetime_format)
            if self.yes_or_no(f"You entered {formatted}, is that correct?"):
                return formatted
            else:
                return self.ask_user_for_time()

        except ValueError:
            print(str_formatting_error)
            return self.ask_user_for_time()

    def count_down_until(self, target):
        """Start countdown until the target datetime object"""

        done = False
        while not done:
            self.clear()

            # Using the dateutil relativedata function, this is useful for splitting time up
            diff = relativedelta(dt.now(), target)
            data = {
                        "years": -diff.years,
                        "months": -diff.months,
                        "days": -diff.days,
                        "hours": -diff.hours,
                        "minutes": -diff.minutes,
                        "seconds": -diff.seconds
                    }

            countdown_msg = str_countdown_msg

            # Good attempt at using list comprehension here
            countdown_msg += ", ".join([f"{data[key]} {key}" for key in data.keys() if data[key]])
            print(countdown_msg)
            time.sleep(0.1)



    def __init__(self):
        target = self.ask_user_for_time()
        self.count_down_until(target)

PyCountDown = PyCountDown()
