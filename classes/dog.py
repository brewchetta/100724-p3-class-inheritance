from classes.mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, rested, is_good=True):
        super().__init__(name=name, rested=rested)
        self.is_good = is_good

    def __repr__(self):
        return f"Dog(name={self.name}, rested={self.rested}, is_good={self.is_good})"

    def make_sound(self):
        return "WOOF WOOF"

    def sleep(self):
        super().sleep()
        print("lil woof woof")

    def run_around(self):
        super().run_around()
        print("ZOINKS!")