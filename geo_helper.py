'''
Module for finding coordinates.
'''

import math
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderTimedOut
from geopy.exc import GeocoderUnavailable

geolocator = Nominatim(user_agent="Geo Helper")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)


def get_coordinates(address: str) -> tuple:
    '''
    Get coordinates of location.
    >>> get_coordinates('Lviv')
    (49.841952, 24.0315921)
    >>> get_coordinates('New York')
    (40.7127281, -74.0060152)
    '''
    try:
        location = try_geocode_until_failure(address)
    except GeocoderUnavailable:
        return 0, 0

    if location is None:
        return 0, 0

    return location.latitude, location.longitude


def try_geocode_until_failure(address: str, attempt=1, max_attempts=3):
    '''
    Check if geopy can find location of address.
    '''
    try:
        return geolocator.geocode(address)
    except GeocoderTimedOut:
        if attempt <= max_attempts:
            return try_geocode_until_failure(address, attempt=attempt+1)
        raise
