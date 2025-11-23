import json
import time
import pprint
import sys
from geopy.geocoders import Nominatim
from load_schools_data import load_schools_data
from config import SCHOOLS_DATA_SRC, NOMINATIM_DELAY, NOMINATIM_TIMEOUT


COORDINATE_KEY = "school_coordinates"
NAME_KEY = "name"
APP_NAME = "My School Finder"


def load_then_geocode_schools_data():
    """
    Loads a list of dictionaries containing school data from global file path
    for each school dictionary in list, will use Nominatum API to add latitude and longitude 
    to the dictionary 
    This function will run the geocoding loop and save progress after each successful request
    
    return: updated list of schools
    """
    schools_data = load_schools_data(SCHOOLS_DATA_SRC)
    if not schools_data:
        print("Error: Could not load schools data")
        sys.exit(1)

    geolocator = Nominatim(user_agent=APP_NAME, timeout=NOMINATIM_TIMEOUT)
    longitude, latitude = "longitude", "latitude"
    name = NAME_KEY

    total_schools = len(schools_data)
    geocoded_count = sum(1 for school in schools_data if COORDINATE_KEY in school)
    print(f"Starting geocoding process for {total_schools} schools")
    print(f"{geocoded_count}/{total_schools} schools already have coordinates. Resuming pre-geocoding...")

    for i, school in enumerate(schools_data):     
        if COORDINATE_KEY not in school.keys(): 
            try:   
                location = geolocator.geocode(school["address"], timeout=NOMINATIM_TIMEOUT)
                if location:
                    school[COORDINATE_KEY] = (location.latitude, location.longitude)
                    save_schools_data(schools_data)
                else:
                    print(f"Unable to determine geolocation for {school[name]}")
                time.sleep(NOMINATIM_DELAY)
            except Exception as e:
                print(f"{i + 1}/{total_schools} geocoded")
                print(f"Error accessing Nominatim for {school[name]}: {e}")
                save_schools_data(schools_data)
                time.sleep(NOMINATIM_DELAY)
                print("Progress saved. Exiting script due to API error.")
                sys.exit(1)

    print("\n--- Geocoding process finished successfully! ---")
    return schools_data

def pre_geocode_schools():
    """
    Main function to run the geocoding script.
    """
    pre_geocoded_schools_data = load_then_geocode_schools_data()
    pprint.pprint(pre_geocoded_schools_data) #TODO remove
    save_schools_data(pre_geocoded_schools_data)

def save_schools_data(pre_geocoded_schools_data):
    """
    Helper function to save the list of dictionaries back to the original JSON file.
    This overwrites the file with the most current data.
    """
    try:
        with open(SCHOOLS_DATA_SRC, "w") as f:
            json.dump(pre_geocoded_schools_data, f, indent=4)
    except Exception as e:
        print(f"FATAL EXPORT ERROR: Could not write to {SCHOOLS_DATA_SRC}.\n{e}")        


if __name__ == "__main__":
    pre_geocode_schools()