class Car:
    num_of_cars = 0

    def __init__(self, ID, car_type, driver_cost, cost_per_minute, capacity, wheelchair):
        self.ID = ID
        self.car_type = car_type
        self.driver_cost = driver_cost
        self.cost_per_minute = cost_per_minute
        self.capacity = capacity
        self.wheelchair = wheelchair

        Car.num_of_cars += 1

    # car's constructor from excel
    def __init__(self, cars_sheet, number_row):
        cell_obj_id = cars_sheet.cell(row=number_row, column=1)
        cell_obj_car_type = cars_sheet.cell(row=number_row, column=2)
        cell_obj_driver_cost = cars_sheet.cell(row=number_row, column=3)
        cell_obj_cost_per_minute = cars_sheet.cell(row=number_row, column=4)
        cell_obj_capacity = cars_sheet.cell(row=number_row, column=5)
        cell_obj_wheelchair = cars_sheet.cell(row=number_row, column=6)
        self.ID = cell_obj_id.value
        self.car_type = cell_obj_car_type.value
        self.driver_cost = cell_obj_driver_cost.value
        self.cost_per_minute = cell_obj_cost_per_minute.value
        self.capacity = cell_obj_capacity.value
        self.wheelchair = cell_obj_wheelchair.value

        Car.num_of_cars += 1

    def __repr__(self):
        return "('{}', '{}', '{}', '{}')".format(self.ID, self.car_type, self.driver_cost, self.cost_per_minute,
                                                 self.capacity, self.wheelchair)

    def calculate_cost(self, minutes):
        return self.cost_per_minute * minutes + self.driver_cost

    def wheelchair_option(self):
        return self.wheelchair
