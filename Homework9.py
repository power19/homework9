class Vehicle:
    def __init__(self,make,model,year,weight,needsmaintenance = False ,TripsSinceMaintenance = 0,repair = False):
        self.make = make
        self.model = model
        self.year = year 
        self.weight = weight
        self.needsmaintenance = needsmaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

 #getters
    def getMake(self):
        return self.make
    
    def getModel(self):
        return self.model
    
    def getYear(self):
        return self.year
    
    def getWeight(self):
        return self.weight
    
    def getNeedsMaintenance(self):
        return self.needsmaintenance

    def getTripsSinceMaintenance(self):
        return self.TripsSinceMaintenance

#Setters

    def setMake(self,make):
        self.make = make
    
    def setModel(self,model):
        self.model = model

    def setYear(self,year):
        self.year = year

    def setWeight(self,weight):
        self.weight = weight
    
    def setNeedsMaintenance(self,needs):
        self.needsmaintenance = needs

    def setTripsSinceMaintenance(self,trips):
        self.TripsSinceMaintenance = trips
        
    
#Repair
    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.needsmaintenance = False

class cars(Vehicle):
    def __init__(self,make,model,year,weight, isDriving = False):
        Vehicle.__init__(self,make,model,year,weight)
        self.isDriving = isDriving
    
    def drive(self):
        self.isDriving = True
    def stop(self):
        if self.isDriving:
            self.TripsSinceMaintenance +=1
            if self.TripsSinceMaintenance > 100:
                self.needsmaintenance = True
        self.isDriving = False



def driving(cars,times):
    # drive_times = random.randint(1,101)
    for i in range(times):
        cars.drive()
        cars.stop()


# print car attributes         
def car_specs(car):
    print("Make ",car.make)
    print("Model ",car.model)
    print("Year ",car.year)
    print("Weight ",car.weight,"KG")
    print("Needs Maintenance ",car.needsmaintenance)
    print("Trips Since Maintenance ",car.TripsSinceMaintenance)
    print("Weight ",car.weight,"\n")
    


car1 = cars("toyota","Auris",2019,10000)
car2 = cars("VW","Jetta",2018,12000)
car3 = cars("Mazda","3",2016,15000)

driving(car1,101)
driving(car2,80)
driving(car3,70)

car_specs(car1)
car_specs(car2)
car_specs(car3)
