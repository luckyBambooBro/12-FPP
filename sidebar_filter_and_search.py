import streamlit as st

YEARS_LEVELS_OPTIONS = ["All", "Primary", "Secondary", "Combined"]
SCHOOL_TYPE_OPTIONS = ["All", "Public", "Private"]
GENDER_OPTIONS = ["All", "Co-education", "Boys", "Girls"]


def sidebar_filter_and_search():

    

    with st.sidebar:
        st.header("Filter & Search")

        user_address_input = st.text_input("Enter Your Home Address:")

        with st.form(key="filter_form"):
            st.subheader("Core Criteria")
        

            year_levels = st.selectbox(
                "Select Year Level", 
                options = YEARS_LEVELS_OPTIONS, 
                index=YEARS_LEVELS_OPTIONS.index("All"))

            school_type = st.selectbox(
                "Select School Type:", 
                options=SCHOOL_TYPE_OPTIONS,
                index=SCHOOL_TYPE_OPTIONS.index("All") 
            )

            gender_type = st.selectbox(
                "Select Gender:", 
                options=GENDER_OPTIONS,
                index=GENDER_OPTIONS.index("All") 
            )


            st.markdown("---")
            st.subheader("Additional Facilities and Programs:")

            option_religious = st.checkbox("Religious School")
            option_osch = st.checkbox("Out of School Hours Care (OSHC)")
            option_pre_school = st.checkbox("Pre-School")
            
            st.markdown("---")
            search_button = st.form_submit_button("Run Search and Filter")

    # --- MAIN EXECUTION BLOCK ---
    # This block only runs the logic if the form was submitted.

    if search_button:
        # 1. Collect all inputs (The variables above hold the final state)
        filter_choices = {
            "year_levels": year_levels,
            "school_type": school_type,
            "gender_type": gender_type,
            "is_religious": option_religious,
            "has_oshc": option_osch,
            "has_preschool": option_pre_school,
            "address": user_address_input
        }
        st.success(f"Processing search for schools near you...")
        return search_button