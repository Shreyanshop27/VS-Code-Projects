import random

store=[]
words = [
    "science" ,"computer" , "lottery" , "laptop" , "hundred",
    "grand" , "shooter" , "cable" , "scissors" , "bagpack" ,
    "gymnast" , "players" , "motivation" , "potato" , "twilight"    
         ]
word=random.choice(words)
i=10
while i != 0:
    print("---",i,"chance left---")
    miss=""
    user=input(f"\nEnter the alphabet:- ")
    if user in word:
        i+=1

    store.append(user)
    for alphabet in word:
        if alphabet in store:
            miss+=alphabet
        else:
            miss+="_"
    i+= -1
    print(miss)
    if "_" not in miss:
        print("You Win!")
        break

if "_" not in miss:
    pass
else:
    print("You lose , The word is -",word)
