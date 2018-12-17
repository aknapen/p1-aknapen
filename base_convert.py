
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""

    '''List to be used to convert values greater than 10 to their alphabetic
       counterparts for bases greater than 10'''
    symbols = ["A", "B", "C", "D", "E", "F"]

    quotient = num//b
    remainder = num % b

    '''Converts values greater than 10 to their alphabetical counterparts if
       the base is greater than 10'''
    if b > 10:
        if remainder >= 10:
            remainder = symbols[remainder - 10]

    '''Base Case'''
    if quotient == 0:
        return str(remainder)

    return str(convert(quotient, b)) + str(remainder)



print(convert(40, 3))
