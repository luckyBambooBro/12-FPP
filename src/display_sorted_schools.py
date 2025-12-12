import streamlit as st

def display_sorted_schools(sorted_schools_list):
    """
    Displays schools in a visually appealing 'Card' format.
    """
    if not sorted_schools_list:
        st.warning("No schools found matching your criteria")
    st.warning("No schools found matching your criteria")
    for school in sorted_schools_list:
        st.markdown(school)