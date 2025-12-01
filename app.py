import streamlit as st
from sidebar_filter_and_search import sidebar_filter_and_search


st.set_page_config(page_title="School Selector GUI", layout="wide")
st.title("🏫 School Locator Dashboard")

filter_choices, search_button = sidebar_filter_and_search()
    