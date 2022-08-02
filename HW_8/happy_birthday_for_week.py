from datetime import datetime, timedelta


# main function
def get_birthdays_per_week(users):
    greetings = {}
    days_in_greeting_week = greeting_week()
    for user in users:
        for greeting_day in days_in_greeting_week:
            if user['birthday'].month == greeting_day.month and user['birthday'].day == greeting_day.day:
                greeting_day = check_if_birthday_on_weekend(greeting_day)
                try:
                    greetings[greeting_day.strftime("%A")].append(user['name'])
                except KeyError:
                    greetings[greeting_day.strftime("%A")] = [user['name']]

    for key, values in greetings.items():
        print(f'{key}: {", ".join(values)}')


# support function
def greeting_week():
    today = datetime.now()
    days_in_greeting_week = [(today + timedelta(days=x)).date() for x in range(7)]
    return days_in_greeting_week


# support function
def check_if_birthday_on_weekend(day):
    if day.strftime("%A") == "Sunday":
        return day + timedelta(days=1)
    elif day.strftime("%A") == "Saturday":
        return day + timedelta(days=2)
    else:
        return day


# Data for testing
users = [
    {'name': 'Karl',
     'birthday': datetime(year=2012, month=8, day=7)},
    {'name': 'Sara',
     'birthday': datetime(year=1985, month=8, day=4)},
    {'name': 'Alex',
     'birthday': datetime(year=2001, month=8, day=4)},
    {'name': 'Den',
     'birthday': datetime(year=1991, month=8, day=6)},
    {'name': 'Max',
     'birthday': datetime(year=2012, month=9, day=3)},
    {'name': 'Ann',
     'birthday': datetime(year=1981, month=8, day=6)},
]

get_birthdays_per_week(users)
