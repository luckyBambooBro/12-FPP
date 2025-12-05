from geopy.geocoders import Nominatim
import streamlit as st
import time
from .config import geolocator, NOMINATIM_DELAY, NOMINATIM_TIMEOUT

MIN_ADDRESS_LENGTH = 5


@st.cache_data
def user_address_autocomplete(user_address_input):
    if len(user_address_input) > MIN_ADDRESS_LENGTH:
        address = geolocator.geocode(user_address_input, NOMINATIM_TIMEOUT)
        time.sleep(NOMINATIM_DELAY)
