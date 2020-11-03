'''
    OOP Concepts
    --------------------------------------------------------
    What are?
        - class
        - properities/attributes
        - methods
            -constructor
        - objects/instances
        - self
    Inheritance
'''
# create a class
class Car(object):
    number_made = 0
    # magic
    def __init__(self, num_of_doors: int, fuel_type, sun_roof = False):
        # print(self)
        Car.number_made += 1
        self.doors = num_of_doors
        self.sun_roof = sun_roof
        self.fuel_type = fuel_type

    def move(self):
        pass

    def brake(self):
        pass

    def setWindows(self, num):
        self.windows = num
        return self

    def __str__(self):
        # print(super().__str__())
        return f'<Car object: Doors={self.doors}, Number made={Car.number_made}, Fuel Type={self.fuel_type}, Has Sunroof={self.sun_roof}>'


# instances of class
ford = Car('two', 'gas')
print(ford)
# print(ford)
# chevy = Car(4, True)
# chevy.setWindows(8).setWindows(4)
# print(chevy)



# print(type(ford))
# print(ford.window)
# print(type(''))