class Car:

    num_of_cars = 0

    def __init__(self, id, car_type, driver_cost, cost_per_minute, capacity, wheelchair):
        self.id = id
        self.car_type = car_type
        self.driver_cost = driver_cost
        self.cost_per_minute = cost_per_minute
        self.capacity = capacity
        self.wheelchair = wheelchair

        Car.num_of_cars += 1

    def calculat_cost(self, minutes):
        return self.cost_per_minute * minutes + self.driver_cost

print(Car.num_of_cars)

car_1 = Car(123, 'minibus', 25, 14, 5, 'yes')
car_2 = Car(122, 'car', 25, 7, 3, 'no')

print(car_1.calculat_cost(5))
print(car_2.calculat_cost(5))
print(Car.num_of_cars)
