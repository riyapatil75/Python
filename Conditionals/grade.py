marks=input("Whats your score ?")
grade=int(marks)

if grade>=101:
    print("Please veriffy your grade again")
    exit()
if grade >=90 :
    print("your grade is A")
elif grade >=80 :
    print("your grade is B")
elif grade >=70 :
    print("your grade is C")
elif grade >=60:
    print("your grade is D")
else :
    print("your grade is F")




