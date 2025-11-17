import json
import time
import pprint
import sys
from geopy.geocoders import Nominatim
from load_schools_data import load_schools_data
from config import SCHOOLS_DATA_SRC, NOMINATIM_DELAY, NOMINATIM_TIMEOUT

def load_then_geocode_schools_data():
    schools_data = load_schools_data()
    if not schools_data:
        print("Error: Could not load schools data")
        sys.exit(1)

    app_name = "My School Finder"
    geolocator = Nominatim(user_agent=app_name, timeout=NOMINATIM_TIMEOUT)
    longitude, latitude = "longitude", "latitude"
    name = "name"

    total_schools = len(schools_data)
    geocoded_count = sum(1 for school in schools_data if latitude in school)
    print(f"Starting geocoding process for {total_schools} schools")
    print(f"{geocoded_count}/{total_schools} schools already have coordinates. Resuming pre-geocoding...")

    for i, school in enumerate(schools_data):     
        if latitude not in school.keys() or longitude not in school.keys(): 
            try:   
                location = geolocator.geocode(school["address"], timeout=NOMINATIM_TIMEOUT)
                if location:
                    school[latitude], school[longitude] = location.latitude, location.longitude
                else:
                    print(f"Unable to determine geolocation for {school[name]}")
                time.sleep(NOMINATIM_DELAY)
            except Exception as e:
                print(f"{i + 1}/{total_schools} geocoded")
                print(f"Error accessing Nominatim for {school[name]}: {e}")
                save_schools_data(schools_data)
                print("Progress saved. Exiting script due to API error.")
                sys.exit(1)

    return schools_data

def pre_geocode_schools():
    pre_geocoded_schools_data = load_then_geocode_schools_data()
    pprint.pprint(pre_geocoded_schools_data)
    save_schools_data(pre_geocoded_schools_data)

def save_schools_data(pre_geocoded_schools_data):
    try:
        with open(SCHOOLS_DATA_SRC, "w") as f:
            json.dump(pre_geocoded_schools_data, f, indent=4)
    except Exception as e:
        print(f"FATAL EXPORT ERROR: Could not write to {SCHOOLS_DATA_SRC}.\n{e}")        


if __name__ == "__main__":
    pre_geocode_schools()