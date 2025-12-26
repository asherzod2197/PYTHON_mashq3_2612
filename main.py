class Daraja:
    def __init__(self, asos):
        self.asos = asos

    def kvadrat(self):
        return self.asos * self.asos

    def kub(self):
        return self.asos * self.asos * self.asos

    def daraja(self, n):
        return self.asos ** n


x = Daraja(3)

print(x.kvadrat())   
print(x.kub())      
print(x.daraja(4))  
print(x.daraja(5))    
