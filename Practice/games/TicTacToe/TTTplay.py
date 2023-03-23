from TicTacToe import TTT
from random import choice

t=TTT()
print("""
Each key represent the 'O' place on Board
q | w | e 
a | s | d
z | x | c
after '->' enter the position hv
""")

keys=["q","w","e","a","s","d","z","x","c"]

while True:
    t.board()
    c=t.check()
    if c == 1:
        print("You lose")
        break
    elif c == 0 :
        print("You Win!!")
        break
    elif c == 2:
        pass
    
    user=input("->")
    if user in keys:
        keys.remove(user)
        t.place(letter=user,player="h")
        t.check()
    else:
        continue
    if len(keys) == 0:
        print("Draw")
        break
    comp=choice(keys)
    keys.remove(comp)
    t.place(letter=comp,player="c")
    

