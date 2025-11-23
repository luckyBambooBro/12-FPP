import time
import inquirer
from geopy.geocoders import Nominatim
from config import NOMINATIM_DELAY, NOMINATIM_TIMEOUT

YES = "Yes"
NO = "No"
MIN_ADDRESS_LENGTH = 3
app_name = "My School Finder"

def seek_user_address():
    #returns (latitude, longitude) if user provides address 
    #returns None if not
    geolocator = query_address_permission() # if user agrees obtains geolocator from Nominatum in order to obtain address
    if geolocator:
        user_address_coordinates = obtain_user_address(geolocator)
        return user_address_coordinates #can still be None if user changes mind after failed address attempt
    else:
        return

def obtain_user_address(geolocator):
    #returns latitude,longitude or None
    location = None
    while not location:
        address = input("Please enter your address:\n>")
        #TODO for some reason when i tested this before
            #and typed a random string like "aseftegsga" the terminal would sit still and do nothing as if
            #it was waiting for a response. this would go on forever until i command C. needs thorough testing
        # CRITICAL FIX: Input validation added back
        if not address.strip() or len(address.strip()) < MIN_ADDRESS_LENGTH:
            print("Please enter a valid address.")
            continue
        try:
            location = geolocator.geocode(address, timeout=NOMINATIM_TIMEOUT)
            if location is None:
                print(f"The geocoding service could not find that address. Please check your spelling or use a more specific address")
                if not confirm_retry_or_exit():
                    return
            time.sleep(NOMINATIM_DELAY)
        except Exception as e:
            print(f"Network timeout/server error. Please try again")
            time.sleep(NOMINATIM_DELAY)
            if not confirm_retry_or_exit():
                return
    user_coordinates = (location.latitude, location.longitude)
    return user_coordinates

def query_address_permission():
    #Ask the user if they want to provide their address. #
    #returns geolocator if yes
    #returns None if no
    question = [inquirer.List(
        "query_input_address", 
        message="Would you like to provide an address to show nearby schools in that area?", 
        choices=[YES, NO], 
        default=YES
        )
    ]
    answer = inquirer.prompt(question)

    if YES in answer["query_input_address"]:
        geolocator = Nominatim(user_agent=app_name, timeout=NOMINATIM_TIMEOUT)
        return geolocator
    elif NO in answer["query_input_address"]:
        return
    
def confirm_retry_or_exit():
    question = [inquirer.List(
    "query continue", 
    message="Do you want to try entering a new address?", 
    choices=[YES, NO], 
    default=YES
    )
    ]
    answer = inquirer.prompt(question)
    return answer and answer.get("query continue") == YES

#TODO get rid of this if using as a utility script
if __name__ == "__main__":
    seek_user_address()

