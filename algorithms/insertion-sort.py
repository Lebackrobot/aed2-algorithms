# -*- coding utf-8 -*-
def insertion_sort(A):
    for j in range(1, len(A)):
        
        key = A[i]
        i = j - 1

        while i >= 0 and key < A[j]:
            A[i + 1] = A[i]
            i -= 1
            A[i + 1] = key

