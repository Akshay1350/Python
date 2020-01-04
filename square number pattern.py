while True:
    n=int(input("enter value of n:"))

    if n==0:
        break
    else:
        for i in range(n):
            print((str(i+1)+ " ")*n)
                
