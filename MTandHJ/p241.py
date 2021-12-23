

from typing import Collection, List

from base import version


def compute(part1, part2, sign):
    if sign == '+':
        operate = lambda x, y: x + y
    elif sign == '-':
        operate = lambda x, y: x - y
    else:
        operate = lambda x, y: x * y

    results = list()
    for x in part1:
        for y in part2:
            results.append(operate(x, y))
    return results

class Solution:

    def dealeach(self, expression: List):
        if len(expression) == 1:
            return expression
        results = list()
        for i in range(2, len(expression), 2):
            sign = expression[i-1]
            part1 = self.dealeach(expression[:i-1])
            part2 = self.dealeach(expression[i:])
            results += compute(part1, part2, sign)
        return results

    @version("28ms, 15mb")
    def diffWaysToCompute(self, expression: str) -> List[int]:
        collections = ['']
        for s in expression:
            if s in ['+', '-', '*']:
                collections[-1] = int(collections[-1])
                collections += [s, '']
            else:
                collections[-1] += s
        collections[-1] = int(collections[-1])
        results = self.dealeach(collections)
        return results
