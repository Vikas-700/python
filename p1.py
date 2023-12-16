try:
    x=int(input("Enter Days:"))
    l1=[100]
    total=100
    for i in range(x-1):
        total+=100
        l1.append(total)
    print(l1)
    print("Total income:",sum(l1))    
except:
    print("Done!")    
    