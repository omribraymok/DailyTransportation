# from clCar import Car
# from clHuman import Child
# from clHuman import Accompanier
# from openpyxl import workbook
from openpyxl import load_workbook

# import numpy as np
# import random
#
# # # Reading an excel file using Python
# # import xlrd as xlr
#
#
# def calculat_time_a_to_b(stop_a, stop_b):
#     return np.linalg.norm(stop_a - stop_b) * random.randrange(1, 1.5)
#
#
# def calculat(child_a, child_b, car, accompanier):
#     time = calculat_time_a_to_b(child_a.address, accompanier.address)
#     time += calculat_time_a_to_b(accompanier.address, child_b.address)
#     time += calculat_time_a_to_b(accompanier.address, child_b.address)
#     cost = car.driver_cost + (car.cost_per_minute * time)
#     return cost, time


# Give the location of the file
loc = "Worksheet.xlsx"

# To open Workbook
wb = load_workbook(loc)
childs = wb["Child"]
childs.cell(row=1, column=1).value = "ron"  # This will change the cell(1,1) to ron

# wb = xlr.open_workbook(loc)
# childs = wb.sheet_by_index(0)
# accompaniers = wb.sheet_by_index(1)
# cars = wb.sheet_by_index(2)
#
# child_1 = Child(childs.cell_value(1, 0), childs.cell_value(1, 1), childs.cell_value(1, 2), childs.cell_value(1, 3),
#                 childs.cell_value(1, 4), childs.cell_value(1, 5), childs.cell_value(1, 6))
# child_2 = Child(childs.cell_value(2, 0), childs.cell_value(2, 1), childs.cell_value(2, 2), childs.cell_value(1, 3),
#                 childs.cell_value(2, 4), childs.cell_value(2, 5), childs.cell_value(2, 6))
#
# accompanier_1 = Accompanier(accompaniers.cell_value(1, 0), accompaniers.cell_value(1, 1), accompaniers.cell_value(1, 2),
#                             accompaniers.cell_value(1, 3), accompaniers.cell_value(1, 4), accompaniers.cell_value(1, 5),
#                             accompaniers.cell_value(1, 6), accompaniers.cell_value(1, 7))
#
# car_1 = Car(cars.cell_value(1, 0), cars.cell_value(1, 1), cars.cell_value(1, 2), cars.cell_value(1, 3),
#             cars.cell_value(1, 4), cars.cell_value(1, 5))

# print(calculat(child_1, child_2, car_1, accompanier_1))
