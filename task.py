class task:
    # Class constructor
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # Converts the task to a string
    def __str__(self):
        return("["+self.str_id()+"] "+self.name)

    # Prepends zeroes to the task id to make it a 3-digits string id
    def str_id(self):
        if self.id<10:
            return "00"+str(self.id)
        elif self.id>=10 and self.id<100:
            return "0"+str(self.id)
        else:
            return str(self.id)
