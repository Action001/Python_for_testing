import random
from bus import Bus
import support_function

class SimpleGroundBus(Bus):


    def __init__(self):
        self.cost = 1_000_000
        self.capacity = 50 # people
        self.consumption = 15 # l/100km
        self.pilots = 1
        self.capacity_gas_tank = 70
        self.model = support_function.random_mark()
        self.number = random.randint(100, 1000)
        self.max_speed = 99 # km/h
        self.wheel = 4
        self.floors = 1
        super().__init__()

    def just_ride_very_slow(self):
        print("For a while we will crawl like turtles ...")

    def change_wheel(self):
        print("One of the wheels successfully replaced")

    def just_falling_apart(self):
        print("The bus starts to fall apart ... but don't be afraid of anything")

