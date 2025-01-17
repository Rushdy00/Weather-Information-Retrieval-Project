import requests

API_KEY = "2627447e739ad1d7aba45a7a11fa6ea9"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code ==200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"])
    print("weather:",weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")