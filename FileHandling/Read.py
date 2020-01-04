def fileRead(fname):
    f=None
    try:
        f=open(fname,'r')
        data=f.read()
        print("File ",f.name,"opened for ", f.mode,"operation ")
        print(data)
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
    return

def fileReadPlus():
    f=None
    try:
        f=open("abc.txt",'r+')
        print("File opened for read operation ",f.name)
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
    return

def fileReadChar():
    f=None
    try:
        f=open("abc.txt",'r')
        data=f.read(10)
        print("File ",f.name,"opened for ", f.mode,"operation ")
        print(data)
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
    return

def fileReadLine():
    f=None
    try:
        f=open("abc.txt",'r')
        data=f.readline()
        print("File ",f.name,"opened for ", f.mode,"operation ")
        print(data)
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
    return


def fileReadLines():
    f=None
    try:
        f=open("abc.txt",'r')
        data=f.readlines()
        print("File ",f.name,"opened for ", f.mode,"operation ")
        print(data)
    except Exception as msg:
        print("Exception : ",msg)
    finally:
        if not f==None:
            f.close()
    return
#fileReadPlus()

#fileRead()
##fileReadChar()
##fileReadLine()
#fileReadLines()   
        
        
        
        
