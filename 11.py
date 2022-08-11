import datetime
from time import sleep
import requests
response = requests.get("https://github.com")
if response.status_code == 200:
    print("Github is up and running")
print(datetime.datetime.now())
sleep(10)
print(datetime.datetime.now())
