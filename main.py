from clCar import Car
from clHuman import Child


from openpyxl import load_workbook
from openpyxl.compat.numbers import NUMPY
import random
import math

# Reading an excel file using Python
import xlrd as xlr


def calculat_time_a_to_b(stop_a, stop_b):
    (x1, y1) = stop_a.split(',')
    (x2, y2) = stop_b.split(',')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = (int(x2), int(y2))
    temp = (x1 - x2)**2 + (y1 - y2)**2
    return math.sqrt(temp) * random.randrange(1, 2)


def calculat(child_a, child_b, car):
    time = calculat_time_a_to_b(child_a.address, child_b.address)
    print(time)
    cost = car.driver_cost + (car.cost_per_minute * time)
    return cost, time


# Give the location of the file
loc = "Worksheet.xlsx"


# To open Workbook
wb = load_workbook(loc)

ws = wb.worksheets[0]

for i in range(20):
    temp = "D" + str(i+2)
    (x, y) = random.randrange(-10, 10), random.randrange(-10, 10)
    ws[temp] = str(x) + ',' + str(y)

tmp = [ws.tables for ws in wb.worksheets]
tables = [{v.name:v} for t in tmp for v in t.values()]

for table in tables:
    if list(table.keys())[0] == 'Child':
        table['Child'].ref = 'A1:G21'

wb.save(loc)


wb = xlr.open_workbook(loc)
childs = wb.sheet_by_index(0)
cars = wb.sheet_by_index(2)

child_1 = Child(childs.cell_value(1, 0), childs.cell_value(1, 1), childs.cell_value(1, 2), childs.cell_value(1, 3),
                childs.cell_value(1, 4), childs.cell_value(1, 5), childs.cell_value(1, 6))

child_2 = Child(childs.cell_value(2, 0), childs.cell_value(2, 1), childs.cell_value(2, 2), childs.cell_value(2, 3),
                childs.cell_value(2, 4), childs.cell_value(2, 5), childs.cell_value(2, 6))

car_1 = Car(cars.cell_value(1, 0), cars.cell_value(1, 1), cars.cell_value(1, 2), cars.cell_value(1, 3),
            cars.cell_value(1, 4), cars.cell_value(1, 5))

print(calculat(child_1, child_2, car_1))
