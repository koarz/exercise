def square(number):
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    t = 0
    for number in range(1, 65):
        t += square(number)
    return t
        
