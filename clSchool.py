class School:

    def __init__(self, id, name, address, contacts, v_time):
        self.id = id
        self.name = name
        self.address = address
        self.contacts = contacts
        self.v_time = v_time

    def __repr__(self):
        return "('{}', '{}', '{}', '{}', '{}')".format(self.id, self.name, self.address, self.contacts,
                                                       self.v_time)
