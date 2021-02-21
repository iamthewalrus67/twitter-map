'''
Module for working with folium maps.
'''

import folium


def place_markers(folium_map, locations: list, color='blue'):
    '''
    Place multiple markers on map.
    '''
    for location in locations:
        place_marker(folium_map, location[0], location[1], color=color)


def place_marker(folium_map, name, location: list, color='blue'):
    '''
    Place one mark on map.
    '''
    if location == (0, 0):
        return
    folium_map.add_child(folium.Marker(
        location=location, popup=name, icon=folium.Icon(color=color)))


def create_group(name: str, show=True):
    '''
    Create new feature group.
    '''
    feature_group = folium.FeatureGroup(name=name, show=show)
    return feature_group


def create_map() -> folium.Map:
    '''
    Create new folium map.
    '''
    folium_map = folium.Map()
    return folium_map


def save_map(folium_map):
    '''
    Save map to file.
    '''
    return folium_map._repr_html_()
