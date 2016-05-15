class task:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return("["+self.str_id()+"] "+self.name)

    def str_id(self):
        if self.id<10:
            return "00"+str(self.id)
        elif self.id>=10 and self.id<100:
            return "0"+str(self.id)
        else:
            return str(self.id)
