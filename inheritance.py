class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def start_engine(self):
        return f"The engine of the {self.model} is starting."
    
    def stop_engine(self):
        return f"The engine of the {self.model} is stopping."
    
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year) # Inheriting from Vehicle
        self.num_doors = num_doors

    def open_trunk(self):
        return f"The trunk of the {self.model} is open."
    
    # Overriding display_info method
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Doors: {self.num_doors}"
    
class Bicycle(Vehicle):
    def __init__(self, brand, model, year, type_bike):
        super().__init__(brand, model, year) # Inherited from Vehicle
        self.type_bike = type_bike

    def ring_bell(self):
        return f"The bell of the {self.model} is ringing."
    
    # Overriding display_info method
    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Type: {self.type_bike}"
    

my_car = Car("Toyota", "Corolla", 2021, 4)
my_bicycle = Bicycle("Giant", "Escape 3", 2022, "Road Bike")

print(my_car.start_engine())
print(my_bicycle.start_engine())

print(my_car.display_info())
print(my_bicycle.display_info())

print(my_car.open_trunk())
print(my_bicycle.ring_bell())


    
