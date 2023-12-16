#46.	Python Remove all occurrences a given element from the list.
list1=[1,2,3,2,4,6,7,2,8]
for item in list1:
    if item==2:
       list1.remove(2)
print(list1)