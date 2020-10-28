class Human:

    def __init__(self, id, first_name, lest_name, address, contacts):
        self.id = id
        self.first_name = first_name
        self.lest_name = lest_name
        self.address = address
        self.contacts = contacts


class Child(Human):
    num_of_children = 0

    def __init__(self, id_school, special_needs):
        self.id_school = id_school
        self.spacial_needs = special_needs

        Child.num_of_children += 1


class Accompanier(Human):
    number_of_accompaniers = 0

    def __init__(self, preferences, history, special):
        self.preferences = preferences
        self.history = history
        self.special = special

        Accompanier.number_of_accompaniers += 1
