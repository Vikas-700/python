'''num=input("Enter any buttun:")
if num.isalpha():
    if num.isupper():
        print("You entur a upper case letter.")
    else:
        print("You enter a lower case letter.")
elif num.isdigit():
    print("you enput a digit.")
else:
    print("you enter a special charechter.") 
n=int(input("Enter number:"))                   
sum=0
for i in range(i,n+i):
    if i%2==0:
       sum+=i    
print("Total Sum=",sum)   
base=int(input("Enter the base."))
ex=int(input("Enter the Exponent."))
result=i
for i in range (ex):
    result*=base
    print(i)
print(result)    
def find_hcf(x,y):
    if x>y:
        lowest=y
    else:
        lowest=x    
    for i in range(1,lowest+1):
       if(x%i==0) and (y%i==0):
          hcf=i
    return hcf
numi=int(input("Enter first number"))
num2=int(input("Enter second number"))  
result=find_hcf(numi,num2)
print("HCF = ",result)  
num=int(input("Enter the last value."))
for i in range(num,0,-1):
    print(i)
for i in range(1,1001):
    if i%7==0 and i%5!=0:
        print(i)
char=input("Enter any character.")
ascii_value=ord(char)
print(ascii_value)
def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
num=int(input("Enter the number."))
fac=factorial(num)
print("Factorial is =",fac)  
arr1=[1,2,3,5,5,3]
set1=set(arr1)
for i in set1:
    num=arr1.count(i)
    print(i,"is",num,"time")
arr=[12,34,54,34,23,-12,3445]
for i in arr:
    if i>0:
       if i%2==0:
            print(i)
arr=[10,9,8,7,6,5,4,3,2,1]
len_arr=len(arr)
for i in range (len_arr):
     if i%2!=0:
          print("At",i,"is",arr[i-1])
def calculate_s_b(arr):
    l=s=arr[0]
    for i in arr:
        if i>l:
            l=i
        if i<s:
            s=i
    print("Largest is",l)
    print("smallest is",s)                
arr=[889,1,3,2,6,7,89,34,2]
calculate_s_b(arr)
arr=[1,35,8,9,0,6,78]
print(min(arr))
print(max(arr))
arr=[2,4,6,7,8,9,0,2]
print(sum(arr))
sum_all=0
for i in arr:
    sum_all+=i
print("Total sum is ",sum_all)
arr=['a','s','d','e','f','h','t','l','v','b','n','a']
print(arr)
arr.sort()
print(arr)  
s="eman ym si ramuk sakiv"
print(s)
s=s[::-1]
print(s)  
arr=["Hello","Sir"]
new_str=" ".join(arr)
print(new_str)
print(type(new_str))
a="Harshit"
b="Gangwar"
print(a+" "+b)
l1=['harshit','Bhuvnesh','vikas','vikas']
l1.append("Gangwar")
print(l1)
l1.remove("harshit")
print(l1)
l1.insert(0,"vikas")
print(l1)
index=l1.index("vikas")
l1.pop(index)
print(l1)
del(l1[1:3])
print(l1)
l1=[1,2,953,4,5,2,3,4,8,99,0]
minimum=min(l1)
maximum=max(l1)
print("Minimum  at",l1.index(minimum),"is",minimum)
print("Maximum  at",l1.index(maximum),"is",maximum)
l1=['vikas','Kumar']
l2=["from",'Bareilly']
print(l1+l2)
l1.extend(l2)
print(l1)
l1=[12,34,3,45,7,7,898,6,78,7677,67,7]
new_list=[]
for i in l1:
   if i%2!=0:
      new_list.append(i)
print(new_list)  
l1=["vikas","kumar","from","Bareily"]    
l1[0],l1[3]=l1[3],l1[0]
print(l1)
dist1={2:"Kumar",1:"vikas"}
dist1_sort=sorted(dist1.items())
print(dist1)
print(dist1_sort)
dist1={2:"Kumar",1:"vikas"}
dist2={3:"raj",4:"Rahul"}
new_dist={**dist1,**dist2}
print(new_dist)
t1=(90,2,3,5,65,45,4,2,0)
print(t1)
print("Size is",len(t1))
for i in range(5,0,-1):
    print("\n")
    for j in range(1,i+1):
        print(j,end=' ')'''
import numpy
arr=numpy.array([1,2,3,45,45])
print(arr)
