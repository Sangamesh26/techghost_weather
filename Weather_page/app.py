# -*- coding: utf-8 -*-

# Importing essential libraries
from flask import Flask, render_template, request
import requests
app = Flask(__name__)

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    #api_key = config.weather_api_key
    api_key = "5db93eca8e26e903b16716756e9b2d6b"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    if request.method == 'POST':
        city_name = request.form['city']
        if weather_fetch(city_name) != None:
            temperature, humidity = weather_fetch(city_name)
            return render_template('index.html', weather="The temperature and Humidity of the {} is {} celsius and {}%" .format(city_name,temperature, humidity))
    
if __name__ == '__main__':
	app.run(debug=True)