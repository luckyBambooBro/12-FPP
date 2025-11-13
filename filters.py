import inquirer
import pyinputplus as pyip
import pprint
import sys

def obtain_filter_choices():
    print("With My School Selector you can specify criteria to filter through our list of schools!")
    response = pyip.inputYesNo("Would you like to select your filter criteria?\n")

    filter_choices = {}
    if response.lower().startswith("y"):

        def val_function_no_answer(answers, current):
            if len(current) == 0:
                raise inquirer.errors.ValidationError('', reason="Please select an option")
            return True  
        
        def val_funct_one_answer(answers, current):
            if len(current) == 0:
                raise inquirer.errors.ValidationError('', reason="Please select an option")
            if len(current) > 1:
                raise inquirer.errors.ValidationError('', reason="Please select only one option")
            return True  

        questions = [
            inquirer.Checkbox(
                "years_taught",
                message="Which schooling level are you searching for?",
                choices = ["Any", ("Primary", "primary"), ("Secondary", "secondary"), ("Combined", "combined")],
                validate=val_function_no_answer
            ),
            inquirer.Checkbox(
                "gender",
                message="Which types of school will you consider?",
                choices=["Any", ("Boys", "boys"), ("Girls", "girls"), ("Co-ed", "co_ed")],
                validate=val_function_no_answer
            ),
            inquirer.Checkbox(
                "type",
                message="Do you prefer a public or private school?",
                choices=["Any", ("Public", "public"), ("Private", "private")],
                validate=val_function_no_answer
            ),
            inquirer.Checkbox(
                "religious",
                message="Do you have a religious preference for the school?",
                choices=["Any", ("Religious", True), ("Non-religious", False)],
                validate=val_funct_one_answer
            ),
            inquirer.Checkbox(
                "preschool",
                message="Are you looking for a school that includes a preschool?",
                choices=[("Yes", True), ("No", "Any")],
                validate=val_funct_one_answer
            ),
            inquirer.Checkbox(
                "osch",
                message="Are you looking for OSHC?",
                choices=[("Yes", True), ("No", "Any")],
                validate=val_funct_one_answer
            )    
        ]
        answers = inquirer.prompt(questions)
        return answers
    return {}




def obtain_filtered_schools(filter_choices, schools_data):
    if not filter_choices:
        print("No filters applied. Returning all schools")
        return schools_data

    filter_choices = {k: v for k, v in filter_choices.items() if "Any" not in v}
    pprint.pprint(filter_choices) #TODO remove

    try:
        current_list = schools_data
        for k, v in filter_choices.items():
            current_list = [school for school in current_list if school[k] in v]    
        pprint.pprint(f"CURRENT LIST:\n{current_list}")
    except Exception as e: #TODO: gemini had a key error but i didnt understand it so i did an Exception for now 
        print(e)
        sys.exit(1)

       
       
       

    
    
    