import requests

# Get city name from user
city = input("Enter city name: ")

# Geocoding API -> City to Latitude & Longitude
geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)

geo_data = geo_response.json()

# Extract latitude and longitude
lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]

# Weather Forecast API
weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max,temperature_2m_min&forecast_days=4"

weather_response = requests.get(weather_url)

weather_data = weather_response.json()

# Current temperature
temperature = weather_data["current_weather"]["temperature"]

print(f"\nCurrent temperature in {city} is {temperature}°C")

# Forecast data
dates = weather_data["daily"]["time"]

max_temps = weather_data["daily"]["temperature_2m_max"]

min_temps = weather_data["daily"]["temperature_2m_min"]

print("\n3-Day Forecast:")

for i in range(len(dates)):
    print(f"{dates[i]} - Max: {max_temps[i]}°C, Min: {min_temps[i]}°C")
