class Car:

    num_of_cars = 0

    def __init__(self, ID, car_type, driver_cost, cost_per_minute, capacity, wheelchair, lift):
        self.ID = ID
        self.car_type = car_type
        self.driver_cost = driver_cost
        self.cost_per_minute = cost_per_minute
        self.capacity = capacity
        self.wheelchair = wheelchair
        self.lift = lift

        Car.num_of_cars += 1

    def calculate_cost(self, minutes):
        return self.cost_per_minute * minutes + self.driver_cost

    def wheelchair_option(self):
        return self.wheelchair
