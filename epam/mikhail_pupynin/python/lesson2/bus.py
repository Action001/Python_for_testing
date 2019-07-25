import random
import support_function

class Bus:

    
    def __init__(self):
        self.color = support_function.random_color() # create a random color (red, green or blue)
        self.location = "park"
        self.condition = "not broken"

    def start_work(self):
        if self.location == "city":
            print("The bus already working!")
        else: self.location = "city"

    def finish_work(self):
        if self.location == "park":
            print("The bus already in the park!")
        else: self.location = "park"

    def break_it(self):
        if self.condition == "broke":
            print("Already broken, stop it!")
        else: self.condition = "broke"

    def fix_it(self):
        if self.condition == "not broken":
            print("Bus in perfect condition.")
        else: self.condition = "not broken"

