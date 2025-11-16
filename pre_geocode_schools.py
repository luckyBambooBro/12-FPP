import json
import time
import pprint
import sys
from geopy.geocoders import Nominatim
from load_school_data import load_school_data, schools_data_SRC

def load_non_geocoded_schools_data():
    schools_data = load_school_data()
    if not schools_data:
        print("Error: Could not load schools data")
        sys.exit(1)

    app_name = "My School Finder"
    geolocator = Nominatim(user_agent=app_name, timeout=10)
    longitude, latitude = "longitude", "latitude"

    for school in schools_data:     
        if latitude not in school.keys() or longitude not in school.keys(): 
            try:   
                location = geolocator.geocode(school["address"])
                if not location:
                    print(f"Unable to determine geolocation for {school["name"]}")
                school[latitude], school[longitude] = location.latitude, location.longitude
                time.sleep(1.1)
            except Exception as e:
                print(f"Error accessing Nominatim: {e}")
                save_schools_data(schools_data)

    pprint.pprint(schools_data)
    return schools_data

def pre_geocode_schools():
    pre_geocoded_schools_data = load_non_geocoded_schools_data()
    save_schools_data(pre_geocoded_schools_data)

def save_schools_data(pre_geocoded_schools_data):
    with open(schools_data_SRC, "w") as f:
        json.dump(pre_geocoded_schools_data)
        #TODO save the data

pre_geocode_schools()