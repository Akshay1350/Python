#Function Definitions
def tryExceptBlock():
    print("akshay")
    try:
        print(10/0)
    except ZeroDivisionError:
        print(10/2)
    print("Chetan")
    return


def ExceptionMsg():
    try:
        print(10/0)
    except ZeroDivisionError as msg:
        print("exception raised and it's description is ",msg)
    return


def multipleExceptBlock():
    try:
        x=int(input("enter the first number:"))
        y=int(input("enter the second number:"))
        print(x/y)
    except ZeroDivisionError as msg:
        print("zero divison error :",msg)
    except:
        print("Default Except: Please enter valid value")
    return        


def finallyBlock():
    try:
        print("try1")
        print("try2",10/0)
        print("try3")
    except ValueError:
        print("except")
    finally:
        print("finally1")
    print("finally2")
    return
        
#Function Calls
n=0
while n<5: 
#tryExceptBlock()
#ExceptionMsg()

    #multipleExceptBlock()
    
    n=n+1

finallyBlock()




    
