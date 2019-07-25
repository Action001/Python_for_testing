import random
from bus import Bus
import support_function

class SuperModernGroundBus(Bus):


    def __init__(self):
        self.cost = 2_500_000
        self.capacity = 100 # people
        self.consumption = 20 # l/100km
        self.pilots = 2
        self.capacity_gas_tank = 100
        self.model = support_function.random_mark()
        self.number = random.randint(100, 1000)
        self.max_speed = 200 # km/h
        self.wheel = 8
        self.floors = 2
        super().__init__()

    def play_music(self):
        print("For a few minutes you can listen to RAMSHTAYN")

    def teleport(self):
        print("For a small fee, using advanced technology, teleports to the desired point")

