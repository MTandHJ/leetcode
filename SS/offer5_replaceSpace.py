
# TODO:
class Solution:
    def replaceSpace(self, s:str) -> str:
        length = len(s)
        array = []
        size = 0
        for i in range(length):
            c = s[i]
            if c == ' ':
                # size += 1
                array[size] = '%'
                size += 1
                array[size] = '2'
                size += 1
                array[size] = '0'
            else:
                array[size] = c
                size += 1
            
