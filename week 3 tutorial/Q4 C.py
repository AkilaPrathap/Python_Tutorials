# week 3 tutorial
# Question 4
# C

val =float(input("Enter the cost of the meal"))
print('''How satisfied are you with our servise
1... totally satisfied
2... sarisfied
3... dissarisfied''')
num=int(input())#input for satisfied level

# calculating tip.
if (num==1):
    print("your tip would be",val*(20/100))# tip = 20% of the total bill
elif (num==2):
    print("your tip woulb be", val*(15/100))# tip= 15% of the total  bill
elif (num==3):
    print("your tip would be", vaal*(10/100))# tip = 10% of the total bill
else:
    print("wrong value !!!")
    
