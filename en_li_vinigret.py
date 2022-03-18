#submitted by Keren Or Hadad 208025205
import datetime
import random


def en_li_vinigret(start_date: datetime, end_date: datetime):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    if random_date.weekday() == 0:   #monday is 0
        print("there is no vinigrate")
        return random_date
    else:
        return random_date

print(en_li_vinigret(datetime.date(2022, 3, 7), datetime.date(2022, 3, 8)))

"""
output:
there is no vinigrate
2022-03-07
"""
