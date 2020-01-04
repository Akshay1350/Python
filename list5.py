n=[10,9,65,35,23]
y=n[:]
y[1]='777'
print(id(n))
print(id(y))
print(n)
print(y)

