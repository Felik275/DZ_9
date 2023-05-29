#Task 3

class Parallelogram(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_area(self):
        return print(self.width * self.length)

class Square(Parallelogram):
    def get_area(self):
        return print(self.width * self.width)