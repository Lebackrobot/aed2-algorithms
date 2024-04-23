# -*- coding utf-8 -*-
def insertion_sort(A):
    for j in range(1, len(A)):
        
        key = A[i]
        i = j - 1

        while i >= 0 and key < A[j]:
            A[i + 1] = A[i]
            i -= 1
            A[i + 1] = key

    """ def __normalize(self):
        middle_list = self.__middle_list
        middle_array = self.__middle_memory

        print(f'middle_array = {self.__middle_memory}')
        print(f'middle_list = {self.__middle_list}')
        print(self.__middle_memory == self.__middle_list)


        if self.__middle_memory == self.__middle_list:
                return
        
        index_leap = abs(middle_array - middle_list)

        for i in range(self.head, self.length):
            if middle_list > middle_array: 
                value = self.array[i]

                self.array[i] = None
                self.array[i - index_leap] = value

            elif middle_list < middle_array:
                value = self.array[i]
                self.array[i + index_leap] = value
                self.array[i] = None

        if middle_list > middle_array:
            self.head -= index_leap

        elif middle_list < middle_array:
            self.head += index_leap

        print(f'new head = {self.head}') """
