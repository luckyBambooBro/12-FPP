import json, sys

def load_schools_data(file_path):
    """
    load data from specified file path (.json) and performs data validation via enums
    returns a list of dictionaries of the schools or an empty list

    """
    try:
        with open(file_path, "r") as f:
            schools_data = json.load(f)
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
    

