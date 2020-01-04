def withFile():
    f=None
    try:
        with open("abc.txt",'w') as f:
            f.write("nag")
            f.write("\n durga")
            print("File closed : ",f.closed)
        print("File closed : ",f.closed) 

    
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

withFile()

        
        
        
