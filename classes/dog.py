from classes.mammal import Mammal

class Dog( Mammal ):

    def __init__(self, name, rested, is_good=True):
        super().__init__(name, rested)
        self.is_good = is_good

    def __repr__(self):
        return super().__repr__()[:-1] + f", {self.name} is a good dog={self.is_good})"
    
    def make_sound(self):
        return "BARK BARK BARK"
    
    def sleep(self):
        super().sleep()
        return f"I am a well rested dog, {self.rested}"

    def run_around(self):
        super().run_around()
        return f"{self.name} is chasing his own tail"