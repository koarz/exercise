def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    res = 0
    while number != 1:
        res += 1
        if number % 2 == 0:
            number /= 2
            continue
        number = number * 3 + 1
    return res
