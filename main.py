from clCar import Car
from clHuman import Child
from clSchool import School

# Reading and Writing from/to excel file
import openpyxl
# Calculation of random points
import random
# Calculation of Euclidean distance
import math
import numpy as np


# Function to print all the point and all the time to excel
def print_matrix_to_excel(point_list_fun, time_matrix_fun):
    # create workbook
    wb = openpyxl.Workbook()
    # get worksheet
    ws = wb.active
    # print the point on the first row and column
    for x in range(2, 23):
        # get a pointer for tab in table
        tab = ws.cell(row=x, column=1)
        # write in the tab
        tab.value = str(point_list_fun[x - 2])
        tab = ws.cell(row=1, column=x)
        # write in the tab
        tab.value = str(point_list_fun[x - 2])
    # print the time travel matrix
    for x in range(2, 23):
        for y in range(2, 23):
            # get a pointer for tab in table
            tab = ws.cell(row=x, column=y)
            # write in the tab
            tab.value = str(time_matrix_fun[x - 2][y - 2])
    wb.save("matrix.xlsx")


# Calculation of Euclidean distance ("time travel")
def calculate_euclidean_dist(point_a, point_b):
    (x_1, y_1) = point_a
    (x_2, y_2) = point_b
    temp_var = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2
    return math.sqrt(temp_var) * random.uniform(1, 1.5)


# Calculation of time and cost
def find_time_travel_in_matrix(start_point, end_point):
    (x1, y1) = start_point.split(',')
    (x1, y1) = (int(x1), int(y1))
    (x2, y2) = end_point.split(',')
    (x2, y2) = (int(x2), int(y2))
    number_in_a_row = point_list.index((x1, y1))
    number_in_a_col = point_list.index((x2, y2))
    print("\ntime travel from " + start_point + " to " + end_point + ":")
    print(number_in_a_row, number_in_a_col, time_matrix[number_in_a_col][number_in_a_row])
    return time_matrix[number_in_a_col][number_in_a_row]


def calculate_cost_time(child_a, child_b, car):
    time_of_path = find_time_travel_in_matrix(child_a.address, child_b.address)
    cost_of_path = car.cost_per_minute * time_of_path
    return cost_of_path, time_of_path


file_number = 0


def print_to_excel(dic, car, cost, time):
    # create workbook
    wb = openpyxl.Workbook()
    # get worksheet
    ws = wb.active
    # # change sheet name
    # ws.title = "Group" + str(sheet_number)
    # for column use
    r = 1
    for t in dic:
        # get a pointer for tab in table
        tab = ws.cell(row=1, column=r)
        r = r + 1
        # write in the tab
        tab.value = str(dic[t])

    tab = ws.cell(row=2, column=1)
    # write in the tab
    tab.value = "car id: " + str(car.ID)
    tab = ws.cell(row=3, column=1)
    # write in the tab
    tab.value = "cost: " + str(cost)
    tab = ws.cell(row=4, column=1)
    # write in the tab
    tab.value = "time: " + str(time)
    wb.save("Groups" + str(file_number) + ".xlsx")


def calculate_time_cost_per_group(dic_of_children, car):
    total_cost = car.driver_cost
    total_time = 0
    for key in dic_of_children:
        # to break when loop get to the obj before the lest one
        if key == ((len(dic_of_children) - 1) * (file_number + 1)):
            break
        (cost, time) = calculate_cost_time(dic_of_children[key], dic_of_children[key + 1], car)
        total_cost += cost
        total_time += time
    print_to_excel(dic_of_children, car, total_cost, total_time)


# Using openpyxl to writing to excel file
# Give the location of the file
data_file = "Worksheet.xlsx"

# To open Workbook
excel_file = openpyxl.load_workbook(data_file)

# To open sheets
child_sheet = excel_file.worksheets[0]

# Enter a random point to address column in Child table
for x in range(20):
    temp = "D" + str(x + 2)
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

# This list will contain the school address and all children address
point_list = []
# Enter the school's address to the matrix
temp_point = dict_of_school[0].address
(x1, y1) = temp_point.split(',')
(x1, y1) = (int(x1), int(y1))
point_list.insert(0, (x1, y1))
# Enter the children's address to the list
for x in range(0, 20):
    temp_point = dict_of_all_children[x].address
    (x1, y1) = temp_point.split(',')
    (x1, y1) = (int(x1), int(y1))
    point_list.insert(x, (x1, y1))
# Matrix 21X21, this matrix will contain all the time travel from point A (row0) to point B (column0)
time_matrix = np.zeros((21, 21))
# Enter all the time travel
for x in range(0, 21):
    for y in range(0, 21):
        time_matrix[x, y] = calculate_euclidean_dist(point_list[y], point_list[x])

print_matrix_to_excel(point_list, time_matrix)


# this func will divide dictionary
def div_groups(dict_of_all: dict, num_of_parts: int):
    list_len: int = len(dict_of_all_children)
    return [dict(list(dict_of_all.items())[k * list_len // num_of_parts:(k + 1) * list_len // num_of_parts])
            for k in range(num_of_parts)]


# print res
for x in range(0, 3):
    temp = div_groups(dict_of_all_children, 3)[x]
    file_number = x
    calculate_time_cost_per_group(temp, dict_of_cars[x])
