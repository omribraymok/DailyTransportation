class Child:

    num_of_children = 0

    def __init__(self, id, first_name, lest_name, address, id_school, contacts, special_needs):
        self.id = id
        self.first_name = first_name
        self.lest_name = lest_name
        self.address = address
        self.id_school = id_school
        self.contacts = contacts
        self.spacial_needs = special_needs

        Child.num_of_children += 1

