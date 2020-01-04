def tellFile():
    f=None
    try:
        f=open("abc.txt",'r')
        print(f.tell())

        print(f.read(2))
        print(f.tell())
        print(f.read(9))
        


    
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f.closed:
            print("File closed : ",f.closed)
            f.close()
        else:
            print("File closed : ",f.closed)
            print("File Closed with help of 'with' ")
        

    return

def seekFile():
    f=None
    try:
        f=open("abc.txt",'r')
        f.seek(1)
        print(f.tell())
        print(f.read(2))
      
    
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f.closed:
            print("File closed : ",f.closed)
            f.close()
        else:
            print("File closed : ",f.closed)
            print("File Closed with help of 'with' ")
        

    return




##tellFile()
seekFile()
        
        
        
