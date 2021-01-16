# Write a demo program for class & object, also with constructor.
class Buy:
    def __init__(self, car, bike, truck):
        self.car = car
        self.bike = bike
        self.truck = truck

    def printing(self):
        print(self.car)
        print(self.bike)
        print(self.truck)

x = Buy('Baleno', 'FZ', 'Cybertruck')
x.printing()

