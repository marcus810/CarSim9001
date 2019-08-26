from random import randint

class Car(object):
    pass

class Wheel(object):

    pass

class Engine(object):
    pass

class Gearbox(object):
    pass

class Tank(object):

    def __init__(self):
        Tank.capacity = 100
        Tank.contents = 100

    def remove(self, amount):
        self.contents = self.contents - amount
        if self.contents < 0:
            self.contents = 0
        return self.contents


    def refuel(self):
        self.contents = self.capacity
        return self.contents
    pass
