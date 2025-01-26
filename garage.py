import car as c
import random

class Garage:
    car_list = []
    plates1 = ['ish8374','ish9205','ish5410','ish6761','ish4028','ish1593','ish7832','ish2647']
    register = {}

    def load_cars(self):
        infile = open("cars.txt","r")
        cars = infile.readlines()

        for line in cars:
            car_info = line.replace("Brand: ","").replace("Make: ","").replace("HP: ","").replace("CC: ","").replace("\n","").replace(", "," ").split(" ")
            # print(car_info) --------------------- debuging code
            self.car_list.append(c.Car(car_info[0], car_info[1], int(car_info[2]), int(car_info[3])))

    def list_all(self):
        for car in self.car_list:
            print(car.get_brand() +" " + car.get_make()+" " + str(car.get_hp())+" " + str(car.get_cc()))

    def register_cars(self):
        for car in self.car_list:
            rand_plate = self.plates1[random.randint(0,(len(self.plates1)-1))]
            self.register[rand_plate] = car
            self.plates1.remove(rand_plate)
     
    def list_register(self):
        for reg in self.register.items():
            print(reg[0] + ': ' + reg[1].get_details())
