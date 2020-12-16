from clCar import Car
from clHuman import Child
from clSchool import School
from k_means import k_means
import global_variables as gv
# Reading and Writing from/to excel file
import openpyxl
# Calculation of random points
import random
import numpy as np


def divide_list_of_children_by_k_means(k):
    children_coordinates = []
    divide_list_of_children = []
    temp_list_of_children = []
    for i in gv.point_list:
        children_coordinates.append(list(i))
    children_coordinates.remove([0, 0])
    clusters = k_means(children_coordinates, k)
    for i in clusters:
        for j in i:
            (x1, y1) = j
            index = gv.point_list.index((x1, y1))
            temp = gv.list_of_all_children[index]
            temp_list_of_children.append(temp)
        new_list = temp_list_of_children.copy()
        divide_list_of_children.append(new_list)
        temp_list_of_children.clear()
    return divide_list_of_children


# Python function to get permutations of a given list
# https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
def permutation(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        m = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutation(remLst):
            l.append([m] + p)
    return l


# Break a list into chunks of size N
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]


# Enter a random point to address column in Child table
def enter_random_point(number, data_file):
    for t in range(number):
        temp = "D" + str(t + 2)
        (number_row, y) = random.randrange(-10, 10), random.randrange(-10, 10)
        child_sheet[temp] = str(number_row) + ',' + str(y)

    # Increases the  child table
    tmp = [ws.tables for ws in excel_file.worksheets]
    tables_in_sheet = [{v.name: v} for t in tmp for v in t.values()]

    for table in tables_in_sheet:
        if list(table.keys())[0] == 'Child':
            temp_str = 'A1:G' + str(t + 2)
            table['Child'].ref = temp_str

    excel_file.save(data_file)


# Function to print all the point and all the time to excel
def print_matrix_to_excel():
    # create workbook
    wb = openpyxl.Workbook()
    # get worksheet
    ws = wb.active
    # print the point on the first row
    for x in range(2, number_of_children + 3):
        # get a pointer for tab in table
        tab = ws.cell(row=x, column=1)
        # write in the tab
        tab.value = str(gv.point_list[x - 2])

    # print the point on the first row column
    r = 2  # for column use
    length = len(gv.list_of_all_children)
    for i in range(length):
        tab = ws.cell(row=1, column=r)
        r = r + 1
        # write in the tab
        tab.value = str(gv.list_of_all_children[i])
    # print the time travel matrix
    for x in range(2, number_of_children + 3):
        for y in range(2, number_of_children + 2):
            # get a pointer for tab in table
            tab = ws.cell(row=x, column=y)
            # write in the tab
            tab.value = str(gv.time_matrix[x - 2][y - 2])
    wb.save("matrix.xlsx")


# Creates an excel file for each group
# that contains the travel path, cost and travel time
def print_to_excel_time_cost_per_group(lst, car, cost, time):
    # create workbook
    wb = openpyxl.Workbook()
    # get worksheet
    ws = wb.active
    # # change sheet name
    # ws.title = "Group" + str(sheet_number)
    r = 1  # for column use
    length = len(lst)
    for t in range(length):
        # get a pointer for tab in table
        tab = ws.cell(row=1, column=r)
        r = r + 1
        # write in the tab
        tab.value = str(lst[t])

    tab = ws.cell(row=2, column=1)
    # write in the tab
    tab.value = "car id: " + str(car.ID)
    tab = ws.cell(row=3, column=1)
    # write in the tab
    tab.value = "cost: " + str(cost)
    tab = ws.cell(row=4, column=1)
    # write in the tab
    tab.value = "time: " + str(time)
    wb.save("Groups" + str(gv.file_number) + ".xlsx")


# For each group calculate the time and cost
# The function checks all possible path and choosing the shortest path
def calculate_time_cost_per_group(list_of_children, car, school_address):
    total_cost = car.driver_cost
    total_cost_temp_perm = car.driver_cost
    total_time = 0
    total_time_temp_perm = 0
    length = len(list_of_children)
    short_path = []
    flag = 0
    for temp_list_of_children in permutation(list_of_children):
        for i in range(length - 1):
            (cost, time) = car.calculate_cost_time(temp_list_of_children[i].address,
                                                   temp_list_of_children[i + 1].address)
            total_cost_temp_perm += cost
            total_time_temp_perm += time
        # calculate the time and cost for school
        (cost, time) = car.calculate_cost_time(temp_list_of_children[i + 1].address, school_address)
        total_cost_temp_perm += cost
        total_time_temp_perm += time
        if total_time_temp_perm < total_time or flag == 0:
            flag = 1
            short_path = temp_list_of_children
            total_time = total_time_temp_perm
            total_cost = total_cost_temp_perm
        total_cost_temp_perm = car.driver_cost
        total_time_temp_perm = 0

    print('group:' + str(gv.file_number))
    print_to_excel_time_cost_per_group(short_path, car, total_cost, total_time)


# Using openpyxl to writing to excel file
# Give the location of the file
data_file = "Worksheet.xlsx"

# To open Workbook
excel_file = openpyxl.load_workbook(data_file)

# To open sheets
child_sheet = excel_file.worksheets[0]

number_of_children = 21

enter_random_point(number_of_children, data_file)

# get data from excel file
for number_row in range(2, number_of_children + 2):
    gv.list_of_all_children.insert((number_row - 2), (Child(child_sheet, number_row)))

# Reading from excel file from Car table
cars_sheet = excel_file.worksheets[2]

# get cars data from data sheet
for number_row in range(2, 5):
    gv.list_of_cars.insert((number_row - 2), (Car(cars_sheet, number_row)))

# Reading from excel file from School table
schools_sheet = excel_file.worksheets[4]

for number_row in range(2, 3):
    gv.list_of_school.insert((number_row - 2), (School(schools_sheet, number_row)))

# Enter the school's address to the matrix
temp_point = gv.list_of_school[0].address
(x1, y1) = temp_point.split(',')
(x1, y1) = (int(x1), int(y1))
gv.point_list.insert(0, (x1, y1))

# Enter the children's address to the list
for number_row in range(0, number_of_children):
    temp_point = gv.list_of_all_children[number_row].address
    (x1, y1) = temp_point.split(',')
    (x1, y1) = (int(x1), int(y1))
    gv.point_list.insert(number_row, (x1, y1))

# Matrix 21X21, this matrix will contain all the time travel from point A (row0) to point B (column0)
gv.time_matrix = np.zeros((number_of_children + 1, number_of_children))

length = len(gv.list_of_all_children)
# Enter all the time travel
for i in range(length):
    for number_row in range(0, number_of_children + 1):
        gv.time_matrix[number_row, i] = Child.calculate_euclidean_dist(gv.list_of_all_children[i],
                                                                       gv.point_list[number_row])

print_matrix_to_excel()

print(gv.point_list)
# divide_list_of_children = list(divide_chunks(gv.list_of_all_children, int(number_of_children / 3)))
divide_list_of_children = divide_list_of_children_by_k_means(3)

length = len(divide_list_of_children)
for i in range(length):
    gv.file_number = i
    calculate_time_cost_per_group(divide_list_of_children[i], gv.list_of_cars[i], gv.list_of_school[0].address)
