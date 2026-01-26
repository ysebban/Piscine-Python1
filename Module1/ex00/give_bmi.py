def check_type(blob: object) -> bool:
    """ Check is arg is int/float or not
        return true is arg is number an > 0
    """
    if isinstance(blob, bool) or not isinstance(blob, (int, float)):
        return False
    return blob > 0


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    takes height and weight and returns a BMI(IMC in french)
    both list has to be same size and both can be either int or float
    weight / (height*height)
    """
    if len(height) != len(weight):
        return (print("Error: Both list aren't same size"))
    bmi = []
    for h, w in zip(height, weight):
        if not check_type(h) or not check_type(w):
            return (print("Error: one of the entry is neither int or float"))

        square_h = h * h
        result = w / square_h
        bmi.append(result)
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    looks at BMI in list input and returns a list a bool
    true if bmi > limit
    """
    result = []
    for x in bmi:
        if not check_type(x):
            return (print("Error:BMI is neither int or float"))
        if x > limit:
            result.append(True)
        else:
            result.append(False)
    return result
