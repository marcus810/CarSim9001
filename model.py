from random import randint

class Car(object):

    def __init__(self):
        Car.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)


class Wheel(object):

    def __init__(self):
        Wheel.orientation = randint(0, 360)

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360

class Engine(object):

    def __init__(self):
        Engine.throttlePosition = 0
        Engine.theGearbox = Gearbox()
        Engine.currentRpm = 0
        Engine.consumptionConstant = 0.0025
        Engine.maxRpm = 100
        Engine.theTank = Tank()

    def updateModel(self, dt):
        if self.theTank.contents != 0:
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        else:
            self.currentRpm = 0



class Gearbox(object):

    def __init__(self):
        Gearbox.wheels = {"frontLeft": Wheel(), "frontRight": Wheel(), "rearLeft": Wheel(), "rearRight": Wheel()}
        Gearbox.currentGear = 0
        Gearbox.clutchEngaged = False
        Gearbox.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self):
        if self.currentGear == len(self.gears) - 1 or self.clutchEngaged == True:
            pass
        else:
            self.currentGear = self.currentGear + 1

    def shiftDown(self):
        if self.currentGear == 0 or self.clutchEngaged == True:
            pass
        else:
            self.currentGear = self.currentGear - 1

    def rotate(self, revolutions):
        if self.clutchEngaged == True:
            for key in self.wheels:
                self.wheels[key].rotate(revolutions * self.gears[self.currentGear])


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
