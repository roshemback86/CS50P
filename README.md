# LITTLE DAY-OFF TRIP
#### Video Demo: https://youtu.be/WVISiontG2s
#### Description:

This project is intended to simulate some parts of the car’s “brains” and to show how it works on a little trip through the USA. As well it could be implemented into bigger games or systems.

You can choose one of two cars: WV Passat or Tesla Model S and go to one of four cities. At the end you get the car’s parameters.

Usual on-board computer tracks vehicle’s fuel consumption, mileage, engine state(ON or OFF), fuel reserve, range reserve etc.

“On-board computer” is realized by two classes: “Vehicle”(for petrol car) and “Electric_Vehicle”(for electromobile), which contain car brand, car model, year, color, consumption, tank volume, tank reserve, mileage and engine state(on/off).

As well in those classes there are functions:

**start_engine()** - checks the state of the engine and if it’s OFF and there’s more than 0 fuel(or charge) changes it to ON.


**stop_engine()** - checks the state of the engine and if it’s ON changes it to OFF.


**drive()** - takes as argument distance you cover and returns distance covered and fuel left. As well it changes the odometer value. If the engine is OFF, your car won't go.


**refuel()** - allows you to set tank volume to max


Or in case of “Tesla”:
**recharge()** - allows you to set battery volume to max


**get_odometer()** - returns you covered distance


**get_left()** - returns fuel/battery left in tank.


**get_consumption()** - returns fuel/battery consumption


**__str__()** - returns year, color, odometer value and fuel left in the tank(battery charge)
