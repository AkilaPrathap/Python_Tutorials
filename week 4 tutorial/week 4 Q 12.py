import random



hidden= random.randrange(1,20)

for i in range (5):
    guess=int(input("enter the gussed number"))
    if(hidden==guess):
        print(hidden,guess,"was correct")
        break
    else:
        print("is not correct try again")
        
