# Абстрактный класс посредника
class Mediator:
    def send(self, message, colleague):
        pass

# Абстрактный класс коллеги
class Colleague:
    def __init__(self, mediator):
        self.mediator = mediator

    def send(self, message):
        self.mediator.send(message, self)

    def receive(self, message):
        pass

# Конкретный посредник
class ConcreteMediator(Mediator):
    def __init__(self, colleague1, colleague2):
        self.colleague1 = colleague1
        self.colleague2 = colleague2

    def send(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.receive(message)
        else:
            self.colleague1.receive(message)

# Конкретный коллега
class ConcreteColleague1(Colleague):
    def receive(self, message):
        print("Colleague 1 received message: " + message)

# Конкретный коллега
class ConcreteColleague2(Colleague):
    def receive(self, message):
        print("Colleague 2 received message: " + message)

if __name__ == "__main__":
    col1 = ConcreteColleague1("")
    col2 = ConcreteColleague2("")
    med = ConcreteMediator(col1, col2)
    med.send("message", col1)
    med.send("hello", col2)

    col1.receive("Hello from colleague 1!")
    col2.receive("Hello from colleague 2!")

    