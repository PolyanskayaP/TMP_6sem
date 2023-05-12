class AbstractClass:
    def template_method(self):
        self.operation1()
        self.operation2()
        self.operation3()

    def operation1(self):
        pass

    def operation2(self):
        pass

    def operation3(self):
        pass

class ConcreteClass(AbstractClass):
    def operation1(self):
        print("ConcreteClass: operation1")

    def operation2(self):
        print("ConcreteClass: operation2")

class AnotherConcreteClass(AbstractClass):
    def operation1(self):
        print("AnotherConcreteClass: operation1")

    def operation3(self):
        print("AnotherConcreteClass: operation3")

concrete = ConcreteClass()
concrete.template_method()

another_concrete = AnotherConcreteClass()
another_concrete.template_method()


#В этом примере класс `AbstractClass` является абстрактным классом, 
# который определяет шаблонный метод `template_method`, который 
# содержит последовательность вызовов операций `operation1`, 
# `operation2` и `operation3`. Классы `ConcreteClass` и 
# `AnotherConcreteClass` представляют конкретные реализации 
# операций, которые могут быть переопределены в подклассах. 
# При вызове метода `template_method` у каждого объекта будет 
# вызвана своя последовательность операций в соответствии с его реализацией.