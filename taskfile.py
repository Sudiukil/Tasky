from collections import OrderedDict

from task import *

class taskfile:
    def __init__(self, path):
        self.path = path
        self.tasks = self.parse()

    def parse(self):
        tasks_file = open(self.path, "r")
        str_tasks = tasks_file.read().split("\n")[:-1]
        tasks_file.close()

        tasks = OrderedDict()

        for st in str_tasks:
            start = st.find("[")+1
            end = st.find("]", start)
            id = int(st[start:end])
            
            start = st.find(" ")+1
            end = len(st)
            name = st[start:end]

            t = task(id, name)

            tasks[id] = t

        return tasks

    def add(self, name):
        id = list(self.tasks)[-1]+1
        t = task(id, name)
        self.tasks[id] = t

        print("Task \"{}\" added (id: {})".format(name, id))

    def remove(self, ids):
        for str_id in ids:
            id = int(str_id)
            if id in self.tasks.keys():
                name = self.tasks[id].name
                del self.tasks[id]

                print("Task \"{}\" deleted (id: {})".format(name, id))


    def show(self):
        print("----- Tasks -----\n")
        print(self.__str__())
        print("----- ~ -----")

    def __str__(self):
        string = ""

        for k in self.tasks:
            string += str(self.tasks[k])
            string += "\n"

        return string

    def save(self):
        tasks_file = open(self.path, "w")
        tasks_file.write(self.__str__())
        tasks_file.close()
