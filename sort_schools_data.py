from geopy.distance import geodesic
import pprint

SCHOOL_COORDINATES = "school_coordinates"
DISTANCE_TO_USER = "distance_to_user_km"

def sort_schools_data(filtered_schools, user_address):
    """
    sorts school data according to whatever sorting mode user selects (however currently there is 
    no functionality for user to select other sorting modes as there is only one sorting mode 
    so far. these other sorting modes may be built  later in this script
    """
    filtered_schools_with_distances = calculate_distance_user_to_schools(filtered_schools, user_address)
    sorted_schools_list = sort_by_distance(filtered_schools_with_distances)
    pprint.pprint(f"SORTED LIST:\n{sorted_schools_list}") #TODO remove this
    #create other ways to sort below here:

    return sorted_schools_list

def calculate_distance_user_to_schools(filtered_schools, user_address):
    for school in filtered_schools:
        try:
            distance = geodesic(school[SCHOOL_COORDINATES], user_address).km
        except KeyError as k_Error:
            print(k_Error)
        except Exception as e:
            print(e)
        else:
            school[DISTANCE_TO_USER] = distance
    return filtered_schools

def sort_by_distance(filtered_schools_with_distances):
    #sorts schools by distance to users addres and returns list
    filtered_schools_with_distances.sort(key=lambda school: school[DISTANCE_TO_USER])
    return filtered_schools_with_distances
    