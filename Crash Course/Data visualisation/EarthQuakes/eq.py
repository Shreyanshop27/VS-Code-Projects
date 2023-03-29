import json
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline


file='Crash Course\Data visualisation\EarthQuakes\earthquakes.json'
with open (file) as f:
    data=json.load(f)
datadic=data['features']

mags,lons,lats,hover_text=[],[],[],[]
for dic in datadic:
    mag=dic['properties']['mag']
    lon=dic['geometry']['coordinates'][0]
    lat=dic['geometry']['coordinates'][1]    
    title=dic['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

cordinate = [{
 'type': 'scattergeo',
 'lon': lons,
 'lat': lats,
 'text':hover_text,
 'marker': {
 'size': [15*mag for mag in mags],
 'color': mags,
 'colorscale':'Viridis',
 'reversescale':True,
 'colorbar':{'title':"Magnitude"}
 },
}]
my_layout=Layout(title="Earthquakes in past hour")
fig={'data':cordinate,'layout':my_layout}
offline.plot(fig,filename='geoeq.html')




