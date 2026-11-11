# creates three classes with same method name
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")


# creates function that works with any object with move()
def start_trip(vehicle):
    vehicle.move()


# creates one object for each class
car = Car()
boat = Boat()
drone = Drone()

# calls the function for each object
start_trip(car)
start_trip(boat)
start_trip(drone)
