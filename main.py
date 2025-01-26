import garage as g

def main():

    print("\tLAB 2 - Task One")
    print("-" * 50)
    garage = g.Garage()
    garage.load_cars()
    garage.register_cars()
    garage.list_register()
     
main()
