class Test:
    def __init__(self):
        print("constructor called")
        return
    def m1(self):
        print("m1 called  ",self)
        return

t1=Test()

print("t1 =",t1)

t1.m1()

t1=Test()

print("t1 =",t1)

t1.m1()

t2=Test()
print("t2 =",t2)


t1=Test()
print("t1 =",t1)

t1.m1()
