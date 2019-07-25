import random
from bus import Bus
import support_function

class FlyingBus(Bus):

    
    def __init__(self):
        self.cost = 5_000_000
        self.wings = 2
        self.capacity = 20 # people
        self.consumption = 27 # l/100km
        self.pilots = 3
        self.capacity_gas_tank = 150
        self.model = support_function.random_mark()
        self.number = random.randint(100, 1000)
        self.max_speed = 999 # km/h
        self.floors = 1
        super().__init__()

    def just_flying(self):
        print("For a while he really flew!")

    def nitro(self):
        print("Yes, he got accelerated :D")

