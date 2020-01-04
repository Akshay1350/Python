class Student:
    def __init__(self):
        self.name='durga'
        self.age=40
        self.marks=80
        return


    def talk(self):
        print("Hello I am :  ",self.name)
        print("My Age is  : ",self.age)
        print("My Marks is : ",self.marks)
        return


class Access():
    def main():
        obj=Student()
        obj.talk()
        print("%d",obj)
        return

Access.main()
