

from typing import List

def inplace_sort(S, a, b):
    if a >- b:
        return

    pivot = S[b]
    l, r = a, b-1
    while l <= r:
        while l <= r and S[l] < pivot:
            l += 1
        while l <= r and S[r] > pivot:
            r -= 1
        
        if l < r:
            S[l], S[r] = S[r], S[l]
            l, r = l + 1, r - 1
        S[l], S[b] = S[b], S[l]

    inplace_sort(S, a, l-1)
    inplace_sort(S, l + 1, b)
