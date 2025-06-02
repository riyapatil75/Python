num=input("Enter any number to get its factorial ")
number=int(num)
fact=1
while number>0:
    fact=fact*number
    number = number-1  

print(fact)