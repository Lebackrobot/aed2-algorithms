class ContiguosStack:
    def __init__(self, n):
        self.top = -1
        self.array = n * [None]
        self.memory = n

    @property
    def length(self):
        return self.top + 1

    @property
    def is_full(self):
        return self.top == (self.memory) - 1

    @property
    def is_empty(self):
        return self.top == -1
    

    def push(self, value):
        try:
            if self.is_full:
                return Exception('stack is full')

            self.top += 1
            self.array[self.top] = value

        except Exception as error:
            print(f'(BUG 🐞): {error}')


    def pop(self):
        try:
            if self.is_empty:
                return Exception('stack is empty')

            self.top -= 1

            return self.array[self.top + 1]
            

        except Exception as error:
            print(f'(BUG 🐞): {error}')
            

    def peek(self): 
        try:
            if self.is_empty:
                return Exception('stack is empty')

            return self.array[self.top]

        except Exception as error:
            print(f'(BUG 🐞): {error}')


    def delete(self):
        try:
            self.top = -1

        except Exception as error:
            print(f'(BUG 🐞): {error}')


    def __repr__(self):
        return f"Stack {'->'.join(str(self.array[i]) for i in range(0, self.top + 1))}"
