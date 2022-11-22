class User():

    def __init__(self, first_name, last_name, age, status_in_love, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status_in_love = status_in_love
        self.job = job
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name - {self.first_name}"
              f"\nLast name - {self.last_name}"
              f"\nAge - {self.age}"
              f"\nStatus in love - {self.status_in_love}"
              f"\nJob - {self.job}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f'{self.login_attempts}')

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f'{self.login_attempts}')

def u(user):
    user.greet_user()
    user.describe_user()


user0 = User('Вася', 'Пупкин', 16, 'не женат', 'студент')
user0.greet_user()
user0.describe_user()

user0.increment_login_attempts()
user0.increment_login_attempts()
user0.reset_login_attempts()
print(f'{user0.login_attempts}')

user1 = User('Серега', 'Макаров', 28, 'женат', 'грузчик')
user1.greet_user()
user1.describe_user()

user2 = User('Лена', 'Мирова', 23, 'замужем', 'программист')
u(user2)


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



user_admin = Admin('Толя', 'Быков', 30, 'не женат', 'админ')
user_admin.greet_user()
user_admin.describe_user()
user_admin.privileges_admin.show_privileges()

