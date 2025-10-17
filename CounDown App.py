from Helper import validation_user_type

import datetime


user_input = input("Enter your goal and a deadline separated by column\n")
input_list = user_input.split(":")

goal = input_list[0]
date_deadline = input_list[1]

deadline_date = datetime.datetime.strptime(date_deadline, "%d.%m.%Y")
today_date = datetime.datetime.today()
time_till = deadline_date - today_date

print(
    f"Please note that the time remaining for your goal to {goal} is {time_till.days} days"
)
