from matplotlib import pyplot as plt
from die_m import Die

d = Die()
s=6
frequency = d.roll(nroll=10_000, nside=s, ndie=1)
sides=list(range(1,s+1))


fig,img=plt.subplots()
# fig,imgbar=plt.subplots()
# fig,imgscatter=plt.subplots()


img.plot(sides,frequency,linewidth=5)
# imgbar.bar(sides,frequency)
# imgscatter.scatter(sides,frequency)

img.set_title("Rolling Dice 10,000 Times" , fontsize=24)
img.set_xlabel("Sides",fontsize=12,color='red')
img.set_ylabel("Frequency",fontsize=12,color='green')
img.tick_params(axis='both',labelsize=12)


plt.style.use('seaborn')
plt.show()

