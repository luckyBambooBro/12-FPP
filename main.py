import sys
from filters import obtain_filter_choices, obtain_filtered_schools
from load_schools_data import load_schools_data
from seek_user_address import seek_user_address
from sort_schools_data import sort_schools_data
from config import SCHOOLS_DATA_SRC

print("***Welcome to My School Selector. This app lists all the schools in your desired area!***\n")

def main():
    schools_data = load_schools_data(SCHOOLS_DATA_SRC)
    if not schools_data:
        print("School data failed to load")
        sys.exit(1)
        
    filter_choices = obtain_filter_choices()
    filtered_schools = obtain_filtered_schools(filter_choices, schools_data)
    user_address = seek_user_address() #returns (latitude,longitude)
    if not user_address:
        print(f"FILTERED SCHOOLD = {filtered_schools}") #TODO delete later
        return filtered_schools
    else:
        filtered_sorted_schools_list = sort_schools_data(filtered_schools, user_address)
        
"""
consider building the app as a loop function that allows user to start again from the 
beginning, intead of the app just shutting down
"""

if __name__ == "__main__":
    main()