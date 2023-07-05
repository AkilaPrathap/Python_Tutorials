# week 3 tutorial

#Question 4
#A

print('''1... Convert from Celsuis to Fahrenheit
2... Convert from Fahrenheute to Celsius''')
num=int(input())

if (num==1):
    temp=int(input("Enter the temperature"))
    print("temperature in Fahrenhit is = ",(temp*1.8)+32)
    
elif (num==2):
    temp=int(input("Enter the temperature"))
    print("temperature in Celsius is = ",(temp-32)/1.8)
else:
    print("Wrong choice")

    
