import pyinputplus as pyip, pprint

def obtain_filter_choices():
    print("With My School Selector you can specify criteria to filter through our list of schools!")
    response = pyip.inputYesNo("Would you like to select your filter criteria?\n")

    filter_choices = {}
    if response.lower().startswith("y"):
        years_taught = pyip.inputMenu(["Any", "Primary", "Secondary", "Combined"], "Which schooling level are you searching for\n",)
        #gender = pyip.inputChoice(["Any", "Boys", "Girls", "Co-ed"], "Which types of school will you consider?\n",)
        
        gender = pyip.inputChoice(
        ["Any", "Boys", "Girls", "Co-ed"],
        limit=3,
        separator=',', # Specifies the delimiter for multiple choices
        allowRegexes=[r'^\s*Any\s*$'] # Allows "Any" as a single choice to skip filtering
    )

        type = pyip.inputMenu(["Any", "Public", "Private"], "Do you prefer a public or private school?\n",)
        religious = pyip.inputMenu(["Any", "Religious", "Non-religious"], "Do you have a religious preference for the school?\n")
        preschool = pyip.inputYesNo("Are you looking for a school that includes a preschool? (Y/N)\n")
        osch = pyip.inputYesNo("Are you looking for OSHC? (Y/N)\n")

        if not years_taught == "Any": 
            filter_choices["years_taught"] = years_taught.lower()
        if not gender == "Any":
            filter_choices["gender"] = gender.lower()
        if not type == "Any":
            filter_choices["type"] = type.lower()

        if religious == "Religious":        
            filter_choices["religious"] = True 
        elif religious == "Non-religious":
            filter_choices["religious"] = False

        if preschool == "yes":    
            filter_choices["preschool"] = True
        if osch == "yes":
            filter_choices["osch"] = True

        if not filter_choices:
            response = pyip.inputYesNo("You have not selected any filters. Would you like to re-select filters?")
            if response.lower().startswith("n"):
                return filter_choices
            return obtain_filter_choices()
    return filter_choices

def obtain_filtered_schools(filter_choices, schools_data):
    print(f"FILTER CHOICES = {filter_choices}")
    
    filtered_school_data = schools_data
    for filter_keys, filter_values in filter_choices.items():
        filtered_school_data = [school for school in filtered_school_data if school[filter_keys] == filter_values]
    pprint.pprint(filtered_school_data)





    
    
    
    
    """ THE FOLLOWING WORKS BUT LIST COMP BETTER
    for filter_keys, filter_values in filter_choices.items():
        filtered_school_data = list(filter(lambda school_dict: school_dict[filter_keys] == filter_values, schools_data))
    print(filtered_school_data)"""


    
    