class School:

    def __init__(self, id, name, address, contacts, v_time):
        self.id = id
        self.name = name
        self.address = address
        self.contacts = contacts
        self.v_time = v_time

    # school's constructor from excel
    def __init__(self, schools_sheet, number_row):
        cell_obj_id = schools_sheet.cell(row=number_row, column=1)
        cell_obj_name = schools_sheet.cell(row=number_row, column=2)
        cell_obj_address = schools_sheet.cell(row=number_row, column=3)
        cell_obj_contacts = schools_sheet.cell(row=number_row, column=4)
        cell_obj_v_time = schools_sheet.cell(row=number_row, column=5)
        self.id = cell_obj_id.value
        self.name = cell_obj_name.value
        self.address = cell_obj_address.value
        self.contacts = cell_obj_contacts.value
        self.v_time = cell_obj_v_time.value

    def __repr__(self):
        return "('{}', '{}', '{}', '{}', '{}')".format(self.id, self.name, self.address, self.contacts,
                                                       self.v_time)
