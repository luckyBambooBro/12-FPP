import json, sys, time
from geopy.geocoders import Nominatim
import streamlit as st
from src.filters import obtain_filtered_schools
from src.load_schools_data import load_schools_data
from src.config import (
    APP_NAME, NOMINATIM_TIMEOUT,
    SCHOOLS_DATA_SRC
)



#============= Cached Variables=============
@st.cache_resource
def initialise_geolocator():
    geolocator = Nominatim(user_agent=APP_NAME, timeout=NOMINATIM_TIMEOUT)
    return geolocator
#================ FUNCTIONS ================
@st.cache_data
def user_address_input_autocomplete(address):
    geolocator = initialise_geolocator()
    address = geolocator.geocode(address, timeout = NOMINATIM_TIMEOUT)
    return address

def sidebar_filter_and_search():
    """
Presents the filter options to the user in the sidebar. Once user clicks on "Search", all the 
selected filters (and address if supplied) are return as a dictionary
"""
    SELECT_YEAR_LEVELS = ["All", "Primary", "Secondary", "Combined"]
    SELECT_SCHOOL_TYPE = ["All", "Public", "Private"]
    SELECT_GENDER = ["All", "Co-education", "Boys", "Girls"]
    SELECT_RELIGIOUS_SCHOOL = "Religious School"
    SELECT_OSCH = "Out of School Hours Care (OSHC)"
    SELECT_PRE_SCHOOL = "Pre-School"

    with st.sidebar:
        st.header("Filter & Search")


        address = st.text_input("Please enter your address:")
        user_address = user_address_input_autocomplete(address)
        print(f"ADDRESS  ={user_address}")
        print(user_address.latitude)
        print(user_address.longitude)

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
               
#===========================================

# ---PAGE SETUP ---
st.set_page_config(page_title="School Selector GUI", layout="wide")
st.title("🏫 School Locator Dashboard")

@st.cache_data(show_spinner=False)
def load_schools_data_cached(): #this function must stay in app.py due to the streamlit import
    """
    load data from specified file path (.json) and performs data validation via enums
    returns a list of dictionaries of the schools or an empty list

    """
    with st.spinner("Loading school data..."):
        schools_data = load_schools_data(SCHOOLS_DATA_SRC)
        time.sleep(5)
        return schools_data


    #=====Variables for sidebar_filter_and_search()=====
    SELECT_YEAR_LEVELS = ["All", "Primary", "Secondary", "Combined"]
    SELECT_SCHOOL_TYPE = ["All", "Public", "Private"]
    SELECT_GENDER = ["All", "Co-education", "Boys", "Girls"]
    SELECT_RELIGIOUS_SCHOOL = "Religious School"
    SELECT_OSCH = "Out of School Hours Care (OSHC)"
    SELECT_PRE_SCHOOL = "Pre-School"
    #===================================================
    """
Presents the filter options to the user in the sidebar. Once user clicks on "Search", all the 
selected filters (and address if supplied) are return as a dictionary
"""
    with st.sidebar:
        st.header("Filter & Search")

        user_address_input = user_address_input_autocomplete()
        

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
               
schools_data = load_schools_data_cached()












filter_choices, search_button = sidebar_filter_and_search()


filtered_schools = obtain_filtered_schools(filter_choices, None)

