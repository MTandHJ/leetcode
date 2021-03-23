
from typing import Callable, List, Tuple, Union

def version(annotation: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            return  func(*args, **kwargs)
        wrapper.__name__ = func.__name__ 
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator