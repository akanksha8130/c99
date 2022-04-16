class Car(object):
     def __init__(self, name, color, company, speed_limit,gear_type):

        self.name = name
        self.company = company
        self.color = color
        self.speed_limit= speed_limit
        self.gear_type=gear_type

     def start(self):
        print('started')
        
    
     def stop(self):
        print('stop')

     def accerlerator(self):
        print('accelerating')
    
     def changegear(self):

        print('gear changed')

        
audi=Car("A6","red","audi","500","forward")

print(audi.changegear())
                                                         
