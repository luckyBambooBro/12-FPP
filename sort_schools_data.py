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
        return user_address_coordinates #can still be None if user changes mind after failed address attempt
    else:
        return

def obtain_user_address(geolocator):
    location = None
    while not location:
        try:
            address = input("Please enter your address:\n>") #TODO for some reason when i tested this before
            #and typed a random string like "aseftegsga" the terminal would sit still and do nothing as if
            #it was waiting for a response. this would go on forever until i command C. needs thorough testing
            location = geolocator.geocode(address, timeout=NOMINATIM_TIMEOUT)
            if location is None:
                print(f"The geocoding service could not find that address. Please check your spelling or use a more specific address")
                continue_permission = query_address_permission
                if not continue_permission:
                    return
        except Exception as e:
            print(f"Network timeout/server error. Please try again")
            time.sleep(1.1)
    address_latitude, address_longitude = location.latitude, location.longitude
    return (address_latitude, address_longitude)

def query_address_permission():
    #Ask the user if they want to provide their address. returns geolocator if yes
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

