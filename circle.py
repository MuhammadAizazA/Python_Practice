import math

class Circle:
    num_instances = 0
    
    def __init__(self,radius):
        type(self).num_instances += 1
        self.instance_number=type(self).num_instances
        self.radius=radius

    def calculate_area(self):
        return round(math.pi * self.radius**2,2)