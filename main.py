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
        print(self.brand + " - " + self.make + "\n" + self.hp + "HP (" + self.cc + "CC)\n")

class Garage:
    car_list = []

    def load_cars(self):
        infile = open("cars.txt","r")
        cars = infile.readlines()

        for line in cars:
            car_info = line.replace("Brand: ","").replace("Make: ","").replace("HP: ","").replace("CC: ","").replace("\n","").replace(", "," ").split(" ")
            self.car_list.append(Car(car_info[0], car_info[1], car_info[2], car_info[3]))

    def list_all(self):
        for car in self.car_list:
            print(car.get_brand() +" " + car.get_make()+" " + car.get_hp()+" " + car.get_cc())     

def main():

    print("\tTask One")
    print("-------------------------")
    garage = Garage()
    garage.load_cars()
    garage.list_all() 

    print("\n\tTask Two")
    print("-------------------------")
    for car in garage.car_list:
        if int(car.get_cc()) >= 800:
            car.get_details()
     
main()
