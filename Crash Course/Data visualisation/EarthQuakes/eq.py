import json
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline


file='Crash Course\Data visualisation\EarthQuakes\earthquakes.json'
with open (file) as f:
    data=json.load(f)
datadic=data['features']

mags,lons,lats=[],[],[]
for dic in datadic:
    mag=dic['properties']['mag']
    lon=dic['geometry']['coordinates'][0]
    lat=dic['geometry']['coordinates'][1]    
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

cordinate = [{
 'type': 'scattergeo',
 'lon': lons,
 'lat': lats,
 'marker': {
 'size': [15*mag for mag in mags],
 },
}]
my_layout=Layout(title="Earthquakes in past hour")
fig={'data':cordinate,'layout':my_layout}
offline.plot(fig,filename='geoeq.html')

 


