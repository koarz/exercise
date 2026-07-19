def is_armstrong_number(number):
    temp_number = number
    arr = []
    while number != 0:
        arr.append(number % 10)
        number = int(number / 10)
    calc = 0
    for num in arr:
        calc += num ** len(arr)
    return calc == temp_number
