import random
class Die():

    def __init__(self, value):
        self.sides = value

    def roll_die(self, x):
        self.x = x
        self.y = self.sides
        print(random.randint(self.x, self.y))

def roll(die):
    i = 0
    while i < 10:
        i += 1
        die.roll_die(1)

die = Die(6)
print("*----------6-----------*")
roll(die)

die10 = Die(10)
print("*----------10-----------*")
roll(die10)

die20 = Die(20)
print("*----------20-----------*")
roll(die20)