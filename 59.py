#59.	Linear Search in Python.
def linear(arr,el):
    n=len(arr)
    for i in range(n):
        if arr[i]==el:
            return i
    return -1
array=[1,4,5,3,7,2,90,76,23,5,54]
element=54
result=linear(array,element)
if result == -1:
    print("Element is not found in this array.")
else:
    print(f"{element} Found at index {result}.")    