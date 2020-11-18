from clCar import Car
from clHuman import Child
from clSchool import School

# Reading and Writing from/to excel file
import openpyxl
# Calculation of random points
import random
# Calculation of Euclidean distance;\\
import math


# Calculation of Euclidean distance ("time travel")
def calculate_euclidean_dist(stop_a, stop_b):
    (x1, y1) = stop_a.split(',')
    (x2, y2) = stop_b.split(',')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = (int(x2), int(y2))
    temp_var = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(temp_var) * random.uniform(1, 1.5)


# Calculation of time and cost
def calculate_time_cost(child_a, child_b, car):
    time_of_path = calculate_euclidean_dist(child_a.address, child_b.address)
    cost_of_path = car.driver_cost + (car.cost_per_minute * time_of_path)
    return cost_of_path, time_of_path


# Using openpyxl to writing to excel file
# Give the location of the file
data_file = "Worksheet.xlsx"

# To open Workbook
excel_file = openpyxl.load_workbook(data_file)

# To open sheets
child_sheet = excel_file.worksheets[0]

# Enter a random point to address column in Child table
for i in range(20):
    temp = "D" + str(i + 2)
    (x, y) = random.randrange(-10, 10), random.randrange(-10, 10)
    child_sheet[temp] = str(x) + ',' + str(y)

# Increases the  child table{
tmp = [ws.tables for ws in excel_file.worksheets]
tables_in_sheet = [{v.name: v} for t in tmp for v in t.values()]

for table in tables_in_sheet:
    if list(table.keys())[0] == 'Child':
        table['Child'].ref = 'A1:G21'
# }

excel_file.save(data_file)

dict_of_all_children = {}

# get data from excel file
for x in range(2, 22):
    cell_obj1 = child_sheet.cell(row=x, column=1)
    cell_obj2 = child_sheet.cell(row=x, column=2)
    cell_obj3 = child_sheet.cell(row=x, column=3)
    cell_obj4 = child_sheet.cell(row=x, column=4)
    cell_obj5 = child_sheet.cell(row=x, column=5)
    cell_obj6 = child_sheet.cell(row=x, column=6)
    cell_obj7 = child_sheet.cell(row=x, column=7)
    dict_of_all_children[x - 2] = Child(cell_obj1.value, cell_obj2.value, cell_obj3.value,
                                        cell_obj4.value, cell_obj5.value, cell_obj6.value,
                                        cell_obj7.value)
for x in range(0, 20):
    print(dict_of_all_children[x])

# Reading from excel file from Car table
cars = excel_file.worksheets[2]
dict_of_cars = {}
# get cars data from data sheet
for x in range(2, 5):
    cell_obj1 = cars.cell(row=x, column=1)
    cell_obj2 = cars.cell(row=x, column=2)
    cell_obj3 = cars.cell(row=x, column=3)
    cell_obj4 = cars.cell(row=x, column=4)
    cell_obj5 = cars.cell(row=x, column=5)
    cell_obj6 = cars.cell(row=x, column=6)
    dict_of_cars[x - 2] = Car(cell_obj1.value, cell_obj2.value, cell_obj3.value,
                              cell_obj4.value, cell_obj5.value, cell_obj6.value)
for x in range(0, 3):
    print(dict_of_cars[x])

# Reading from excel file from School table
schools = excel_file.worksheets[4]
dict_of_school = {}
for x in range(2, 3):
    cell_obj1 = schools.cell(row=x, column=1)
    cell_obj2 = schools.cell(row=x, column=2)
    cell_obj3 = schools.cell(row=x, column=3)
    cell_obj4 = schools.cell(row=x, column=4)
    cell_obj5 = schools.cell(row=x, column=5)
    dict_of_school[x - 2] = School(cell_obj1.value, cell_obj2.value, cell_obj3.value,
                                   cell_obj4.value, cell_obj5.value)
for x in range(0, 1):
    print(dict_of_school[x])


# print(calculat(child_dic[1], child_dic[2], car_1))


# this func will divide dictionary
def div_groups(dict_of_all: dict, num_of_parts: int):
    list_len: int = len(dict_of_all_children)
    return [dict(list(dict_of_all.items())[i * list_len // num_of_parts:(i + 1) * list_len // num_of_parts])
            for i in range(num_of_parts)]


# print res
for x in range(0, 20):
    print((div_groups(dict_of_all_children, 3)[x]))
