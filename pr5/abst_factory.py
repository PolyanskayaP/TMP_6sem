# Абстрактные классы продуктов
class AbstractProductA:
    def operationA(self):
        pass

class AbstractProductB:
    def operationB(self):
        pass

# Конкретные классы продуктов
class ProductA1(AbstractProductA):
    def operationA(self):
        return "Product A1"

class ProductA2(AbstractProductA):
    def operationA(self):
        return "Product A2"

class ProductB1(AbstractProductB):
    def operationB(self):
        return "Product B1"

class ProductB2(AbstractProductB):
    def operationB(self):
        return "Product B2"

# Абстрактная фабрика
class AbstractFactory:
    def createProductA(self):
        pass

    def createProductB(self):
        pass

# Конкретные фабрики
class ConcreteFactory1(AbstractFactory):
    def createProductA(self):
        return ProductA1()

    def createProductB(self):
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def createProductA(self):
        return ProductA2()

    def createProductB(self):
        return ProductB2()

def clientCode(factory: AbstractFactory) -> None:
    productA = factory.createProductA()
    productB = factory.createProductB()

    print(productA.operationA())
    print(productB.operationB())

if __name__ == "__main__":
    print("Client code with ConcreteFactory1:")
    clientCode(ConcreteFactory1())

    print("\nClient code with ConcreteFactory2:")
    clientCode(ConcreteFactory2())