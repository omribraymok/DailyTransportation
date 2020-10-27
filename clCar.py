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

    def calculate_cost(self, minutes):
        return self.cost_per_minute * minutes + self.driver_cost

    def wheelchair_option(self):
        return self.wheelchair

print(Car.num_of_cars)

car_1 = Car(123, 'minibus', 25, 14, 5, True)
car_2 = Car(122, 'car', 25, 7, 3, False)

print(car_1.calculate_cost(5))
print(car_2.calculate_cost(5))
print(Car.num_of_cars)

print(car_1.wheelchair_option())
