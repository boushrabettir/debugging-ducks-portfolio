import folium

def generate_map(places):
    MAP_CENTER = [37.0902, -95.7129]  
    MAP = folium.Map(location=MAP_CENTER, zoom_start=4)

    for place in places:
        folium.Marker(location=place["location"], popup=place["name"]).add_to(MAP)

    return MAP._repr_html_()

# Example places data
LOCATIONS = [
    {"location": [40.7128, -74.0060], "name": "New York City"},
    {"location": [47.6062, -122.3321], "name": "Seattle, Washington"},
    {"location": [38.9072, -77.0369], "name": "Washington, D.C."},
    {"location": [31.9686, -99.9018], "name": "Texas"}
]

MAP_HTML = generate_map(LOCATIONS)
