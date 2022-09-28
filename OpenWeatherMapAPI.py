# Importing libraries
import requests
import json
 
# Enter your OpenWeatherMap API key here
# DO NOT push it to a public repository
API_Key = "Your_API_Key"

# Provide a valid city name
city_name = input("Enter city name: ")

# Constructing the API URL path
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}"

# Making a get request to the API
response = requests.get(url)

# Converting JSON reponse to a dictionary
res = response.json()

# Uncomment the next line to see all 
# data that are fetched from the API
# print(res)
 
# Checking if the city is found
# If the value of "cod" is not 404,
# that means the city is found
if res["cod"] != "404":
    data = res["main"]

    # Storing the live temperature data
    live_temperature = data["temp"]
    # Storing the live pressure data
    live_pressure = data["pressure"]
    desc = res["weather"]
     # Storing the weather description
    weather_description = desc[0]["description"]

    print("Temperature (in Kelvin scale): " + str(live_temperature))
    print("Pressure: " + str(live_pressure))
    print("Description: " + str(weather_description))
 
else:
    # If the city is not found,
    # this block of code will be executed
    print("Please enter a valid city name")