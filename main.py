import sys
from filters import obtain_filter_choices, obtain_filtered_schools
from load_schools_data import load_schools_data
from obtain_distance_to_schools import obtain_distance_to_schools
from config import SCHOOLS_DATA_SRC

print("***Welcome to My School Selector. This app lists all the schools in your desired area!***\n")

def main():
    schools_data = load_schools_data(SCHOOLS_DATA_SRC)
    if not schools_data:
        print("School data failed to load")
        sys.exit(1)
        
    filter_choices = obtain_filter_choices()
    filtered_schools = obtain_filtered_schools(filter_choices, schools_data)
    obtain_distance_to_schools(filtered_schools)
    
"""
consider building the app as a loop function that allows user to start again from the 
beginning, intead of the app just shutting down
"""

if __name__ == "__main__":
    main()