from flying_bus import FlyingBus
from simple_ground_bus import SimpleGroundBus
from super_modern_ground_bus import SuperModernGroundBus 

class CreateAutopark:
    """Hi! It's my autopark ^_^"""
    
    def __init__(self, count_fly, count_simple, count_modern):
        self.g = globals()
        self.names = []
        self.count_fly = count_fly
        self.count_simple = count_simple
        self.count_modern = count_modern
        for i in range(self.count_fly):
            name = 'fly_{}'.format(i)
            self.g[name] = FlyingBus()
            self.names.append(name)
        for i in range(self.count_simple):
            name = 'simple_{}'.format(i)
            self.g[name] = SimpleGroundBus()
            self.names.append(name)
        for i in range(self.count_modern):
            name = 'modern_{}'.format(i)
            self.g[name] = SuperModernGroundBus()
            self.names.append(name)

    def get_autopark_cost(self):
        summ = 0
        for name in self.names:
            summ += self.g[name].cost
        return summ

    def sort_by_consumption(self):
        all_consumption = []
        for name in self.names:
            all_consumption.append(self.g[name].consumption)
        all_consumption = list(set(all_consumption)) # kill dub
        all_consumption.sort() 
        print("\tModel\tNumber\tConsumption\n")
        for con in all_consumption:
            for name in self.names:
                if con == self.g[name].consumption:
                    print("\t{0}\t{1}\t{2}".format(
                        self.g[name].model, self.g[name].number, self.g[name].consumption))
    """

        #This code will be work if u paste your parrams in 'if' ^_^
        
    def find_some_bus(self):                                                                                
        for name in self.names:
            if self.g[name].some_par1 = some_par and self.g[name].some_par2 = some_par and on and on and on: 
                print(self.g[name].model, self.g[name].number)
    """   


        
c = CreateAutopark(5, 20, 10)
print("###First Task###\n")
print("\tAutopark cost: {0}\n".format(c.get_autopark_cost()))
print("###Second Task###\n")
c.sort_by_consumption()
