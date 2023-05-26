class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class GraphIterator:
    def __init__(self, start_node):
        self.stack = [start_node]
        self.visited = set()

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()
        self.visited.add(node)

        for neighbor in node.neighbors:
            if neighbor not in self.visited:
                self.stack.append(neighbor)

        return node

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, val):
        node = GraphNode(val)
        self.nodes.append(node)
        return node

    def dfs(self, start_node):
        return GraphIterator(start_node)

graph = Graph()

node1 = graph.add_node(1)
node2 = graph.add_node(2)
node3 = graph.add_node(3)
node4 = graph.add_node(4)
node5 = graph.add_node(5)

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node2.neighbors.append(node4)
node3.neighbors.append(node4)
node4.neighbors.append(node5)

for node in graph.dfs(node1):
    print(node.val)
