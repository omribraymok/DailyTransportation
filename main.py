from clCar import Car
from clHuman import Child
from clSchool import School

# Reading and Writing from/to excel file
import openpyxl
# Calculation of random points
import random
# Calculation of Euclidean distance
import math


# Calculation of Euclidean distance ("time travel")
def calculat_time_a_to_b(stop_a, stop_b):
    (x1, y1) = stop_a.split(',')
    (x2, y2) = stop_b.split(',')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = (int(x2), int(y2))
    temp_var = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(temp_var) * random.uniform(1, 1.5)


# Calculation of time and cost
def calculat(child_a, child_b, car):
    time = calculat_time_a_to_b(child_a.address, child_b.address)
    cost = car.driver_cost + (car.cost_per_minute * time)
    return cost, time


# Using openpyxl to writing to excel file
# Give the location of the file
loc = "Worksheet.xlsx"

# To open Workbook
excel_file = openpyxl.load_workbook(loc)

# To open sheets
child_sheet = excel_file.worksheets[0]

# Enter a random point to address column in Child table
for i in range(20):
    temp = "D" + str(i + 2)
    (x, y) = random.randrange(-10, 10), random.randrange(-10, 10)
    child_sheet[temp] = str(x) + ',' + str(y)

# Increases the  child table{
tmp = [ws.tables for ws in excel_file.worksheets]
tables = [{v.name: v} for t in tmp for v in t.values()]

for table in tables:
    if list(table.keys())[0] == 'Child':
        table['Child'].ref = 'A1:G21'
# }

excel_file.save(loc)

child_dic = {}
for x in range(2, 22):
    cell_obj1 = child_sheet.cell(row=x, column=1)
    cell_obj2 = child_sheet.cell(row=x, column=2)
    cell_obj3 = child_sheet.cell(row=x, column=3)
    cell_obj4 = child_sheet.cell(row=x, column=4)
    cell_obj5 = child_sheet.cell(row=x, column=5)
    cell_obj6 = child_sheet.cell(row=x, column=6)
    cell_obj7 = child_sheet.cell(row=x, column=7)
    child_dic[x - 2] = Child(cell_obj1.value, cell_obj2.value, cell_obj3.value,
                             cell_obj4.value, cell_obj5.value, cell_obj6.value,
                             cell_obj7.value)
for x in range(0, 20):
    print(child_dic[x])

# Reading from excel file from Car table
cars = excel_file.worksheets[2]
car_dic = {}
for x in range(2, 5):
    cell_obj1 = cars.cell(row=x, column=1)
    cell_obj2 = cars.cell(row=x, column=2)
    cell_obj3 = cars.cell(row=x, column=3)
    cell_obj4 = cars.cell(row=x, column=4)
    cell_obj5 = cars.cell(row=x, column=5)
    cell_obj6 = cars.cell(row=x, column=6)
    car_dic[x - 2] = Car(cell_obj1.value, cell_obj2.value, cell_obj3.value,
                         cell_obj4.value, cell_obj5.value, cell_obj6.value)
for x in range(0, 3):
    print(car_dic[x])

# Reading from excel file from School table
schools = excel_file.worksheets[4]
schools_dic = {}
for x in range(2, 3):
    cell_obj1 = schools.cell(row=x, column=1)
    cell_obj2 = schools.cell(row=x, column=2)
    cell_obj3 = schools.cell(row=x, column=3)
    cell_obj4 = schools.cell(row=x, column=4)
    cell_obj5 = schools.cell(row=x, column=5)
    schools_dic[x - 2] = School(cell_obj1.value, cell_obj2.value, cell_obj3.value,
                                cell_obj4.value, cell_obj5.value)
for x in range(0, 1):
    print(schools_dic[x])

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

# print(calculat(child_dic[1], child_dic[2], car_1))
