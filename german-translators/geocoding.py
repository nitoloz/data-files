from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

def get_coordinates(address):
    load_dotenv()
    OPENCAGE_API_KEY = os.getenv('OPENCAGE_API_KEY')
    geocoder = OpenCageGeocode(OPENCAGE_API_KEY)
    results = geocoder.geocode(address)
    return results[0]['geometry']