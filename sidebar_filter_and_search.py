import streamlit as st
from src.config import (
    GENDER_OPTIONS, 
    OSCH,
    PRE_SCHOOL,
    RELIGIOUS_SCHOOL,
    SCHOOL_TYPE_OPTIONS, 
    YEAR_LEVELS_OPTIONS
)

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
        

            selectbox_year_levels = st.selectbox(
                "Select Year Level", 
                options = YEAR_LEVELS_OPTIONS, 
                index=YEAR_LEVELS_OPTIONS.index("All"))

            selectbox_school_type = st.selectbox(
                "Select School Type:", 
                options=SCHOOL_TYPE_OPTIONS,
                index=SCHOOL_TYPE_OPTIONS.index("All") 
            )

            selectbox_gender_type = st.selectbox(
                "Select Gender:", 
                options=GENDER_OPTIONS,
                index=GENDER_OPTIONS.index("All") 
            )


            st.markdown("---")
            st.subheader("Additional Facilities and Programs:")

            checkbox_religious = st.checkbox(RELIGIOUS_SCHOOL)
            checkbox_oshc = st.checkbox(OSCH)
            checkbox_pre_school = st.checkbox(PRE_SCHOOL)
            
            st.markdown("---")
            search_button = st.form_submit_button("Run Search and Filter")

    # --- MAIN EXECUTION BLOCK ---
    # This block only runs the logic if the form was submitted.


    # 1. Collect all inputs (The variables above hold the final state)
    filter_choices = {
        "year_levels": selectbox_year_levels,
        "school_type": selectbox_school_type,
        "gender_type": selectbox_gender_type,
        "is_religious": checkbox_religious,
        "has_oshc": checkbox_oshc,
        "has_preschool": checkbox_pre_school,
        "address": user_address_input
    }
    st.success(f"Processing search for schools near you...")
    return filter_choices, search_button