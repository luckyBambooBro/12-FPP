"""
in filters.py obtain_filtered_schools:
        we are unable to check for the aftual school that KeyErrored here because we have chosen
        to do list comprehension. if we did a for loop we could identify the school that 
        KeyErrored, but we are using list comprehension to optimise UX. instead, we will 
        make sure all schools have the correct keys in the backend when we preload the school
        data
"""


