import requests
import time

url = 'http://api.open-notify.org/iss-now.json'

while True:
    response = requests.get(url)
    data = response.json()
    latitude = data['iss_position']['latitude']
    longitude = data['iss_position']['longitude']
    print(latitude, longitude)
    with open('statistics.csv', 'w') as file:
        file.write(f"{latitude};{longitude}\n")
    time.sleep(5)