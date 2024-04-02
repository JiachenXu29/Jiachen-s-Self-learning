import random

class Hat:

    house = ["A","B","C","D"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.house))     

Hat.sort("Harry")
