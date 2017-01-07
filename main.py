# -*- coding: utf-8 -*-
import requests
import json


def convert_kel_cel(kel_value):
    return int(kel_value - 273.15)

city = raw_input("City name: ")
key = 'APP-KEY'
url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + key

# Call to the weather api server
response = requests.get(url)

# Extract the response content
content = response.content

# Convert Json into python dict
data = json.loads(content)

# Get the temp from the data dict
temp = data['main']['temp']

# Print the result
print "The weather in " + city + " is : " + str(convert_kel_cel(temp)) + '°'
