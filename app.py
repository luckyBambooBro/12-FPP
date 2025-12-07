import json, sys, time
from geopy.geocoders import Nominatim
import streamlit as st
from src.filters import obtain_filtered_schools
from src.load_schools_data import load_schools_data
from src.config import (
    APP_NAME, NOMINATIM_DELAY, NOMINATIM_TIMEOUT,
    SCHOOLS_DATA_SRC
)
#================= GLOBAL VARIABLES =======================
LAST_GEOCODED_TIME = "last geocoding time"
LAST_SUCCESSFUL_LOCATION = "last successful location"
# =========================================================
# CACHED RESOURCES & DATA
# =========================================================
@st.cache_resource
def initialise_geolocator():
    return Nominatim(user_agent=APP_NAME, timeout=NOMINATIM_TIMEOUT)

@st.cache_data
def obtain_geolocation_from_address(address, geolocator):
    if not address:
        return None
    return geolocator.geocode(address, timeout = NOMINATIM_TIMEOUT)

@st.cache_data(show_spinner=False)
def load_schools_data_cached(): #this function must stay in app.py due to the streamlit import
    """
    load data from specified file path (.json) and performs data validation via enums
    returns a list of dictionaries of the schools or an empty list

    """
    with st.spinner("Loading school data..."):
        schools_data = load_schools_data(SCHOOLS_DATA_SRC)
        time.sleep(5) #TODO delete this. its only to show me the spinner is working while loading
        return schools_data

# =========================================================
# FUNCTIONS
# =========================================================

def throttled_autocomplete(address, geolocator):
    if not address:
        return
    current_time = time.time()
    time_since_last_call = current_time - st.session_state[LAST_GEOCODED_TIME]

    if time_since_last_call <= NOMINATIM_DELAY:
        return st.session_state.get[LAST_SUCCESSFUL_LOCATION]
    
    st.session_state[LAST_GEOCODED_TIME] = current_time
    
    with st.spinner(f"Searching for {address}..."):
        location = obtain_geolocation_from_address(address, geolocator)
        st.session_state[LAST_SUCCESSFUL_LOCATION] = location
        return location

def sidebar_filter_and_search(geolocator):
    """
Presents the filter options to the user in the sidebar. Once user clicks on "Search", all the 
selected filters (and address if supplied) are return as a dictionary
"""
    filter_choices = {}
    search_button = False

    SELECT_YEAR_LEVELS = ["All", "Primary", "Secondary", "Combined"]
    SELECT_SCHOOL_TYPE = ["All", "Public", "Private"]
    SELECT_GENDER = ["All", "Co-education", "Boys", "Girls"]
    SELECT_RELIGIOUS_SCHOOL = "Religious School"
    SELECT_OSCH = "Out of School Hours Care (OSHC)"
    SELECT_PRE_SCHOOL = "Pre-School"

    with st.sidebar:
        st.header("Filter & Search")

        address = st.text_input("Please enter your address:")
        user_location_data = throttled_autocomplete(address, geolocator)
        print(f"ADDRESS  = {address}")

        #"address" will keep returning None, until it returns a valid geolocator address. Then the 
        # following checks run
        if user_location_data:
            st.info(f"📍 Address found: {user_location_data.address}")
        elif address and time.time() - st.session[LAST_GEOCODED_TIME] <= NOMINATIM_DELAY:
            st.caption("🔍 Searching")


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

#============= SCRIPT EXECUTION ============

#--- Initialise Session State for Throttling ---
if LAST_GEOCODED_TIME not in st.session_state:
    st.session_state[LAST_GEOCODED_TIME] = 0

# ---PAGE SETUP ---
st.set_page_config(page_title="School Selector GUI", layout="wide")
st.title("🏫 School Locator Dashboard")
schools_data = load_schools_data_cached()
geolocator = initialise_geolocator()


filter_choices, search_button = sidebar_filter_and_search(geolocator)


filtered_schools = obtain_filtered_schools(filter_choices, None)

