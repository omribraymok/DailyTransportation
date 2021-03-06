
class Child:
    num_of_children = 0

    def __init__(self, ID, first_name, lest_name, address, contacts, id_school, special_needs):
        self.id = ID
        self.first_name = first_name
        self.lest_name = lest_name
        self.address = address
        self.contacts = contacts
        self.id_school = id_school
        self.spacial_needs = special_needs

        Child.num_of_children += 1

    # child's constructor from excel
    def __init__(self, child_sheet, number_row):
        cell_obj_id = child_sheet.cell(row=number_row, column=1)
        cell_obj_first_name = child_sheet.cell(row=number_row, column=2)
        cell_obj_lest_name = child_sheet.cell(row=number_row, column=3)
        cell_obj_address = child_sheet.cell(row=number_row, column=4)
        cell_obj_contacts = child_sheet.cell(row=number_row, column=5)
        cell_obj_id_school = child_sheet.cell(row=number_row, column=6)
        cell_obj_spacial_needs = child_sheet.cell(row=number_row, column=7)
        self.id = cell_obj_id.value
        self.first_name = cell_obj_first_name.value
        self.lest_name = cell_obj_lest_name.value
        self.address = cell_obj_address.value
        self.contacts = cell_obj_contacts.value
        self.id_school = cell_obj_id_school.value
        self.spacial_needs = cell_obj_spacial_needs.value

        Child.num_of_children += 1

    def __repr__(self):
        return "('{}', '{}', '{}', '{}')".format(self.id, self.first_name, self.lest_name, self.address)

    def __str__(self):
        return "({}, {} {}: {})".format(self.id, self.first_name, self.lest_name, self.address)
