import json, sys, time
import streamlit as st
from src.filters import obtain_filtered_schools
from src.load_schools_data import load_schools_data
from src.sidebar_filter_and_search import sidebar_filter_and_search
from src.config import SCHOOLS_DATA_SRC


# ---PAGE SETUP ---
st.set_page_config(page_title="School Selector GUI", layout="wide")
st.title("🏫 School Locator Dashboard")

@st.cache_data
def load_schools_data_cached(): #this function must stay in app.py due to the streamlit import
    """
    load data from specified file path (.json) and performs data validation via enums
    returns a list of dictionaries of the schools or an empty list

    """
    with st.spinner("Loading school data..."):
        schools_data = load_schools_data(SCHOOLS_DATA_SRC)
        time.sleep(5)
        return schools_data


schools_data = load_schools_data_cached()












filter_choices, search_button = sidebar_filter_and_search()


filtered_schools = obtain_filtered_schools(filter_choices, None)

