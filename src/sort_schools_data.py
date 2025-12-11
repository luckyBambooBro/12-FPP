from geopy.distance import geodesic
import pprint
import sys
from src.config import DISTANCE_TO_USER, NAME, SCHOOL_COORDINATES

def sort_schools_data(filtered_schools, user_address, user_selected_radius):
    """
    sorts school data according to whatever sorting mode user selects (however currently there is 
    no functionality for user to select other sorting modes as there is only one sorting mode 
    so far. these other sorting modes may be built  later in this script
    """
    if not filtered_schools:
        print("No schools found after filtering")
        return
    if not user_address:
        return filtered_schools
    #elif user_selected_radius is None: doesnt matter, this condition is addressed in sort_by_distance()

    filtered_schools_with_distances = calculate_distance_user_to_schools(filtered_schools, user_address)
    sorted_schools_list = sort_by_distance(filtered_schools_with_distances, user_selected_radius)
    #TODO In future: can create other sorting methods below here:
    return sorted_schools_list


def calculate_distance_user_to_schools(filtered_schools, user_address):
    for school in filtered_schools:
        try:
            distance = round(
                geodesic(school[SCHOOL_COORDINATES], user_address).km,
                2)
        except KeyError as k_Error:
            print(f"kEYeRROR: Unable to determine distance from {school[NAME]}\n{k_Error}")
        except Exception as e:
            print(f"Unable to determine distance from {school[NAME]}\n{e}")
        else:
            school[DISTANCE_TO_USER] = distance
    return filtered_schools

def sort_by_distance(filtered_schools_with_distances, user_selected_radius):
    if user_selected_radius is None:
        user_selected_radius = float("inf")
    #sorts schools by distance to users addres and returns list
    #initially did this with list comprehension, but a for loop allows us to use dict.get()
    #which is safer in case one of the schools is missing the school[DISTANCE_TO_USER] key
    schools_with_radius = []
    for school in filtered_schools_with_distances:
        if school.get(DISTANCE_TO_USER, float("inf")) <= user_selected_radius:
            schools_with_radius.append(school)
    
    schools_with_radius.sort(key=lambda x: x.get(DISTANCE_TO_USER, float("inf")))
    return schools_with_radius
