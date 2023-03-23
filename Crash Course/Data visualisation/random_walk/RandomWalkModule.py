from random import choice

class RandomWalk:
    def __init__(self, numpoint=50_000):
        self.numpoint = numpoint

        self.x_value=[0]
        self.y_value=[0]
    
    def fillwalk(self):
        while len(self.x_value) < self.numpoint:

            x_direction=choice([1,-1])
            x_distance=choice([1,2,3,4,5,6,7,8,9,10])
            x_steps=x_distance*x_direction

            y_direction=choice([1,-1])
            y_distance=choice([1,2,3,4,5,6,7,8,9,10])
            y_steps=y_distance*y_direction

            if x_steps == 0 and y_steps == 0:
                continue

            x = self.x_value[-1] + x_steps
            y = self.y_value[-1] + y_steps
 
            self.x_value.append(x)
            self.y_value.append(y)

