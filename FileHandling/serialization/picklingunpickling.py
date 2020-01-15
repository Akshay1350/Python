import pickle

class Car:
    def __init__(self,brand,model,color,fueltype):
        self.brand=brand
        self.model=model
        self.color=color
        self.fueltype=fueltype
        return
    
    def display(self):
        print("Car Details : ")
        print("Brand : ",self.brand)
        print("Model : ",self.model)
        print("Color : ",self.color)
        print("Fuel Type : ",self.fueltype)
        return


class Access:
    
    def pickling():
        with open("car1.dat","wb") as f:
            car1=Car("Hyundai","Santro","White","Petrol")
            pickle.dump(car1,f)
            print("Object car1 pickled to file car1.dat")
        return
    
    def unpickling():
        with open("car1.dat","rb") as f:
            #car1=Car("Hyundai","Santro","White","Petrol")
            car2=pickle.load(f)
            print("Object car2 loaded from car1.dat")
            car2.display()
        return

Access.unpickling()
            
    
