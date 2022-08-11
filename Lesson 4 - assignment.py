# 1
import requests
from selenium import webdriver
import names

response = requests.get("https://api.github.com/users/avielb/repos")
count = 0
assert len(response.json()) > 5

# 2

my_names = []
for i in range(3):
    if not 0 <= requests.get(f"https://api.agify.io/?name={names.get_first_name()}").json()["age"] <= 120:
        my_names.append(i)
assert len(my_names) == 0

# 3
unis = requests.get("http://universities.hipolabs.com/search?country=Israel")
assert len(unis.json()) > 5

# 4
my_driver = webdriver.Chrome()
my_driver.get("https://www.ycombinator.com")
assert my_driver.title == "Y Combinator"

# 5
my_driver2 = webdriver.Chrome()
my_driver2.get("https://hub.docker.com")
assert my_driver2.title == "Docker Hub Container Image Library | App Containerization"
