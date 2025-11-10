from load_school_data import load_school_data
from obtain_filter_choices import obtain_filter_choices
import sys

print("***Welcome to My School Selector. This app lists all the schools in your desired area!***\n")

def main():
    schools_data = load_school_data()
    if not schools_data:
        print("School data failed to load")
        sys.exit(1)
        
    filter_choices = obtain_filter_choices()
    print(filter_choices)
    


if __name__ == "__main__":
    main()