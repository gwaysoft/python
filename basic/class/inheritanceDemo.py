class Fruit:
    color = "green"

    def __init__(self, color):
        print("Fruit", color)
        Fruit.color = color

    def harvest(self, color):
        print("param: %s" %color, "Fruit color: %s" %Fruit.color)

#fruit = Fruit()
#fruit.harvest("red")

class Apple(Fruit):
    color = "Apple.red"
    def __init__(self):
        print("apple")

    def harvest(self, color):
        print("Apple param: %s" %color, "Fruit color: %s" %Fruit.color)

class Orange(Fruit):
    color = "Orange.orange"
    def __init__(self):
        super().__init__(Orange.color)
        print("orange")

#apple = Apple()
#apple.harvest(Apple.color)

orange = Orange()
