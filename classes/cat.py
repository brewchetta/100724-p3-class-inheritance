from classes.mammal import Mammal

class Cat():

    def __init__(self, name, rested):
        self.name = name
        self.rested = rested
    
    def __repr__(self):
        return f"Cat(name={self.name}, rested={self.rested})"
    
    def make_sound(self):
        return "MEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOW"
    
    def sleep(self):
        self.rested = True

    def run_around(self):
        self.rested = False