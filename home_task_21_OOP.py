import time


class Auto:
    
    def __init__(self, brand, age, mark, cоlor = None, weight = None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.cоlor = cоlor
        self.weight = weight
    
    def move(self):
        print('move')
        
    def birthday(self):
        self.age += 1
        
    def stop(self):
        print('stop')
        

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, cоlor = None, weight = None):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_speed = max_speed
        
    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')
        

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, cоlor = None, weight = None):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_load = max_load
        
    def move(self):
        print('attention')
        super().move()
        
    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)
        

car_1 = Car('Toyta', 2, 'Corolla', 200, 'black', 2000)
car_1.move()
print('name:', car_1.brand)
print('age:', car_1.age)
print('mark:', car_1.mark)
print('max_speed:', car_1.max_speed)
print('cоlor:', car_1.cоlor)
print('weight:', car_1.weight)
        
car_2 = Car('BMW', 5, 'M2', 300, 'red', 3000)
car_2.move()
print('name:', car_2.brand)
print('age:', car_2.age)
print('mark:', car_2.mark)
print('max_speed:', car_2.max_speed)
print('cоlor:', car_2.cоlor)
print('weight:', car_2.weight)

truck_1 = Truck('ITM', 15, 'hhgg', 60, 'red', 10000)
truck_1.move()
truck_1.load()
print('name:', truck_1.brand)
print('age:', truck_1.age)
print('mark:', truck_1.mark)
print('max_load:', truck_1.max_load)
print('cоlor:', truck_1.cоlor)
print('weight:', truck_1.weight)

truck_2 = Truck('BHY', 7, 'mogg', 50, 'blue', 50000)
truck_2.move()
truck_2.load()
print('name:', truck_2.brand)
print('age:', truck_2.age)
print('mark:', truck_2.mark)
print('max_load:', truck_2.max_load)
print('cоlor:', truck_2.cоlor)
print('weight:', truck_2.weight)
