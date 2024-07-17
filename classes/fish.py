class Fish:

    all_fish = []

    @classmethod
    def num_fish(cls):
        return len(cls.all_fish)

    @classmethod
    def all_fish_names(cls):
        fish_names_list = []
        for fish in cls.all_fish:
            fish_names_list.append(f"name={fish.name}")
        return fish_names_list
    
    @classmethod
    def average_length(cls):
        sum_total = 0

        for fish in cls.all_fish:
            sum_total += fish.length_in_inches

        number_of_fishes = len(cls.all_fish)

        result = sum_total / number_of_fishes

        return result

    def __init__(self, name, length_in_inches):
        self.name = name
        self.length_in_inches = length_in_inches
        Fish.all_fish.append(self)

    def __repr__(self):
        return f"Fish(name={self.name}, length_in_inches={self.length_in_inches})"

    def make_bubbles(self):
        return "bloop bloop"


class Shark(Fish):
    
    all_fish = []

    def __init__(self, name, length_in_inches):
        super().__init__(name, length_in_inches)
        Shark.all_fish.append(self)