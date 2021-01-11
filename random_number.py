import openpyxl
import random


# Enter a random point to address column in Child table
def _enter_random_point(number, data_file):
    for t in range(number):
        temp = "D" + str(t + 2)
        (number_row, y) = random.uniform(-10, 10), random.uniform(-10, 10)
        (number_row, y) = (round(number_row, 2), round(y, 2))
        child_sheet[temp] = str(number_row) + ',' + str(y)

    # Increases the  child table
    tmp = [ws.tables for ws in excel_file.worksheets]
    tables_in_sheet = [{v.name: v} for t in tmp for v in t.values()]

    for table in tables_in_sheet:
        if list(table.keys())[0] == 'Child':
            temp_str = 'A1:G' + str(t + 2)
            table['Child'].ref = temp_str

    excel_file.save(data_file)


# Using openpyxl to writing to excel file
# Give the location of the file
data_file = "Worksheet.xlsx"

# To open Workbook
excel_file = openpyxl.load_workbook(data_file)

# To open sheets
child_sheet = excel_file.worksheets[0]

number_of_children = 21

_enter_random_point(number_of_children, data_file)
