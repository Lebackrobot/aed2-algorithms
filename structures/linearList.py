import math 

class LinearList:
    def __init__(self, n):
        self.head = None
        self.tail = None
        self.array = n * [None]
        self.memory = n

    
    @property
    def length(self):
        if self.head == None:
            return 0
        
        return abs(self.head - self.tail) + 1
    
    @property
    def middle_list(self): 
        return self.length // 2
    

    @property
    def middle_memory(self):
        return self.memory // 2
    
    
    def is_valid_position(self, index):
        return (index >= 0 and index <= self.length and index < self.memory)
    

    def is_overflow(self, side=''):
        if side == 'RIGHT' and self.tail == self.memory - 1:
            return True 
            
        elif side == 'LEFT' and self.head == 0:
            return True
        
        return self.length == self.memory
    
    def slide(self, start, end, leap, side='LEFT', updateFields=['head', 'tail']):
        if side == 'RIGHT':
            leap = abs(leap)

            for i in range(end, start - 1, -1):
                self.array[i + leap] = self.array[i]
                self.array[i] = None

        else:
            leap = - abs(leap)

            for i in range(start, end + 1):
                self.array[i + leap] = self.array[i]
                self.array[i] = None


        if 'head' in updateFields: self.head += leap 
        if 'tail' in updateFields: self.tail += leap


    def push(self, value):
        try:
            if self.head == None:
                self.head = self.middle_memory
                self.tail = self.middle_memory

                # subtracting to add in first insert to tail
                self.tail -= 1

            if self.is_overflow():
                raise Exception('Overflow')

            if self.is_overflow(side='RIGHT'):
                leap = self.middle_list - self.middle_memory
                self.slide(start=self.head, end=self.tail, leap=leap)

            self.tail += 1
            self.array[self.tail] = value

        except Exception as error: 
            print(f'🐞 (BUG): {error}')



    def splice(self, index, value):
        try:
            if self.head == None:
                self.head = self.middle_memory - 1
                self.tail = self.middle_memory - 1

                if (index == 0):
                    self.array[self.head] = value
                    return

                else: raise Exception('Invalid Position')

            if self.is_overflow(): raise Exception('Overflow')

            if not self.is_valid_position(index): raise Exception('Invalid position')
            
            if index <= self.middle_list:
                if self.head == 0:
                    leap = abs(self.middle_list - self.middle_memory)
                    self.slide(start=self.head, end=self.tail, leap=leap, side='RIGHT')

                if index == 0 and self.head != 0:
                    self.head -= 1

                else:
                    start = self.head
                    end = (self.head + index - 1)
                    index -= 1
                    leap = -1

                    self.slide(start=start, end=end, leap=leap, updateFields=['tail'])

            else:
                if self.tail == self.length - 1:
                    leap = self.middle_list - self.middle_memory
                    self.slide(start=self.head, end=self.tail, leap=leap)

                elif self.tail == self.length - 1:
                    self.slide(start=self.head, end=self.tail, leap=1)

                start = self.head + index
                end = self.tail
                self.slide(start=start, end=end, leap=1, updateFields=['tail'])

            self.array[self.head + index] = value

        except Exception as error:
            print(f'🐞 (BUG): {error}')


    def reset(self):
        self.head = None
        self.tail = None


if __name__ == '__main__':
    linearList  = LinearList(10)
    print(linearList.array)