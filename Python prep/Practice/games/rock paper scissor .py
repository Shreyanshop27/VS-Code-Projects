import random as r 

# user and computer point
cp=0
up=0
while True:
    print(f"Computer-{cp}-------You-{up}")
    #take the user input
    user = input("Enter r p s \n-->")
    #computer choice
    options=["r","p","s"]
    comp=r.choice(options)
    ## print(comp)


    #if user take rock
    if user == "r":
        if comp == "r":
            pass
        elif comp == "p":
            cp+=1
        elif comp == "s":
            up += 1

    #if user take paper
    elif user == "p":
        if comp == "p":
            pass
        elif comp == "s":
            cp += 1
        elif comp == "r":
            up += 1

    #if user take scissor
    if user == "s":
        if comp == "s":
            pass
        elif comp == "r":
            cp += 1
        elif comp == "s":
            up += 1


