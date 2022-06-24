class vehicle():
    def __init__ (self, color,capacity,enginepower,typee):
        self.color = color
        self.capacity = capacity
        self.enginepower = enginepower
        self.typee = typee

    def vehiclecar(self):
        print("car color is : {}".format(self.color))
        print("car capacity is : {}".format(self.capacity))
        print("cars engine horsepower is : {}".format(self.enginepower))
        print("car type is : {}".format(self.typee))

    def start(self):
        print("car engine start")

    def stop(self):
        print("car engine stop")

class car(vehicle):
    def __init__(self,airbags,gear,speed,fuel,color,capacity,engin,typee):
        super().__init__(color,capacity,engin,typee)
        self.airbags = airbags
        self.gear = gear
        self.speed = speed
        self.fuel = fuel
    
    def electriccar(self):
        print("do you have airbags : {}".format(self.airbags))
        print("how many gears in car : {}".format(self.gear))
        print("best speed of your car : {} km/h".format(self.speed))
        print("what is the variant of your car : {}".format(self.fuel))
    
    def accelerate (self):
        print("now your accelerating the car")
    
    def fillfuel(self):
        print("fuel is low fill the fuel")
    
    def playmusic(self):
        print("music is playing your play list is on")
    
    def onAC(self):
        print("AC is on")

class electric_car(vehicle):
    def __init__(self, battery_level):
        self.battery_level = battery_level
    
    def battery(self):
        print("your cars charging is : {}%  ".format(self.battery_level))
    
    def charging(self):
        print("car is on charging")
    
car1 = car(4,6,200,"petrol","red","1300kg","1400cc","XUV")
car2 = electric_car(40)
car1.start()
car1.vehiclecar()
car1.electriccar()
car1.accelerate()
car1.fillfuel()
car1.playmusic()
car1.onAC()
car2.battery()
car2.charging()
car1.stop()
