from classes.mammal import Mammal

class Cat( Mammal ):

    def __init__(self, name, rested=True, lives_remaining=9):
        # passing from the cat class to the mammal class
        super().__init__(name, rested) 
        self.lives_remaining = lives_remaining

    
    def __repr__(self):
        # return f"Cat(name={self.name}, rested={self.rested}, live_remaining={self.lives_remaining})"
        return super().__repr__()[:-1] + f", lives_remaining={self.lives_remaining})"


    def make_sound(self):
        return "MEOWMEOWMEOWMEOW"
    

    def sleep(self):
        super().sleep()
        return f"{self.name}'s little paws are running in their sleep"