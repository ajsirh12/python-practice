class Car:
    def __init__(self, name, engine, power, piston, wheel):
        self.name = name
        self.__engine = engine
        self.power = power
        self.piston = piston
        self.wheel  = wheel

    def get_engine(self):
        return self.__engine

    def set_engine(self, engine):
        self.__engine = engine

    def display(self):
        print(self.name, self.__engine, self.power, self.piston, self.wheel)

    def __del__(self):
        print('{} Object Deleted'.format(self.name))


carob1 = Car('bus', 1000, 600, 10, 50)
carob2 = Car('taxi', 500, 195, 4, 20)

print(carob1.get_engine())
carob1.set_engine(3000)
print(carob1.get_engine())

print(carob2.get_engine())
carob2.set_engine(300)
print(carob2.get_engine())

carList = []
carList.append(carob1)
carList.append(carob2)

for i in carList:
    i.display()