import os,sys,Read as r,imp
def checkFile():
    fname=input("Enter file name ")
    
    if os.path.isfile(fname):
        print("File exists:",fname)
        imp.reload(r)
        r.fileRead(fname)
    else:
        print("file doesn't exist")
        sys.exit(0)


    return

checkFile()
        
        
        
