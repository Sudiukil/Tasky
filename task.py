"""Task class definition"""

class Task:
    """Task class, representing a task"""
    def __init__(self, num, name):
        self.num = num
        self.name = name

    def __str__(self):
        return '['+self.str_num()+'] '+self.name

    def str_num(self):
        """Prepends zeroes to the task id to make it a 3-digits string id"""
        if self.num < 10:
            return '00'+str(self.num)
        elif self.num >= 10 and self.num < 100:
            return '0'+str(self.num)
        else:
            return str(self.num)
