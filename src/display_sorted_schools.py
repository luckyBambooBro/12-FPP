import streamlit as st
from src.config import(
    ADDRESS,
    DISTANCE_TO_USER,
    GENDER,
    NAME, 
    OSHC,
    PRESCHOOL, 
    RELIGIOUS, 
    SCHOOL_COORDINATES, 
    SCHOOL_TYPE,
    WEBSITE,
    YEAR_LEVELS
)

def display_sorted_schools(sorted_schools_list):
    """
    Displays schools in a visually appealing 'Card' format.
    """
    if not sorted_schools_list:
        st.warning("No schools found matching your criteria")
        return

    st.subheader(f"Found {len(sorted_schools_list)} schools")
    st.markdown("---")

    for school in sorted_schools_list:
        #create a display container for each individual school with border
        with st.container(border=True):
            #create 2 columns, left is 3 parts wide, right 1 part wide. displays school info left, distance right
            col1, col2 = st.columns([3, 1])
            with col1:
                #1. School Name
                st.subheader(f"🏫{school.get(NAME, "Unknown School")}")
                #2. School Address
                st.markdown(f"**📍 Address:** {school.get(ADDRESS, "N/A")}")

                #3. Optional small text display tags
                smallText_school_type = school.get(SCHOOL_TYPE, "N/A")
                smallText_years_taught  = school.get(YEAR_LEVELS, "N/A").title()
                smallText_gender = school.get(GENDER, "N/A").title()

                st.caption(f"🏷️ **Type:** {smallText_school_type} | 👤 **Gender:** {smallText_gender} | 🎓 ** Year Levels:** {smallText_years_taught}")

                #4. Link website if available
                if school[WEBSITE]:
                    st.link_button("Visit Website", school[WEBSITE])

            with col2:
                distance = school.get(DISTANCE_TO_USER, "N/A")
                st.metric(label="Distance", value=distance)