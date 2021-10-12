

from typing import List


def bubbleSort(arr: List[int]):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubbleSort2(arr: List[int]):
    # 初始设置为True
    swapped = True
    for i in range(len(arr) - 1):
        # 如果没有交换过，说明已经到最后了
        if not swapped:
            break
        # 此时设置为False， 如果发生交换，将其设置为True
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                # 此时说明要交换了
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # 已经交换过了
                swapped = True
        
