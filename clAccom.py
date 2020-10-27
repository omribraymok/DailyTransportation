class Accompanier:

    number_of_accompaniers = 0

    def __init__(self, id, lest_name, first_name, contacts, preferences, history, special):
        self.id = id
        self.first_name = first_name
        self.lest_name = lest_name
        self.contacts = contacts
        self.preferences = preferences
        self.history = history
        self.special = special

        Accompanier.number_of_accompaniers += 1
