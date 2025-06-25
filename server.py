from flask import Flask, render_template, request
from waitress import serve
from bs4 import BeautifulSoup

# Import the icon dictionary generator function and create the icon_dict
from static.icons.icon_dict import icons
icon_dict = icons()

# Import the weather function
from weather import get_current_weather

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city or not city.strip():
        city = "Denver"

    # Call the weather function which returns weather data and an icon filename
    weather_response, icon_filename_from_api = get_current_weather(city)

    # Check if the API returned a successful response
    if weather_response.get('cod') != 200:
        return render_template('city-not-found.html')

    # Use the icon code from the weather data to choose the icon filename
    weather_icon_code = weather_response["weather"][0]["icon"]
    # If the weather icon code isn't in our dictionary, fallback to a default icon
    icon_file = f"{icon_dict.get(weather_icon_code)}.svg"

    # Optionally, if you wish to resize images in your HTML using BeautifulSoup,
    # you could add a function here. However, it's generally more efficient
    # to handle image sizing via CSS rather than modifying the HTML file.

    return render_template(
        "weather.html",
        title=weather_response["name"],
        status=weather_response["weather"][0]["description"].capitalize(),
        temp=f"{weather_response['main']['temp']:.1f}",
        feels_like=f"{weather_response['main']['feels_like']:.1f}",
        weather_icon=icon_file
    )

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
