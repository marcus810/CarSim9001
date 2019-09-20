from random import randint

class Car(object):

    def __init__(self):
        Car.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)


class Wheel(object):

    def __init__(self):
        #Erklærer instansvariablen orientation og tildeler en tilfældig værdi mellem 0 og 360
        Wheel.orientation = randint(0, 360)

    def rotate(self, revolutions):
        #bruger en formel til at udregne en ny orientation ud fra antallet af revolutions
        self.orientation = (self.orientation + (revolutions * 360)) % 360

class Engine(object):

    def __init__(self):
        #Erklærer variabler
        Engine.throttlePosition = 0
        Engine.theGearbox = Gearbox()
        Engine.currentRpm = 0
        Engine.consumptionConstant = 0.0025
        Engine.maxRpm = 100
        Engine.theTank = Tank()

    def updateModel(self, dt):
        #hvis tanken ikke er tom...
        if self.theTank.contents != 0:
            #skal der udregnes en currentRpm ved at gange throttlePosition med
            #maxRpm
            self.currentRpm = self.throttlePosition * self.maxRpm
            #skal theTank.remove (remove metoden under klassen Tank.)
            #kaldes med currentRpm ganget med consumptionConstant som parameter
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            #skal theGearbox.rotate(rotate metoden under klassen Gearbox)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        else:
            #hvis tanken er tom skal currentRpm være 0
            self.currentRpm = 0



class Gearbox(object):

    def __init__(self):
        #Erklærer variabler
        Gearbox.wheels = {"frontLeft": Wheel(), "frontRight": Wheel(), "rearLeft": Wheel(), "rearRight": Wheel()}
        Gearbox.currentGear = 0
        Gearbox.clutchEngaged = False
        Gearbox.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self):
        #hvis currentGear er lig antallet af elementer i gears eller hvis
        #clutchEngaged er lig True skal intet ske.
        if self.currentGear == len(self.gears) - 1 or self.clutchEngaged == True:
            pass
        else:
            #hvis currentGear ikke er lig antallet af elementer i gears eller hvis
            #clutchEngaged ikke er lig True skal der lægges 1 til currentGear
            self.currentGear = self.currentGear + 1

    def shiftDown(self):
        #hvis currentGear er lig 0 eller clutchEngaged er true skal intet ske
        if self.currentGear == 0 or self.clutchEngaged == True:
            pass
        else:
            #hvis currentGear ikke er lig 0 eller clutchEngaged ikke er true
            #skal der trækkes en fra currentGear
            self.currentGear = self.currentGear - 1

    def rotate(self, revolutions):
        #hvis clutchEngaged er True skal der klades rotate() på alle instanser
        #af Wheel i wheels med revolutions ganget med værdien på index
        #currentGear i gears
        if self.clutchEngaged == True:
            for key in self.wheels:
                self.wheels[key].rotate(revolutions * self.gears[self.currentGear])


class Tank(object):

    def __init__(self):
        #Erklærer variable
        Tank.capacity = 100
        Tank.contents = 100

    def remove(self, amount):
        #opdatere contents så amount bliver trukket fra contents
        self.contents = self.contents - amount
        #hvis contents bliver mindre en 0...
        if self.contents < 0:
            #skal contents være lig 0 (dette sikre at contents aldirg bliver
            #mindre en 0)
            self.contents = 0


    def refuel(self):
        #opdatere contents til at være lig capacity
        self.contents = self.capacity
