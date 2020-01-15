import csv
with open("emp.csv",'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['eno','ename','esal'])
    n=int(input("enter the number of employess: "))
    for x in range(n):
        eno=int(input("enter eno : "))
        ename=input("enter ename : ")
        esal=int(input("enter esal : "))
        w.writerow([eno,ename,esal])
    print("data written")  
