#Write a demo program for inheritance using super().

class Buy:
    def __init__(self, bike):

        self.bike = bike

    def printing(self):
        print(self.bike)


class Child(Buy):
    def __init__(self, bike):
        super().__init__(bike)


y = Child('FZ')
y.printing()
