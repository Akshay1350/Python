def binaryReadWrite():
    f1=open("./Penguins.jpg",'rb')
    f2=open("./Koala.jpg",'wb')
    bytes=f1.read()
    print(type(bytes))
    f2.write(bytes)
    print("new image overwrittren as koala.jpg")
    return

binaryReadWrite()

