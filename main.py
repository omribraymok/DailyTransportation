from clCar import Car
from clHuman import Child

# writing to excel file
from openpyxl import load_workbook
# Calculation of random points
import random
# Calculation of Euclidean distance
import math
# Reading an excel file
import xlrd as xlr


# Calculation of Euclidean distance ("time travel")
def calculat_time_a_to_b(stop_a, stop_b):
    (x1, y1) = stop_a.split(',')
    (x2, y2) = stop_b.split(',')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = (int(x2), int(y2))
    temp_var = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(temp_var) * random.randrange(1, 2)


# Calculation of time and cost
def calculat(child_a, child_b, car):
    time = calculat_time_a_to_b(child_a.address, child_b.address)
    cost = car.driver_cost + (car.cost_per_minute * time)
    return cost, time


# Give the location of the file
loc = "Worksheet.xlsx"

# To open Workbook
wb = load_workbook(loc)

# To open sheets
ws = wb.worksheets[0]

# Enter a random point to address column in Child table
for i in range(20):
    temp = "D" + str(i + 2)
    (x, y) = random.randrange(-10, 10), random.randrange(-10, 10)
    ws[temp] = str(x) + ',' + str(y)

# Increases thr  child table{
tmp = [ws.tables for ws in wb.worksheets]
tables = [{v.name: v} for t in tmp for v in t.values()]

for table in tables:
    if list(table.keys())[0] == 'Child':
        table['Child'].ref = 'A1:G21'
# }

wb.save(loc)

# Reading from excel file from child table anf insert to dictionary
wb = xlr.open_workbook(loc)
childs = wb.sheet_by_index(0)

child_dic = {}
for x in range(1, 21):
    child_dic[x - 1] = Child(childs.cell_value(x, 0), childs.cell_value(x, 1), childs.cell_value(x, 2),
                             childs.cell_value(x, 3), childs.cell_value(x, 4), childs.cell_value(x, 5),
                             childs.cell_value(x, 6))
# for x in range(0, 20):
#     print(child_dic[x])


# Reading from excel file from Car table
cars = wb.sheet_by_index(2)
car_1 = Car(cars.cell_value(1, 0), cars.cell_value(1, 1), cars.cell_value(1, 2), cars.cell_value(1, 3),
            cars.cell_value(1, 4), cars.cell_value(1, 5))

# child_dic_a = {}
# group_a = random.sample(list(child_dic), 7)
# for i in group_a:
#     child_dic_a = child_dic.pop(i)

# print("group_a:")
# for x in range(0, 6):
#     print(child_dic_a[x])
# print("group_b:")
# for x in range(0, 12):
#     print(child_dic[x])

print(calculat(child_dic[1], child_dic[2], car_1))
