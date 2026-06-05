import requests

city = input("Enter city name: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)

geo_data = geo_response.json()

lat = geo_data["results"][0]["latitude"]

lon = geo_data["results"][0]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

temperature = weather_data["current_weather"]["temperature"]

print(f"Current temperature in {city} is {temperature}°C")