# Абстрактный класс Компонента
class Component:
    def __init__(self, name):
        self._name = name

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def display(self, depth):
        pass

# Конкретный компонент - Лист
class Leaf(Component):
    def add(self, component):
        print("Cannot add to a leaf")

    def remove(self, component):
        print("Cannot remove from a leaf")

    def display(self, depth):
        print('-' * depth + self._name)

# Конкретный компонент - Контейнер
class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def display(self, depth):
        print('-' * depth + self._name)
        for child in self._children:
            child.display(depth + 2)


root = Composite("root")
root.add(Leaf("Лист A"))
root.add(Leaf("Лист B"))

comp = Composite("корень X")
comp.add(Leaf("Лист XA"))
comp.add(Leaf("Лист XB"))

root.add(comp)

root.add(Leaf("Лист C"))

root.display(1)