num=input("Enter the number")
number=int(num)
sum=0

for x in range(number):
    if x%2 ==0 :
        sum+=x

print(sum)