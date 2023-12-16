#60.	Binary Search in Python.
def binary(arr,el):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==el:
            return mid
        elif arr[mid]<el:
            left= mid+1
        else:
            right=mid-1
    return -1
arr=[1,2,4,6,7]
el=7
result=binary(arr,el)
if result == -1:
    print("Element is not found in this array.")
else:
    print(f"{el} found at index {result}.")            