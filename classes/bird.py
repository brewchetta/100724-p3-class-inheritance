class Bird:

    # my_class_attribute = "I AM A CLASS ATTRIBUTE"

    all_birds = []

    @classmethod
    def number_of_birds(cls):
        return len(cls.all_birds)

    def __init__(self, name):
        self.name = name
        Bird.all_birds.append(self)

    def __repr__(self):
        return f"Bird(name={self.name})"

    def tweet(self):
        return f"{self.name} is posting all their tweets... I mean X's"