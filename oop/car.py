from vehicle import Vehicle

class Car(Vehicle):
    def boast(self):
        print("i am the collest car")

car1 = Car()
car1.boast()
car1.drive()
car1.add_warning("new warning")
print(car1.get_warnigs())
print(car1.__dict__)

car2 = Car(200)
car2.drive()
print(car2.get_warnigs())

car3 = Car(300)
car3.drive()
print(car3.get_warnigs())