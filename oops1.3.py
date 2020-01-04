class Outer:
    def __init__(self):
        print("Outer Class Oject Creation")
        return
    class Inner:
        def __init__(self):
            print("Inner Class Object Creation")
            return
        def m1(self):
            print("Inner Class Method")
            return

o=Outer()
i=o.Inner()
i.m1()
