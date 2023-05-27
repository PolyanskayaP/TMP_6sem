# Класс продукта
class Product:
    def __init__(self):
        self.parts = []

    def addPart(self, part):
        self.parts.append(part)

    def listParts(self):
        print("Product parts: ", end="")
        for part in self.parts:
            print(part, end=", ")
        print("\n")

# Абстрактный класс строителя
class Builder:
    def buildPartA(self):
        pass

    def buildPartB(self):
        pass

    def buildPartC(self):
        pass

    def getProduct(self):
        pass

# Конкретный строитель
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def buildPartA(self):
        self.product.addPart("Part A")

    def buildPartB(self):
        self.product.addPart("Part B")

    def buildPartC(self):
        self.product.addPart("Part C")

    def getProduct(self):
        return self.product

# Директор
class Director:
    def __init__(self):
        self.builder = None

    def setBuilder(self, builder):
        self.builder = builder

    def buildMinimalProduct(self):
        self.builder.buildPartA()

    def buildFullProduct(self):
        self.builder.buildPartA()
        self.builder.buildPartB()
        self.builder.buildPartC()

if __name__ == "__main__":
    director = Director()
    builder = ConcreteBuilder()
    director.setBuilder(builder)

    print("Minimal product:")
    director.buildMinimalProduct()
    product = builder.getProduct()
    product.listParts()

    print("Full product:")
    director.buildFullProduct()
    product = builder.getProduct()
    product.listParts()