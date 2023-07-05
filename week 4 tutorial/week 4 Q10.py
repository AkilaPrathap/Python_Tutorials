#importing randon operator
import random
# code
count=0
for i in range (0,100):
    role1=random.randrange(1,6)#simulate first dice role
    role2=random.randrange(1,6)#simukate second dice role
    if (role1==role2):
        count=count+1

print("OUT of 100 you roled",count,"doubles")
