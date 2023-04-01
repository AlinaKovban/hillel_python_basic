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
        
