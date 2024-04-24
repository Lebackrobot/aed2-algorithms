class Node:
    def __init__(self, value):
        self.previus = None
        self.value = value 

class LinkedStack:
    def __init__(self, n):
        self.top = None
        self.memory = n
        self.length = 0


    @property
    def __is_full(self):
        return self.memory == self.length 
    

    @property
    def __is_empty(self):
        return self.length == 0

    def __add_node(self, node, is_first=False):
        if is_first:
            self.top = node
            self.length += 1
            return

        previus_node = Node(self.top.value)
        previus_node.previus = self.top.previus

        self.top = node
        node.previus = previus_node
        self.length += 1

    def push(self, value):
        try:
            node = Node(value)

            if self.__is_full:
                raise Exception('overflow')

            if self.__is_empty:
                self.__add_node(node, is_first=True)

            else:
                self.__add_node(node)


        except Exception as error:
            print(f'(BUG 🐞): {error}')


    def peek(self):
        try:
            if self.__is_empty:
                return None

            return self.top.value
    
        except Exception as error:
            print(f'(BUG 🐞): {error}')

    
    
    def pop(self):
        try:
            if self.__is_empty:
                raise Exception('stack is empty')
            
            popped_value = self.top.value
            self.top = self.top.previus

            return popped_value
        
        except Exception as error:
            print(f'(BUG 🐞): {error}')

    
    def delete(self):
        self.top = None


    def __repr__(self):
        nodes = []
        current_node = self.top

        while current_node:
            nodes.append(str(current_node.value))
            current_node = current_node.previus

        return f"Stack {'->'.join(node for node in nodes)}"

