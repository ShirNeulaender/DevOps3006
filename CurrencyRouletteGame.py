import requests
import random
from Live import set_difficulty

difficulty = set_difficulty()

generated_number = random.randint(1, 100)


def get_rate():
    exchange_rate_site = f"https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount={generated_number}"

    payload = {}
    headers = {
        "apikey": "t44ElVQBlOFs4LybEJND43lLNkOIXjEd"
    }

    response = requests.request("GET", exchange_rate_site, headers=headers, data=payload)
    return response.json()["info"]["rate"]


value_t = get_rate() * generated_number
value_t = round(value_t, 2)


def get_money_interval():
    minimum = str(value_t - (5 - difficulty))
    maximum = str(value_t + (5 - difficulty))
    return minimum, maximum


def get_guess_from_user():
    user_input = input(f"What is the value of {generated_number}$ in ILS? ")
    return user_input


def play():
    minimum, maximum = get_money_interval()
    user_input = get_guess_from_user()
    print(f"The correct value is {value_t}₪,you needed to enter a number between {minimum} and {maximum} in order to win")
    mini = user_input > minimum
    maxi = user_input < maximum
    winning_status = (mini and maxi)
    print(winning_status)
    return winning_status