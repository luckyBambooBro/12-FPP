filter_choices = {
                "school_type": [school_type],#string
                "year levels": year_levels,#list
                "gender": gender,#list
                "religious": [religious], #boolean
                "oshc": [oshc], #boolean
                "pre_school": [pre_school] #boolean
            }

filter_choices = {}
            if school_type:
                filter_choices["school_type"] = [school_type]#string
            if year_levels:
                filter_choices["year levels"] = year_levels#list
            if gender:
                filter_choices["gender"] = gender#list
            if religious:
                filter_choices["religious"] = [religious] #boolean
            filter_choices["oshc"] = [oshc] #boolean
            if pre_school:
                filter_choices["pre_school"] = [pre_school] #boolean