# -*- coding utf-8 -*-
def insertion_sort(array):
    for j in range(1, len(array)):
        
        key = array[i]
        i = j - 1

        while i >= 0 and key < array[j]:
            array[i + 1] = array[i]
            i -= 1
            array[i + 1] = key

