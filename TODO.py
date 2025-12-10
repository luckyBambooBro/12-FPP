"""
in filters.py obtain_filtered_schools:
        we are unable to check for the aftual school that KeyErrored here because we have chosen
        to do list comprehension. if we did a for loop we could identify the school that 
        KeyErrored, but we are using list comprehension to optimise UX. instead, we will 
        make sure all schools have the correct keys in the backend when we preload the school
        data
"""

"""in app.py when i create {filter_choices}, for the keys(which are strings), i hard code the strings and
 have left a note that they must match the json file. it would be good if i could make this more 
 robust. consider enums with fields of what the keys should be then running for k in filter_choices.keys(),
 if not k in enum, raise keyError
"""