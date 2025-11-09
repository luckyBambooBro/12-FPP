import json
from enums.school_data_enums import ( 
gender_enum,
years_taught_enum,
type_enum,
religious_enum,
preschool_enum,
osch_enum)

SRC = "schools.json"

def load_school_data():
    try:
        with open(SRC, "r") as f:
            schools_data = json.load(f)
            check_schools_data(schools_data)
            return schools_data
    except FileNotFoundError:
        print(f'ERROR: File not found: "{SRC}". Check the file path')
        return [] #gemini: prevents crashing if this function fails and returns None
    except json.JSONDecodeError:
        print(f'ERROR: Invalid JSON format in "{SRC}" Check for syntax errors') #gemini: prevents crashing if this function fails and returns None
        return []
    
def check_schools_data(schools_data):
    for school in schools_data:
        if school["gender"] == "co-ed":
            school["gender"] = "co_ed"
        try:
            years_taught_enum[school["years_taught"].upper()]
            gender_enum[school["gender"].upper()]
            type_enum[school["type"].upper()]

            #the below are booleans that need to be converted to strings to check if they qualify in the respective enums
            religious_enum[str(school["religious"]).upper()]
            preschool_enum[str(school["preschool"]).upper()]
            osch_enum[str(school["osch"]).upper()]


        except KeyError:        
            raise Exception(f"School ID: {school["id"]}: Error in school data. Check values")

