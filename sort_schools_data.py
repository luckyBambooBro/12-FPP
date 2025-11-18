import time
import inquirer
from geopy.geocoders import Nominatim
from config import NOMINATIM_TIMEOUT

YES = "Yes"
NO = "No"

def sort_schools_data(filtered_schools):
    geolocator = query_address_permission()
    if geolocator:
        user_address_coordinates = obtain_user_address(geolocator)
        print(user_address_coordinates)
    else:
        pass

def obtain_user_address(geolocator):
    address = input("Please enter your address:\n>")
    location = None
    while not location:
        try:
            location = geolocator.geocode(address, timeout=NOMINATIM_TIMEOUT)
        except Exception as e:
            print(f"Error accessing Nominatim to verify address. Please try again")
            time.sleep(1.1)
    address_latitude, address_longitude = location.latitude, location.longitude
    return (address_latitude, address_longitude)

def query_address_permission():
    question = [inquirer.List(
        "query_input_address", 
        message="Would you like to provide an address to show nearby schools in that area?", 
        choices=[YES, NO], 
        default=YES
        )
    ]
    answer = inquirer.prompt(question)

    if YES in answer["query_input_address"]:
        app_name = "My School Finder"
        geolocator = Nominatim(user_agent=app_name, timeout=NOMINATIM_TIMEOUT)
        return geolocator
    elif NO in answer["query_input_address"]:
        return

#TODO get rid of this if using as a utility script
if __name__ == "__main__":
    sort_schools_data([])

