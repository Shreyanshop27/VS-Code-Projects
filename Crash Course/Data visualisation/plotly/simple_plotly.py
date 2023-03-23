from plotly.graph_objects import Bar,Layout
from plotly import offline

num=[1,2,3,4,5,6,7,8,9,10]
sq=[1,4,9,16,25,36,49,64,81,100]

data= [Bar(x=num,y=sq)]

xtitle={'title':"Numbers"}
ytitle={'title':"Squares"}

my_layout=Layout(title="Numbers and Squares",
                 xaxis=xtitle,yaxis=ytitle)
offline.plot ( {'data':data,'layout':my_layout}, filename='Number and Square.chtml')