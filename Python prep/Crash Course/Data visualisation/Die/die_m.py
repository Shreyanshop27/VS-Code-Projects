from random import choice

class Die:
    def __init__(self):
        self.nroll=10_000
        self.nside=6
        self.ndie=1
        self.f=[]#frequency
    
    def roll(self,nroll,nside,ndie):
        value=[]
        sides=list(range(1,nside+1))

        for _ in range (1,ndie+1):
            for _ in range (1,nroll+1):
                ran=choice(sides)
                self.f.append(ran)
        
        for side in sides:
            value.append(self.f.count(side))
        
        return value

        
        
