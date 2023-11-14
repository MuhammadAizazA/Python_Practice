import copy
class Car:
    def __init__(self, make, model, year, color):
        if isinstance(make, Car):  # Check if the argument is a Car object
            # If it is, copy its attributes
            self.make = make.make
            self.model = make.model
            self.year = make.year
            self.color = make.color
        else:
            # If it's not a Car object, assume individual attributes are passed
            self.make = make
            self.model = model
            self.year = year
            self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def start(self):
        print("Starting the car...")
        self.started = True

    def stop(self):
        print("Stopping the car...")
        self.started = False
        
obj=Car(2001,2000,2001,'blue')
obj1 = copy.copy(obj)
print(obj1.color,obj1.make)