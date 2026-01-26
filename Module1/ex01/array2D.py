import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Print the shape of a list
    Slice it according to start and end integers
    print it's new shape
    return printed errors in case of wrong inputs
    return sliced list otherwise
    """
    if not isinstance(family, list):
        return (print("Input list isn't a list"))
    if not isinstance(start, int) or not isinstance(end, int):
        return (print("Input integers are not int"))
    np_array = np.array(family)
    print(f"My Shape is : {np_array.shape}")
    cut = slice(start, end)
    print(f"My new shape is: {np_array[cut].shape}")
    return np_array[cut]
