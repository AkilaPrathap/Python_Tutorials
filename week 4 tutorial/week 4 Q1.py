import random


while True:
    hidden= random.randrange(1,20)
    guess=int(input("enter the gussed number"))
    if(hidden==guess):
        print(hidden,guess,"was correct")
        break
    else:
        print(hidden,guess,"is not correct")
        
