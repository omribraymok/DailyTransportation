from clCar import Car
from clHuman import Child
from clHuman import Accompanier


def calculat_time_a_to_b(stop_a, stop_b):
    return 30


def calculat(child_a, child_b, car, accompaniers):
    time = calculat_time_a_to_b(child_a.address, accompaniers.address)
    time += calculat_time_a_to_b(accompaniers.address, child_b.address)
    time += calculat_time_a_to_b(accompaniers.address, child_b.address)
    cost = car.driver_cost + (car.cost_per_minute * time)
    return cost, time


car_1 = Car(122, 'car', 25, 7, 3, False, False)

child_1 = Child("20396598", "Omri", "Braymok", "Gan-Nar,305", "0528401211", "003", "none")
child_2 = Child("20369574", "Matan", "Asulin", "Nesher,485", "0521111111", "003", "none")
accompanier_1 = Accompanier("203598746", "Hai", "Levi", "Haifa, 54", "0568942536", "none", "none", "none")

print(calculat(child_1, child_2, car_1, accompanier_1))
