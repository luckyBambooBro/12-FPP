import streamlit as st

SELECT_YEAR_LEVELS = ["All", "Primary", "Secondary", "Combined"]
SELECT_SCHOOL_TYPE = ["All", "Public", "Private"]
SELECT_GENDER = ["All", "Co-education", "Boys", "Girls"]
SELECT_RELIGIOUS_SCHOOL = "Religious School"
SELECT_OSCH = "Out of School Hours Care (OSHC)"
SELECT_PRE_SCHOOL = "Pre-School"


"""
Presents the filter options to the user in the sidebar. Once user clicks on "Search", all the 
selected filters (and address if supplied) are return as a dictionary
"""

def sidebar_filter_and_search():
    with st.sidebar:
        st.header("Filter & Search")

        user_address_input = st.text_input("Enter Your Home Address:")
        

        with st.form(key="filter_form"):
            st.subheader("Core Criteria")

            school_type = st.selectbox(
                "Select School Type:", 
                options=SELECT_SCHOOL_TYPE,
                index=SELECT_SCHOOL_TYPE.index("All") 
            )
            year_levels = st.multiselect(
                "Select Year Level(s)",
                options=SELECT_YEAR_LEVELS
            )

            gender = st.multiselect(
                "Select Gender",
                options=SELECT_GENDER
            )

            religious = st.checkbox(SELECT_RELIGIOUS_SCHOOL)
            oshc = st.checkbox(SELECT_OSCH)
            pre_school = st.checkbox(SELECT_PRE_SCHOOL)

            st.markdown("---")

            search_button = st.form_submit_button("Filter & Search")
            if search_button:
                st.success(f"Processing search for schools near you...")
            
            #Guard against empty filters
            if not year_levels:
                year_levels = SELECT_YEAR_LEVELS
            if not gender:
                gender = SELECT_GENDER
            
            #create dictionary of filters
            filter_choices = {
                "school_type": [school_type],#string
                "year levels": year_levels,#list
                "gender": gender,#list
                "religious": [religious], #boolean
                "oshc": [oshc], #boolean
                "pre_school": [pre_school] #boolean
            }

    return filter_choices, search_button
               