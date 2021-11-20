
from typing import Callable, List, Tuple, Union
import sys

def version(annotation: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            return  func(*args, **kwargs)
        wrapper.__name__ = func.__name__ 
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator


def main():
    import sys
    solver: Callable
    for line in sys.stdin:
        flows = line.split()
        print(solver(*flows))
    return
