total = 0
count = 0
while True:
    num=float(input("Enter a number"))
    if (num==-19):
        print("everage",int(total/count),"%")
        break
    else:
        total=total+num
        count+=1
    
