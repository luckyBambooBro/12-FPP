def obtain_filtered_schools(filter_choices, schools_data):
    if not filter_choices:
        print("No filters applied. Returning all schools")
        return schools_data

    #removes any filters that contain "All" or False since theyre redundant 

    filter_choices = {k: v for k, v in filter_choices.items() if "All" not in v}
    filter_choices = {k: v for k, v in filter_choices.items() if False not in v}
    return filter_choices
    # try:
    #     current_list = schools_data
    #     for k, v in filter_choices.items():
    #         current_list = [school for school in current_list if school[k] in v]    
    #     pprint.pprint(f"CURRENT LIST:\n{current_list}") #TODO remove this
    #     return current_list
    # except Exception as e: #TODO: gemini had a key error but i didnt understand it so i did an Exception for now 
    #     print(e)
    #     sys.exit(1)

