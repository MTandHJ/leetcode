### easy ####

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[] for _ in range(numRows)]