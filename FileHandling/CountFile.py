import os,sys
def countFile():
    fname=input("Enter file name ")
    
    if os.path.isfile(fname):
        print("File exists:",fname)
        f=open(fname,'r')
        lcount=ccount=wcount=0
        for x in f:
            lcount=lcount+1
            ccount=ccount + len(x)
            words=x.split()
            wcount=wcount+len(words)
        print("no: of lines : ",lcount)
        print("no: of characters : ",ccount)
        print("no: of words : ",wcount)


        
    else:
        print("file doesn't exist")
        sys.exit(0)
        


    return

countFile()
