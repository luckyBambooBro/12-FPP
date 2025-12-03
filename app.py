import streamlit as st
from src.sidebar_filter_and_search import sidebar_filter_and_search
from src.filters import obtain_filtered_schools

# ---PAGE SETUP ---
st.set_page_config(page_title="School Selector GUI", layout="wide")
st.title("🏫 School Locator Dashboard")

filter_choices, search_button = sidebar_filter_and_search()


filtered_schools = obtain_filtered_schools(filter_choices, None)
