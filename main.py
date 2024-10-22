# Завдання 1

from datetime import datetime

def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        delta = current_date - given_date
        return delta.days
    except ValueError:
        return "Неправильний формат дати. Використовуйте формат 'YYYY-MM-DD'."

# Завдання 2

import random

def get_numbers_ticket(min_value, max_value, quantity):
    if min_value < 1 or max_value > 1000 or quantity > (max_value - min_value + 1):
        return []

    numbers = random.sample(range(min_value, max_value + 1), quantity)
    return sorted(numbers)

# Завдання 3

import re

def normalize_phone(phone_number):
    phone_number = re.sub(r'\D', '', phone_number)

    if phone_number.startswith('380'):
        return '+{}'.format(phone_number)

    if phone_number.startswith('0'):
        return '+38{}'.format(phone_number)
    return '+38{}'.format(phone_number)

# Завдання 4

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= 7:
            if birthday_this_year.weekday() >= 5:
                next_monday = birthday_this_year + timedelta(days=(7 - birthday_this_year.weekday()))
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": next_monday.strftime("%Y.%m.%d")
                })
            else:
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                })
    return upcoming_birthdays
