class Vehicle:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def start(self):
        print("Starting the engine...")

    def stop(self):
        print("Stopping the engine...")

    def show_technical_specs(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        
    def show_fuel(self):
        print("300 Litters")

class Aircraft(Vehicle):
    def fly(self):
        print("Flying in the sky...")

    def show_fuel(self):
        print("300 Litters")

class Car(Vehicle):
    def drive(self):
        print("Driving on the road...")
        
    def show_fuel(self,value="car"):
        print("40 Litters ",value)



class FlyingCar(Aircraft,Car):
    pass