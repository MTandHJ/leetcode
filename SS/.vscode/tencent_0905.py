from typing import get_origin


def get_expect(n, m):
    return sub(n, m, m)

def sub(n, m, i):
    if i == 1:
        return 3 / (n + m)
    return (2*(i) + n) / (n + i)*sub(n, m, i - 1) + sub(n, m, i - 1)

n, m = 2, 1
print(get_expect(n, m))

expect = 1
for i in range(m, 0, -1):
    expect = expect *  n / (n + i)
    expcet += 



