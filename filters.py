import inquirer
import pyinputplus as pyip
import pprint

def obtain_filter_choices():
    print("With My School Selector you can specify criteria to filter through our list of schools!")
    response = pyip.inputYesNo("Would you like to select your filter criteria?\n")

    filter_choices = {}
    if response.lower().startswith("y"):

        def validation_function_one_answer(answers, current):
            if len(current) > 1:
                raise inquirer.errors.ValidationError('', reason="Please select only one option")
            return True  

        questions = [
            inquirer.Checkbox(
                "years_taught",
                message="Which schooling level are you searching for?",
                choices = ["Any", "Primary", "Secondary", "Combined"]
            ),
            inquirer.Checkbox(
                "gender",
                message="Which types of school will you consider?",
                choices=["Any", "Boys", "Girls", "Co-ed"]
            ),
            inquirer.Checkbox(
                "type",
                message="Do you prefer a public or private school?",
                choices=["Any", "Public", "Private"],
                validate=validation_function_one_answer
            ),
            inquirer.Checkbox(
                "religious",
                message="Do you have a religious preference for the school?",
                choices=["Any", "Religious", "Non-religious"],
                validate=validation_function_one_answer
            ),
            inquirer.Checkbox(
                "preschool",
                message="Are you looking for a school that includes a preschool?",
                choices=["Yes", "No"],
                validate=validation_function_one_answer
            ),
            inquirer.Checkbox(
                "osch",
                message="Are you looking for OSHC?",
                choices=["Yes", "No"],
                validate=validation_function_one_answer
            )    
        ]
        answers = inquirer.prompt(questions)
        pprint.pprint(answers) #TODO uncomment this
    return answers




def obtain_filtered_schools(filter_choices, schools_data):
    """the following is incorrect and needs go be fixed
    
    unfiltered_schools_data = schools_data
    for filter_key, filter_value in filter_choices.items():
        if "Any" in filter_value:
            filtered_schools_data = [school for school in unfiltered_schools_data ]         
        else:
            filtered_schools_data = [school for school in unfiltered_schools_data if school[filter_key] in filter_value]
    print(filtered_schools_data)"""



    
    
    