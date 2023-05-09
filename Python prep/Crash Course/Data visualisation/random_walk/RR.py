import matplotlib.pyplot as plt
# import sys
# sys.path.insert(0, 'c:\\Users\\shreyansh verma\\Documents\\VS Code Projects\\Crash Course\\Data visualisation')
from RandomWalkModule import RandomWalk
rw=RandomWalk()
rw.fillwalk()
plt.style.use("classic")
fig,img= plt.subplots()
img.plot(rw.x_value , rw.y_value )
plt.show()
