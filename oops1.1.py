class Student():
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
        return


    def talk(self):
        print("hello my name is :",self.name)
        print("my rollno is ",self.rollno)
        print("my marks is :",self.marks)
        return

class Access():
    def main():
        s=Student("durga",100,80)
        s.talk()
        return

Access.main()    
        
        
        
