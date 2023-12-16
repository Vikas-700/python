def fiboncci(n):
    if n<=1:
        return n
    else:
        return(fiboncci(n-1)+fiboncci(n-2))
last_term=int(input("How Many Trems:"))
        #for j in range(last_term):
    #sum=fiboncci(j)+j
   # print(sum)
for i in range(last_term):
    print(fiboncci(i))               


