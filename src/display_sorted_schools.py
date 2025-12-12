import streamlit as st

def display_sorted_schools(sorted_schools_list):
    for school in sorted_schools_list:
        st.markdown(school)