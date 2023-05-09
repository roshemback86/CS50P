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


def main():
    dict = {
        "San Diego": 100,
        "Los Angeles": 200,
        "Miami": 350,
        "Washington": 400
    }

    car_1 = Vehicle(brand="Volkswagen", model="Passat", year="2009", color="Black", consumption=10, tank=55)
    car_2 = Electric_Vehicle(brand="Tesla", model="Model S", year="2015",color="White", consumption=15, battery=90)

    print("Available cars for a ride!🚗")
    print(f"1. {car_1}")
    print(f"2. {car_2}")

    x = input("Choose your car: ").lower().strip()
    car = choose_a_car(x)

    print("Where do you want to go?")
    print("1. San Diego")
    print("2. Los Angeles")
    print("3. Miami")
    print("4. Washington")
    y = input("Let's go to... ").lower().strip()
    route = get_route(y)

    if car == '1':
        print(car_1.start_engine())
        print(car_1.drive(dict[route]))
        print(f"Distance covered: {car_1.get_odometer()} kilometers.")
        print(car_1.stop_engine())
        print(f"We're arrived to {route}")
    else:
        print(car_2.start_engine())
        print(car_2.drive(dict[route]))
        print(f"Distance covered: {car_2.get_odometer()} kilometers.")
        print(car_2.stop_engine())
        print(f"We're arrived to {route}")


def range_to_go(car):
    return car.get_left() / car.get_consumption() * 100


def choose_a_car(x):
    while True:
        if x == '1' or x == 'volkswagen passat' or x == 'volkswagen' or x == 'passat':
            print("You've chosen Passat.")
            return '1'
        elif x == '2' or x == 'Tesla Model S' or x == 'Tesla' or x == 'Model S':
            print("You've chosen Tesla Model S.")
            return '2'
        else:
            print("Enter number or name of the car")
            continue


def get_route(y):
    while True:
        if y == "san diego" or y == "1":
            print("We're going to San Diego!")
            return 'San Diego'

        elif y == "los angeles" or y == "2":
            print("We're going to Los Angeles!")
            return 'Los Angeles'

        elif y == "miami" or y == "3":
            print("We're going to Miami")
            return 'Miami'

        elif y == "washington" or y == "4":
            print("We're going to Washington")
            return 'Washington'


if __name__ == "__main__":
    main()
