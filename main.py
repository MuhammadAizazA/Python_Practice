from circle import Circle
from person import Person
from crafts import FlyingCar
first_circle_object = Circle(10)
z = first_circle_object.calculate_area()
print(first_circle_object.radius, ' ', z)
second_circle_object = Circle(27)
x = second_circle_object.calculate_area()
print(second_circle_object.radius, ' ', x)


C3 = Circle(30)
C4 = Circle(48)
C5 = Circle(32)
C6 = Circle(23)

print(C3.num_instances, "-", C4.num_instances,
      "-", C5.num_instances, "-", C6.num_instances)

print(C3.instance_number, "-", C4.instance_number,
      "-", C5.instance_number, "-", C6.instance_number)

new_person=Person("Aizaz")
print(new_person.name)

FlyingCar_obj=FlyingCar('2001','2000','Mate white')

FlyingCar_obj.drive()

FlyingCar_obj.fly()

FlyingCar_obj.show_fuel()