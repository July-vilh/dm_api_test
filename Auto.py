class Auto:
    def __init__(self, mark, type):
        self.mark = mark
        self.type = type

    def drive(self):
        print(f'{self.mark} drive')

mini_couper = Auto(mark='mini_couper', type='sedan')
mini_couper.drive()

rzug = Auto(mark='rzug', type='sedan')
rzug.drive()