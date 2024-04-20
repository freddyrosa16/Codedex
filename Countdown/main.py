import datetime
from bday_messages import random_message

current_date = datetime.date.today()
next_birthday = datetime.date(2025, 1, 16)

days_away = next_birthday - current_date

if current_date == next_birthday:
    print(random_message)
else:
    print(f'My next birthday is {days_away} days away!')
