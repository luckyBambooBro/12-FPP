import json, sys, time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import streamlit as st
from src.display_sorted_schools import display_sorted_schools
from src.filters import obtain_filtered_schools
from src.load_schools_data import load_schools_data
from src.sort_schools_data import sort_schools_data
from src.config import (
    APP_NAME, NOMINATIM_DELAY, NOMINATIM_TIMEOUT,
    SCHOOLS_DATA_SRC,

    GENDER,
    SCHOOL_TYPE,
    YEAR_LEVELS,
    OSHC,
    PRESCHOOL,
    RELIGIOUS,

    SELECT_YEAR_LEVELS,
    SELECT_SCHOOL_TYPE,
    SELECT_GENDER,
    SELECT_RELIGIOUS_SCHOOL ,
    SELECT_OSCH ,
    SELECT_PRE_SCHOOL,
    SELECT_RADIUS
)
import time
#================= GLOBAL VARIABLES =======================
LAST_GEOCODED_TIME = "last geocoding time"
LAST_SUCCESSFUL_LOCATION = "last successful location"
# =========================================================
# CACHED RESOURCES & DATA
# =========================================================
@st.cache_resource
def initialise_geolocator():
    return Nominatim(user_agent=APP_NAME, timeout=NOMINATIM_TIMEOUT)

@st.cache_data(show_spinner=False)
def obtain_geolocation_from_address(address, _geolocator):
    if not address:
        return None
    try:
        return geolocator.geocode(address, timeout = NOMINATIM_TIMEOUT)
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f'Geolocation Error for "{address}": {e}')
    except Exception as e:
        print(e)
    
@st.cache_data(show_spinner=False)
def load_schools_data_cached(): #this function must stay in app.py due to the streamlit import
    """
    load data from specified file path (.json) and performs data validation via enums
    returns a list of dictionaries of the schools or an empty list

    """
    with st.spinner("Loading school data..."):
        schools_data = load_schools_data(SCHOOLS_DATA_SRC)
        time.sleep(2) #TODO delete this. its only to show me the spinner is working while loading
        return schools_data

# =========================================================
# FUNCTIONS
# =========================================================

def throttled_address_search(address, geolocator):
    """
    initially designed as gemini said the script reruns on interaction, but i think st.input() might 
    only rerun on "enter". useful to keep this anyway as it throttles the responses sent off to Nominatim 
    which is useful to due Nominatims restriction on the free tier of its API
    """
    if not address:
        return
    current_time = time.time()
    time_since_last_call = current_time - st.session_state[LAST_GEOCODED_TIME]

    if time_since_last_call <= NOMINATIM_DELAY:
        return st.session_state.get(LAST_SUCCESSFUL_LOCATION)
    
    st.session_state[LAST_GEOCODED_TIME] = current_time
    
    with st.spinner(f"Searching for {address}..."):
        location =  obtain_geolocation_from_address(address, geolocator)
        st.session_state[LAST_SUCCESSFUL_LOCATION] = location
        return location

def sidebar_filter_and_search():
    """
Presents the filter options to the user in the sidebar. Once user clicks on "Search", all the 
selected filters (and address if supplied) are return as a dictionary
"""
    
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
            sidebar_success_msg_placeholder = st.success(f"Processing search for schools near you...",icon="✅")
        else:
            sidebar_success_msg_placeholder = None
        #Guard against empty filters
        if not year_levels:
            year_levels = SELECT_YEAR_LEVELS #"All" will be stripped later but its easier to include it for now 
        if not gender:
            gender = SELECT_GENDER #"All" will be stripped later but its easier to include it for now
        
        #create dictionary of filters
        #keys must match data/schools.json keys
        filter_choices = {
            SCHOOL_TYPE: [school_type],#string
            YEAR_LEVELS: year_levels,#list
            GENDER: gender,#list
            RELIGIOUS: [religious], #boolean
            OSHC: [oshc], #boolean
            PRESCHOOL: [pre_school] #boolean
        }

    return filter_choices, search_button, sidebar_success_msg_placeholder
#===========================================

#============= SCRIPT EXECUTION ============

#--- Initialise Session State for Throttling ---
if LAST_GEOCODED_TIME not in st.session_state:
    st.session_state[LAST_GEOCODED_TIME] = 0
if LAST_SUCCESSFUL_LOCATION not in st.session_state:
    st.session_state[LAST_SUCCESSFUL_LOCATION] = None

# ---PAGE SETUP ---
st.set_page_config(page_title="School Selector GUI", layout="wide")
st.title("🏫 School Locator Dashboard")
schools_data = load_schools_data_cached()
geolocator = initialise_geolocator()

filter_choices = {}
search_button = False

with st.sidebar:
    st.header("Filter & Search")

    address = st.text_input("Please enter your address:")
    user_location_data = throttled_address_search(address, geolocator)

    #"address" will keep returning None, until it returns a valid geolocator address. Then the 
    # following checks run
    if user_location_data:
        st.info(f"📍 Address found: {user_location_data.address}")
    elif address and time.time() - st.session_state[LAST_GEOCODED_TIME] <= NOMINATIM_DELAY:
        st.caption("🔍 Searching for valid address...")

    user_selected_radius = st.selectbox(
        "Search Within Radius (km):",
        options=SELECT_RADIUS, 
        index=SELECT_RADIUS.index(25)
    )
        
    filter_choices, search_button, sidebar_success_msg_placeholder = sidebar_filter_and_search()

if search_button:
    filtered_schools = obtain_filtered_schools(filter_choices, schools_data)
    if user_location_data:
        sorted_schools_list = sort_schools_data(filtered_schools, user_location_data.point, user_selected_radius)
    else:
        sorted_schools_list = sort_schools_data(filtered_schools, user_location_data, user_selected_radius)  
    
    """so the sidebar_success_msg_placeholder success message actually does work but since i only have 7 schools
    the program computes it so quickly that we dont see the message. the time.sleep() is just to showcase the 
    feature, otherwise we wouldnt see it. if we delete this, remember to delete it from sidebar_filter_and_search 
    as well"""
    time.sleep(1)
    sidebar_success_msg_placeholder.empty() 
    
    if not sorted_schools_list:
        #guilty note i used gemini here because i dont know html
        st.markdown(
    "<div style='text-align: center; color: #ff4b4b;'><h3><strong>No schools found!</strong></h3></div>", 
    unsafe_allow_html=True
    )
    else:
        display_sorted_schools(sorted_schools_list)
        