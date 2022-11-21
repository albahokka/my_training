class Dog():

    def __init__(self, dog_name, dog_type):
        self.dog_name = dog_name
        self.dog_type = dog_type

    def sit(self):
        print(f'\n{self.dog_name.title()}, sit!')

    def roll_over(self):
        print(f'This {self.dog_type} dont love roll over.')

def d(dog):
    dog.sit()
    dog.roll_over()

dog0 = Dog('Santiago', 'poodle')
d(dog0)

dog1 = Dog('Millie', 'sheepdog')
d(dog1)