from thefuzz import fuzz, process
import pandas as pd
from PIL import Image
import os

# Example: get_weather_icon and description would be defined elsewhere
# For demonstration, let's use a placeholder
def get_weather_icon(description):
    # Dummy implementation for demonstration
    icon_map = {
        "clear": "sun.png",
        "rain": "rain.png",
        "cloudy": "cloud.png"
    }
    return icon_map.get(description, "default.png")

description = "clear"  # Example description

# Example icon dictionary and data
icon_dict = {
    "sun.png": "Sunny",
    "rain.png": "Rainy",
    "cloud.png": "Cloudy"
}
dict_two = {
    "icon_file": ["sun.png", "rain.png", "cloud.png"],
    "weather_type": ["Sunny", "Rainy", "Cloudy"]
}

icon_filename = get_weather_icon(description)
icon_path = f"./icons/{icon_filename}"

# Load the icon dictionary and exported data into DataFrames
existing_data = pd.DataFrame(list(icon_dict.items()), columns=["icon_file", "description"])
exported_data = pd.DataFrame(dict_two)

# Merge the DataFrames on the icon_file column
merged_data = pd.merge(existing_data, exported_data, on="icon_file", how="left")

# Display the icon using Pillow (PIL)
if os.path.exists(icon_path):
    img = Image.open(icon_path)
    img.show()
else:
    print(f"Icon file {icon_path} not found.")

# Fuzzy matching example
api_data = ["Appple", "Grapes", "Banna"]  # Example API data with potential misspellings
local_list = ["Apple", "Orange", "Banana", "Grape"] # Example local list

matched_and_renamed_data = []

for api_item in api_data:
    match = process.extractOne(api_item, local_list, scorer=fuzz.ratio) # Use a suitable fuzzy matching ratio
    if match[1] >= 80:  # Set a similarity threshold (e.g., 80)
        matched_and_renamed_data.append({"original_name": api_item, "matched_name": match[0]}) # Store original and matched names
    else:
        matched_and_renamed_data.append({"original_name": api_item, "matched_name": "No match found"}) # Handle cases with no match

print(matched_and_renamed_data)
