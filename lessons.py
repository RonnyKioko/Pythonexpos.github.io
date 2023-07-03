class people:
    def __init__(self, name, age, gender):
        self.peoplename = name
        self.peopleage = age
        self.peoplegender = gender

    def display(self):
        print(self.peoplename, self.peopleage, self.peoplegender)


myobj = people("Tirop", 18, "Male")
myobj.display()
myobj1 = people("Sydney", 16, "Female")
myobj1.display()
myobj2 = people("Ronny", "18", "Male")
myobj2.display()
