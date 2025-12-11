import pprint, sys

def convert_values_to_match_json_file(filter_choices):
    """converts values in dictionary to usable values for filtering in backend"""
    for k, v in filter_choices.items():
        filter_choices[k] = [item.lower().replace("co-education", "co_ed") if isinstance(item, str) else item 
                             for item in v]
    return filter_choices

def obtain_filtered_schools(filter_choices, schools_data):
    if not filter_choices:
        print("No filters applied. Returning all schools")
        return schools_data

    #removes any filters that contain "All" or False since theyre redundant 
    filter_choices = {k: v for k, v in filter_choices.items() if "All" not in v and False not in v}
    if not filter_choices:
        print("No filters applied. Returning all schools")
        return schools_data
    filter_choices = convert_values_to_match_json_file(filter_choices)

    try:
        current_list = schools_data
        for k, v in filter_choices.items():
            current_list = [school for school in current_list if school[k] in v]    
        return current_list
    except KeyError:
        print(f"KeyError filtering school data") 
        """
        we are unable to check for the actual school that KeyErrored here because we have chosen
        to do list comprehension. if we did a for loop we could identify the school that 
        KeyErrored, but we are using list comprehension to optimise UX. instead, we will 
        make sure all schools have the correct keys in the backend when we preload the school
        data
    
        i have also decided not to raise the error and exit the program, so the user can 
        continue with the program. it may be missing the school that errored, but it 
        will still return all the other schools that match the filter criteria and the user 
        can continue with the program"""
    except Exception as e: #TODO: gemini had a key error but i didnt understand it so i did an Exception for now 
        print(e)
        sys.exit(1)


