from clCar import Car
from clHuman import Child

print(Car.num_of_cars)

car_1 = Car(123, 'minibus', 25, 14, 5, True, True)
car_2 = Car(122, 'car', 25, 7, 3, False, False)

print(car_1.calculate_cost(5))
print(car_2.calculate_cost(5))
print(Car.num_of_cars)

print(car_1.wheelchair_option())

child_1 = Child("20396598", "omri", "braymok", "Gan-Nar,305", "0528401211", "003", "none")

print(child_1)