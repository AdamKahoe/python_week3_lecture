# vehicle = {"brand_name": "Nissan", "color": "pearl_white"}

# def paint_job(vehicle, "red"):

#print(vehicle)

class Vehicle:
    all_vehicle = []
    def __init__(self, brand_name, color):
        self.brand_name = brand_name
        self.color = color
        Vehicle.all_vehicle.append(self)
        #print("Done!")

    def paint_job(self):
        print(self.brand_name)

    @classmethod
    def print_all_vehicle_brand_names(cls):
        for vehicle in Vehicle.all_vehicle:
            print(vehicle.brand_name)

    @staticmethod
    def print_hello():
        pass


#Vehicle = {"brand_name": "Nissan", "color": "pearl_white"}
vehicle1 = Vehicle("Nissan", "pearl_white")
vehicle2 = Vehicle("Ford", "Red")

#print(Vehicle.brand_name])
#print(vehicle1.brand_name)

# print(vehicle1.paint_job())
# print(vehicle2.paint_job())

vehicle1.paint_job()
vehicle2.paint_job()

Vehicle.print_all_vehicle_brand_names