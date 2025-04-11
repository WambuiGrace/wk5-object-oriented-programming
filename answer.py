# 1. Define the base class
class superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __str__(self):
        return f"{self.name} has the power of {self.power}"
    
    def __repr__(self):
        return f"superhero({self.name}, {self.power})"
    
    def use_power(self):
        return f"{self.name} uses {self.power}!"

# 2. Subclass for a specific superheros
class Technology(superhero):
    def __init__(self, name, power, gadget):
        super().__init__(name, power)
        self.gadget = gadget

    def __str__(self):
        return f"{self.name} has the power of {self.power} and uses {', '.join(self.gadget)}"
    
    def use_gadget(self, gadget):
        if gadget in self.gadget:
            return f"{self.name} uses the gadget: {gadget}!"
        else:
            return f"{self.name} doesn't have the gadget: {gadget}."
        
class elemental(superhero):
    def __init__(self, name, power, element):
        super().__init__(name, power)
        self.element = element

    def __str__(self):
        return f"{self.name} has the power of {self.power} and controls {self.element}"
    
    def use_element(self):
        return f"{self.name} unleashes the power of {self.element}!"

# 3. Usage of the classes
if __name__ == "__main__":
    hero = superhero("Superman", "Super Strength")
    tech_hero = Technology("Cyborg", "Technological integration", ["Hacker", "Gadgets"])
    elemental_hero = elemental("Spiderman", "Spider sense", "Agility")

    print(f"1. {hero}")
    print(f"2. {tech_hero}")
    print(f"3. {elemental_hero}")
    print()
    print(hero.use_power())
    print()
    print(tech_hero.use_power())
    print(tech_hero.use_gadget("Hacker"))
    print()
    print(elemental_hero.use_power())
    print(elemental_hero.use_element())
    print()


# Polymorphism Challenge! 🎭
class vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        return f"{self.name} is moving at {self.speed} speed."

class car(vehicle):
    def move(self):
        return f"{self.name} is driving at {self.speed} speed."

class plane(vehicle):
    def move(self):
        return f"{self.name} is flying at {self.speed} speed."

class boat(vehicle):
    def move(self):
        return f"{self.name} is sailing at {self.speed} speed."

if __name__ == "__main__":
    car = car("Car", "80 km/h")
    plane = plane("Jet", "900 km/h")
    boat = boat("Yacht", "50 km/h")

    vehicles = [car, plane, boat]
    for vehicle in vehicles:
        print(vehicle.move())