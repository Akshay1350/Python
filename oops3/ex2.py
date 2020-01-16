class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        return
    
    def __mul__(self,other):
        if self.name==other.name:
            return self.salary*other.days
        else:    
            return
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
        return
name=input("Enter employee name:")
sal=int(input("enter employee ssalary:"))
time=int(input("enter no: of days:"))
        
e=Employee(name,sal)
t=Timesheet(name,time)
sal=e*t
if sal!=None:
    print("this month salary=",sal)
else:
    print("name mismatch")
    

    
