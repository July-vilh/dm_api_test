class Human:
    def __init__(self, name, sex, years, height, weight):
        self.name = name
        self.sex = sex
        self.years = years
        self.height = height
        self.weight = weight

    # def walk(self):
    #     print(f'{self.name} walk')

    def run(self):
        if self.years > 3:
            return print(f'{self.name} run!')
        else:
            return print(f'{self.name} can not run!')

    # @staticmethod
    # def speak(word):
    #     print(word)

    # @classmethod
    # def birth(cls, name, sex, years, height, weight):
    #     return cls(name, sex, years, height, weight)
    #
    # def __repr__(self):
    #     return f'Human consists: name = {self.name}, sex = {self.sex}, years = {self.years}, height = {self.height}, weight = {self.weight}'



Yuliya = Human(name='Yuliya', sex='female', years=25, height=165, weight=45)
Vlad = Human(name='Vlad', sex='male', years=1, height=165, weight=60)
# Sirius = Human.birth(name='Sirius', sex='male', years=1, height=30, weight=5)
# print(Sirius)
# Yuliya.walk();

print(Yuliya.sex)

Vlad.run()
Yuliya.run()

# Yuliya.speak('I am Yulya')