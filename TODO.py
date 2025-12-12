"""
in filters.py obtain_filtered_schools:
        we are unable to check for the aftual school that KeyErrored here because we have chosen
        to do list comprehension. if we did a for loop we could identify the school that 
        KeyErrored, but we are using list comprehension to optimise UX. instead, we will 
        make sure all schools have the correct keys in the backend when we preload the school
        data
"""

"""another logistics error. if you select secondary schools + boys + religious
CBC doesnt come up. you need to select combined for it to come up
fix it so it comes up without combined

ALSO SEE: load_schools_data.py modify_schools_data()"""

"""after clicking on filter & search button a popupo message says 
"processing search for schools near you". try make this disappear
after a few seconds"""