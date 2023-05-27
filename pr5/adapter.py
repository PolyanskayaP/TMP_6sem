# Класс, который нужно адаптировать
class person1:
    def specificRequest(self):
        return "dumplings"
    def recieve(self,req):
        return req

class person2:
    def specificRequest(self):
        return "skovorodka"
    def recieve(self, req):
        return req

# Абстрактный класс адаптера
class Target:
    def request(self):
        pass

# Конкретный адаптер
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self): 
        word = self.adaptee.specificRequest()
        if word == "dumplings":
            return  "let's cook together"
        if word == "skovorodka":
            return "stop cooking"

# Клиентский код
if __name__ == "__main__":
    adaptee = person1()
    adapter = Adapter(adaptee)
    recipient = person2()
    print(recipient.recieve(adapter.request()))
    
    adaptee = person2()
    adapter = Adapter(adaptee)
    recepient = person1()
    print(recipient.recieve(adapter.request()))