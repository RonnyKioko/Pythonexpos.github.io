class fruits:
    def __init__(self, type, color, price,shape):
        self.fruittype = type
        self.fruitcolour = color
        self.fruitprice = price
        self.fruitshape= shape

    def display(self):
        print(self.fruittype, self.fruitcolour, self.fruitprice,self.fruitshape)


myobj = fruits("Apple", "Red", 30, "Round")
myobj.display()
myobj2=fruits("Grapes","Purple",50,"Circle")
myobj2.display()