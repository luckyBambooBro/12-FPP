import json
import time
import pprint
import sys
from geopy.geocoders import Nominatim
from load_school_data import load_school_data
from .config import schools_data_SRC

def load_then_geocode_schools_data():
    schools_data = load_school_data()
    if not schools_data:
        print("Error: Could not load schools data")
        sys.exit(1)

    app_name = "My School Finder"
    geolocator = Nominatim(user_agent=app_name, timeout=10)
    longitude, latitude = "longitude", "latitude"
    name = "name"

    total_schools = len(schools_data)
    geocoded_count = sum(1 for school in schools_data if latitude in school)
    print(f"Starting geocoding process for {total_schools}")
    print(f"{geocoded_count}/{total_schools} schools already have coordinates. Resuming pre-geocoding...")

    for i, school in enumerate(schools_data):     
        if latitude not in school.keys() or longitude not in school.keys(): 
            try:   
                location = geolocator.geocode(school["address"], timeout=10)
                if location:
                    school[latitude], school[longitude] = location.latitude, location.longitude
                else:
                    print(f"Unable to determine geolocation for {school[name]}")
                time.sleep(1.1)
            except Exception as e:
                print(f"Geocoding: {i + 1}/{total_schools}")
                print(f"Error accessing Nominatim for {school[name]}: {e}")
                save_schools_data(schools_data)
    return schools_data

def pre_geocode_schools():
    pre_geocoded_schools_data = load_then_geocode_schools_data()
    pprint.pprint(pre_geocoded_schools_data)
    save_schools_data(pre_geocoded_schools_data)

def save_schools_data(pre_geocoded_schools_data):
    try:
        with open(schools_data_SRC, "w") as f:
            json.dump(pre_geocoded_schools_data, f, indent=4)
    except Exception as e:
        print(f"FATAL EXPORT ERROR: Could not write to {schools_data_SRC}.\n{e}")        

pre_geocode_schools()