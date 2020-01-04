def fileWrite():
    f=None
    try:
        f=open("abc.txt",'w')
        data=f.read()
        print("File ",f.name,"opened for ", f.mode,"operation ")
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
            print("File Closed")
    return

def fileWritePlus():
    f=None
    try:
        f=open("abc.txt",'w+')
        print("File ",f.name,"opened for ", f.mode,"operation ")
        print(data)
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
            print("File Closed")
    return

#fileWritePlus()

#fileWrite()

def fileWriteData():
    f=None
    try:
        f=open("abc.txt",'w')
        print("File ",f.name,"opened for ", f.mode,"operation ")
        f.write("Durga\n")
        f.write("Chethan\n")
##        data=f.read()
##        print(data)
       
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
            print("File Closed")
    return



def fileWriteAppend():
    f=None
    try:
        f=open("abc.txt",'a')
        print("File ",f.name,"opened for ", f.mode,"operation ")
        f.write("Durga\n")
        f.write("Chethan\n")
##        data=f.read()
##        print(data)
       
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
            print("File Closed")
    return


def fileWriteLine():
    f=None
    try:
        f=open("abc.txt",'a')
        print("File ",f.name,"opened for ", f.mode,"operation ")
        l=["durga","nagoor","narayan","mahesh","sriman"]
        f.writelines(l)
##        data=f.read()
##        print(data)
       
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
            print("File Closed")
    return
            
#fileWriteData()
#fileWriteAppend()
fileWriteLine()
        
        
        
