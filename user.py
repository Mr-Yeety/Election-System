import imp
from election import Election

class User():
    
    def __init__(self, name, address, id):
        self.name = name
        self.address = address
        self.id = id
    
    def verify(self):
        id = 6969420

        if self.id != id:
            return False
        else:
            return True
   
    







