class Cash:
    __count = 100
    
    def top_up(self,x):
        self.__count += x
        return "yeap!"
        
    def count_1000(self):
        return  self.__count
    
    def take_away (self,x):
        if self.__count < (self.__count - x):
            print("No cash")
        else:
         self.__count - x 
        
       
       
c = Cash()
print(c.count_1000())
print(c.top_up(200))
print(c.count_1000())