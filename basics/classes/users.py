class User():

    def __init__(self, first_name, last_name, age, status_in_love, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status_in_love = status_in_love
        self.job = job

    def describe_user(self):
        print(f"First name - {self.first_name}"
              f"\nLast name - {self.last_name}"
              f"\nAge - {self.age}"
              f"\nStatus in love - {self.status_in_love}"
              f"\nJob - {self.job}")

    def greet_user(self):
        print(f"\nHello, {self.first_name} {self.last_name}!")

def u(user):
    user.greet_user()
    user.describe_user()

user0 = User('Вася', 'Пупкин', 16, 'не женат', 'студент')
user0.greet_user()
user0.describe_user()

user1 = User('Серега', 'Макаров', 28, 'женат', 'грузчик')
user1.greet_user()
user1.describe_user()

user2 = User('Лена', 'Мирова', 23, 'замужем', 'программист')
u(user2)
