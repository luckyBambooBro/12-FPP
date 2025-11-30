from config import DISTANCE_TO_USER, NAME

def display_sorted_schools_list(sorted_schools_list):
    for school in sorted_schools_list:
        print(school[NAME])
        print(f"Distance: {school[DISTANCE_TO_USER]}\n")