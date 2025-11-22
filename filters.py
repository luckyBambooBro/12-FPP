import sys
import pprint
import inquirer
from inquirer import errors as inquirer_errors # CRITICAL: Keeping this explicit import as it is required to access the ValidationError class.

ANY = "Any" 
YES = "Yes"
NO = "No"

def obtain_filter_choices():
    
    def val_function_no_answer(answers, current):
        if len(current) == 0:
            raise inquirer_errors.ValidationError('', reason="Please select an option")
        return True  
    
    def val_funct_one_answer(answers, current):
        if len(current) == 0:
            raise inquirer_errors.ValidationError('', reason="Please select an option")
        if len(current) > 1:
            raise inquirer_errors.ValidationError('', reason="Please select only one option")
        return True  

    print("With My School Selector you can specify criteria to filter through our list of schools!")
    
    question = [inquirer.List(
        "query_select_filter", 
        message="Would you like to select your filter criteria?", 
        choices=[YES, NO], 
        default=YES
        )
    ]
    answer = inquirer.prompt(question)
    

    if YES in answer["query_select_filter"]:
        questions = [
            inquirer.Checkbox(
                "years_taught",
                message="Which schooling level are you searching for?",
                choices = [ANY, ("Primary", "primary"), ("Secondary", "secondary"), ("Combined", "combined")],
                validate=val_function_no_answer
            ),
            inquirer.Checkbox(
                "gender",
                message="Which types of school will you consider?",
                choices=[ANY, ("Boys", "boys"), ("Girls", "girls"), ("Co-ed", "co_ed")],
                validate=val_function_no_answer
            ),
            inquirer.Checkbox(
                "type",
                message="Do you prefer a public or private school?",
                choices=[ANY, ("Public", "public"), ("Private", "private")],
                validate=val_function_no_answer
            ),
            inquirer.Checkbox(
                "religious",
                message="Do you have a religious preference for the school?",
                choices=[ANY, ("Religious", True), ("Non-religious", False)],
                validate=val_funct_one_answer
            ),
            inquirer.Checkbox(
                "preschool",
                message="Are you looking for a school that includes a preschool?",
                choices=[(YES, True), (NO, ANY)],
                validate=val_funct_one_answer
            ),
            inquirer.Checkbox(
                "osch",
                message="Are you looking for OSHC?",
                choices=[(YES, True), (NO, ANY)],
                validate=val_funct_one_answer
            )    
        ]
        answers = inquirer.prompt(questions)
        return answers  
    return {}

def handle_umbrella_terms(filter_choices):
    if "years_taught" in filter_choices:
        if "primary" in filter_choices["years_taught"] or "secondary" in filter_choices["years_taught"]:
            filter_choices["years_taught"].append("combined")
    return filter_choices


def obtain_filtered_schools(filter_choices, schools_data):
    if not filter_choices:
        print("No filters applied. Returning all schools")
        return schools_data

    filter_choices = {k: v for k, v in filter_choices.items() if ANY not in v}
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

