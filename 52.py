#52.	Python program to print positive or negative numbers in a list.
list1=[3,4,-3,5,-1,-4,4,9,30,-4,2]
l1=[]
l2=[]
for item in list1:
    if item>=0:
        l1.append(item)
    else:
        l2.append(item)  
print("Positive:",l1)  
print("Negative:",l2)
