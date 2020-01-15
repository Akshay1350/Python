import random
l=['sunny','priyanka','katrina','kareena']
while True:
    name=input("enter your name ")
    print("hello",name,"congratulation you are going to date:", random.choice(l))
    if name==input():
        break
    #print("congratulation you are going to date:", random.choice(l))
