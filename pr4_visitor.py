# Абстрактный класс узла дерева
class Node:
    def accept(self, visitor):
        pass

# Конкретный класс узла - число
class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_number(self)

# Конкретный класс узла - операция сложения
class AddNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_add(self)

# Конкретный класс узла - операция умножения
class MultiplyNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_multiply(self)

# Абстрактный класс посетителя
class Visitor:
    def visit_number(self, node):
        pass

    def visit_add(self, node):
        pass

    def visit_multiply(self, node):
        pass

# Конкретный класс посетителя - вычисление значения выражения
class CalculateVisitor(Visitor):
    def visit_number(self, node):
        return node.value

    def visit_add(self, node):
        return node.left.accept(self) + node.right.accept(self)

    def visit_multiply(self, node):
        return node.left.accept(self) * node.right.accept(self)

expression = AddNode(
    MultiplyNode(NumberNode(2), NumberNode(3)),
    NumberNode(4)
)

result = expression.accept(CalculateVisitor())
print(result) # 10

