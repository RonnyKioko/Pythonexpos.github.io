class cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def colour(self):
        raise NotImplementedError("Child classes must be implemented")


class Ronny(cars):
    def colour(self):
        return "Black"


class Aggy(cars):
    def colour(self):
        return "Golden"


class Sydney(cars):
    def colour(self):
        return "White"


# create an object
ronny = Ronny("Toyota", "Rav4")
print(ronny.brand)
print(ronny.model)
print(ronny.colour())

aggy = Aggy("Mitsubishi", "Outlander")
print(aggy.brand)
print(aggy.model)
print(aggy.colour())

sydney = Sydney("Bentley", "Flying Spur")
print(sydney.brand)
print(sydney.model)
print(sydney.colour())
