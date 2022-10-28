import folium
from folium.map import Icon, Popup
import pandas

data = pandas.read_csv("Volcanoes.txt")
lati = list(data["LAT"])
longi = list(data["LON"])
nam = list(data["NAME"])
stat = list(data["STATUS"])
elev = list(data["ELEV"])

def color_prod(el):
    """ This function gives color to the markers on map,
        according to the elevation of volcanoes.
    """
    if el >= 3000:
        return 'red'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'green'


map = folium.Map(location=[37.763351, -122.408937], zoom_start=5, tiles="OpenStreetMap")

fgv = folium.FeatureGroup(name="Volcanoes Marker")
for lat, lon, na, st, el in zip(lati, longi, nam, stat, elev):
    fgv.add_child(folium.Marker(location=[lat, lon], tooltip=na, popup=(st +" "+str(el)+" m") , icon=Icon(color=color_prod(el))))

fgp = folium.FeatureGroup(name="Population Shade")
fgp.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] >20000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'green'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")