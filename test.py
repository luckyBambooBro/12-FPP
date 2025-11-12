def obtain_filtered_schools(filter_choices, schools_data):
    print(f"FILTER CHOICES = {filter_choices}")
    
    filtered_school_data = schools_data
    for filter_keys, filter_values in filter_choices.items():
        filtered_school_data = [school for school in filtered_school_data if school[filter_keys] == filter_values]
    pprint.pprint(filtered_school_data)