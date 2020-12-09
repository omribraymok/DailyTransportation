import global_variables as gv


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

    # Calculation of time and cost
    def calculate_cost_time(self, address_1, address_2):
        time_of_path = find_time_travel_in_matrix(address_1, address_2)
        cost_of_path = self.cost_per_minute * time_of_path
        return cost_of_path, time_of_path


# Finding the time travel from starting point to ending point in the time matrix
def find_time_travel_in_matrix(start_point, end_point):
    (x1, y1) = start_point.split(',')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = end_point.split(',')
    (x2, y2) = (int(x2), int(y2))
    number_in_a_row = gv.point_list.index((x1, y1))
    number_in_a_col = gv.point_list.index((x2, y2))
    # ################################################
    # print("\ntime travel from " + start_point + " to " + end_point + ":")
    # print(number_in_a_row, number_in_a_col, gv.time_matrix[number_in_a_col][number_in_a_row])
    # ################################################
    return gv.time_matrix[number_in_a_col][number_in_a_row]
