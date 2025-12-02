import sys
import pprint
from st_src.config import ALL, NO, YES
from config import YEAR_LEVELS_OPTIONS

PRIMARY = "primary"
SECONDARY = "secondary"
COMBINED = "Combined"
def handle_umbrella_terms(filter_choices):
    if YEAR_LEVELS_OPTIONS in filter_choices:
        if PRIMARY in filter_choices[YEAR_LEVELS_OPTIONS] or SECONDARY in filter_choices[YEAR_LEVELS_OPTIONS]:
            filter_choices[YEAR_LEVELS_OPTIONS].append(COMBINED)
    return filter_choices


def obtain_filtered_schools(filter_choices, schools_data):
    if not filter_choices:
        print("No filters applied. Returning all schools")
        return schools_data

    filter_choices = {k: v for k, v in filter_choices.items() if ALL not in v}
    handle_umbrella_terms(filter_choices)

    pprint.pprint(f"FILTER_CHOICES: {filter_choices}") #TODO remove

    try:
        current_list = schools_data
        for k, v in filter_choices.items():
            current_list = [school for school in current_list if school[k] in v]    
        pprint.pprint(f"CURRENT LIST:\n{current_list}") #TODO remove this
        return current_list
    except Exception as e: #TODO: gemini had a key error but i didnt understand it so i did an Exception for now 
        print(e)
        sys.exit(1)

