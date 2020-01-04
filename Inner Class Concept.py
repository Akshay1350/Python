class Outer:
    def __init__(self):
        print("Outer Class Oject Creation",id(self))
        return
    class Inner:
        def __init__(self):
            print("Inner Class Object Creation",id(self))
            return
        def m1(self):
            print("Inner Class Method",id(self))
            return

i=Outer().Inner()
i.m1()
