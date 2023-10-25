class Transport(object):
    
    def __init__(self, name, max_speed, millage):
      self.name = name
      self.max_speed = max_speed
      self.millage = millage
      
      
      
class Autobus(Transport):
    
 def __init__(self, name, max_speed, millage):
  super().__init__(name, max_speed, millage)
  
 def seating_capacity(self, capacity=50):
     print(f"Name {self.name} capacity {capacity} ")
       



  
t = Transport("lada",120,12000)
a = Autobus("Ikar",90,45000)

print(t.name)
print(a.name)
a.seating_capacity()



