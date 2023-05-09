import matplotlib.pyplot as plt
# print(plt.style.available)

# num=[1,100,1,100,2,69]

###
x_value=[1,100,4,27]
y_value=[23,12,34,3]
###
plt.style.use("dark_background")
fig,chart=plt.subplots()
# chart.plot(num , linewidth=10)

####
chart.scatter(x_value,y_value , c= y_value , cmap=plt.cm.Reds)
####

chart.set_title("Test")
chart.set_xlabel("x" , fontsize=30)
chart.set_ylabel("y", fontsize=30)
chart.tick_params(axis="both" , labelsize=30)


plt.show()