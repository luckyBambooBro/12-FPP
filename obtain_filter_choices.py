import pyinputplus as pyip

def obtain_filter_choices():
    print("With My School Selector you can specify criteria to filter through our list of schools!")
    response = pyip.inputYesNo("Would you like to select your filter criteria?\n")

    filter_choices = {}
    if response.lower().startswith("y"):
        
        years_taught = pyip.inputMenu(["Any", "Primary", "Secondary", "Combined"], "Which schooling level are you searching for\n",)
        gender = pyip.inputMenu(["Any", "Boys", "Girls", "Co-ed"], "Which student gender school are you looking for?\n",)
        type = pyip.inputMenu(["Any", "Public", "Private"], "Do you prefer a public or private school?\n",)
        religious = pyip.inputYesNo("Do you have a religious preference for the school? (Y/N)\n")
        preschool = pyip.inputYesNo("Are you looking for a school that includes a preschool? (Y/N)\n")
        osch = pyip.inputYesNo("Are you looking for OSHC? (Y/N)\n")

        if not years_taught == "Any": 
            filter_choices["years_taught"] = years_taught.lower()
        if not gender == "Any":
            filter_choices["gender"] = gender.lower()
        if not type == "Any":
            filter_choices["type"] = type.lower()
        if religious == "yes":        
            filter_choices["religious"] = True 
        if preschool == "yes":    
            filter_choices["preschool"] = True
        if osch == "yes":
            filter_choices["osch"] = True

    if not filter_choices:
        pyip.inputYesNo("You have not selected any filters. Would you like to continue?")
        

    
    return filter_choices



    