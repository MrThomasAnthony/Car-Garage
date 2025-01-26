class Car:
    def __init__(self, brand, make, hp=0, cc=0):
        self.brand = brand
        self.make = make
        self.hp = hp
        self.cc = cc
    
    def get_brand(self):
        return self.brand
    
    def get_make(self):
        return self.make
    
    def get_hp(self):
        return self.hp
    
    def get_cc(self):
        return self.cc
    
    def set_brand(self, brand):
        self.brand = brand
    
    def set_make(self, make):
        self.make = make
    
    def set_hp(self, hp):
        self.hp = hp
    
    def set_cc(self, cc):
        self.cc = cc

    def get_details(self):
        car_details = self.brand + " - " + self.make + " " + str(self.hp) + "HP (" + str(self.cc)+ "CC)"
        return car_details
