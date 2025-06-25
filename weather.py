from dotenv import load_dotenv
import requests
import os

load_dotenv()

def get_current_weather(city="Denver"):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY not set in environment.")

    request_url = f"http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial"
    response = requests.get(request_url)
    weather_data = response.json()

    # Determine icon filename if available
    if 'weather' in weather_data and isinstance(weather_data['weather'], list) and weather_data['weather']:
        weather_icon = weather_data['weather'][0].get('icon', 'default_icon')
    else:
        weather_icon = 'default_icon'
    icon_filename = f"{weather_icon}.svg"

    return weather_data, icon_filename

if __name__ == "__main__":
    city = input("Enter a city name (default is Denver): ").strip() or "Denver"
    try:
        weather_data, icon_filename = get_current_weather(city)
        print("Weather Data:", weather_data)
        print("Icon Filename:", icon_filename)
    except Exception as e:
        print("Error:", e)
