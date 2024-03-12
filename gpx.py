import gpxpy
import folium
#import webbrowser
import os

fmap = folium.Map(location=[45.7683706528849, 3.0956084546599207], titles="OpenStreetMap", zoom_start=11.75)
folium.Marker([45.7683706528849, 3.0956084546599207], popup="Maison", icon=folium.Icon(color='green')).add_to(fmap)
    
for filename in os.listdir("data"):
    print(filename)

    if filename.lower().find("nordique") == -1:
        couleur = 'blue'
    else:
        couleur = 'red'

    gpx_file = open(os.path.join("data", filename), 'r')
    gpx = gpxpy.parse(gpx_file)
     
    points=gpx.tracks[0].segments[0].points

    latitude = []
    longitude = []
    coordinates = []
    point = []

    for i, point in enumerate(points):
        latitude.append(float(point.latitude))
        longitude.append(float(point.longitude))
    i = 0
    for x in latitude:
        if i > 0:
            mypoints = [(latitude[i-1], longitude[i-1]), (latitude[i], longitude[i])]
            folium.PolyLine(mypoints, color=couleur, weight=2, opacity=0.6).add_to(fmap)
        i = i + 1


fmap.save('cartes_test.html')
#webbrowser.open('cartes_test.html')
