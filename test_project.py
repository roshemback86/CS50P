from project import choose_a_car
from project import get_route
from project import range_to_go

class Vehicle:
    def __init__(self, brand, model, year, color, consumption, tank, odometer=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.consumption = consumption
        self.tank = tank
        self.left = tank
        self.odometer = odometer
        self.engine_works = False

    def start_engine(self):
        if self.engine_works == False and self.left > 0:
            self.engine_works = True
            return "Engine is ON"
        elif self.left < 1:
            return "Not enough fuel (Low battery)"
        return "Engine is already ON"

    def stop_engine(self):
        if self.engine_works:
            self.engine_works = False
            return "Engine is OFF"
        return "Engine is alredy OFF"

    def drive(self, range):
        if self.engine_works == False:
            return "Start engine please!"
        if self.left / self.consumption * 100 < range:
            return "Not enough fuel (Low battery)"
        self.odometer = self.odometer + range
        self.left = self.left - range / 100 * self.consumption
        return f"Covered {range} km. Fuel left: {self.left} liters."

    def refuel(self):
        self.left = self.tank

    def get_odometer(self):
        return self.odometer

    def get_left(self):
        return self.left

    def get_consumption(self):
        return self.consumption

    def __str__(self):
        return f"{self.brand} {self.model}. " \
            f"Year: {self.year}. " \
            f"Color: {self.color}. " \
            f"Odometer: {self.odometer} km. " \
            f"Fuel: {self.left} l."

class Electric_Vehicle(Vehicle):
    def __init__(self, brand, model, year, color, consumption, battery, odometer=0):
        super().__init__(brand, model, year, color, consumption, battery, odometer)
        self.battery = battery

    def drive(self, distance):
        super().drive(distance)
        return f"Covered {distance} km. Battery: {self.left} %."

    def recharge(self):
        self.left = self.battery

    def __str__(self):
        return f"{self.brand} {self.model}. " \
            f"Year: {self.year}. " \
            f"Color: {self.color}. " \
            f"Odometer: {self.odometer} km. " \
            f"Battery: {self.left}%."

car_1 = Vehicle(brand="Volkswagen", model="Passat", year="2009", color="Black", consumption=10, tank=55)
car_2 = Electric_Vehicle(brand="Tesla", model="Model S", year="2015",color="White", consumption=15, battery=90)

def test_choose_a_car():
    assert choose_a_car('1') == '1'
    assert choose_a_car('2') == '2'


def test_function_2():
    assert get_route('1') == 'San Diego'
    assert get_route('san diego') == 'San Diego'

def test_range_to_go():
    assert range_to_go(car_2) == 600.0
    assert range_to_go(car_1) == 550.0
