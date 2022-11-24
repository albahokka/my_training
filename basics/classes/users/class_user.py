"""Creating class"""
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