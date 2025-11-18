import json, sys
from enums.school_data_enums import ( 
gender_enum,
years_taught_enum,
type_enum,
boolean_enum)

def load_schools_data(file_path):
    """
    load data from specified file path (.json) and performs data validation via enums
    returns a list of dictionaries of the schools or an empty list

    """
    try:
        with open(file_path, "r") as f:
            schools_data = json.load(f)
            check_schools_data(schools_data)
            return schools_data
    except FileNotFoundError:
        print(f'ERROR: File not found: "{file_path}". Check the file path')
        return [] #gemini: prevents crashing if this function fails and returns None
    except json.JSONDecodeError:
        print(f'ERROR: Invalid JSON format in "{file_path}" Check for syntax errors') #gemini: prevents crashing if this function fails and returns None
        return []
    except ValueError as e:
        print(e)
        sys.exit(1)
    
def check_schools_data(schools_data):
    for school in schools_data:
        try:
            years_taught_enum[school["years_taught"].upper()]
            gender_enum[school["gender"].upper()]
            type_enum[school["type"].upper()]

            #the below are booleans that need to be converted to strings to check if they qualify in the respective enums
            boolean_enum[str(school["religious"]).upper()]
            boolean_enum[str(school["preschool"]).upper()]
            boolean_enum[str(school["osch"]).upper()]


        except KeyError:        
            raise ValueError(f"\nFATAL DATA ERROR: School ID: {school['id']} ({school['name']})."
                "\nCheck the value of a 'years_taught', 'gender', 'type', 'religious', 'preschool', or 'osch' field.")
        except Exception as e:
            raise Exception(f"\nUNEXPECTED FATAL ERROR at School ID: {school['id']} ({school['name']})."
            f"\nDetails: {e}")

