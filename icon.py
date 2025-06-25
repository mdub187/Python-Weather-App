import os
import sys
import pandas as pd
import requests
import PIL
from locale import D_FMT
from PIL import Image
import datetime
from datetime import datetime


icon_path = "./icons/"
current_time = datetime.now()
current_hour = current_time.hour
def get_day_night():
    # Get the current time

    def get_weather_icon(weather_description):
        """
        Maps weather descriptions to corresponding icon filenames.
        """
    weather_icon_map = {
        "clear sky": "wi-day-sunny.svg",
        "few clouds": "wi-day-sunny-overcast.svg",
        "scattered clouds": "wi-day-cloudy-high.svg",
        "shower rain": "wi-day-rain.svg",
        "rain": "wi-day-showers.svg",
        "thunderstorm": "wi-day-storm-showers.svg",
        "snow": "wi-day-snow.svg",
        "mist": "wi-day-sprinkle.svg"
        }
        # Add more mappings as needed



    def moon_sun():
        # Define day and night hours
        day = 6 <= current_hour < 18;
        night = bool(not day)

        if day == True:
            print(f"The current time is {current_time.strftime('%H:%M')}. It's daytime!")
        elif night == True:

            print(f"The current time is {current_time.strftime('%H:%M')}. It's nighttime!")
        else:
            print("idek what time it is")

    # Convert to lowercase for case-insensitive matching
    weather_code = weather_description.lower()

    # return weather_icon_map.get(weather_code)
    weather_icon_map.get(weather_code)

    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        weather_code = main_data["temp"]
        # Assuming temperature is in Kelvin, convert to Fahrenheit or Celsius as needed
        # Here, we'll just display the raw Kelvin temperature
        weather = weather_data["weather"][0]
        description = weather["description"]

        icon_filename = get_weather_icon(description)
        if icon_filename
            img = Image.open(icon_path)
            new_width = 75
            new_height = 75
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            resized_img.show() # or display it in a GUI
            # 2. Using an image widget in a GUI framework like Tkinter, PyQt, etc.
            # 3. If using HTML/CSS, you would set the `src` attribute of an `<img>` tag.
    for infile in sys.argv[1:]:
            try:
                with Image.open(infile) as im:
                    print(infile, im.format, f"{im.size}x{im.mode}")
            except OSError:
                pass
    return get_weather_icon
    return moon_sun
if __name__ == "__main__":
    print(icon_path)
    print("__main__")
    print(get_day_night)
