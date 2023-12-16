def linearsearch(arr,element):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==el:
            return mid
        elif arr[mid]>el:
            r=mid-1
        else:
            l=mid+1    
    return -1        
arr=input("Enter element with space.")
arr=[int(arr) for arr in arr.split()]
el=int(input("Enter that element you want do find in this array."))
result=linearsearch(arr,el)
if result==-1:
    print("element is not found")
else:
    print(f"{el} is find at index{result}")
