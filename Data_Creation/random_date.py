import datetime
import random

# A function given seed will generate a random date between
# start_date and end_date
def random_date(am):
    random.seed(am)

    start_date = datetime.date(2021, 10, 1)
    end_date = datetime.date(2021, 11, 15)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
##    print(random_date)
    return(random_date)


