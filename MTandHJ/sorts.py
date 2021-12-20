



from typing import Iterable, List, Optional


def quicksort(nums:List) -> List:
    if len(nums) <= 1:
        return nums
    else:
        mark = nums[0]
        left = []
        right = []
        for num in nums[1:]:
            if num < mark:
                left.append(num)
            else:
                right.append(num)
        return quicksort(left) + [mark] + quicksort(right)

def quicksort_(nums:List, low: int, high: int) -> List:
    if low < high:
        pivot = nums[low]
        left, right = low, high
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left], nums[right] = nums[right], nums[left]
            while left < right and pivot > nums[left]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]

        quicksort_(nums, low=low, high=left-1) 
        quicksort_(nums, low=right+1, high=high)


class MaxHeap:

    def __init__(self, data: Optional[Iterable] = None) -> None:
        if data is None:
            data = []
        self.data = []
        for element in data:
            self.add(element)

    def get(self, index: int):
        return self.data[index]
    
    def swap(self, i: int, j: int):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def b2t(self, index: int):
        parent = (index - 1) >> 1
        if index and self.get(index) > self.get(parent):
            self.swap(index, parent)
            return self.b2t(parent)
        return index

    def t2b(self, index: int):
        try:
            child = (index << 1) + 1
            if self.get(child) > self.get(index):
                self.swap(index, child)
                self.t2b(child)
            elif self.get(child + 1) > self.get(index):
                self.swap(index, child + 1)
                self.t2b(child + 1)
        except IndexError:
            pass

    def add(self, x):
        self.data.append(x)
        return self.b2t(len(self.data) - 1)
    
    def pop(self):
        self.swap(0, -1)
        element = self.data.pop()
        self.t2b(0)
        return element

    def __len__(self):
        return len(self.data)

class MinHeap(MaxHeap):

    def b2t(self, index: int):
        parent = (index - 1) >> 1
        if index and self.get(index) < self.get(parent):
            self.swap(index, parent)
            self.b2t(parent)
        return index

    def t2b(self, index: int):
        try:
            child = (index << 1) + 1
            if self.get(child) < self.get(index):
                self.swap(index, child)
                self.t2b(child)
            if self.get(child + 1) < self.get(index):
                self.swap(index, child + 1)
                self.t2b(child + 1)
        except IndexError:
            pass
