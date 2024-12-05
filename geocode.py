import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep

# Load your alumni data
df = pd.read_excel("/Users/shriatluri/DATAMINE/dataminealumniscraper/Formatted_Alumni.xlsx")  # Replace with your file
unique_locations = df['home_town'].dropna().unique()

# Initialize geolocator
geolocator = Nominatim(user_agent="streamlit-pre-geocoder")
geocoded_data = []

# Geocode each location
for location in unique_locations:
    try:
        loc = geolocator.geocode(location)
        if loc:
            geocoded_data.append({'Location': location, 'Latitude': loc.latitude, 'Longitude': loc.longitude})
        else:
            geocoded_data.append({'Location': location, 'Latitude': None, 'Longitude': None})
    except:
        geocoded_data.append({'Location': location, 'Latitude': None, 'Longitude': None})
    sleep(1)  # Add a delay to respect rate limits

# Save the geocoded data to a CSV
geocoded_df = pd.DataFrame(geocoded_data)
geocoded_df.to_csv("geocoded_locations.csv", index=False)
print("Geocoding complete and saved to geocoded_locations.csv")
