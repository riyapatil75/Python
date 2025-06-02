items=["apple","banna]","orange","apple","mango"]

unique_item =set() #set do not involve duplicates

for i in items:
    if i in unique_item:
        print ("Duplicate:", i)
        break
    unique_item.add(i) #else statement