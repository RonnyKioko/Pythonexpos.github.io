class Animal:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def speak(self):
        raise NotImplementedError("Child classes must implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# create an object

dog = Dog("Tom", "Golden")
print(dog.name)
print(dog.colour)
print(dog.speak())
# create an object
cat = Cat("Puss", "White")

print(cat.name)
print(cat.speak())
print(cat.colour)

