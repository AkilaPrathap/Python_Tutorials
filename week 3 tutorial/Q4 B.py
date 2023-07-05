# week 3 Tutorial
#question 4
#B

num1= int(input("Enter the first number"))
sym= str(input("Enter the operator"))
num2= int(input("Enter the second number"))

if (sym=="+"):
    print(num1,"+",num2,"=",num1+num2)
elif(sym=="-"):
    print(num1,"-",num2,"=",num1-num2)
elif(sym=="*"):
    print(num1,"*",num2,"=",num1*num2)
elif (sym=="/"):
    print(num1,"/",num2,"=",num1/num2)
else:
    print("invallied Symbol !!")
