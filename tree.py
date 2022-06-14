class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
    
    def add_child(self, value):
        if not isinstance(value, Node):
            value = Node(value)
        if len(self.children) == 0:
            self.children = {"0": value}
        else:
            self.children[str(len(self.children))] = value

    def __str__(self) -> str:
        return str(self.data)

    def visit(self,navigate_to: str):
        directions = navigate_to.split(".")
        current_node = self
        for direction in directions:
            current_node = current_node.children[direction]
        return current_node
        


