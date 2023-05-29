# Task 1 class Car

class Car(object):

    def __init__(self, mark, color, engine):
        self.mark = mark
        self.color = color
        self.engine = engine

    def move_forward(self):
        return print('Car is moving forward ...')

    def move_back(self):
        return print('Car is moving back ...')

class SuperCar(Car):

    def turn_left(self):
        return print('Car is turning to the left ...')

    def turn_right(self):
        return print('Car is turning to the left ...')

bmw = SuperCar('BMW', 'Black', 4)

print(bmw.mark)
print(bmw.move_forward())