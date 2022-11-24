"""Importing classes from the module"""
from class_user import User

class Priviliges():

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения",
                           "разрешено удалять пользователей",
                           "разрешено банить пользователей",
                           ]

    def show_privileges(self):
        print(f'Следующее может делать админ:')
        for p in self.privileges:
            print('- ' + p + ';')

class Admin(User):

    def __init__(self, first_name, last_name, age, status_in_love, job):
        super().__init__(first_name, last_name, age, status_in_love, job)
        self.privileges_admin = Priviliges()