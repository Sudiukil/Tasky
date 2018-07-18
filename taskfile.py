"""Taskfile class definition"""

from collections import OrderedDict
from task import Task

class Taskfile:
    """Taskfile class, represents a set of tasks to be saved in a file"""
    def __init__(self, path):
        self.path = path
        self.tasks = self.parse()

    def __str__(self):
        """Converts the task list to a string"""
        string = ''

        for k in self.tasks:
            string += str(self.tasks[k])
            string += '\n'

        return string

    def parse(self):
        """Reads and parses the task list file"""
        try:
            tasks_file = open(self.path, 'r')
        except IOError:
            tasks_file = open(self.path, 'w')
            tasks_file.close()
            tasks_file = open(self.path, 'r')

        str_tasks = tasks_file.read().split('\n')[:-1]
        tasks_file.close()

        tasks = OrderedDict()

        for task_str in str_tasks:
            start = task_str.find('[')+1
            end = task_str.find(']', start)
            task_id = int(task_str[start:end])

            start = task_str.find(' ')+1
            end = len(task_str)
            name = task_str[start:end]

            tasks[task_id] = Task(task_id, name)

        return tasks

    def add(self, name):
        """Adds a task to the task list"""
        if len(self.tasks) > 0:
            task_id = list(self.tasks)[-1]+1
        else:
            task_id = 1

        self.tasks[task_id] = Task(task_id, name)

        print('Task "{}" added (task_id: {})'.format(name, task_id))

    def remove(self, ids):
        """Removes one or many tasks from the task list"""
        for task_id in ids:
            if task_id in self.tasks.keys():
                name = self.tasks[task_id].name
                del self.tasks[task_id]
                print('Task "{}" deleted (task_id: {})'.format(name, task_id))
            else:
                print('No task with task_id = {}'.format(task_id))

    def rename(self, task_id, name):
        """Renames a task"""
        task_id = int(task_id)
        if task_id in self.tasks.keys():
            old_name = self.tasks[task_id].name
            self.tasks[task_id].name = name

        print('Task "{}" renamed to "{}" (task_id: {})'.format(old_name, name, task_id))

    def show(self):
        """Shows the task list"""
        print('----- Tasks -----\n')
        print(self.__str__())
        print('----- ~ -----')

    def save(self):
        """Saves the task list to file"""
        tasks_file = open(self.path, 'w')
        tasks_file.write(self.__str__())
        tasks_file.close()
