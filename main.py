# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з
# ними.

import time
import json

current_time = time.localtime()


class Tasks():
    def __init__(self, lst):
        self.lst = lst

    def get_tasks(self):
        return f"Tasks: {self.lst}"

    def add_tasks(self, filename='tasks.json'):
        number_of_tasks = int(input("How many tasks do you want to add? "))
        for i in range(number_of_tasks):
            task = input("Input task name: ")
            self.lst.append(task)

        dct = {"list_of_tasks": self.lst}
        with open(filename, 'w') as file:
            json.dump(dct, file)

    def del_tasks(self, filename='tasks.json'):
        number_of_tasks = int(input("How many tasks do you want to delete? "))
        for i in range(number_of_tasks):
            self.lst.pop()
        dct = {"list_of_tasks": self.lst}
        with open(filename, 'w') as file:
            json.dump(dct, file)

    def read_tasks(self, filename='tasks.json'):
        with open(filename, 'r') as file:
            dct = json.load(file)
        self.lst = dct['list_of_tasks']
        return self.lst


    def is_task_in_list(self, task):
        self.task = task
        if self.task in  self.lst:
            return True
        else:
            return False

tasks = Tasks(["task_1", "task_2", "task_3", "task_4"])
print(tasks.get_tasks())
tasks.add_tasks()
tasks.del_tasks()
print(tasks.read_tasks())
print(tasks.is_task_in_list("task_1"))
print(tasks.is_task_in_list("t"))















